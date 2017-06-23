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

form = cgi.FieldStorage()
IN = form.getfirst("in","empty")

cursor=db.cursor()
sql="Select * From imagenes where inmueble_id='%d'" % (int(IN))
cursor.execute(sql)
resultado=cursor.fetchall()
sql="Select * From inmuebles where id='%i'" % (int(IN))
cursor.execute(sql)
resultado2=cursor.fetchall()

func.inicio()

print(""" <script type="text/javascript"> 
	       $(document).ready(function(){
				formSubmit()
			})
			function formSubmit(){
				$('#contenido').submit(function(e){
					e.preventDefault()
					var correo=$('.correo').val()
					var password=$('.password').val()
					var consulta=$('.consulta').val()
					var data='correo='+correo+'&password='+password+'&consulta='+consulta;

					$.ajax({
						url:'interesado.py?in=%i',"""%(int(IN))+"""
						type: 'get',
						data: data,
						beforeSend: function () {
			                    $("#contenido .msn").html("<br>Procesando, espere por favor...");
			            },
			            success:  function (response) {
								$("#contenido .msn").html("");
			                    $("#contenido .show").html(response);
			            }
					})

				})
			}
			</script> """)
print ("""
    </head> 
    <body>
    <div id="portada">
            <a href="_main.py"><img src="../sws/icono.png" alt="Obra de K. Haring" width="40" height="40"></a>
            <div id="header">""")
func.portada()
print("""    </div>
             </div>""")
lista=['"imagen1"','"imagen2"','"imagen3"'];

print("""<div class="titulo">
            <h1>%s</h1>"""%(resultado2[0][11])+"""
            <div id="galeria">""")
for resul in resultado:
    if(str(resul[3])=="si"):
        print("""<img data-original='%s'"""%(resul[2])+"""src='%s'"""%(resul[2])+"""alt="Obra de K. Haring" width="400" height="258">""")
print("</div>")
for i in range(0,len(lista)):
    print("""<div id="""+str(lista[i])+">")
    print("""<img src='%s'"""%(resultado[0][2])+"""alt="Obra de K. Haring" width="80" height="50">""")
    print("""</div>""")
print("""
            <div id="precio">
                    <h2>Precio: $2500</h2>
            </div>
    </div>
    <div id="anunciante">
            <center><h1>@Angelscutipa</h1></center>
            <h2>Aqui si esta interesado:</h2>
            <form method="post" id="contenido" >
            <input type="text" placeholder="Ingrese su Correo" class="correo">
            <input type="password" placeholder="Ingrese su Password" class="password">
            <input style="height:30px" type="text" placeholder="Ingrese su Consulta" class="consulta">
            <center><button class="">Enviar</button></center>
            <div class="msn"></div>
	    <div class="show"></div>
            </form>
            
    </div>
    <div id="deta"><h1>Detalles del Inmueble</h1></div>

    <div class="detalles">
            <table>""")

lista=["Habitaciones","SS.HH.","Servicios","Area m2","Direccion","Direccion"];

func.tabla(lista);
print ("""
                    <tr>
                      <td>15</td>
                      <td>15</td>
                      <td><ul>
                            <li>Internet</li>
                            <li>Cable</li>
                            <li>Mobilidad</li>
                      </ul></td>
                      <td>250 m2</td>
                      <td>Plaza de Armas</td>
                      <td>954821563</td>
                    </tr>
            </table>
            <h2><>Descripcion:</h2>
            <p>'%s'</p>"""%(resultado2[0][7])+"""
            <h2><>Referencias:</h2>
            <p>'%s'</p>"""%(resultado2[0][3])+"""
    </div>
    <script type="text/javascript">
        //<![CDATA[  
        google.load('maps', '1', {callback:simple});var map;
        function simple(){	
        if (GBrowserIsCompatible()) { 
        var map = new GMap2(document.getElementById("map1"));
        map.setCenter(new GLatLng(20.0972, -81.6503), 4);}}
        window.onload=function(){simple();}
        //]]>
        </script>
        <div id="map1"></div>
    </body>
    </html>

	"""
)
