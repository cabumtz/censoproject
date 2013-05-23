'''
Created on 01/04/2013

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


class DjangoProcess(object):
    
    logger = logging.getLogger("djangoutil")
    _process = None
    
    def __init__(self, parent=None):
        DjangoProcess.logger.debug("__init__ - begin")
        self._process = QtCore.QProcess(parent)
        DjangoProcess.logger.debug("__init__ - end")
        pass
    
    def startProcess(self, program, argumentList="", workingdir="."):
        
        DjangoProcess.logger.debug("startProcess - program: %s, argumentList: %s, workingdir: %s" % (program, argumentList, workingdir))
        self._process.setWorkingDirectory(workingdir)
        self._process.start(program, argumentList)
        DjangoProcess.logger.debug("startProcess - started")
        pass
    
    
    def stopProcess(self):
        DjangoProcess.logger.debug("stopProcess - stopping")
        
        procinfo = ProcessInformation.from_address(int(self._process.pid()))
        realPid = procinfo.dwProcessId
        DjangoProcess.logger.debug("stopProcess - pid: %s :: %s :: %s" % ( self._process.pid(), self._process.pid().__int__(), realPid ) )
        #os.kill( realPid , signal.SIGINT)
        os.kill( realPid , signal.SIGBREAK)
        #os.kill( realPid , signal.SIGINT)
        self._process.writeData("exit()")
        self._process.close()
        
        #self._process = None
        DjangoProcess.logger.debug("stopProcess - aparently stopped")
        pass
    
    def getProcess(self):
        return self._process

    