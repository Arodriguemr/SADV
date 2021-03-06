import itertools
import locale
import time
from statistics import mean
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def fecha():
    fechaVenta = ''
    formato_tiempo = time.ctime()
    formato_tiempo = formato_tiempo.split(" ")
    diasIngles = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    diasEspanol = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    mesIngles = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dic"]
    mesEspanol = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct",
                  "Nov", "Dic"]

    aux = diasIngles.index(formato_tiempo[0])
    fechaVenta += diasEspanol[aux] + ","
    aux = mesIngles.index(formato_tiempo[1])
    fechaVenta += " " + mesEspanol[aux]  + " " + formato_tiempo[3] + ", " + formato_tiempo[4]
    return fechaVenta


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)


def generarFactura(PathNombre, lista, informacionCliente, consola):
    PathNombre = PathNombre
    fecha = informacionCliente[0]
    factura = informacionCliente[1]
    cliente = informacionCliente[2]
    cedula = informacionCliente[3]
    contacto = informacionCliente[4]
    departamento = informacionCliente[5]
    telefono = informacionCliente[6]
    direccion = informacionCliente[7]
    email = informacionCliente[8]
    descuento = informacionCliente[9]
    tpago = informacionCliente[10]
    valorDescuento = informacionCliente[11]
    valorTotal = informacionCliente[12]
    valorSubtotal = informacionCliente[13]

    locale.setlocale(locale.LC_ALL, '')

    subtotal = int(valorSubtotal)
    total = float(valorTotal)
    descuentoValor = float(valorDescuento)

    subtotal = str(locale.currency(subtotal, grouping=True))
    total = str(locale.currency(total, grouping=True))
    descuentoValor = str(locale.currency(descuentoValor, grouping=True))

    for i in range(len(lista)):
        lista[i][2] = str(locale.currency(int(lista[i][2]), grouping=True))
        lista[i][3] = str(locale.currency(int(lista[i][3]), grouping=True))

    lista.insert(0, ['DESCRIPCION', 'CANT', 'VALOR UNITARIO', 'VALOR TOTAL'])

    c = canvas.Canvas("Facturas/" + PathNombre +".pdf", pagesize=A4)
    c.drawImage("Imagenes/LogotipoPDF.png", 29, 730, width=130, height=50)
    c.drawString(270, 760, 'SADV')
    c.drawString(490, 760, 'FACTURA')

    c.setFont('Helvetica', 9)
    c.drawString(242, 750, 'NIT: 1214724312 - 8')
    c.drawString(495, 750, factura)

    c.drawString(50, 710, 'Cedula:')
    c.drawString(150, 710, 'Cliente:')
    c.drawString(250, 710, 'Contacto:')
    c.drawString(350, 710, 'Fecha:')
    c.drawString(490, 710, 'Departamento:')
    c.drawString(50, 700, cedula)
    c.drawString(150, 700, cliente)
    c.drawString(250, 700, contacto)
    c.drawString(350, 700, fecha)
    c.drawString(490, 700, departamento)

    c.setLineWidth(.7)
    c.line(50, 692, 550, 692)

    c.drawString(50, 680, 'Telefono:')
    c.drawString(150, 680, 'Direccion:')
    c.drawString(250, 680, 'E-MAIL:')
    c.drawString(350, 680, 'Descuento:')
    c.drawString(490, 680, 'T.PAGO:')
    c.drawString(50, 670, telefono)
    c.drawString(150, 670, direccion)
    c.setFont('Helvetica', 6)
    if len(email) < 20: 
        c.drawString(250, 670, email)
    else:
        c.drawString(250, 670, email[0:18]+"...")
    c.setFont('Helvetica', 9)
    c.drawString(350, 670, descuento + '%')
    c.drawString(490, 670, tpago)

    c.setLineWidth(.3)
    c.setFont('Helvetica', 7)
    w, h = A4
    max_rows_per_page = 16
    # Margen.
    x_offset = 50
    y_offset = 200
    # Espacio entre renglones.
    padding = 15

    xlist = [x + x_offset for x in [0, 220, 250, 350, 500]]
    ylist = [h - y_offset - i * padding for i in range(max_rows_per_page + 1)]

    for rows in grouper(lista, max_rows_per_page):
        rows = tuple(filter(bool, rows))
        c.grid(xlist, ylist[:len(rows) + 1])
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                c.drawString(x + 2, y - padding + 3, str(cell))

    c.drawString(50, y - padding - 13, "SUBTOTAL: " + subtotal)
    c.drawString(50, y - padding - 23, "DCTO TOTAL: " + descuentoValor)
    c.drawString(50, y - padding - 33, "VALOR TOTAL: " + total)

    c.drawString(120, 100, "Los precios en esta factura son v??lidos solo el d??a en curso. Costos de env??o, seguro y")
    c.drawString(124, 90, "adicionales son valores aproximados, sujetos a modificaci??n luego de constatar con")
    c.drawString(240, 80, "empresa transportadora.")

    if consola == True:
        c.showPage()
        c.setFont('Helvetica', 12)
        c.drawString(50, 760, 'T??RMINOS Y CONDICIONES')
        c.setFont('Helvetica', 9)
        c.drawString(50, 740,
                     'A continuaci??n, encontrar?? las pol??ticas que deber?? tener presente, en caso de que requiera iniciar')
        c.drawString(50, 730, 'un tr??mite de cambio, retracto o garant??a.')

        c.setFont('Helvetica', 12)
        c.drawString(50, 700, 'GARANT??A.')
        c.setFont('Helvetica', 9)
        c.drawString(50, 680, 'La garant??a proceder?? ??nicamente por defectos de fabricaci??n.')

        c.setFont('Helvetica', 12)
        c.drawString(50, 650, 'CATEGORIA O PRODUCTO.')
        c.setFont('Helvetica', 9)
        c.drawString(70, 630, '???TIEMPO DE GARANTIA EN D??AS - Consolas de Video Juego: 360 D??as')
        c.drawString(50, 620,
                     'Da??os provocados golpes, humedad, cambio de voltaje, rayones o por el manejo inadecuado del')
        c.drawString(50, 610,
                     'producto. Recuerde que para todos los productos cualquier modificaci??n, manipulaci??n, o ')
        c.drawString(50, 600, 'reparaci??n por terceros (servicio t??cnico no autorizado) o mal uso del mismo anulan ')
        c.drawString(50, 590, 'autom??ticamente su garant??a.')

        c.setFont('Helvetica', 12)
        c.drawString(50, 560, 'CONDICION')
        c.setFont('Helvetica', 9)
        c.drawString(50, 540, 'Que el producto cuente con su caja, empaques, accesorios y factura o documento ')
        c.drawString(50, 530,
                     'equivalente y que se encuentre dentro del periodo de garant??a ofrecido. Adicional, se debe enviar.')

        c.setFont('Helvetica', 12)
        c.drawString(50, 500, 'TIEMPO PARA DAR RESPUESTA AL TR??MITE')
        c.setFont('Helvetica', 9)
        c.drawString(50, 480, 'El tiempo establecido por la ley para dar respuesta a la solicitud del tr??mite de ')
        c.drawString(50, 470, 'garant??a es de 30 d??as h??biles desde el recibo del producto en')
        c.drawString(50, 460, ' el Centro de Servicios Autorizado.')

        c.setFont('Helvetica', 12)
        c.drawString(50, 430, 'PARA TENER EN CUENTA EN EL TR??MITE DE GARANT??A')
        c.setFont('Helvetica', 9)
        c.drawString(50, 410, 'El hecho de dar inicio al proceso de garant??a no implica la aceptaci??n de la misma,')
        c.drawString(50, 400,
                     'esta estar?? sujeta a la revisi??n t??cnica que haga constar que no cabe causal de rechazo.')
        c.drawString(50, 390,
                     'As?? mismo, si el producto cuenta con garant??a directa del fabricante, el cliente tendr?? que')
        c.drawString(50, 380, 'tramitarla directamente con quien este designe para tal fin y')
        c.drawString(50, 370, 'estar?? sujeta a sus pol??ticas y condiciones.')

        c.setFont('Helvetica', 12)
        c.drawString(50, 340, 'GENERALIDADES DEL TR??MITE DE GARANT??A:')
        c.setFont('Helvetica', 9)
        c.drawString(50, 320, 'En caso de que la garant??a sea aceptada lo que estipula la ley es lo siguiente:')
        c.drawString(50, 310,
                     'Se reparar?? el equipo dentro de los siguientes 30 d??as h??biles siguientes a la recepci??n del mismo.')
        c.drawString(50, 300,
                     'El t??rmino de la garant??a se suspender?? mientras el consumidor est?? privado del uso del producto.')
        c.drawString(50, 290,
                     'Solo si el bien no admite reparaci??n se proceder?? a su reposici??n, inicialmente por uno igual, en el ')
        c.drawString(50, 280, 'caso de que no sea posible, por otro de la misma especie, similares caracter??sticas o ')
        c.drawString(50, 270, 'especificaciones t??cnicas.')
        c.drawString(50, 250, 'En caso de que la garant??a sea rechazada:')
        c.drawString(50, 240, 'Se notificar?? por escrito el dictamen t??cnico y las causales de rechazo.')
        c.drawString(50, 230, 'Se retornar?? el equipo a la direcci??n registrada en la orden.')
        c.drawString(50, 210, 'Cambios y Retractos:')
        c.drawString(50, 200,
                     'Si una vez recibido el producto desea cambiarlo o retractarse, puede hacerlo siempre y cuando ')
        c.drawString(50, 190, 'cumpla con lo siguiente:')
        c.drawString(50, 170,
                     'VIGENCIA: Este tr??mite se podr?? realizar ??nicamente durante los primeros 5 d??as h??biles siguiente ')
        c.drawString(50, 160, 'al recibo del paquete.')
        c.drawString(50, 140,
                     'CONDICI??N: Es indispensable que se garantice la integridad del producto; solo se podr?? iniciar el ')
        c.drawString(50, 130,
                     'tr??mite de cambio o retracto, cuando los productos no presentan rastros de haber sido usados, ')
        c.drawString(50, 120,
                     'cuenten con las etiquetas intactas, est??n en un estado de limpieza impecable y la caja y los ')
        c.drawString(50, 110, 'accesorios se encuentran en perfecto estado.')
        c.drawString(50, 90,
                     'FLETES: Los costos de los fletes y seguros correr??n por cuenta del cliente y el embalaje deber?? ')
        c.drawString(50, 80,
                     'garantizar que el producto se reciba en perfectas condiciones. Ser?? responsabilidad del comprador ')
        c.drawString(50, 70,
                     'tomar las medidas pertinentes para que el producto, incluida su caja, no sufra deterioros en el ')
        c.drawString(50, 60, 'transporte.')

    c.save()

def hacerCodigos(lista):
    lista = lista[0]
    w, h = A4
    c = canvas.Canvas("Codigos/TusCodigos.pdf", pagesize=A4)
    lista = lista 
    text = c.beginText(50, h - 50)
    
    text.setFont("Times-Roman", 16)
    text.textLine('Tus codigos son:')
    for i in lista:
        text.textLine("      " + str(i))
    c.drawText(text)
    c.showPage()
    c.save()
     