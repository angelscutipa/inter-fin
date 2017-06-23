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
IN = form.getfirst("in","empty")
cursor=db.cursor()
sql="Select * From inmuebles where inmobiliaria_id='%s'"%(IN)
cursor.execute(sql)
resultado=cursor.fetchall()

print("""
	<html>
	<head>		
        <meta charset="utf-8">
        <script type="text/javascript" src="../js/load.js"></script>
        <link rel="stylesheet" href="../css/style_ad.css">
        <link rel="shortcut icon" type="image/x-icon" href="../../sws/icono.png">
        <script type="text/javascript" src="jquery.min.js"></script>
        <title>Panel de Administrador</title>
	</head>""")

print(""" <script type="text/javascript"> 
           $(document).ready(function(){
                formSubmit()
            })
            function formSubmit(){
                $('.articles').submit(function(e){
                    e.preventDefault()
                    var estado=$('#correo').val()

                    var data='estado='+estado;

                    $.ajax({
                        url:'lista.py',
                        type: 'get',
                        data: data,
                        beforeSend: function () {
                                $(".article .msn").html("<br>Procesando, espere por favor...");
                        },
                        success:  function (response) {
                                $(".articles .msn").html("");
                                $(".articles .show").html(response);
                        }
                    })

                })
            }
            </script> """)

print("""<body>
    <header>
        <nav>        
            <ul>
                <li><a href="_admin.py">Administrador</a></li>
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

men = ["Multimedias","Enlaces","Paginas","Comentarios","Ventas","Alquiler","Apariencia","Interesados","Herramientas","Ajustes"];
func.printba(men, IN)

print("""
            </ul>
        </div>""")
print("""<div class="articles">
        <table border>
        <TR>
        <TD>Correo</TD> <TD>Password</TD> <TD>Usuario</TD>           
        </TR>""")
for res in resultado:
    sql="Select * From interes where inmueble_id='%d'"% (res[0]);
    cursor.execute(sql)
    resultado2=cursor.fetchall()
    for resul in resultado2:
            sql="Select * From interesado where id='%d'"% (resul[1]);
            cursor.execute(sql)
            resultado3=cursor.fetchall()
            for result in resultado3:
                print("<TR><TD>"+str(result[1])+"</TD> <TD>"+str(result[2])+"</TD> <TD>"+str(result[3])+"</TD></TR>")
print("""</table>
    </div> """)
