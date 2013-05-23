'''
Created on 26/03/2013

@author: Carlos
'''

import sip
from magmasoft.censomanager.util.djangoutil import DjangoProcess
import logging

# import this
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

from PyQt4 import QtGui, QtCore, QtNetwork
#import PyQt4.QtCore.QStringList


from magmasoft.censomanager.view.ui_mainWindow import Ui_MainWindow
from magmasoft.censomanager.util.configuration import Configuration

class MainWindow(QtGui.QMainWindow):
    '''
    classdocs
    '''
        
    logger = logging.getLogger('gui')
    
    htmlBody = """
        <html>
            <head>
                <style>
                body {
                    background-color: black;
                    color: gray;
                }
                </style>
            </head>
            <body>
                <ul>
                    %s
                </ul>
            </body>
        </html>
    """
    
    actualMessage = ""

    
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(MainWindow, self).__init__(parent)
        self.__initialize()
        pass
    
    
    def __initialize(self):
        #strProgramm = ''
        #argList = QtCore.QStringList()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.actionSalir.triggered.connect(self.on_salir_triggered)
        
        self.confObj = Configuration.parseConf('conf/censomanager.conf.json')
        
        self._djp = DjangoProcess(self)
        
        self._djp.getProcess().started.connect(self.on_djangoprocess_started)
        self._djp.getProcess().finished.connect(self.on_djangoprocess_finished)
        self._djp.getProcess().readyReadStandardOutput.connect(self.on_djangoprocess_readyReadStandardOutput)
        self._djp.getProcess().readyReadStandardError.connect(self.on_djangoprocess_readyReadStandardError)
        
        
        
        command = "%s/%s" % ( self.confObj[u"execution"][u"python.path"],
                              self.confObj[u"execution"][u"python.bin"] )
        
        arglist = list()
        arglist.append( "%s/%s" %
                        ( self.confObj[u"censodjango"][u"project.dir"],
                          self.confObj[u"censodjango"][u"manage.name"] )  )
        arglist.append( self.confObj[u"censodjango"][u"manage.command"] )
        
        workingdir = self.confObj[u"censodjango"][u"manage.workingdir"]
        
        self._djp.startProcess( command, arglist, workingdir)
        
        #self.webprocess = QtCore.QProcess(self)
        #argList.append()
        
        #self.webprocess.start(strProgramm, argList)
        
        pass
    
    @QtCore.pyqtSlot()
    def cleanup_app(self):
        
        self._djp.stopProcess()
        
        QtGui.QApplication.quit()
        
        pass
    
    @QtCore.pyqtSlot()
    def on_salir_triggered(self):
        self._djp.stopProcess()
        
        QtGui.QApplication.quit()
        
        
        pass
    
    @QtCore.pyqtSlot()
    def on_refrescar_triggered(self):
        
        pass

    @QtCore.pyqtSlot()
    def on_exportar_triggered(self):
        
        pass

    @QtCore.pyqtSlot()
    def on_djangoprocess_readyReadStandardOutput(self):
        MainWindow.logger.debug("readyReadStandardOutput")
        msg = self._djp.getProcess().readAllStandardOutput()
        self.ui.txtEdtConsole.append()
        self.consolePrint(msg)
        pass

    @QtCore.pyqtSlot()
    def on_djangoprocess_readyReadStandardError(self):
        MainWindow.logger.debug("readyReadStandardError")
        msg = self._djp.getProcess().readAllStandardError()
        #self.ui.txtEdtConsole.append(msg)
        self.consolePrint(msg)
        pass
    
    @QtCore.pyqtSlot()
    def on_djangoprocess_started(self):
        msg = "El proceso inicio"
        
        self.ui.wbvwWebView.setUrl(QtCore.QUrl('http://127.0.0.1:8000/admin/'))
        
        #self.ui.txtEdtConsole.append(msg)
        self.consolePrint(msg)
        
        MainWindow.logger.debug(msg)
        pass
    
    @QtCore.pyqtSlot(int, QtCore.QProcess.ExitStatus)
    def on_djangoprocess_finished(self, exitCode, exitStatus):
        msg = "El proceso finalizo ( %s, %s )" % (exitCode, exitStatus)
        #self.ui.txtEdtConsole.append(msg)
        self.consolePrint(msg)
        MainWindow.logger.debug(msg)
        pass
    
    
    def consolePrint(self, message):
        self.actualMessage = self.actualMessage + "<li>" + message + "</li>"
        
        self.ui.txtEdtConsole.setHtml( MainWindow.htmlBody %  self.actualMessage )
        pass
    
    
    pass


class ConsoleInterface(QtCore.QObject):
    '''
    Class doc
    '''
    
    def __init__(self, _txtEdtConsole, parent=None):
        '''
        Constructor
        '''
        super(ConsoleInterface, self).__init__(parent)
        self.txtEdtConsole = _txtEdtConsole
        self.actualMessage = ''
        self.htmlTemplate = ''
        pass
    
    def printLi(self, message):
        self.actualMessage = self.actualMessage + "<li>" + message + "</li>"
        
        self.txtEdtConsole.setHtml( self.htmlTemplate %  self.actualMessage )
        
        pass
