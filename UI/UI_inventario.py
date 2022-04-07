import sys,time
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Constantes import *

class UI_Inventario(QMainWindow):
    switch_Compra = QtCore.pyqtSignal()
    switch_Venta = QtCore.pyqtSignal()
    switch_Usuario = QtCore.pyqtSignal()
    switch_Login = QtCore.pyqtSignal()
    def __init__(self, inventario):
        super(UI_Inventario,self).__init__()
        loadUi('UI/templates/Inventario.ui', self)
        self.setWindowIcon(QIcon(ICONO))
        self.inventario = inventario
        # -----------------Triggers-----------------
        self.botonCompras.clicked.connect(self.abrirCompras)
        self.botonVentas.clicked.connect(self.abrirVentas)
        self.botonUsuarios.clicked.connect(self.abrirUsuarios)
        self.botonCerrarSesion.clicked.connect(self.abrirLogin)
        # -----------------TABLA-----------------
        self.tablaInventario
        self.tablaInventario.setColumnCount(6)
        nombreColumnas = ("Cantidad", "Denominacion", "Acumulado", "Descripcion", "Stock Minimo", "Estado")
        self.tablaInventario.setHorizontalHeaderLabels(nombreColumnas)
        self.tablaInventario.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaInventario.verticalHeader().setVisible(False)
        self.tablaInventario.setAlternatingRowColors(True)
        self.tablaInventario.setDragDropOverwriteMode(False)
        self.tablaInventario.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # -----------------Ancho columnas-----------------
        for indice, ancho in enumerate((70, 110, 87, 470, 100, 150), start=0):
            self.tablaInventario.setColumnWidth(indice, ancho)
        row = -1
        self.tablaInventario.setRowCount(row + 1)
        for dato in self.inventario:
            row += 1
            self.tablaInventario.setRowCount(row + 1)

            self.tablaInventario.setItem(row, 0, QTableWidgetItem(str(dato[0])))
            self.tablaInventario.setItem(row, 1, QTableWidgetItem(str(dato[1])))
            self.tablaInventario.setItem(row, 2, QTableWidgetItem(str(dato[2])))
            self.tablaInventario.setItem(row, 3, QTableWidgetItem(str(dato[3])))
            self.tablaInventario.setItem(row, 4, QTableWidgetItem(str(dato[4])))
            self.tablaInventario.setItem(row, 5, QTableWidgetItem(str(dato[5])))
    # -----------------Triggers-----------------        
    def abrirCompras(self):
        self.switch_Compra.emit()
    def abrirVentas(self):
        self.switch_Venta.emit()
    def abrirUsuarios(self):
        self.switch_Usuario.emit()
    def abrirLogin(self):
        self.switch_Login.emit()
        self.close()
    # -----------------Enables----------------- 
    def enableBTinventario(self,tmp):
        self.botonInventario.setEnabled(tmp)
    def enableBTcompra(self,tmp):
        self.botonCompras.setEnabled(tmp)
    def enableBTventa(self,tmp):
        self.botonVentas.setEnabled(tmp)
    def enableBTusuario(self,tmp):
        self.botonUsuarios.setEnabled(tmp)