'''
Created on 20/04/2013

@author: WICO MX 2
'''

import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

import logging

from PyQt4 import QtCore


class Console(QtCore.QObject):
    '''
    classdocs
    '''
    logger = logging.getLogger('htmlConsole')
    
    _htmlBody = """
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
    
    _actualMessage = ""
    
    
    def __init__(self, txtEdtConsole, parent=None):
        '''
        Constructor
        '''
        super(Console, self).__init__(parent)
        self._txtEdtConsole = txtEdtConsole
        self._actualMessage = ""
        self._htmlTemplate = ""
        pass
    
    def printHtmlLi(self, htmlMessage):
        self._actualMessage = self._actualMessage + "\n<li>" + htmlMessage + "</li>"
        
        self._txtEdtConsole.setHtml( Console._htmlBody %  self._actualMessage )
        
        pass

    def printHtml(self, htmlMessage):
        self._actualMessage = self._actualMessage + htmlMessage
        
        self._txtEdtConsole.setHtml( Console._htmlBody %  self._actualMessage )
        
        pass

