def prepararCorreo(v1,v2):
    html = """\
    <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="utf-8">
            <title></title>
        </head>
        <body style="background-color: #dadddf ">

        <!--Copia desde aquí-->
        <table style="max-width: 600px; padding: 10px; margin:0 auto; border-collapse: collapse;">
            <tr>
                <td style="background-color: #dadddf; text-align: left; padding: 0">
                </td>
            </tr>

            <div style="text-align: center">
                <a href="link">
                
                <img src="https://i.imgur.com/GC2k8fX.png" align="center"></a>
                </div>

            <tr>
                <td style="background-color: #white">
                    <div style="color: #white; margin: %s %s %s; text-align: justify;font-family: sans-serif">
                        <h1 align="center" style="color: #7c0a02; margin: 0 0 7px">%s</h1>
                        <p align="center" style="color: #3c4245; margin: 2px; font-size: 15px">
                            Fecha: %s</p>
                            <p align="center" style="color: #ecf0f1; margin: 5px; font-size: px">
                        </ul>
                        <div style="width: %s;margin:10px 0; display: inline-block;text-align: center">
                
                        </div>
                        <div style="width: %s; text-align: center">
                            <a style="text-decoration: none; margin: 10px; border-radius: 5px; padding: 11px 23px; color: white; background-color: #7c0a02" href="http://google.com/">Ir a la página</a>	
                        </div>
                        <p style="color: #3c4245; font-size: 12px; text-align: center;margin: 30px 0 0">SADV.COM.CO</p>
                    </div>
                </td>
            </tr>
        </table>
        <!--hasta aquí-->

        </body>
        </html>
        
    """ %("4%","10%","%2",v1, v2,"100%","100%")
    return html