# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_design/mainDialog.ui'
#
# Created: Thu Apr 25 02:20:52 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(294, 495)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.grpbx = QtGui.QGroupBox(self.splitter)
        self.grpbx.setTitle(_fromUtf8(""))
        self.grpbx.setObjectName(_fromUtf8("grpbx"))
        self.verticalLayout = QtGui.QVBoxLayout(self.grpbx)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tlbttnLanzar = QtGui.QToolButton(self.grpbx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tlbttnLanzar.sizePolicy().hasHeightForWidth())
        self.tlbttnLanzar.setSizePolicy(sizePolicy)
        self.tlbttnLanzar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tlbttnLanzar.setObjectName(_fromUtf8("tlbttnLanzar"))
        self.verticalLayout.addWidget(self.tlbttnLanzar)
        self.tlbttnExportar = QtGui.QToolButton(self.grpbx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tlbttnExportar.sizePolicy().hasHeightForWidth())
        self.tlbttnExportar.setSizePolicy(sizePolicy)
        self.tlbttnExportar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tlbttnExportar.setObjectName(_fromUtf8("tlbttnExportar"))
        self.verticalLayout.addWidget(self.tlbttnExportar)
        self.tlbttnSalir = QtGui.QToolButton(self.grpbx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tlbttnSalir.sizePolicy().hasHeightForWidth())
        self.tlbttnSalir.setSizePolicy(sizePolicy)
        self.tlbttnSalir.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tlbttnSalir.setObjectName(_fromUtf8("tlbttnSalir"))
        self.verticalLayout.addWidget(self.tlbttnSalir)
        self.tlbttnAyuda = QtGui.QToolButton(self.grpbx)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tlbttnAyuda.sizePolicy().hasHeightForWidth())
        self.tlbttnAyuda.setSizePolicy(sizePolicy)
        self.tlbttnAyuda.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.tlbttnAyuda.setObjectName(_fromUtf8("tlbttnAyuda"))
        self.verticalLayout.addWidget(self.tlbttnAyuda)
        spacerItem = QtGui.QSpacerItem(20, 38, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.grpBxConsole = QtGui.QGroupBox(self.splitter)
        self.grpBxConsole.setTitle(_fromUtf8(""))
        self.grpBxConsole.setObjectName(_fromUtf8("grpBxConsole"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.grpBxConsole)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.txtEdtConsole = QtGui.QTextEdit(self.grpBxConsole)
        self.txtEdtConsole.setObjectName(_fromUtf8("txtEdtConsole"))
        self.horizontalLayout.addWidget(self.txtEdtConsole)
        self.verticalLayout_2.addWidget(self.splitter)
        self.actionSalir = QtGui.QAction(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icos32/icos32/system-log-out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalir.setIcon(icon)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionExportar = QtGui.QAction(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icos32/icos32/document-save-as.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExportar.setIcon(icon1)
        self.actionExportar.setObjectName(_fromUtf8("actionExportar"))
        self.actionAyuda = QtGui.QAction(Dialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icos32/icos32/help-browser.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAyuda.setIcon(icon2)
        self.actionAyuda.setObjectName(_fromUtf8("actionAyuda"))
        self.actionLanzarApp = QtGui.QAction(Dialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icos32/icos32/applications-internet.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLanzarApp.setIcon(icon3)
        self.actionLanzarApp.setObjectName(_fromUtf8("actionLanzarApp"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setText(QtGui.QApplication.translate("Dialog", "&Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setToolTip(QtGui.QApplication.translate("Dialog", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setShortcut(QtGui.QApplication.translate("Dialog", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportar.setText(QtGui.QApplication.translate("Dialog", "&Exportar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportar.setToolTip(QtGui.QApplication.translate("Dialog", "Exportar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportar.setShortcut(QtGui.QApplication.translate("Dialog", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAyuda.setText(QtGui.QApplication.translate("Dialog", "Ay&uda", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAyuda.setToolTip(QtGui.QApplication.translate("Dialog", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAyuda.setShortcut(QtGui.QApplication.translate("Dialog", "Ctrl+H", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLanzarApp.setText(QtGui.QApplication.translate("Dialog", "&Lanzar App", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLanzarApp.setToolTip(QtGui.QApplication.translate("Dialog", "Lanzar App", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLanzarApp.setShortcut(QtGui.QApplication.translate("Dialog", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))

import actionIcos_rc
