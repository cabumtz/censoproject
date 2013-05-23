'''
Created on 20/04/2013

@author: WICO MX 2
'''
import logging
import sip
import ctypes
from ctypes import wintypes

# import this
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

from PyQt4 import QtCore

import os
import signal


class ProcessInformation(ctypes.Structure):
    _fields_ = [('hProcess', wintypes.HANDLE),
                ('hThread', wintypes.HANDLE),
                ('dwProcessId', wintypes.DWORD),
                ('dwThreadId', wintypes.DWORD)]


class DjangoProcess(QtCore.QProcess):
    '''
    classdocs
    '''
    logger = logging.getLogger("djangoprocess")

    def __init__(self, parent=None, djangoexecpath=None, djangoargs="", workingdir=".", objectName=""):
        '''
        Constructor
        '''
        DjangoProcess.logger.debug("__init__ - begin")
        super(DjangoProcess, self).__init__(parent)
        DjangoProcess.logger.debug("__init__ - end")
        self.djangoexexpath = djangoexecpath
        self.djangoargs = djangoargs
        
        self.workingdir = workingdir
        self.setWorkingDirectory(self.workingdir)
        self.setObjectName(objectName)
        pass
        
    def start(self):
        DjangoProcess.logger.debug("start - init")
        super(DjangoProcess, self).start(self.djangoexexpath, self.djangoargs)
        DjangoProcess.logger.debug("start - finished")
        pass
    
    def stop(self):
        DjangoProcess.logger.debug("stop - init")
        
        procinfo = ProcessInformation.from_address(int(self.pid()))
        realPid = procinfo.dwProcessId
        DjangoProcess.logger.debug("stop - pid: %s :: %s :: %s" % ( self.pid(), self.pid().__int__(), realPid ) )
        
        #os.kill( realPid , signal.SIGINT)
        #os.kill( realPid , signal.SIGBREAK)
        os.kill( realPid , signal.SIGINT)
        
        self.close()
        
        DjangoProcess.logger.debug("stop - aparently stopped")
        pass
        
        