import os
import re
import pandas as pd
import vcgencmd
#import pickle as pk

from time import sleep
from gpiozero import CPUTemperature

__cpuObj = CPUTemperature()
__df = pd.DataFrame({'cpu':[0.0], 'gpu':[0.0], 'carm':[0], 'ccore':[0],
                     'ch264':[0], 'cuart':[0], 'cpwm':[0], 'chdmi':[0],
                     'vcore':[0], 'sdram_c':[0], 'sdram_i':[0], 'sdram_p':[0],
                     'coh264':[''], 'compg2':[''], 'compg4':[''], 'cowvc1':[''], 'comjpg':[''],
                     'mcpu':[0], 'mgpu':[0]
                     })

while True:
    __gpu = os.popen("vcgencmd measure_temp").readline()
    __gpu = float(re.sub("[^0-9.\-]", "", __gpu))
    __cpu = __cpuObj.temperature

    ######  Clocks    ########
    __carm   = vcgencmd.measure_clock('arm')
    __ccore  = vcgencmd.measure_clock('core')
    __ch264  = vcgencmd.measure_clock('h264')
    __cuart  = vcgencmd.measure_clock('uart')
    __cpwm   = vcgencmd.measure_clock('pwm')
    __chdmi  = vcgencmd.measure_clock('hdmi')
    #####   Volts   ##########
    __vcore   = vcgencmd.measure_volts('core')
    __sdram_c = vcgencmd.measure_volts('sdram_c')
    __sdram_i = vcgencmd.measure_volts('sdram_i')
    __sdram_p = vcgencmd.measure_volts('sdram_p')
    ######  Codecs ###########
    __coh264 = vcgencmd.codec_enabled('h264')
    __compg2 = vcgencmd.codec_enabled('mpg2')
    __compg4 = vcgencmd.codec_enabled('mpg4')
    __cowvc1 = vcgencmd.codec_enabled('wvc1')
    __comjpg = vcgencmd.codec_enabled('mjpg')
    ######  mem  #############
    __mcpu = vcgencmd.get_mem('arm')
    __mgpu = vcgencmd.get_mem('gpu')


    __tempInfos = {'cpu':__cpu, 'gpu':__gpu, 'carm':__carm, 'ccore':__ccore,
                   'ch264':__ch264, 'cuart':__cuart, 'cpwm':__cpwm, 'chdmi':__chdmi,
                   'vcore':__vcore, 'sdram_c':__sdram_c, 'sdram_i':__sdram_i, 'sdram_p':__sdram_p,
                   'coh264':__coh264, 'compg2':__compg2, 'compg4':__compg4, 'cowvc1':__cowvc1,
                   'comjpg':__comjpg, 'mcpu':__mcpu, 'mgpu':__mgpu
                   }

    __df = __df.append(__tempInfos, ignore_index=True) 
    try:
        __df.to_csv('data.csv')
    except:
        pass
    sleep(5)

