import sys,time, locale, ast, re, os
from Utiles.Conexion import borrarUs, agregarUs, getUsuarios
from UI.UI_Usuario import *


class Usuario(): 
    def __init__(self):
        self.UIu = UI_Usuario(getUsuarios())
        self.UIu.sigBorrar.connect(self.borrarUsuario)
        self.UIu.sigAggUsuario.connect(self.aggUsuario)       
        #-----------------FUNCIONES-----------------
    def show(self):
        self.UIu.show()
        
    def borrarUsuario(self):
        usuario = self.UIu.getCBusuarios()
        buttonReply = self.UIu.throwMsgProcesoEliminar()
        if buttonReply == self.UIu.getQMrespuesta():
            try:
                borrarUs(usuario)
                self.UIu.throwMsgCompletado()
            except:
                self.UIu.throwMsgErrorEliminar()

    def aggUsuario(self):
        usu = self.UIu.getLEusuario()
        con = self.UIu.getLEcontrasena()
        tipo = True if (self.UIu.getCBtipoCuenta() == "Administrador/a") else False
        try:
            agregarUs(usu, con, tipo)
            self.UIu.clearLEusuario()
            self.UIu.clearLEcontrasena()
            self.UIu.throwMsgCompletado()
        except Exception as e :
            self.UIu.throwMsgErrorCreacion()
        
    
