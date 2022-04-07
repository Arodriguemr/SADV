import sys
from Utiles.Conexion import getInventario
from PyQt5 import QtCore, QtWidgets
from UI.UI_inventario import *

class Inventario():
    
    def __init__(self,tipoCuenta):    
        inventario = getInventario()
        self.UIi = UI_Inventario(inventario)
        self.UIi.enableBTcompra(tipoCuenta)
        self.UIi.enableBTinventario(tipoCuenta)
        self.UIi.enableBTventa(tipoCuenta)
        self.UIi.enableBTusuario(tipoCuenta)
    def show(self):
        self.UIi.show()
