import sys,time
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Constantes import *

class UI_venta (QMainWindow):
    switch_Inventario = QtCore.pyqtSignal()
    switch_Compra = QtCore.pyqtSignal()
    switch_Usuario = QtCore.pyqtSignal()
    switch_Verificacion = QtCore.pyqtSignal(list)
    
    sigPreparar = QtCore.pyqtSignal()
    sigAceptar = QtCore.pyqtSignal()
    sigEliminar = QtCore.pyqtSignal()
    sigEliminarTodo = QtCore.pyqtSignal()
    sigCBdigital = QtCore.pyqtSignal()
    sigCBfisico = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        super(UI_venta, self).__init__()
        loadUi('UI/templates/Venta.ui', self)
        self.setWindowIcon(QIcon(ICONO))
        """# -----------------LineEdit-----------------
        self.lineEditFactura 
        self.lineEditCelular
        self.lineEditCliente
        self.lineEditDepartamento
        self.lineEditDescuento
        self.lineEditDireccion
        self.lineEditEMAIL
        self.lineEditIdentificacion
        self.lineEditPrecio
        self.lineEditTelefono
        self.lineEditTipoPago
        # -----------------Labels-----------------
        self.labelTotal
        self.labelDescuento
        # -----------------Botones-----------------
        self.Usuarios
        self.botonCompras
        self.botonContinuarVenta
        self.botonEliminar
        self.botonEliminarTodo
        self.botonInventario
        self.botonVentas
        self.botonVentasAceptar
        # -----------------List-----------------
        self.listWidget
        # -----------------Spinboxes-----------------
        self.spinBoxCantidad
        #-----------------ComboBox-----------------
        self.comboBoxDescripcion    """
        # -----------------LineEdit-----------------
        self.lineEditDescuento.setText('0')
        
        # -----------------Triggers-----------------

        self.botonInventario.clicked.connect(self.abrirInventario)
        self.botonCompras.clicked.connect(self.abrirCompras)
        self.botonVentasAceptar.clicked.connect(self.aceptar)
        self.botonEliminar.clicked.connect(self.eliminar)
        self.botonEliminarTodo.clicked.connect(self.eliminarTodo)
        self.botonContinuarVenta.clicked.connect(self.prepararDatos)
        self.botonUsuarios.clicked.connect(self.abrirUsuarios)
        self.checkBoxDigital.stateChanged.connect(self.clickBoxDigital)
        self.checkBoxFisico.stateChanged.connect(self.clickBoxFisico)
        
    # -----------------gets-----------------
    def getCBdescripcion(self):
        return self.comboBoxDescripcion.currentText()
    def getSBcantidad(self):
        return self.spinBoxCantidad.value()
    def getLEdescuento(self):
        return self.lineEditDescuento.text()
    def getLEfactura(self):
        return self.lineEditFactura.text()
    def getCBdescripcion(self):
        return self.comboBoxDescripcion.currentText()
    def getLEprecio(self):
        return self.lineEditPrecio.text()
    def getLWcurrenRow(self):
        return self.listWidget.currentRow()
    def getQTChecked(self):
        return Qt.Checked
    def getLEcliente(self):
        return self.lineEditCliente.text()
    def getLEidentificacion(self):
        return self.lineEditIdentificacion.text()
    def getLEcelular(self):
        return self.lineEditCelular.text()
    def getLEtelefono(self):
        return self.lineEditTelefono.text()
    def getLEdireccion(self):
        return self.lineEditDireccion.text()
    def getLEdepartamento(self):
        return self.lineEditDepartamento.text()
    def getLEcorreo(self):
        return self.lineEditEMAIL.text()
    def getLEtipoPago(self):
        return self.lineEditTipoPago.text()
    
    # -----------------sets-----------------
    def setLEfecha(self,tmp):
        self.lineEditFecha.setText(tmp)
    def setLBtotal(self,tmp):
        self.labelTotal.setText(str(tmp))
    def setLBdescuento(self,tmp):
        self.labelDescuento.setText(str(tmp))
    def setLEprecio(self,tmp):
        self.lineEditPrecio.setText(str(tmp))
    def setSBcantidad(self,tmp):
        self.spinBoxCantidad.setValue(tmp)
    def setCBfisico(self,tmp):
        self.checkBoxFisico.setChecked(tmp)
    def setCBdigital(self,tmp):
        self.checkBoxDigital.setChecked(tmp)
        
    # -----------------adds-----------------
    def addData(self,tmp):
        self.data.append(tmp)
    def addCBdescripcion(self,tmp):
        self.comboBoxDescripcion.addItems(tmp)
    def addLW(self,tmp):
        self.listWidget.addItem(tmp)
    # -----------------enables-----------------
    def enableBTcontinuarVenta(self,tmp):
        self.botonContinuarVenta.setEnabled(tmp)
    def enableLEDescuento(self,tmp):
        self.lineEditDescuento.setEnabled(tmp)
    # -----------------takes-----------------
    def takeItemLW(self,tmp):
        self.listWidget.takeItem(tmp)
    # -----------------clear-----------------
    def clearLW(self):
        self.listWidget.clear()
        
    # -----------------Triggers-----------------
    def abrirInventario(self):
        self.switch_Inventario.emit()
        self.close()
    def abrirCompras(self):
        self.switch_Compra.emit()
        self.close()
    def abrirUsuarios(self):
        self.switch_Usuario.emit()
        self.close()
    def abrirVerificacion(self,tmp):
        self.switch_Verificacion.emit(tmp)
        self.close()
        
    def prepararDatos(self):
        self.sigPreparar.emit()
    def aceptar(self):
        self.sigAceptar.emit()   
    def eliminar(self):
        self.sigEliminar.emit()
    def eliminarTodo(self):
        self.sigEliminarTodo.emit()
    def clickBoxDigital(self):
        self.sigCBdigital.emit()
    def clickBoxFisico(self):
        self.sigCBfisico.emit()
    # -----------------throwMsg-----------------
    def throwMsgErrorProceso(self):
        QMessageBox.information(self, "Mensaje", "Proceso interrumpido,  Ingrese una identificacion y un correo", QMessageBox.Ok)
    def throwMsgErrorValoresIngresados(self):
        QMessageBox.information(self, "Mensaje", "Proceso interrumpido, Corrija los valores introducidos",
                                        QMessageBox.Ok)
    def throwMsgErrorCantidadPrecio(self):
        QMessageBox.information(self, "Mensaje", "Proceso interrumpido, Observe cantidad y precio introducido", QMessageBox.Ok)