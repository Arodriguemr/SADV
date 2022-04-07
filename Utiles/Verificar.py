from cryptography.fernet import Fernet
from pymongo import MongoClient

#---------------------------Encriptar-----------------------------------
def encriptar(message):
    file = open('key.key','rb')
    key = file.read()
    file.close()

    encoded = message.encode()

    f = Fernet(key)
    encrypted = f.encrypt(encoded)

    return encrypted
#------------------Desencriptar-------------------------
def desencriptarContra(usuario):
    
    tipoCuenta = []
    client = MongoClient()
    db = client['Diem']
    usuarios = db.Usuarios
    result = usuarios.find({
        'Nombre del usuario': usuario
    })
      
    if not(type(result) == None):
        for i in result:
            m = i['Contraseña']
            tipoCuenta.append(i['Administrador'])
            file = open('key.key','rb')
            key2 = file.read()
            file.close()
            f2 = Fernet(key2)
            m = m.encode()
            decrypted = f2.decrypt(m).decode()   
            return decrypted, bool(tipoCuenta[0])
#------------------------Verificar---------------------------- ----

def verificar(usuario,contra):
    entrar = False
    res,tipoCuenta = desencriptarContra(usuario)
    if contra == res :
        entrar = True
        return entrar, tipoCuenta
    else:
        return entrar, tipoCuenta
    
