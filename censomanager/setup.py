'''
Created on 13/03/2013

@author: Carlos
'''
from distutils.core import setup
import py2exe

setup(
      console = [ {'script': 'magmasoft/censomanager/main.py', 'icon_resources': [(1, 'gui_design/resources/censocath.ico')]} ]
      
      #,
      #windows = [ {
      #             'script': 'magmasoft/censomanager/main.py',
      #             'icon_resources': [(1, 'gui_design/resources/censocath.ico')]
      #             }
      #           
      #           ]
      #
      
      )
