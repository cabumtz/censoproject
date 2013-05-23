'''
Created on 26/03/2013

@author: Carlos
'''

import logging
import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)


from PyQt4 import QtGui, QtCore
from magmasoft.censomanager.view.ui_mainDialog import Ui_Dialog
from magmasoft.censomanager.util.configuration import Configuration
from magmasoft.censomanager.console import Console
from magmasoft.censomanager.djangoprocess import DjangoProcess

class MainDialog(QtGui.QDialog):
    '''
    classdocs
    '''
        
    logger = logging.getLogger('gui')

    
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(MainDialog, self).__init__(parent)
        self.__init()
        pass
    
    
    def __init(self):
        '''
        '''
        self.__initConf()
        self.__initDjangoProcess(self._confObj)
        self.__initGui()
        self.__initConsole(self.ui.txtEdtConsole)
        
        self._djp.start()
        
        pass
    
    def __initConf(self):
        '''
        '''
        self._confObj = Configuration.parseConf('conf/censomanager.conf.json')
        pass
    
    def __initGui(self):
        '''
        '''
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # assign buttons to actions
        self.ui.tlbttnLanzar.setDefaultAction(self.ui.actionLanzarApp)
        self.ui.tlbttnSalir.setDefaultAction(self.ui.actionSalir)
        self.ui.tlbttnExportar.setDefaultAction(self.ui.actionExportar)
        self.ui.tlbttnAyuda.setDefaultAction(self.ui.actionAyuda)
    
        pass
    
    
    def __initConsole(self, txtEdtConsole):
        '''
        '''
        self._console = Console(txtEdtConsole, self)
        pass
    
    
    def __initDjangoProcess(self, confObj):
        '''
        '''
        djangoexecpath = "%s/%s" % ( confObj[u"execution"][u"python.path"],
                              confObj[u"execution"][u"python.bin"] )
        
        djangoargs = confObj[u"censodjango"][u"args"]
        
        workingdir = confObj[u"censodjango"][u"workingdir"]
        
        self._djp = DjangoProcess(self, djangoexecpath, djangoargs, workingdir, "djangoProcess")
        
        MainDialog.logger.debug("__initDjangoProcess - djp.name: %s" % self._djp.objectName())
        
        pass
    
    
    def closeEvent(self, closeEvent): # closeEvent(self, *args, **kwargs):
        '''
        '''
        self.on_actionSalir_triggered()
        closeEvent.accept();
        pass
        
    @QtCore.pyqtSlot()
    def on_actionLanzarApp_triggered(self):
        MainDialog.logger.debug("on_actionLanzarApp_triggered - start")
        
        args = list()
        args.append("/c")
        args.append("start")
        args.append(self._confObj[u"censodjango"][u"url"])
        
        QtCore.QProcess.execute( "cmd", args )
        
        MainDialog.logger.debug("on_actionLanzarApp_triggered - end")
        pass
        
    @QtCore.pyqtSlot()
    def on_actionSalir_triggered(self):
        MainDialog.logger.debug("on_actionSalir_triggered - starting exit process")
        self._djp.stop()
        QtGui.QApplication.quit()
        pass

    @QtCore.pyqtSlot()
    def on_actionExportar_triggered(self):
        MainDialog.logger.debug("on_actionExportar_triggered - start")
        
        options = QtGui.QFileDialog.DontResolveSymlinks | QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.Directory
        destinationDir = QtGui.QFileDialog.getExistingDirectory(
                                                    parent=self,
                                                    caption=self.tr("Selecciona directorio destino"),
                                                    directory="/",
                                                    options=options
                                                    )
        if ( destinationDir == ""):
            return
        
        MainDialog.logger.debug("on_actionExportar_triggered - destinationDir: %s" % destinationDir)
        
        sourcefile = "%s/%s" % (self._confObj[u"censodjango"][u"workingdir"], "censocath.db")
        
        MainDialog.logger.debug("on_actionExportar_triggered - sourcefile: %s" % sourcefile)
        
        
        fileInfo = QtCore.QFileInfo( sourcefile )
        destinationfile = destinationDir + QtCore.QDir.separator() + fileInfo.fileName()
        
        MainDialog.logger.debug("on_actionExportar_triggered - destinationFile: %s" % destinationfile)
        
        self._djp.stop()
        
        result = QtCore.QFile.copy(sourcefile, destinationfile)
        
        if (not result) :
            QtCore.QFile(destinationfile).remove()
            result = QtCore.QFile.copy(sourcefile, destinationfile)
        
        MainDialog.logger.debug("on_actionExportar_triggered - result: %s" % result)
        
        self._djp.start()
        
        pass
        

    
    @QtCore.pyqtSlot()
    def on_actionAyuda_triggered(self):
        pass

    @QtCore.pyqtSlot()
    def on_djangoProcess_readyReadStandardOutput(self):
        MainDialog.logger.debug("readyReadStandardOutput")
        msg = self._djp.readAllStandardOutput()
        self._console.printHtmlLi(msg)
        pass

    @QtCore.pyqtSlot()
    def on_djangoProcess_readyReadStandardError(self):
        MainDialog.logger.debug("readyReadStandardError")
        msg = self._djp.readAllStandardError()
        self._console.printHtmlLi(msg)
        pass
    
    @QtCore.pyqtSlot()
    def on_djangoProcess_started(self):
        msg = "El proceso inicio"
        self._console.printHtmlLi(msg)
        MainDialog.logger.debug(msg)
        pass
    
    @QtCore.pyqtSlot(int, QtCore.QProcess.ExitStatus)
    def on_djangoProcess_finished(self, exitCode, exitStatus):
        msg = "El proceso finalizo ( %s, %s )" % (exitCode, exitStatus)
        self._console.printHtmlLi(msg)
        MainDialog.logger.debug(msg)
        pass
    
    
    pass


