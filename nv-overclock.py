# https://www.reddit.com/r/linux_gaming/comments/17kx3vu/how_to_crudely_overclock_your_nvidia_gpu_on/
# systemctl restart nvidia-undervolt

from pynvml import *

nvmlInit()

#This sets the GPU to adjust - if this gives you errors or you have multiple GPUs, set to 1 or try other values

myGPU = nvmlDeviceGetHandleByIndex(0)

nvmlDeviceSetPersistenceMode (myGPU, 1)

nvmlDeviceSetPowerManagementLimit (myGPU, 310000)
# nvmlDeviceSetGpuLockedClocks (myGPU, 210,2970)

# 295/1100 works fine in windows 
# 300/1200 crash blender
# 295/1000 crash AMWF
# 290/900 crash AMWF
# 285/800 crash AMWF
# 280/600 crash AMWF
# 266/0 works fine AMWF, so good interval between 0-600 memory and unknown CPU
# 285/500 crash Blonde Angel
# 266/250 works fine Blonde Angel, good ram in 250-500
# 266/400 works, small file, +1. Good Mem near 400, try to raise GPU
# 295/400 error, I'm so horny. Failed, try to reduce GPU significantly and memory a bit
# 280/350 error, I'm so horny. Failed, try to ensure that 266/400 works for this problem file
# 266/400 ok, I'm so horny. Seems like 266 for cpu is max, try to increase memory
# 266/500 ok, large model. Try to speedup memory again
# 266/600 crash, so good values below 266/600, ensure that 266/500 stable
# 266/500 ok, a lot of tests, try to raise clock a little, 280/500 already problems
# 272/500 ok, continue test. 285/500 and 266/600 are known crash
# 272/550 ok
# 272/575 error 
# 278 575 error
# 272/587 error
# 266 / 550 error
# 266 / 500 error
# 266 / 450 error
# 255 / 450 error
# 255 / 400 error
# 240 / 400 super-ok
# 240 / 450 ok
# 240 / 1700 ok
# 240 / 2000 ok 
# 240 / 2500 ok
# 240 / 3000 ok
# 240 / 3500 ok
# 240 2500 / error
# 235/2400 - cpu crash
# 235/2000 - crash
# 230/1900 - crash
# 225/1850

nvmlDeviceSetGpcClkVfOffset (myGPU, 225)
nvmlDeviceSetMemClkVfOffset (myGPU, 1850)

# reset overclock to default
#nvmlDeviceSetGpcClkVfOffset (myGPU, 0)
#nvmlDeviceSetMemClkVfOffset (myGPU, 0)

#my4060 = nvmlDeviceGetHandleByIndex(1)
#nvmlDeviceSetPersistenceMode(my4060, 1)
#nvmlDeviceSetPowerManagementLimit(my4060, 130000)

##################################################
# NVidia Tesla P40
#################################################

myGPUTesla = nvmlDeviceGetHandleByIndex(1)

nvmlDeviceSetPersistenceMode (myGPUTesla, 1)

nvmlDeviceSetPowerManagementLimit (myGPUTesla, 225000)
# Clocks hardcoded