import os
try:
    import configparser
except:
    import ConfigParser as configparser

config = configparser.ConfigParser()

filepath = '/Library/Application Support/DLP3.0/config/webservice.ini'
# filepath = '/Users/wucheng3/Documents/works/DLP/peizhi/webservice.ini'

if os.path.exists(filepath):
    config.read(filepath)
    config.set('WebService', 'IP', 'dlpconn.tuhu.vip111')
    config.write(open(filepath, 'r+'))
else:
    pass