"""This module demonstrates various ways of adding
VTKPythonAlgorithmBase subclasses as filters, sources, readers,
and writers in ParaView"""


# This is module to import. It provides VTKPythonAlgorithmBase, the base class
# for all python-based vtkAlgorithm subclasses in VTK and decorators used to
# 'register' the algorithm with ParaView along with information about UI.
from paraview.util.vtkAlgorithm import *
import uuid
from pathlib import Path

import numpy as np

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

# To add a reader, we can use the following decorators
#   @smproxy.source(name="PythonnumpyReader", label="Python-based numpy Reader")
#   @smhint.xml("""<ReaderFactory extensions="csv" file_description="Numpy numpy files" />""")
# or directly use the "@reader" decorator.
@smproxy.reader(name="Sama Lidar Full Model Numpy Reader", label="Python-based numpy pcd Reader for full models",
                extensions="npy",
                 file_description="numpy files")
class PythonNumpyPCDFullModelReader(VTKPythonAlgorithmBase):
    """A reader that reads a numpy file. If the numpy has a "time" column, then
    the data is treated as a temporal dataset"""
    def __init__(self):
        VTKPythonAlgorithmBase.__init__(self, nInputPorts=0, nOutputPorts=1, outputType='vtkTable')
        self._filename = None
        self._ndata = None
        print("starting",uuid.uuid1())

        from vtkmodules.vtkCommonCore import vtkDataArraySelection
        self._arrayselection = vtkDataArraySelection()
        self._arrayselection.AddObserver("ModifiedEvent", createModifiedCallback(self))

    def _get_raw_data(self, requested_time=None):

        # self._ndata = numpy.genfromtxt(self._filename, dtype=None, names=True, delimiter=',', autostrip=True)
        self.pth = Path(self._filename)
        self._ndata = np.load(self.pth)

        return self._ndata


    @smproperty.stringvector(name="FileName")
    @smdomain.filelist()
    @smhint.filechooser(extensions="npy", file_description="numpy pcd file")
    def SetFileName(self, name):
        """Specify filename for the file to read."""
        print(name)
        if self._filename != name:
            self._filename = name
            self._ndata = None
            self.Modified()


    def RequestData(self, request, inInfoVec, outInfoVec):
        print("requesting data")
        from vtkmodules.vtkCommonDataModel import vtkTable
        from vtkmodules.numpy_interface import dataset_adapter as dsa

        output = dsa.WrapDataObject(vtkTable.GetData(outInfoVec, 0))
        self._get_raw_data()
        raw_data = self._ndata
        print(raw_data)
        # for name in raw_data.dtype.names:
        #     if self._arrayselection.ArrayIsEnabled(name):
        #         output.RowData.append(raw_data[name], name)
        output.RowData.append(raw_data[:,0],"x")
        output.RowData.append(raw_data[:,1],"y")
        output.RowData.append(raw_data[:,2],"z")
        output.RowData.append(raw_data[:,3],"intensity")

        return 1
