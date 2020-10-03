import sys
from PySide2.QtWidgets import QApplication
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl, pyqtProperty, pyqtSlot, pyqtSignal, QVariant

from time import sleep 
import pandas as pd
import numpy as  np

class CPUInfo(QObject):
    def __init__(self):
        QObject.__init__(self)
        
        self.ctemp, self.gtemp, self.time = [], [], []
        self.cpuAvg, self.gpuAvg = 0.0, 0.0
        
        self.carm, self.ccore, self.ch264 = 0, 0, 0
        self.cuart, self.cpwm, self.chdmi = 0, 0, 0
        self.vcore, self.sdram_c, self.sdram_i, self.sdram_p = 0.0, 0.0, 0.0, 0.0
        self.coh264, self.compg2, self.compg4 = False, False, False
        self.cowvc1, self.comjpg = False, False        
        self.mcpu, self.mgpu = 0, 0
        
        
        
        
        
    cpuSig  = pyqtSignal(list)
    gpuSig  = pyqtSignal(list)
    timeSig = pyqtSignal(list)
    
    cpuAvgSig = pyqtSignal(float)
    gpuAvgSig = pyqtSignal(float)
    
    
    #************  1  **************#
    
    carmSig  = pyqtSignal(int)
    ccoreSig  = pyqtSignal(int)
    ch264Sig  = pyqtSignal(int)
    
    cuartSig  = pyqtSignal(int)
    cpwmSig   = pyqtSignal(int)
    chdmiSig  = pyqtSignal(int)
     
    
    #************  2  ****************#
    
    vcoreSig    = pyqtSignal(float)
    sdram_cSig  = pyqtSignal(float)
    sdram_iSig  = pyqtSignal(float)
    sdram_pSig  = pyqtSignal(float)
    
    #*********** 3 ******************#
    
    coh264Sig    = pyqtSignal(bool)
    compg2Sig    = pyqtSignal(bool)
    compg4Sig    = pyqtSignal(bool)
    cowvc1Sig    = pyqtSignal(bool)
    comjpgSig    = pyqtSignal(bool)
    
    #********** 4 *******************#
    
    mcpuSig = pyqtSignal(int)
    mgpuSig = pyqtSignal(int)
        
    def setCputemp(self, temp):
        if self.ctemp != temp:
            self.ctemp = temp
        self.cpuSig.emit(self.ctemp)
            
    def getCputemp(self):
        return self.ctemp
        
    def setGputemp(self, temp):
        if self.gtemp != temp:
            self.gtemp = temp
        self.gpuSig.emit(self.gtemp)
            
    def getGputemp(self):
        return self.gtemp
        
    def setTime(self, t):
        if self.time != t:
            self.time = t
        self.timeSig.emit(self.time)
            
    def getTime(self):
        return self.time
    
    def setCpuAvg(self, temp):
        if self.cpuAvg != temp:
            self.cpuAvg = temp
        self.cpuAvgSig.emit(self.cpuAvg)
            
    def getCpuAvg(self):
        return self.cpuAvg
    
    def setGpuAvg(self, temp):
        if self.gpuAvg != temp:
            self.gpuAvg = temp
        self.gpuAvgSig.emit(self.gpuAvg)
            
    def getGpuAvg(self):
        return self.gpuAvg
        
    
    def setCarm(self, arm):
        if self.carm != arm:
            self.carm = arm
        self.carmSig.emit(self.carm)
    
    def getCarm(self):
        return self.carm
    
    def setCcore(self, core):
        if self.ccore != core:
            self.ccore = core
        self.ccoreSig.emit(self.ccore)
    
    def getCcore(self):
        return self.ccore
    
    def setCh264(self, h264):
        if self.ch264 != h264:
            self.ch264 = h264
        self.ch264Sig.emit(self.ch264)
    
    def getCh264(self):
        return self.ch264
    
    def setCuart(self, uart):
        if self.cuart != uart:
            self.cuart = uart
        self.cuartSig.emit(self.cuart)
    
    def getCuart(self):
        return self.cuart
    
    def setCpwm(self, pwm):
        if self.cpwm != pwm:
            self.cpwm = pwm
        self.cpwmSig.emit(self.cpwm)
    
    def getCpwm(self):
        return self.cpwm
    
    
    def setChdmi(self, hdmi):
        if self.chdmi != hdmi:
            self.chdmi = hdmi
        self.chdmiSig.emit(self.chdmi)
    
    def getChdmi(self):
        return self.chdmi
    
    
    def setVcore(self, core):
        if self.vcore != core:
            self.vcore = core
        self.vcoreSig.emit(self.vcore)
    
    def getVcore(self):
        return self.vcore
    
    
    def setSdram_c(self, ram):
        if self.sdram_c != ram:
            self.sdram_c = ram
        self.sdram_cSig.emit(self.sdram_c)
    
    def getSdram_c(self):
        return self.sdram_c
    
    
    def setSdram_i(self, ram):
        if self.sdram_i != ram:
            self.sdram_i = ram
        self.sdram_iSig.emit(self.sdram_i)
    
    def getSdram_i(self):
        return self.sdram_i
    
    
    def setSdram_p(self, ram):
        if self.sdram_p != ram:
            self.sdram_p = ram
        self.sdram_pSig.emit(self.sdram_p)
    
    def getSdram_p(self):
        return self.sdram_p
    
    
    def setCoh264(self, h):
        if self.coh264 != h:
            self.coh264 = h
        self.coh264Sig.emit(self.coh264)
    
    def getCoh264(self):
        return self.coh264
    
    def setCompg2(self, h):
        if self.compg2 != h:
            self.compg2 = h
        self.compg2Sig.emit(self.compg2)
    
    def getCompg2(self):
        return self.compg2
    
    def setCompg4(self, h):
        if self.compg4 != h:
            self.compg4 = h
        self.compg4Sig.emit(self.compg4)
    
    def getCompg4(self):
        return self.compg4
    
    
    def setCowvc1(self, h):
        if self.cowvc1 != h:
            self.cowvc1 = h
        self.cowvc1Sig.emit(self.cowvc1)
    
    def getCowvc1(self):
        return self.cowvc1
    
        
    def setComjpg(self, h):
        if self.comjpg != h:
            self.comjpg = h
        self.comjpgSig.emit(self.comjpg)
    
    def getComjpg(self):
        return self.comjpg
 
 
         
    def setMcpu(self, u):
        if self.mcpu != u:
            self.mcpu = u
        self.mcpuSig.emit(self.mcpu)
    
    def getMcpu(self):
        return self.mcpu   
    
             
    def setMgpu(self, u):
        if self.mgpu != u:
            self.mgpu = u
        self.mgpuSig.emit(self.mgpu)
    
    def getMgpu(self):
        return self.mgpu
    
       
    @pyqtSlot()
    def sig(self):
        try:
            data = pd.read_csv("data.csv")
        except:
            pass
        
        data = pd.read_csv("data.csv")
        time = np.arange(len(data['cpu'].tolist()))
        cavg = format(np.mean(data['cpu'].to_numpy()), '.1f')
        gavg = format(np.mean(data['gpu'].to_numpy()), '.1f')
         
                     
        self.setCputemp(data['cpu'].tolist())
        self.setGputemp(data['gpu'].tolist())               
        self.setTime(time.tolist())
        self.setCpuAvg(float(cavg))     
        self.setGpuAvg(float(gavg))       
        
        #*********************************#
        self.setCarm(data['carm'].to_numpy()[-1])
        self.setCcore(data['ccore'].to_numpy()[-1])
        self.setCh264(data['ch264'].to_numpy()[-1])
        self.setCuart(data['cuart'].to_numpy()[-1])
        self.setCpwm(data['cpwm'].to_numpy()[-1])
        self.setChdmi(data['chdmi'].to_numpy()[-1])
        
        
        vc = float(format(data['vcore'].to_numpy()[-1],'.3f'))
        vs = float(format(data['sdram_c'].to_numpy()[-1],'.3f'))
        vi = float(format(data['sdram_i'].to_numpy()[-1],'.3f'))
        vp = float(format(data['sdram_p'].to_numpy()[-1],'.3f'))

        self.setVcore(vc)
        self.setSdram_c(vs)
        self.setSdram_i(vi)
        self.setSdram_p(vp)
        
        
        self.setCoh264(data['coh264'].tolist()[-1])
        self.setCompg2(data['compg2'].tolist()[-1])
        self.setCompg4(data['compg4'].tolist()[-1])
        self.setCowvc1(data['cowvc1'].tolist()[-1])
        self.setComjpg(data['comjpg'].tolist()[-1])
        
        self.setMcpu(data['mcpu'].to_numpy()[-1])
        self.setMgpu(data['mgpu'].to_numpy()[-1])
        
                     
    sig_cpu  = pyqtProperty(list, getCputemp, notify=cpuSig)
    sig_gpu  = pyqtProperty(list, getGputemp, notify=gpuSig)
    sig_time = pyqtProperty(list, getTime, notify=timeSig)
    sig_cavg = pyqtProperty(float, getCpuAvg, notify=cpuAvgSig)
    sig_gavg = pyqtProperty(float, getGpuAvg, notify=gpuAvgSig)
    
    sig_carm    = pyqtProperty(int, getCarm, notify=carmSig)
    sig_ccore   = pyqtProperty(int, getCcore, notify=ccoreSig)
    sig_ch264   = pyqtProperty(int, getCh264, notify=ch264Sig)
    sig_cuart   = pyqtProperty(int, getCuart, notify=cuartSig)
    sig_cpwm    = pyqtProperty(int, getCpwm, notify=cpwmSig)
    sig_chdmi   = pyqtProperty(int, getChdmi, notify=chdmiSig)
    
    
    sig_vcore   = pyqtProperty(float, getVcore, notify=vcoreSig)
    sig_sdram_c = pyqtProperty(float, getSdram_c, notify=sdram_cSig)
    sig_sdram_i = pyqtProperty(float, getSdram_i, notify=sdram_iSig)
    sig_sdram_p = pyqtProperty(float, getSdram_p, notify=sdram_pSig)
    
     
    sig_coh264  = pyqtProperty(bool, getCoh264, notify=coh264Sig)
    sig_compg2  = pyqtProperty(bool, getCompg2, notify=compg2Sig)
    sig_compg4  = pyqtProperty(bool, getCompg4, notify=compg4Sig)
    sig_comjpg  = pyqtProperty(bool, getComjpg, notify=comjpgSig)
    sig_cowvc1  = pyqtProperty(bool, getCowvc1, notify=cowvc1Sig)
    
    
    sig_mcpu  = pyqtProperty(int, getMcpu, notify=mcpuSig)
    sig_mgpu  = pyqtProperty(int, getMgpu, notify=mgpuSig)
        
        
        
    """ 
    @pyqtSlot()
    def sig(self):           
        while True:
            try:
                data = pd.read_csv("data.csv")
            except:
               pass
                
            t = np.arange(len(data['cpu'].tolist()))              
            self.setCputemp(data['cpu'].tolist())
            self.setCputemp(data['gpu'].tolist())                
            self.setTime(t.tolist())
                
                
            self.sig_cpu  = pyqtProperty(list, self.getCputemp, notify=self.cpuSig)
            self.sig_gpu  = pyqtProperty(list, self.getGputemp, notify=self.gpuSig)
            self.sig_time = pyqtProperty(list, self.getTime, notify=self.timeSig)
                
            sleep(15)
    """    
                
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    CPU = CPUInfo()
    engine.rootContext().setContextProperty("CPU",CPU)
    engine.load(QUrl("/home/mohamedlassine/Desktop/Programming/qml/SOURCE CODE/RPiCPUInfo/RPiCPUInfo.qml"))
    sys.exit(app.exec_())
          