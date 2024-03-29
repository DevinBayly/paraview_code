"""This module demonstrates various ways of adding
VTKPythonAlgorithmBase subclasses as filters, sources, readers,
and writers in ParaView"""


# This is module to import. It provides VTKPythonAlgorithmBase, the base class
# for all python-based vtkAlgorithm subclasses in VTK and decorators used to
# 'register' the algorithm with ParaView along with information about UI.
from paraview.util.vtkAlgorithm import *
import uuid
from pathlib import Path



#------------------------------------------------------------------------------
# A reader example.
#------------------------------------------------------------------------------
def createModifiedCallback(anobject):
    import weakref
    weakref_obj = weakref.ref(anobject)
    anobject = None
    def _markmodified(*args, **kwars):
        o = weakref_obj()
        if o is not None:
            o.Modified()
    return _markmodified

def makepcloud(pcd_name):
    import numpy as np
    with open(pcd_name,"rb") as phile:
        line = phile.readline()
        header = []
        while not b"DATA" in line:
            line = phile.readline()
            print(line)
            header.append(line)
        buf = phile.read()
    parts = [[e for e in d.decode().strip().split(" ")[1:]] for d in header[1:] ]
    parts = [p for p in parts if len(p) >0]
    parts
    print("parts are",parts)
    collection = []
    for attri,e in enumerate(parts[3]):
        print("e is ",e)
        for i in range(int(e)):
            name = parts[0][attri]
            if name =="_":
                name+=str(i)+str(attri)
            unit = (parts[2][attri]+parts[1][attri]).lower()
            collection.append((name,unit))
    d = np.dtype(collection)
    d.itemsize
    arr = np.frombuffer(buf[:d.itemsize*int(parts[7][0])],dtype=d)
    return arr

# To add a reader, we can use the following decorators
#   @smproxy.source(name="PythonnumpyReader", label="Python-based numpy Reader")
#   @smhint.xml("""<ReaderFactory extensions="csv" file_description="Numpy numpy files" />""")
# or directly use the "@reader" decorator.
@smproxy.reader(name="Pcd loader plugin", label="Python-based numpy pcd Reader for timeseries data",
                extensions="pcd",
                 file_description="point cloud descriptor files")
class PythonNumpyPCDReader(VTKPythonAlgorithmBase):
    """A reader that reads a numpy file. If the numpy has a "time" column, then
    the data is treated as a temporal dataset"""
    def __init__(self):
        VTKPythonAlgorithmBase.__init__(self, nInputPorts=0, nOutputPorts=1, outputType='vtkPolyData')
        self._filename = None
        self._ndata = None
        self._timesteps = None
        print("starting",uuid.uuid1())

        from vtkmodules.vtkCommonCore import vtkDataArraySelection
        self._arrayselection = vtkDataArraySelection()
        self._arrayselection.AddObserver("ModifiedEvent", createModifiedCallback(self))

    def _get_raw_data(self, requested_time=None):
        import numpy
        if self._ndata is not None:
            if requested_time is not None:
                ##### load specific npy file from fnmes
                fname = self.fnames[int(requested_time)]
                self._ndata = makepcloud(fname)
                print(self._ndata.dtype)
                # self._ndata.dtype = numpy.dtype([("x",numpy.float32),("y",numpy.float32),("z",numpy.float32),("intensity",numpy.float32)])
                return self._ndata
            return self._ndata

        if self._filename is None:
            # Note, exceptions are totally fine!
            raise RuntimeError("No filename specified")

        # self._ndata = numpy.genfromtxt(self._filename, dtype=None, names=True, delimiter=',', autostrip=True)
        self.pth = Path(self._filename)
        self.fnames = list(self.pth.parent.rglob("*pcd"))
        self.fnames.sort()
        times =  [i for i,e in enumerate(self.fnames)]
        self._ndata = 0
        self._timesteps = times

        return self._get_raw_data(requested_time)

    def _get_timesteps(self):
        self._get_raw_data()
        return self._timesteps if self._timesteps is not None else None

    def _get_update_time(self, outInfo):
        executive = self.GetExecutive()
        timesteps = self._get_timesteps()
        if timesteps is None or len(timesteps) == 0:
            return None
        elif outInfo.Has(executive.UPDATE_TIME_STEP()) and len(timesteps) > 0:
            utime = outInfo.Get(executive.UPDATE_TIME_STEP())
            print("using inner method get update time",utime)
            dtime = timesteps[0]
            for atime in timesteps:
                if atime > utime:
                    return dtime
                else:
                    dtime = atime
            return dtime
        else:
            assert(len(timesteps) > 0)
            return timesteps[0]

    def _get_array_selection(self):
        return self._arrayselection

    @smproperty.stringvector(name="FileName")
    @smdomain.filelist()
    @smhint.filechooser(extensions="pcd", file_description="pcd file")
    def SetFileName(self, name):
        """Specify filename for the file to read."""
        print(name)
        if self._filename != name:
            self._filename = name
            self._ndata = None
            self._timesteps = None
            self.Modified()

    @smproperty.doublevector(name="TimestepValues", information_only="1", si_class="vtkSITimeStepsProperty")
    def GetTimestepValues(self):
        print("getting time steps")
        return self._get_timesteps()

    # Array selection API is typical with readers in VTK
    # This is intended to allow ability for users to choose which arrays to
    # load. To expose that in ParaView, simply use the
    # smproperty.dataarrayselection().
    # This method **must** return a `vtkDataArraySelection` instance.
    @smproperty.dataarrayselection(name="Arrays")
    def GetDataArraySelection(self):
        return self._get_array_selection()

    def RequestInformation(self, request, inInfoVec, outInfoVec):
        print("requesting information")
        executive = self.GetExecutive()
        outInfo = outInfoVec.GetInformationObject(0)
        outInfo.Remove(executive.TIME_STEPS())
        outInfo.Remove(executive.TIME_RANGE())

        timesteps = self._get_timesteps()
        if timesteps is not None:
            for t in timesteps:
                outInfo.Append(executive.TIME_STEPS(), t)
            outInfo.Append(executive.TIME_RANGE(), timesteps[0])
            outInfo.Append(executive.TIME_RANGE(), timesteps[-1])
        return 1

    def RequestData(self, request, inInfoVec, outInfoVec):
        print("requesting data")
        from vtkmodules.vtkCommonDataModel import vtkPolyData
        from vtkmodules.numpy_interface import dataset_adapter as dsa
        import vtk
        import numpy as np

        data_time = self._get_update_time(outInfoVec.GetInformationObject(0))

        output = dsa.WrapDataObject(vtkPolyData.GetData(outInfoVec, 0))
        all_data = self._get_raw_data(data_time)
        data = np.column_stack([all_data["x"],all_data["y"],all_data["z"]])
        intensity = all_data["intensity"]
        #points = self._ndata
        
        pts = vtk.vtkPoints()
        pts.SetData(dsa.numpyTovtkDataArray(data,"Points"))

        output.SetPoints(pts)
        #make single cell
        numpts = pts.GetNumberOfPoints()
        ids = vtk.vtkIdList()
        ids.SetNumberOfIds(numpts)
        for a in range(numpts):
            ids.SetId(a,a)

        output.Allocate(1)
        output.InsertNextCell(vtk.VTK_POLY_VERTEX,ids)
        #add scalar data to output
        output.PointData.append(intensity,"intensity")

        if data_time is not None:
            output.GetInformation().Set(output.DATA_TIME_STEP(), data_time)
        return 1
