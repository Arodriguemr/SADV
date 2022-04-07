import pymongo
from Utiles.Verificar import encriptar

def conectar():
   client = pymongo.MongoClient('localhost',27017)
   db = client['Diem']
   return db

def getProductos():
   db = conectar()
   result = db.Productos.find()
   productos = []
   for i in result:
      productos.append(i['Descripcion'])
   return productos

def setCompra(factura, descripcion, socio, moneda, tasa, fecha, valorLote, codigos):
   db = conectar()
   db.Compras.insert({
      'Factura': factura,
      'Descripcion': descripcion,
      'Socio': socio,
      'Moneda': moneda,
      'Tasa': tasa,
      'Fecha': fecha,
      'ValorLote': valorLote,
      'Codigos': codigos
   })

def getCodigosActualizacion(descripcion):
   db = conectar()
   result = db.Productos.find({'Descripcion': descripcion})
   codigos = []
   denominacion = 0
   stockMinimo = 0
   for i in result:
      codigos = i['Codigos']
      denominacion = i['Denominacion']
      stockMinimo = i['StockMinimo']

   return denominacion, descripcion, stockMinimo, codigos

def setCodigos(codigos, descripcion):

   db = conectar()
   denominacion, descripcion, stockMinimo, codigosViejos = getCodigosActualizacion(descripcion)
   codigos.extend([element for element in codigosViejos if element not in codigos])

   db.Productos.update({
      'Descripcion': descripcion
   },
   {
      'Denominacion': denominacion,
      'Descripcion': descripcion,
      'StockMinimo' : stockMinimo,
      'Codigos': codigos
   })

def getInventario():
   db = conectar()
   result = db.Productos.find()
   inventario = []
   for i in result:
      cantidad = len(i['Codigos'])
      stockMinimo = i['StockMinimo']
      denominacion = i['Denominacion']
      acumulado = denominacion * cantidad
      if (cantidad >= stockMinimo):
         inventario.append([cantidad,denominacion,acumulado,i['Descripcion'],stockMinimo,'Stock Completo'])
      else:
         inventario.append([cantidad,denominacion,acumulado,i['Descripcion'],stockMinimo,'No suficiente'])
   return inventario

def getCodigosParaVender(producto, cantidad):
   db = conectar()
   denominacion, descripcion, stockMinimo, codigosViejos = getCodigosActualizacion(producto)

   aux = 0
   codigosParaVender = []
   codigos = []
   for i in codigosViejos:
      aux += 1
      if aux <= int(cantidad):
         codigosParaVender.append(i)
      if aux > int(cantidad):
         codigos.append(i)
   db.Productos.update({
      'Descripcion': descripcion
   },
   {
      'Denominacion': denominacion,
      'Descripcion': descripcion,
      'StockMinimo' : stockMinimo,
      'Codigos': codigos
   })

   return codigosParaVender

def verificarCodigos(codigos):

      db = conectar()
      result = db.Productos.find()

      for i in result:
         codigosDB = i['Codigos']
         comparacion = [item for item in codigos if item in codigosDB]
         comparacion.insert(0, "Codigos Repetidos")
         if len(comparacion) > 1:
            return comparacion
         else:
            return ['False']

def setVenta(arrC, arrV):
   #FECHA, NUMERO FACTURA, CLIENTE, IDENTIFICACION, CELULAR, DEPARTAMENTO, TELEFONO, DIRECCION, CORREO, DESCUENTO, TPAGO
   cliente = arrC[0]
   venta = arrV[0]
   db = conectar()
   db.ventas.insert({
      'Fecha': cliente[0],
      'Factura': cliente[1],
      'Cliente': cliente[2],
      'Identificacion': cliente[3],
      'Celular': cliente[4],
      'Departamento': cliente[5],
      'Telefono': cliente[6],
      'Direccion': cliente[7],
      'Correo': cliente[8],
      'Descuento': cliente[9],
      'Tipo_Pago': cliente[10],
      'Productos': venta
   })

def getUsuarios():
   db = conectar()

   usuarios = db.Usuarios.find({'Administrador': False})
   us = []
   for i in usuarios:
      us.append(i['Nombre del usuario']) 
   return us

def borrarUs(usuario):
   db = conectar()
   db.Usuarios.remove({'Nombre del usuario': usuario})

def agregarUs(usuario,contraseña, tipoUsu) :
    con = encriptar(contraseña)
  
    db = conectar()
    try:
     db.Usuarios.insert({
        'Nombre del usuario' : usuario,
        'Contraseña' : con.decode('utf-8'),
        'Administrador' : tipoUsu
     })
     return True
    except Exception as e :
       print(str(e))
       return False
    