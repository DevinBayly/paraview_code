# state file generated using paraview version 5.11.0-RC2
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1428, 789]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [50.00001623673597, 49.999972780919734, 50.000000539279995]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-284.60635836417435, 49.999972780919734, 50.000000539279995]
renderView1.CameraFocalPoint = [50.00001623673597, 49.999972780919734, 50.000000539279995]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 86.60250235942397
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1428, 789)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Programmable Source'
programmableSource1 = ProgrammableSource(registrationName='ProgrammableSource1')
programmableSource1.Script = """import h5py
from pathlib import Path
import numpy as np
from vtk.numpy_interface import algorithms as algs
from vtk.numpy_interface import dataset_adapter as dsa

pth = list(Path.home().rglob("*position*h5"))[0]
f = h5py.File(str(pth))
keys = list(f.keys())

data = f[keys[0]][:]
#print(data)


# make vtk points
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
#add scalar data to output"""
programmableSource1.ScriptRequestInformation = ''
programmableSource1.PythonPath = ''

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=programmableSource1,
    GlyphType='2D Glyph')
glyph1.OrientationArray = ['POINTS', 'No orientation array']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 9.999999892144002
glyph1.GlyphTransform = 'Transform2'
glyph1.GlyphMode = 'Every Nth Point'

# init the '2D Glyph' selected for 'GlyphType'
glyph1.GlyphType.GlyphType = 'Vertex'

