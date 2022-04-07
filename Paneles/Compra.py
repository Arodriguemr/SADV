import sys, time, locale
from Utiles.Factura import fecha as getFecha
from Utiles.Conexion import getProductos, verificarCodigos, setCompra, setCodigos
from UI.UI_compra import *
from Utiles.EnviarCorreo import enviarCorreo
from Constantes import CORREO

"""
Clase Compra
En esta clase se realiza  toda la actividad de realizar una compra, confirmar comprar
confirmar envio de correos y confirmar la genereacion de facturas.
"""
class Compra():
    def __init__(self):
        self.UIc = UI_Compra(getProductos())
        self.fecha = getFecha()
        self.UIc.setLEfecha(self.fecha)
        self.UIc.sigAceptar.connect(self.aceptar)
        self.UIc.sigAceptar.connect(self.aceptar)
        self.UIc.sigEliminar.connect(self.eliminar)
        self.UIc.sigEliminarTodo.connect(self.eliminarTodo)
        self.UIc.sigIngresarCodigos.connect(self.ingresarCodigos)
        self.UIc.sigEditar.connect(self.editar)
    #-----------------FUNCIONES-----------------
    def show(self):
        self.UIc.show()
        
    def notificarCompra(self):
        enviarCorreo('NOTIF_COMPRA', CORREO, None, None)
        
    def ingresarCodigos(self):
        codigos = self.UIc.getLECodigos()
        self.UIc.clearLEcodigos()
        codigos = codigos.split(" ")
        codigos = [item for item in codigos if item]
        self.UIc.addLW(codigos)
        
    def aceptar(self):
        repetido = False
        locale.setlocale(locale.LC_ALL, '')
        factura = self.UIc.getLEfactura()
        descripcion = self.UIc.getCBdescripcion()
        codigos = []
        for index in range(self.UIc.countLW()):
            codigos.append(self.UIc.getLWitem(index))
        socio = self.UIc.getLEsocio()
        moneda = self.UIc.getLEmoneda()
        tasa = self.UIc.getLEtasa()
        aux = []
        aux = self.verificarRepetido(codigos)
        if(len(aux)>= 3):
            self.UIc.throwMsgErrorRepetido()
            self.UIc.clearLW()
            self.UIc.addLW(aux)
            repetido = True
        else:
            repetido = False
        aux = []
        if (codigos != aux and repetido == False):
            verificacion = []
            verificacion = verificarCodigos(codigos)
            if (verificacion[0] == 'False'):
                try:
                    valor = float(moneda) * float(tasa)
                    valor = str(locale.currency(valor, grouping=True))
                    setCompra(factura, descripcion, socio, moneda, tasa, self.fecha, valor, codigos)
                    setCodigos(codigos, descripcion)
                    
                    self.UIc.clearLW()
                    self.UIc.clearLEsocio()
                    self.UIc.clearLEmoneda()
                    self.UIc.clearLEtasa()
                    self.UIc.clearLEfactura()
                    self.notificarCompra()
                    self.UIc.throwMsgProcesoTerminado()
                except Exception as e :
                    print(e)
                    self.UIc.throwMsgErrorProceso()
                
            else:
                self.UIc.clearLW()
                self.UIc.addLW(verificacion)
                self.UIc.throwMsgErrorRepetido()
        else:
            self.UIc.throwMsgErrorIngreso()
            
    def verificarRepetido(self, valores):
        repetido = ['Codigos repetidos','No se agregaron codigos']
        unico = []
        for x in valores:
            if x not in unico:
                unico.append(x)
            else:
                if x not in repetido:
                    repetido.append(x)
        if(len(repetido)>= 3):
            return repetido
        else:
            return ['']
    
    def editar(self):
        self.row = self.UIc.getLWrow()
        self.UIc.takeLW(self.row)
        self.UIc.insertLW(self.row, self.UIc.getLECodigos())
    def eliminar(self):
        self.row = self.UIc.getLWrow()
        self.UIc.takeLW(self.row)
    def eliminarTodo(self):
        self.UIc.clearLW()
    def show(self):
        self.UIc.show()
    def hide(self):
        self.UIc.hie()
    