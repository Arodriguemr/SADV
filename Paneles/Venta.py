import  locale, ast, re, os
from Utiles.Factura import fecha as getFecha
from Utiles.Conexion import verificarCodigos, getProductos
from PyQt5 import QtCore
from UI.UI_venta import *
    
class Venta():
    
    def __init__(self):
        self.UIv = UI_venta()
        self.informacionCliente = []
        self.informacionVenta = []
        self.arrAux = []
        self.total = 0
        self.subtotal = 0
        self.vdescuento = 0
        self.UIv.addCBdescripcion(getProductos())
        self.UIv.setLEfecha(getFecha())
        self.UIv.sigAceptar.connect(self.aceptar)
        self.UIv.sigEliminar.connect(self.eliminar)
        self.UIv.sigEliminarTodo.connect(self.eliminarTodo)
        self.UIv.sigCBdigital.connect(self.clickBoxDigital)
        self.UIv.sigCBfisico.connect(self.clickBoxFisico)
        self.UIv.sigPreparar.connect(self.prepararDatos)

    def show(self):
        self.UIv.show()

    #-----------------FUNCIONES-----------------
    def aceptar(self):
        locale.setlocale(locale.LC_ALL, '')
        self.UIv.lineEditDescuento.setEnabled(False)
        producto = self.UIv.getCBdescripcion()
        cantidad = self.UIv.getSBcantidad()
        cantidad = int(cantidad)
        valorTotal = 0
        descuento = int(self.UIv.getLEdescuento())/ 100

        if cantidad > 0:
            try:
                precio = self.UIv.getLEprecio()
                valor = int(cantidad) * int(precio)
                self.arrAux.append(valor)
                self.informacionVenta.append([producto, str(cantidad), precio, str(valor)])
                valorT = str(locale.currency(valor, grouping=True))
                descripcion = producto + ' Cantidad: ' + str(cantidad) + "  Valor: " + str(valorT)

                for i in self.arrAux:
                    valorTotal += int(i)
                
                descuento = descuento * valorTotal
                descuento =  valorTotal - descuento
                self.vdescuento = valorTotal - descuento
                self.subtotal = valorTotal 
                self.total = descuento
                valorTotal = str(locale.currency(valorTotal, grouping=True))
                descuento = str(locale.currency(descuento, grouping=True))

                self.UIv.setLBtotal(valorTotal)
                self.UIv.setLBdescuento(descuento)
                self.UIv.enableBTcontinuarVenta(True)
                self.UIv.addLW(descripcion)
                self.UIv.setLEprecio('')
                self.UIv.setSBcantidad(0)
                

            except:
                self.UIv.throwMsgErrorValoresIngresados()

        else:
            self.UIv.throwMsgErrorCantidadPrecio()

    def eliminar(self):

        self.row = self.UIv.getLWcurrenRow()
        self.arrAux.pop(self.row)
        self.informacionVenta.pop(self.row)

        valorTotal = 0
        descuento = int(self.UIv.getLEdescuento())/ 100

        for i in self.arrAux:
                    valorTotal += int(i)

        descuento = descuento * valorTotal
        descuento =  valorTotal - descuento
        self.vdescuento = valorTotal - descuento
        self.subtotal = valorTotal 
        self.total = descuento
        
        descuento = str(locale.currency(descuento, grouping=True))
        valorTotal = str(locale.currency(valorTotal, grouping=True))

        self.UIv.setLBdescuento(descuento)
        self.UIv.setLBtotal(valorTotal)
        self.UIv.takeItemLW(self.row)
    
    def eliminarTodo(self):
        self.UIv.clearLW()
        self.UIv.setLBtotal('0')
        self.UIv.setLBdescuento('0')
        self.UIv.enableLEDescuento(True)
        self.informacionVenta = []
        self.arrAux = []
        
        
    def clickBoxFisico(self, state):
        if state == self.UIv.getQTChecked():
            self.UIv.setCBfisico(False)

    def clickBoxDigital(self, state):
        if state == self.UIv.getQTChecked():
            self.UIv.setCBdigital(False)

    def prepararDatos(self):
        fecha = getFecha()
        cliente = self.UIv.getLEcliente()
        identificacion = self.UIv.getLEidentificacion()
        celular = self.UIv.getLEcelular()
        telefono = self.UIv.getLEtelefono()
        direccion = self.UIv.getLEdireccion()
        departamento = self.UIv.getLEdepartamento()
        correo = self.UIv.getLEcorreo()
        descuento = self.UIv.getLEdescuento()
        tipoPago = self.UIv.getLEtipoPago()
        factura = self.UIv.getLEfactura()

        # FECHA, NUMERO FACTURA, CLIENTE, IDENTIFICACION, CELULAR, DEPARTAMENTO, TELEFONO, DIRECCION, CORREO, DESCUENTO, TPAGO, VALOR DESCUENTO, TOTAL, SUBTOTAL
        self.informacionCliente.append(
            [fecha, factura, cliente, identificacion, celular, departamento, telefono, direccion, correo, descuento,
             tipoPago, self.vdescuento, self.total, self.subtotal])
               
        if ((identificacion != "" and identificacion != "OBLIGATORIO" ) and (correo != "" and identificacion != "OBLIGATORIO")):
            self.UIv.abrirVerificacion([self.informacionCliente,self.informacionVenta])
        else:
            self.UIv.throwMsgErrorProceso()
        
