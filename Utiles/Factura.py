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

    c.drawString(120, 100, "Los precios en esta factura son válidos solo el día en curso. Costos de envío, seguro y")
    c.drawString(124, 90, "adicionales son valores aproximados, sujetos a modificación luego de constatar con")
    c.drawString(240, 80, "empresa transportadora.")

    if consola == True:
        c.showPage()
        c.setFont('Helvetica', 12)
        c.drawString(50, 760, 'TÉRMINOS Y CONDICIONES')
        c.setFont('Helvetica', 9)
        c.drawString(50, 740,
                     'A continuación, encontrará las políticas que deberá tener presente, en caso de que requiera iniciar')
        c.drawString(50, 730, 'un trámite de cambio, retracto o garantía.')

        c.setFont('Helvetica', 12)
        c.drawString(50, 700, 'GARANTÍA.')
        c.setFont('Helvetica', 9)
        c.drawString(50, 680, 'La garantía procederá únicamente por defectos de fabricación.')

        c.setFont('Helvetica', 12)
        c.drawString(50, 650, 'CATEGORIA O PRODUCTO.')
        c.setFont('Helvetica', 9)
        c.drawString(70, 630, '•TIEMPO DE GARANTIA EN DÍAS - Consolas de Video Juego: 360 Días')
        c.drawString(50, 620,
                     'Daños provocados golpes, humedad, cambio de voltaje, rayones o por el manejo inadecuado del')
        c.drawString(50, 610,
                     'producto. Recuerde que para todos los productos cualquier modificación, manipulación, o ')
        c.drawString(50, 600, 'reparación por terceros (servicio técnico no autorizado) o mal uso del mismo anulan ')
        c.drawString(50, 590, 'automáticamente su garantía.')

        c.setFont('Helvetica', 12)
        c.drawString(50, 560, 'CONDICION')
        c.setFont('Helvetica', 9)
        c.drawString(50, 540, 'Que el producto cuente con su caja, empaques, accesorios y factura o documento ')
        c.drawString(50, 530,
                     'equivalente y que se encuentre dentro del periodo de garantía ofrecido. Adicional, se debe enviar.')

        c.setFont('Helvetica', 12)
        c.drawString(50, 500, 'TIEMPO PARA DAR RESPUESTA AL TRÁMITE')
        c.setFont('Helvetica', 9)
        c.drawString(50, 480, 'El tiempo establecido por la ley para dar respuesta a la solicitud del trámite de ')
        c.drawString(50, 470, 'garantía es de 30 días hábiles desde el recibo del producto en')
        c.drawString(50, 460, ' el Centro de Servicios Autorizado.')

        c.setFont('Helvetica', 12)
        c.drawString(50, 430, 'PARA TENER EN CUENTA EN EL TRÁMITE DE GARANTÍA')
        c.setFont('Helvetica', 9)
        c.drawString(50, 410, 'El hecho de dar inicio al proceso de garantía no implica la aceptación de la misma,')
        c.drawString(50, 400,
                     'esta estará sujeta a la revisión técnica que haga constar que no cabe causal de rechazo.')
        c.drawString(50, 390,
                     'Así mismo, si el producto cuenta con garantía directa del fabricante, el cliente tendrá que')
        c.drawString(50, 380, 'tramitarla directamente con quien este designe para tal fin y')
        c.drawString(50, 370, 'estará sujeta a sus políticas y condiciones.')

        c.setFont('Helvetica', 12)
        c.drawString(50, 340, 'GENERALIDADES DEL TRÁMITE DE GARANTÍA:')
        c.setFont('Helvetica', 9)
        c.drawString(50, 320, 'En caso de que la garantía sea aceptada lo que estipula la ley es lo siguiente:')
        c.drawString(50, 310,
                     'Se reparará el equipo dentro de los siguientes 30 días hábiles siguientes a la recepción del mismo.')
        c.drawString(50, 300,
                     'El término de la garantía se suspenderá mientras el consumidor esté privado del uso del producto.')
        c.drawString(50, 290,
                     'Solo si el bien no admite reparación se procederá a su reposición, inicialmente por uno igual, en el ')
        c.drawString(50, 280, 'caso de que no sea posible, por otro de la misma especie, similares características o ')
        c.drawString(50, 270, 'especificaciones técnicas.')
        c.drawString(50, 250, 'En caso de que la garantía sea rechazada:')
        c.drawString(50, 240, 'Se notificará por escrito el dictamen técnico y las causales de rechazo.')
        c.drawString(50, 230, 'Se retornará el equipo a la dirección registrada en la orden.')
        c.drawString(50, 210, 'Cambios y Retractos:')
        c.drawString(50, 200,
                     'Si una vez recibido el producto desea cambiarlo o retractarse, puede hacerlo siempre y cuando ')
        c.drawString(50, 190, 'cumpla con lo siguiente:')
        c.drawString(50, 170,
                     'VIGENCIA: Este trámite se podrá realizar únicamente durante los primeros 5 días hábiles siguiente ')
        c.drawString(50, 160, 'al recibo del paquete.')
        c.drawString(50, 140,
                     'CONDICIÓN: Es indispensable que se garantice la integridad del producto; solo se podrá iniciar el ')
        c.drawString(50, 130,
                     'trámite de cambio o retracto, cuando los productos no presentan rastros de haber sido usados, ')
        c.drawString(50, 120,
                     'cuenten con las etiquetas intactas, están en un estado de limpieza impecable y la caja y los ')
        c.drawString(50, 110, 'accesorios se encuentran en perfecto estado.')
        c.drawString(50, 90,
                     'FLETES: Los costos de los fletes y seguros correrán por cuenta del cliente y el embalaje deberá ')
        c.drawString(50, 80,
                     'garantizar que el producto se reciba en perfectas condiciones. Será responsabilidad del comprador ')
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
     