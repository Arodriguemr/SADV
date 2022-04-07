from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Constantes import *

class UI_Usuario(QMainWindow):
    
    switch_Inventario = QtCore.pyqtSignal()
    switch_Compra = QtCore.pyqtSignal()
    switch_Venta = QtCore.pyqtSignal()
    
    sigBorrar = QtCore.pyqtSignal()
    sigAggUsuario = QtCore.pyqtSignal()
    
    def __init__(self, usuarios,parent=None):
        super(UI_Usuario, self).__init__()
        loadUi('UI/templates/Usuario.ui', self)
        self.setWindowIcon(QIcon(ICONO))
        self.comboBoxTipoCuenta.addItems(TIPO_CUENTA)
        self.usuarios = usuarios
        self.comboBoxUsuarios.addItems(self.usuarios)
    
    #-----------------BOTONES-----------------
        self.botonInventario.clicked.connect(self.abrirInventario)
        self.botonCompras.clicked.connect(self.abrirCompras)
        self.botonVentas.clicked.connect(self.abrirVentas)
        self.botonEliminarU.clicked.connect(self.borrarUsuario)
        self.botonAgregarU.clicked.connect(self.aggUsuario)
    #-----------------gets-----------------
    def getCBusuarios(self):
        return self.comboBoxUsuarios.currentText()
    def getLEusuario(self):
        return self.lineEditUsuario.text()
    def getLEcontrasena(self):
        return self.lineEditContrasena.text()
    def getQMrespuesta(self):
        return QMessageBox.Yes
    def getCBtipoCuenta(self):
        return self.comboBoxTipoCuenta.currentText()
    # -----------------triggers-----------------
    def abrirInventario(self):
        self.switch_Inventario.emit()
        self.close()
    def abrirCompras(self):
        self.switch_Compra.emit()
        self.close()
    def abrirVentas(self):
        self.switch_Venta.emit()
        self.close()
    def borrarUsuario(self):
        self.sigBorrar.emit()
    def aggUsuario(self):
        self.sigAggUsuario.emit()
    # -----------------throwMsg-----------------
    def throwMsgProcesoEliminar(self):
        return QMessageBox.question(self, 'Eliminar', "¿Esta seguro que desea eliminar este usuario?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    def throwMsgCompletado(self):
        return QMessageBox.question(self, 'Agregar', "Proceso completado con exito", QMessageBox.Ok)
    def throwMsgErrorEliminar(self):
        return QMessageBox.question(self, 'Eliminar', "No fue posible eliminar esta cuenta", QMessageBox.Ok)
    def throwMsgErrorCreacion(self):
        return QMessageBox.question(self, 'Agregar', "No fue posible crear esta cuenta", QMessageBox.Ok)
    # -----------------throwMsg-----------------
    def clearLEusuario(self):
        self.lineEditUsuario.clear()
    def clearLEcontrasena(self):
        self.lineEditContrasena.clear()