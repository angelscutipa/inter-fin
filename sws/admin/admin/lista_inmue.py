#!C:\Python34\python

import cgi
import cgitb; cgitb.enable()
import func
import mysql.connector
import re

print("Content-Type: text/html\n")

db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='inmobiliaria')


form = cgi.FieldStorage() # se instancia solo una vez

IN=form.getfirst("in","empty")

cursor=db.cursor()
sql="Select * From inmuebles where inmobiliaria_id=1"
cursor.execute(sql)
resultado=cursor.fetchall()
sql="Select * From inmuebles where inmobiliaria_id=2"
cursor.execute(sql)
resultado2=cursor.fetchall()

print("""
	<html>
	<head>		
        <meta charset="utf-8">
        <title>Panel de Administrador</title>
        <script type="text/javascript" src="../js/load.js"></script>
        <link rel="stylesheet" href="../css/style_ad.css">
        <link rel="shortcut icon" type="image/x-icon" href="../../sws/icono.png">
        <script type="text/javascript" src="jquery.min.js"></script>
        <script type="text/javascript"> 
            function formSubmit(estado){
                    var parametros={
                        "estado":estado
                    }
                    $.ajax({
                        url:'lista.py',
                        type: 'get',
                        data: parametros,
                        beforeSend: function () {
                                $("#resultado").html("Procesando, espere por favor...");
                        },
                        success:  function (response) {
                                $("#resultado").html(response);
                        }
                    })

                })
            }
            </script> 
            </head>""")

print("""<body>
    <header>
        <nav>        
            <ul>
                <li><a href="_admin.py?in=%i">"""%(int(IN))+"""Administrador</a></li>
                <li><a>Panel de Control</a></li>
                <li><a>Archivos</a></li>
                <li><a href="../../python/_main.py">Cerrar Sesion</a></li>
            </ul>
""")

print("""
        </nav>
    </header>
    <section class="main">
        <div id = "barra">
            <p>Inmuebles</p>
            <ul>
""")

men = ["Multimedias","Enlaces","Paginas","Comentarios","Escritorio","Apariencia","Inmobiliarias","Herramientas","Ajustes","Otros"];
func.printba1(men,IN)

print("""
            </ul>
        </div>""")
print("""<div class="articles">
        <table border>
        <TR>
        <TD>Nombre</TD><TD>Codigo</TD> <TD>Direccion</TD> <TD>Precio</TD> <TD>Estado</TD>
        </TR>""")

for resul in resultado:
        print("<TR><TD>"+str(resul[11])+"</TD><TD>"+str(resul[1])+"</TD> <TD>"+resul[2]+"</TD> <TD>"+str(resul[4])+"""</TD> <TD><button id="envia" onclick="formSubmit($('%s').val)">"""%resul[10]+resul[10]+"</button></TD></TR>")

for resul in resultado2:
        print("<TR><TD>"+str(resul[11])+"</TD><TD>"+str(resul[1])+"</TD> <TD>"+resul[2]+"</TD> <TD>"+str(resul[4])+"""</TD> <TD><button id="envia" onclick="formSubmit($('%s').val)">"""%resul[10]+resul[10]+"</TD></TR>")
print("""</table>
    </div> """)

print("""</body>
        </html>""")