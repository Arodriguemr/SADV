import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from Paneles.Login  import Login
from Paneles.Inventario import Inventario
from Paneles.Compra import Compra
from Paneles.Venta import Venta
from Paneles.Usuario import Usuario
from Paneles.Verificacion import Verificacion

"""
Clase Main
Encargada de llamara a las demas clases, ponerlas en ejecucion, y administrar datos entre ellas.
"""
class Controlador:

    def __init__(self):
        pass
    
    def show_Ingreso(self):
        self.login = Login()
        self.login.UIl.switch_Inventario.connect(self.show_Inventario)
        self.login.show()

    def show_Inventario(self,tmp = True):
        self.inventario = Inventario(tmp)
        self.inventario.UIi.switch_Compra.connect(self.show_Compra)
        self.inventario.UIi.switch_Venta.connect(self.show_Venta)
        self.inventario.UIi.switch_Usuario.connect(self.show_Usuario)
        self.inventario.UIi.switch_Login.connect(self.show_Ingreso)
        self.login.close()
        self.inventario.show()
        
    def show_Compra(self):
        self.compra = Compra()
        self.compra.UIc.switch_Inventario.connect(self.show_Inventario)
        self.compra.UIc.switch_Venta.connect(self.show_Venta)
        self.compra.UIc.switch_Usuario.connect(self.show_Usuario)
        self.compra.show()
        
    def show_Venta(self):
        self.venta = Venta()
        self.venta.UIv.switch_Inventario.connect(self.show_Inventario)
        self.venta.UIv.switch_Compra.connect(self.show_Compra)
        self.venta.UIv.switch_Usuario.connect(self.show_Usuario)
        self.venta.UIv.switch_Verificacion.connect(self.show_Verificacion)
        self.venta.show()
    
    def show_Verificacion(self, tmp):
        self.verificacion = Verificacion(tmp)
        self.verificacion.UIv.switch_Inventario.connect(self.show_Venta)
        self.verificacion.show()
        
    def show_Usuario(self):
        self.usuario = Usuario()
        self.usuario.UIu.switch_Inventario.connect(self.show_Inventario)
        self.usuario.UIu.switch_Compra.connect(self.show_Compra)
        self.usuario.UIu.switch_Venta.connect(self.show_Venta)
        self.usuario.show()
        
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    controlador = Controlador()
    controlador.show_Ingreso()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
