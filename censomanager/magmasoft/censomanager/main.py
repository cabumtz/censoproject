#-*- coding:utf-8 -*-

'''
Created on 26/03/2013

@author: Carlos
'''
import sip

# import this
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

#import logging
from PyQt4 import QtGui
from magmasoft.censomanager.gui import MainDialog

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
    # QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))
    mainwindow = MainDialog()
    mainwindow.show()
    sys.exit(app.exec_())
    pass
