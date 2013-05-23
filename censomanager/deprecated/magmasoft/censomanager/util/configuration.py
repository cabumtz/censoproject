'''
Created on 30/03/2013

@author: WICO MX 2
'''

import json
import logging

class Configuration:

    logger = logging.getLogger('configuration')

    def __init__(self):
        pass

    @staticmethod
    def parseConf(filename):
        
        with open(filename, 'r') as fp:
            obj = json.load(fp)
            Configuration.logger.debug("parseConf - result %s" % obj)
            pass

        return obj
    
    
