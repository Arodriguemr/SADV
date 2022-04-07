from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Constantes import *

class UI_Compra(QMainWindow):
    
    switch_Inventario = QtCore.pyqtSignal()
    switch_Venta = QtCore.pyqtSignal()
    switch_Usuario = QtCore.pyqtSignal()
    
    sigAceptar  = QtCore.pyqtSignal()
    sigIngresarCodigos  = QtCore.pyqtSignal()
    sigEditar = QtCore.pyqtSignal()
    sigEliminar = QtCore.pyqtSignal()
    sigEliminarTodo = QtCore.pyqtSignal()

    def __init__(self, productos,parent=None):
        super(UI_Compra, self).__init__()
        loadUi('UI/templates/Compra.ui', self)
        self.setWindowIcon(QIcon(ICONO))
        self.addCBdescripcion(productos)
        #-----------------BOTONES-----------------
        self.botonInventario.clicked.connect(self.abrirInventario)
        self.botonVentas.clicked.connect(self.abrirVentas)
        self.botonIngresar.clicked.connect(self.ingresarCodigos)
        self.botonEditar.clicked.connect(self.editar)
        self.botonEliminar.clicked.connect(self.eliminar)
        self.botonEliminarTodo.clicked.connect(self.eliminarTodo)
        self.botonAceptar.clicked.connect(self.aceptar)
        self.botonUsuarios.clicked.connect(self.abrirUsuario)
    #-----------------sets-----------------
    def setLEfecha(self,tmp):
        return self.lineEditFecha.setText(tmp)
    #-----------------gets-----------------        
    def getLECodigos(self):
        return self.lineEditCodigos.text()
    def getLEfactura(self):
        return self.lineEditFactura.text()
    def getCBdescripcion(self):
        return self.comboBoxDescripcion.currentText()
    def getLWitem(self,tmp):
        return self.listWidget.item(tmp).text()
    def getLEsocio(self):
        return self.lineEditSocio.text()
    def getLEmoneda(self):
        return self.lineEditMoneda.text()
    def getLEtasa(self):
        return self.lineEditTasa.text()
    def getLWrow(self):
        return self.listWidget.currentRow()
    #-----------------counts-----------------
    def countLW(self):
        return self.listWidget.count()
    #-----------------adds-----------------
    def addLW(self,tmp):
        self.listWidget.addItems(tmp)
    def addCBdescripcion(self,tmp):
        self.comboBoxDescripcion.addItems(tmp)
    #-----------------clears-----------------
    def clearLEcodigos(self):
        self.lineEditCodigos.clear()
    def clearLW(self):
        self.listWidget.clear()
    def clearLEsocio(self):
        self.lineEditSocio.clear()
    def clearLEmoneda(self):
        self.lineEditMoneda.clear()
    def clearLEfactura(self):
        self.lineEditFactura.clear()
    def clearLEtasa(self):
        self.lineEditTasa.clear()
    #-----------------throwMsg-----------------
    def throwMsgProcesoTerminado(self):
        QMessageBox.information(self, "Mensaje", "Proceso terminado", QMessageBox.Ok)
    def throwMsgErrorProceso(self):
        QMessageBox.information(self, "Mensaje", "Proceso interrumpido, corriga los valores ingresados",
                                            QMessageBox.Ok)
    def throwMsgErrorRepetido(self):
        QMessageBox.information(self, "Mensaje", "Algunos codigos estan repetidos", QMessageBox.Ok)
    def throwMsgErrorIngreso(self):
        QMessageBox.information(self, "Mensaje", "Proceso interrumpido, Ingrese codigos", QMessageBox.Ok)
    #-----------------takes-----------------
    def takeLW(self,tmp):
        self.listWidget.takeItem(tmp)
    #-----------------inserts-----------------
    def insertLW(self,tmp1,tmp2):
        self.listWidget.insertItem(tmp1,tmp2)
    # -----------------Triggers-----------------
    def abrirInventario(self):
        self.switch_Inventario.emit()
        self.close()
    def abrirVentas(self):
        self.switch_Venta.emit()
        self.close()
    def abrirUsuario(self):
        self.switch_Usuario.emit()
        self.close()
    def ingresarCodigos(self):
        self.sigIngresarCodigos.emit()
    def editar(self):
        self.sigEditar.emit()
    def aceptar(self):
        self.sigAceptar.emit()   
    def eliminar(self):
        self.sigEliminar.emit()
    def eliminarTodo(self):
        self.sigEliminarTodo.emit()