from PyQt5.uic import loadUi
from PyQt5 import QtCore, Qt, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Constantes import *

class UI_login(QMainWindow):
    
    switch_Inventario = QtCore.pyqtSignal(bool)
    
    sigValidar = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        super(UI_login, self).__init__()
        loadUi('UI/templates/Login.ui', self)
        
        self.setWindowIcon(QIcon(ICONO))
        self.setContentsMargins(0, 0, 0, 0)
        self.ImagenLabel.setPixmap(QtGui.QPixmap(IMAGEN_RANDOM))
        self.label.setAttribute(Qt.WA_TranslucentBackground, True)
        self.label_2.setAttribute(Qt.WA_TranslucentBackground, True)
        # -----------------Trigger-----------------
        self.botonIngresar.clicked.connect(self.validar)
    
    def validar(self):
        self.sigValidar.emit()
    def abrirInventario(self,tmp):
        self.switch_Inventario.emit(tmp)
    # -----------------gets-----------------
    def getUsuario(self):
        return self.lineEditUsuario.text()
    def getContrasena(self):
        return self.lineEditContrasena.text()
    # -----------------throwMsg-----------------
    def throwMsgErrorProceso(self):
        QMessageBox.information(self, "Mensaje", "Ingreso invalido", QMessageBox.Ok)