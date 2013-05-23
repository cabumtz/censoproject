# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_design/mainWindow.ui'
#
# Created: Sat Apr 06 16:10:30 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(930, 500)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.frmBrowserFrame = QtGui.QFrame(self.splitter)
        self.frmBrowserFrame.setFrameShape(QtGui.QFrame.Box)
        self.frmBrowserFrame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frmBrowserFrame.setObjectName(_fromUtf8("frmBrowserFrame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frmBrowserFrame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.wbvwWebView = QtWebKit.QWebView(self.frmBrowserFrame)
        self.wbvwWebView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.wbvwWebView.setObjectName(_fromUtf8("wbvwWebView"))
        self.horizontalLayout_2.addWidget(self.wbvwWebView)
        self.frmConsoleFrame = QtGui.QFrame(self.splitter)
        self.frmConsoleFrame.setFrameShape(QtGui.QFrame.Box)
        self.frmConsoleFrame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frmConsoleFrame.setObjectName(_fromUtf8("frmConsoleFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frmConsoleFrame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.txtEdtConsole = QtGui.QTextEdit(self.frmConsoleFrame)
        self.txtEdtConsole.setReadOnly(True)
        self.txtEdtConsole.setObjectName(_fromUtf8("txtEdtConsole"))
        self.horizontalLayout.addWidget(self.txtEdtConsole)
        self.horizontalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_Archivo = QtGui.QMenu(self.menubar)
        self.menu_Archivo.setObjectName(_fromUtf8("menu_Archivo"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(MainWindow)
        self.toolBar_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.toolBar_2.setAutoFillBackground(False)
        self.toolBar_2.setMovable(False)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.actionSalir = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icos32/icos32/system-log-out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalir.setIcon(icon)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionRefrescar = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icos32/icos32/view-refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefrescar.setIcon(icon1)
        self.actionRefrescar.setObjectName(_fromUtf8("actionRefrescar"))
        self.actionE_xportar = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icos32/icos32/document-save-as.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionE_xportar.setIcon(icon2)
        self.actionE_xportar.setObjectName(_fromUtf8("actionE_xportar"))
        self.menu_Archivo.addAction(self.actionRefrescar)
        self.menu_Archivo.addAction(self.actionE_xportar)
        self.menu_Archivo.addSeparator()
        self.menu_Archivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menu_Archivo.menuAction())
        self.toolBar.addAction(self.actionRefrescar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionE_xportar)
        self.toolBar_2.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionRefrescar, QtCore.SIGNAL(_fromUtf8("triggered()")), self.wbvwWebView.reload)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Archivo.setTitle(QtGui.QApplication.translate("MainWindow", "&Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar_2.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar_2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setText(QtGui.QApplication.translate("MainWindow", "&Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setToolTip(QtGui.QApplication.translate("MainWindow", "Salir del sistema", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefrescar.setText(QtGui.QApplication.translate("MainWindow", "&Refrescar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefrescar.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionE_xportar.setText(QtGui.QApplication.translate("MainWindow", "E&xportar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionE_xportar.setToolTip(QtGui.QApplication.translate("MainWindow", "Exportar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionE_xportar.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
import actionIcos_rc
