#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
import func

print("Content-Type: text/html\n")

func.inicio()

print ("""
    <body>
    <div id="portada">
            <a href="_main.py"><img src="../sws/icono.png" alt="Obra de K. Haring" width="40" height="40"></a>
            <div id="header">""")
func.portada()
print("""    </div>
             </div>""")
lista=['"imagen1"','"imagen2"','"imagen3"'];

print("""<div class="titulo">
            <h1>Nombre del Inmueble</h1>
            <div id="galeria">
                    <img data-original="../sws/pacman.jpg" src="../sws/pacman.jpg" alt="Obra de K. Haring" width="400" height="258" data-zoom-image="imagenes/pacman.jpg">
            </div>""")
for i in range(0,len(lista)):
    print("""<div id="""+str(lista[i])+">")
    print("""<img src="../sws/casa.jpg" alt="Obra de K. Haring" width="80" height="50">""")
    print("""</div>""")
print("""
            <div id="precio">
                    <h2>Precio: $2500</h2>
            </div>
    </div>
    <div id="anunciante">
            <h1>@Angelscutipa</h1>
            <h2>Anunciante</h2>""")

items=['"Ingrese su Nombre"','"Ingrese su Correo"','"Ingrese su Telefono"','"Ingrese su Texto"']

for i in range(0,len(items)):
    print("<p>")
    print("""<input type="text" placeholder= """+ str(items[i])+""" name="nombre"/>""")
    print("</p>")
print("""
            <a href="#">
            <div id="sent">
                    <h1>Enviar</h1>
            </div>
            </a>
    </div>
    <div class="titulo"><h1>Detalles del Inmueble</h1></div>

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
            <h2>>Descripcion:</h2>
            <p>"But I must explain  truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter because it is pain, but because  pleasure?"</p>
            <h2>>Referencias:</h2>
            <p>En esta parte podria ir una pequenia referencia de donde queda el inmueble que se ofrece. Para la mejor ubicacion del inmueble.</p>
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
