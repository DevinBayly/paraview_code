# state file generated using paraview version 5.11.0-RC1
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
renderView1.ViewSize = [1314, 550]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [3.19286, -0.0782775, -0.25033]
renderView1.CameraViewUp = [0.05492060184057174, 0.90735503040848, 0.416762013967079]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.9527593400091033
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1314, 550)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Cone'
cone1 = Cone(registrationName='Cone1')

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from cone1
cone1Display = Show(cone1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
cone1Display.Representation = 'Surface'
cone1Display.ColorArrayName = [None, '']
cone1Display.SelectTCoordArray = 'None'
cone1Display.SelectNormalArray = 'None'
cone1Display.SelectTangentArray = 'None'
cone1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cone1Display.SelectOrientationVectors = 'None'
cone1Display.ScaleFactor = 0.1
cone1Display.SelectScaleArray = 'None'
cone1Display.GlyphType = 'Arrow'
cone1Display.GlyphTableIndexArray = 'None'
cone1Display.GaussianRadius = 0.005
cone1Display.SetScaleArray = [None, '']
cone1Display.ScaleTransferFunction = 'PiecewiseFunction'
cone1Display.OpacityArray = [None, '']
cone1Display.OpacityTransferFunction = 'PiecewiseFunction'
cone1Display.DataAxesGrid = 'GridAxesRepresentation'
cone1Display.PolarAxes = 'PolarAxesRepresentation'
cone1Display.SelectInputVectors = [None, '']
cone1Display.WriteLog = ''

# ----------------------------------------------------------------
# restore active source
SetActiveSource(cone1)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
