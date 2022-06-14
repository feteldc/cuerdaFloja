# -*- coding: utf-8 -*-

import configparser

##
# Esta es una clase
#
class Parce:
    ##
    # Este metodo es un constructor
    #
    def __init__(self):
        self.Config = configparser.ConfigParser()
        self.Config.read('config.ini')
    ##
    #este metodo lo que hace es 
    ##
    def getConfig(self): 
        return int(self.Config['DIFICULTY']['easyRow']),int(self.Config['DIFICULTY']['easyCol'])
    

##
#ahora lo que hacemos es instanciar la clase
##
#a = Parce()

#print(a.getConfig())