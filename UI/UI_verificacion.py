import sys,time
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Constantes import *

class UI_verificacion (QMainWindow):
    
    switch_Inventario = QtCore.pyqtSignal()
    
    sigFinalizarVenta = QtCore.pyqtSignal()
    sigHacerFactura = QtCore.pyqtSignal()
    sigMandarCorreo = QtCore.pyqtSignal()
    sigMandarFacturaCorreo = QtCore.pyqtSignal()
    
    def __init__(self, informacionCliente, parent=None):
        super(UI_verificacion, self).__init__()
        loadUi('UI/templates/Verificacion.ui', self)
        self.informacionCliente = informacionCliente
        self.setWindowIcon(QIcon(ICONO))

    # -----------------TablaClientes1-------------------------
        self.tablaClientes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaClientes.setTextElideMode(Qt.ElideRight)
        self.tablaClientes.verticalHeader().setVisible(False)
        self.tablaClientes.setColumnCount(3)
        nomCol1 = ("Cliente", "Identificacion", "Celular")
        self.tablaClientes.setHorizontalHeaderLabels(nomCol1)
    # -----------------Ancho columnas-----------------
        for indice, ancho in enumerate((200, 160, 159), start=0):
            self.tablaClientes.setColumnWidth(indice, ancho)
            
        row = -1
        self.tablaClientes.setRowCount(row + 1)
        row += 1
        self.tablaClientes.setRowCount(row + 1)
        self.tablaClientes.setItem(row, 0, QTableWidgetItem(self.informacionCliente[2]))
        self.tablaClientes.setItem(row, 1, QTableWidgetItem(self.informacionCliente[3]))
        self.tablaClientes.setItem(row, 2, QTableWidgetItem(self.informacionCliente[4]))
            
    # -----------------TablaClientes2-------------------------
        self.tablaClientes_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaClientes_2.setTextElideMode(Qt.ElideRight)
        self.tablaClientes_2.verticalHeader().setVisible(False)
        self.tablaClientes_2.setColumnCount(3)
        nomCol1 = ("Telefono", "Direccion", "Departamento")
        self.tablaClientes_2.setHorizontalHeaderLabels(nomCol1)

        # -----------------Ancho columnas-----------------
        for indice, ancho in enumerate((200, 160, 159), start=0):
            self.tablaClientes_2.setColumnWidth(indice, ancho)
            
        row = -1
        self.tablaClientes_2.setRowCount(row + 1)
        row += 1
        self.tablaClientes_2.setRowCount(row + 1)

        self.tablaClientes_2.setItem(row, 0, QTableWidgetItem(self.informacionCliente[6]))
        self.tablaClientes_2.setItem(row, 1, QTableWidgetItem(self.informacionCliente[7]))
        self.tablaClientes_2.setItem(row, 2, QTableWidgetItem(self.informacionCliente[5]))

        # -----------------TablaClientes3-------------------------
        self.tablaClientes_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tablaClientes_3.setTextElideMode(Qt.ElideRight)
        self.tablaClientes_3.verticalHeader().setVisible(False)
        self.tablaClientes_3.setColumnCount(3)
        nomCol1 = ("E-mail", "Tipo de pago", "Fecha")
        self.tablaClientes_3.setHorizontalHeaderLabels(nomCol1)

    # -----------------Ancho columnas-----------------
        for indice, ancho in enumerate((200, 160, 159), start=0):
            self.tablaClientes_3.setColumnWidth(indice, ancho)
            
        row = -1
        self.tablaClientes_3.setRowCount(row + 1)
        row += 1
        self.tablaClientes_3.setRowCount(row + 1)

        self.tablaClientes_3.setItem(row, 0, QTableWidgetItem(self.informacionCliente[8]))
        self.tablaClientes_3.setItem(row, 1, QTableWidgetItem(self.informacionCliente[10]))
        self.tablaClientes_3.setItem(row, 2, QTableWidgetItem(self.informacionCliente[0]))

    # -----------------BOTONES-----------------
        self.botonRegresar.clicked.connect(self.abrirVenta)
        self.botonRegresar_2.clicked.connect(self.abrirVenta)
        self.botonFinalizar.clicked.connect(self.finalizarVenta)
        self.botonFactura.clicked.connect(self.hacerFactura)
        self.botonCorreo.clicked.connect(self.mandarCorreo)
        self.botonFacturaCorreo.clicked.connect(self.mandarFacturaCorreo)
    # -----------------gets-----------------
    def getRDialog(self):
        return QMessageBox.question(self, 'Factura', "Agregar Terminos y Condiciones",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    def getQMBox(self):
        return QMessageBox.Yes
    # -----------------enables-----------------
    def enableBTfinalizar(self,tmp):
        self.botonFinalizar.setEnabled(tmp)
    def enableBTregresarVentas(self,tmp):
        self.botonRegresar_2.setEnabled(tmp)
    def enableBTregresar(self,tmp):
        self.botonRegresar.setEnabled(tmp)
    def enableBTfactura(self,tmp):
        self.botonFactura.setEnabled(tmp)
    def enableBTcorreo(self,tmp):
        self.botonCorreo.setEnabled(tmp)
    def enableBTfacturaCorreo(self,tmp):
        self.botonFacturaCorreo.setEnabled(tmp)
        
    # -----------------CastErrors----------------- 
    def throwMsgTerminado(self):
        QMessageBox.information(self, "Mensaje", "Proceso Terminado", QMessageBox.Ok)  
    def throwMsgErrorProceso(self):
        QMessageBox.information(self, "Mensaje", "Proceso interrumpido, No se pudo realizar la venta", QMessageBox.Ok)
    def throwMsgErrorCorreo(self):
        QMessageBox.information(self, 'Mensaje', "Error verifique correo ingresado", QMessageBox.Ok)
   
    # -----------------adds-----------------
    def addLWcodigos(self,tmp):
        self.listaCodigos.addItem(tmp)
    def pushCodigos(self,tmp):
        self.listaCodigos.addItems(tmp)
    
    # -----------------Triggers-----------------  
    def abrirVenta(self):
        self.switch_Inventario.emit()
        self.close()
    def finalizarVenta(self):
        self.sigFinalizarVenta.emit()
    def hacerFactura(self):   
        self.sigHacerFactura.emit()
    def mandarCorreo(self):
        self.sigMandarCorreo.emit()
    def mandarFacturaCorreo(self):
        self.sigMandarFacturaCorreo.emit()
        
    """
    # -----------------Botones-----------------
        self.botonCorreo
        self.botonFactura
        self.botonFacturaCorreo
        self.botonFinalizar
        self.botonRegresar
        self.botonRegresar_2
        
    # -----------------Listas-----------------
        self.listaCodigos
        
    # -----------------Tabla-----------------
        self.tablaClientes
        self.tablaClientes_2
        self.tablaClientes_3
    """