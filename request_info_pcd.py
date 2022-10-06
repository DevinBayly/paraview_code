# Code for 'RequestInformation Script'.
from pathlib import Path
def setOutputTimesteps(algorithm, timesteps):
    "helper routine to set timestep information"
    executive = algorithm.GetExecutive()
    outInfo = executive.GetOutputInformation(0)

    outInfo.Remove(executive.TIME_STEPS())
    for timestep in timesteps:
        outInfo.Append(executive.TIME_STEPS(), timestep)

    outInfo.Remove(executive.TIME_RANGE())
    outInfo.Append(executive.TIME_RANGE(), timesteps[0])
    outInfo.Append(executive.TIME_RANGE(), timesteps[-1])

# As an example, let's say we have 4 files in the file series that we
# want to say are producing time 0, 10, 20, and 30.
pth = Path("/xdisk/chrisreidy/baylyd/Sama_lidar/temp/babel_pcl")
npy_pcls = list(Path(pth).rglob("*.npy"))
times = [i for i,f in enumerate(npy_pcls)]
print("times are",times)
setOutputTimesteps(self, times)

