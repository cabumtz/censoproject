import os
import logging.config

LOGCONFIG_FILE = "conf/logging.conf"


print "--------------------------------------"
print "configurando logging\n"
print "cwd: %s\n" % os.getcwd()
print "logconfig_file: %s\n" % LOGCONFIG_FILE 

logging.config.fileConfig(LOGCONFIG_FILE)

print "logging configurado\n"

print "--------------------------------------"