# create a new 'Programmable Filter'
programmableFilter1 = ProgrammableFilter(registrationName='ProgrammableFilter1', Input=glyph1)
programmableFilter1.OutputDataSetType = 'vtkImageData'
programmableFilter1.Script = """from vtk.vtkFiltersPoints import vtkPointDensityFilter

bounds = inputs[0].GetBounds()
hBin = vtkPointDensityFilter()
hBin.SetInputData(inputs[0].VTKObject)
hBin.SetModelBounds(bounds)
hBin.SetSampleDimensions(self.dims)
hBin.Update()
output.ShallowCopy(hBin.GetOutput())"""
programmableFilter1.RequestInformationScript = """executive = self.GetExecutive ()
outInfo = executive.GetOutputInformation(0)

self.dims = [512]*3
outInfo.Set(executive.WHOLE_EXTENT(), 0, self.dims[0]-1 , 0, self.dims[1]-1 , 0, self.dims[2]-1)
"""
programmableFilter1.RequestUpdateExtentScript = ''
programmableFilter1.PythonPath = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from programmableSource1
programmableSource1Display = Show(programmableSource1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
programmableSource1Display.Representation = 'Outline'
programmableSource1Display.ColorArrayName = ['POINTS', '']
programmableSource1Display.SelectTCoordArray = 'None'
programmableSource1Display.SelectNormalArray = 'None'
programmableSource1Display.SelectTangentArray = 'None'
programmableSource1Display.OSPRayScaleFunction = 'PiecewiseFunction'
programmableSource1Display.SelectOrientationVectors = 'None'
programmableSource1Display.ScaleFactor = -0.2
programmableSource1Display.SelectScaleArray = 'None'
programmableSource1Display.GlyphType = 'Arrow'
programmableSource1Display.GlyphTableIndexArray = 'None'
programmableSource1Display.GaussianRadius = -0.01
programmableSource1Display.SetScaleArray = ['POINTS', '']
programmableSource1Display.ScaleTransferFunction = 'PiecewiseFunction'
programmableSource1Display.OpacityArray = ['POINTS', '']
programmableSource1Display.OpacityTransferFunction = 'PiecewiseFunction'
programmableSource1Display.DataAxesGrid = 'GridAxesRepresentation'
programmableSource1Display.PolarAxes = 'PolarAxesRepresentation'
programmableSource1Display.SelectInputVectors = ['POINTS', '']
programmableSource1Display.WriteLog = ''

# show data from programmableFilter1
programmableFilter1Display = Show(programmableFilter1, renderView1, 'UniformGridRepresentation')

# get 2D transfer function for 'ImageScalars'
imageScalarsTF2D = GetTransferFunction2D('ImageScalars')
imageScalarsTF2D.ScalarRangeInitialized = 1
imageScalarsTF2D.Range = [0.0, 21234.0, 0.0, 1.0]

# get color transfer function/color map for 'ImageScalars'
imageScalarsLUT = GetColorTransferFunction('ImageScalars')
imageScalarsLUT.TransferFunction2D = imageScalarsTF2D
imageScalarsLUT.RGBPoints = [0.0, 0.301961, 0.047059, 0.090196, 348.0304868102076, 0.396078431372549, 0.0392156862745098, 0.058823529411764705, 696.0609736204141, 0.49411764705882355, 0.054901960784313725, 0.03529411764705882, 1044.0914604306229, 0.5882352941176471, 0.11372549019607843, 0.023529411764705882, 1392.1219472408293, 0.6627450980392157, 0.16862745098039217, 0.01568627450980392, 1740.1524340510368, 0.7411764705882353, 0.22745098039215686, 0.00392156862745098, 2088.1829208612444, 0.788235294117647, 0.2901960784313726, 0.0, 2436.2134076714515, 0.8627450980392157, 0.3803921568627451, 0.011764705882352941, 2784.243894481659, 0.9019607843137255, 0.4588235294117647, 0.027450980392156862, 3132.274381291866, 0.9176470588235294, 0.5215686274509804, 0.047058823529411764, 3480.3048681020737, 0.9254901960784314, 0.5803921568627451, 0.0784313725490196, 3828.3353549122808, 0.9372549019607843, 0.6431372549019608, 0.12156862745098039, 4176.365841722488, 0.9450980392156862, 0.7098039215686275, 0.1843137254901961, 4524.396328532696, 0.9529411764705882, 0.7686274509803922, 0.24705882352941178, 4872.426815342903, 0.9647058823529412, 0.8274509803921568, 0.3254901960784314, 5220.4573021531105, 0.9686274509803922, 0.8784313725490196, 0.4235294117647059, 5568.487788963318, 0.9725490196078431, 0.9176470588235294, 0.5137254901960784, 5916.518275773526, 0.9803921568627451, 0.9490196078431372, 0.596078431372549, 6264.548762583732, 0.9803921568627451, 0.9725490196078431, 0.6705882352941176, 6612.57924939394, 0.9882352941176471, 0.9882352941176471, 0.7568627450980392, 6946.688516731739, 0.984313725490196, 0.9882352941176471, 0.8549019607843137, 6960.609736204147, 0.9882352941176471, 0.9882352941176471, 0.8588235294117647, 6960.822076204147, 0.9529411764705882, 0.9529411764705882, 0.8941176470588236, 6960.822076204147, 0.9529411764705882, 0.9529411764705882, 0.8941176470588236, 7322.241250814091, 0.8901960784313725, 0.8901960784313725, 0.807843137254902, 7683.660425424033, 0.8274509803921568, 0.8235294117647058, 0.7372549019607844, 8045.079600033976, 0.7764705882352941, 0.7647058823529411, 0.6784313725490196, 8406.498774643918, 0.7254901960784313, 0.7137254901960784, 0.6274509803921569, 8767.917949253862, 0.6784313725490196, 0.6627450980392157, 0.5803921568627451, 9129.337123863805, 0.6313725490196078, 0.6078431372549019, 0.5333333333333333, 9490.756298473747, 0.5803921568627451, 0.5568627450980392, 0.48627450980392156, 9852.175473083691, 0.5372549019607843, 0.5058823529411764, 0.44313725490196076, 10213.594647693635, 0.4980392156862745, 0.4588235294117647, 0.40784313725490196, 10575.013822303577, 0.4627450980392157, 0.4196078431372549, 0.37254901960784315, 10936.43299691352, 0.43137254901960786, 0.38823529411764707, 0.34509803921568627, 11297.852171523462, 0.403921568627451, 0.3568627450980392, 0.3176470588235294, 11659.271346133406, 0.37254901960784315, 0.3215686274509804, 0.29411764705882354, 12020.690520743348, 0.34509803921568627, 0.29411764705882354, 0.26666666666666666, 12382.10969535329, 0.3176470588235294, 0.2627450980392157, 0.23921568627450981, 12743.528869963235, 0.28627450980392155, 0.23137254901960785, 0.21176470588235294, 13104.948044573177, 0.2549019607843137, 0.2, 0.1843137254901961, 13466.36721918312, 0.23137254901960785, 0.17254901960784313, 0.16470588235294117, 13827.786393793063, 0.2, 0.1450980392156863, 0.13725490196078433, 14189.417908403007, 0.14902, 0.196078, 0.278431, 14893.876117562704, 0.2, 0.2549019607843137, 0.34509803921568627, 15598.334326722405, 0.24705882352941178, 0.3176470588235294, 0.41568627450980394, 16302.792535882105, 0.3058823529411765, 0.38823529411764707, 0.49411764705882355, 17007.250745041805, 0.37254901960784315, 0.4588235294117647, 0.5686274509803921, 17711.708954201502, 0.44313725490196076, 0.5333333333333333, 0.6431372549019608, 18416.167163361202, 0.5176470588235295, 0.615686274509804, 0.7254901960784313, 19120.625372520903, 0.6, 0.6980392156862745, 0.8, 19825.0835816806, 0.6862745098039216, 0.7843137254901961, 0.8705882352941177, 20529.5417908403, 0.7607843137254902, 0.8588235294117647, 0.9294117647058824, 20881.77089542015, 0.807843137254902, 0.9019607843137255, 0.9607843137254902, 21234.0, 0.8901960784313725, 0.9568627450980393, 0.984313725490196]
imageScalarsLUT.ColorSpace = 'Lab'
imageScalarsLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'ImageScalars'
imageScalarsPWF = GetOpacityTransferFunction('ImageScalars')
imageScalarsPWF.Points = [0.0, 0.0, 0.5, 0.0, 21234.0, 1.0, 0.5, 0.0]
imageScalarsPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
programmableFilter1Display.Representation = 'Volume'
programmableFilter1Display.ColorArrayName = ['POINTS', 'ImageScalars']
programmableFilter1Display.LookupTable = imageScalarsLUT
programmableFilter1Display.SelectTCoordArray = 'None'
programmableFilter1Display.SelectNormalArray = 'None'
programmableFilter1Display.SelectTangentArray = 'None'
programmableFilter1Display.OSPRayScaleArray = 'ImageScalars'
programmableFilter1Display.OSPRayScaleFunction = 'PiecewiseFunction'
programmableFilter1Display.SelectOrientationVectors = 'None'
programmableFilter1Display.ScaleFactor = 9.99827702464536
programmableFilter1Display.SelectScaleArray = 'ImageScalars'
programmableFilter1Display.GlyphType = 'Arrow'
programmableFilter1Display.GlyphTableIndexArray = 'ImageScalars'
programmableFilter1Display.GaussianRadius = 0.49991385123226795
programmableFilter1Display.SetScaleArray = ['POINTS', 'ImageScalars']
programmableFilter1Display.ScaleTransferFunction = 'PiecewiseFunction'
programmableFilter1Display.OpacityArray = ['POINTS', 'ImageScalars']
programmableFilter1Display.OpacityTransferFunction = 'PiecewiseFunction'
programmableFilter1Display.DataAxesGrid = 'GridAxesRepresentation'
programmableFilter1Display.PolarAxes = 'PolarAxesRepresentation'
programmableFilter1Display.ScalarOpacityUnitDistance = 0.3388726861690938
programmableFilter1Display.ScalarOpacityFunction = imageScalarsPWF
programmableFilter1Display.TransferFunction2D = imageScalarsTF2D
programmableFilter1Display.OpacityArrayName = ['POINTS', 'ImageScalars']
programmableFilter1Display.ColorArray2Name = ['POINTS', 'ImageScalars']
programmableFilter1Display.IsosurfaceValues = [11.0]
programmableFilter1Display.SliceFunction = 'Plane'
programmableFilter1Display.Slice = 255
programmableFilter1Display.SelectInputVectors = [None, '']
programmableFilter1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
programmableFilter1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 22.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
programmableFilter1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 22.0, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
programmableFilter1Display.SliceFunction.Origin = [49.995530823711306, 50.00077185919508, 49.98759685468394]

# setup the color legend parameters for each legend in this view

# get color legend/bar for imageScalarsLUT in view renderView1
imageScalarsLUTColorBar = GetScalarBar(imageScalarsLUT, renderView1)
imageScalarsLUTColorBar.Orientation = 'Horizontal'
imageScalarsLUTColorBar.WindowLocation = 'Any Location'
imageScalarsLUTColorBar.Position = [0.3334615384615386, 0.9063624841571606]
imageScalarsLUTColorBar.Title = 'GasDensity'
imageScalarsLUTColorBar.ComponentTitle = ''
imageScalarsLUTColorBar.ScalarBarLength = 0.32999999999999996

# set color bar visibility
imageScalarsLUTColorBar.Visibility = 1

# show color legend
programmableFilter1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(programmableFilter1)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
