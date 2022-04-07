import locale, ast, re, os
from Utiles.Conexion import setVenta, getCodigosParaVender
from Utiles.Factura import generarFactura, hacerCodigos
from Utiles.EnviarCorreo import enviarCorreo
from Constantes import CORREO
from UI.UI_verificacion import *

#Varios
def sizeOf(tmp):
    return tmp.count()

class Verificacion():

    def __init__(self,tmp):
        self.informacionCliente = tmp[0][0]
        self.informacionVenta = tmp[1]
        self.UIv = UI_verificacion(self.informacionCliente)
        self.updateLWcodigos()
        self.UIv.sigFinalizarVenta.connect(self.finalizarVenta)
        self.UIv.sigHacerFactura.connect(self.hacerFactura)
        self.UIv.sigMandarCorreo.connect(self.enviarCodigos)
        self.UIv.sigMandarFacturaCorreo.connect(self.enviarFactura)
        
    # -----------------ListaCodigos-----------------
        # producto, cantidad, precio
    def updateLWcodigos(self):
        venta = []
        for i in self.informacionVenta:
            codigos = getCodigosParaVender(i[0], i[1])
            venta.append([i[0], codigos])
            self.UIv.addLWcodigos(i[0])
            self.UIv.pushCodigos(codigos)
        self.informacionVenta = []
        self.informacionVenta = venta

    # -----------------FUNCIONES-----------------

    def show(self):
        self.UIv.show()
        
    def notificarVenta(self):
        enviarCorreo("NOTIF_VENTA", CORREO, None, None)
        
    def finalizarVenta(self):
        try:
            self.UIv.enableBTfinalizar(False)
            self.UIv.enableBTregresarVentas(False)
            self.UIv.enableBTregresar(True)
            self.UIv.enableBTfactura(True)
            self.UIv.enableBTfacturaCorreo(True)
            self.UIv.enableBTcorreo(True)
            setVenta(self.informacionCliente, self.informacionVenta)
            self.notificarVenta()
            self.UIv.throwMsgTerminado()
            
        except Exception as e:
            self.UIv.enableBTfinalizar(True)
            self.UIv.enableBTregresarVentas(True)
            self.UIv.enableBTregresar(False)
            self.UIv.enableBTfactura(False)
            self.UIv.enableBTfacturaCorreo(False)
            self.UIv.enableBTcorreo(False)
            self.UIv.throwMsgErrorProceso()
            print(e)
            
    def hacerFactura(self):
        pathNombre = self.informacionCliente[3]
        buttonReply = self.UIv.getRDialog()
        
        if (buttonReply == self.UIv.getQMBox()):
            # FECHA, NUMERO FACTURA, CLIENTE, IDENTIFICACION, CELULAR, DEPARTAMENTO, TELEFONO, DIRECCION, CORREO, DESCUENTO, TPAGO, VALOR DESCUENTO
            generarFactura(pathNombre, self.informacionVenta, self.informacionCliente, True)
        else:
            generarFactura(pathNombre, self.informacionVenta, self.informacionCliente, False)
        self.UIv.enableBTfactura(False)
        self.UIv.enableBTfacturaCorreo(True)
		
    def enviarCodigos(self):
        hacerCodigos(self.informacionVenta)
        try:
            enviarCorreo("CODIGO",self.informacionCliente[8],None,None)
            self.UIv.enableBTcorreo(False)
            self.UIv.throwMsgTerminado()
        except Exception as e:
            self.UIv.enableBTcorreo(True)
            print(e)
            self.UIv.throwMsgErrorCorreo()

    def enviarFactura(self):
        hacerCodigos(self.informacionVenta)
        pathArchivo = "Facturas/" + self.informacionCliente[3] + ".pdf"
        
        try:
            enviarCorreo("FACTURA",self.informacionCliente[8], pathArchivo,None)
            self.UIv.enableBTfacturaCorreo(False)
            self.UIv.throwMsgTerminado()
        except:
            self.UIv.enableBTfacturaCorreo(True)
            self.UIv.throwMsgErrorCorreo()
    
    