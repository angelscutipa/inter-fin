#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
import portada

print("Content-Type: text/html\n")

portada.inicio()

print ("""
    <body>
    <div id="portada">
            <img src="../sws/icono.png" alt="Obra de K. Haring" width="40" height="40">
            <div id="header">
            
        </div>
    </div>
    <div class="titulo">
            <h1>Nombre del Inmueble</h1>
            <div id="galeria">
                    <img data-original="../sws/pacman.jpg" src="../sws/pacman.jpg" alt="Obra de K. Haring" width="400" height="258" data-zoom-image="imagenes/pacman.jpg">
            </div>
            <div id="imagen1">
                    <img src="../sws/casa.jpg" alt="Obra de K. Haring" width="80" height="50">
            </div>
            <div id="imagen2">
                    <img src="../sws/casa.jpg" alt="Obra de K. Haring" width="80" height="50">
            </div>
            <div id="imagen3">
                    <img src="../sws/casa.jpg" alt="Obra de K. Haring" width="80" height="50">
            </div>
            <div id="precio">
                    <h2>Precio: $2500</h2>
            </div>
    </div>
    <div id="anunciante">
            <h1>@Angelscutipa</h1>
            <h2>Anunciante</h2>
            <p>
                    <input type="text" placeholder="Ingrese su Nombre" name="nombre"/>
            </p>
            <p> 
                    <input type="text" placeholder="Ingrese su Correo" name="nombre"/>
            </p>
            <p>
                    <input type="text" placeholder="Ingrese su telefono" name="nombre"/>
            </p>
            <p>
                    <input type="text" placeholder="Ingrese su texto" name="nombre"/>
            </p>
            <a href="#">
            <div id="sent">
                    <h1>Enviar</h1>
            </div>
            </a>
    </div>
    <div class="titulo"><h1>Detalles del Inmueble</h1></div>

    <div class="detalles">
            <table>
                    <tr>
                      <td><strong>Habitaciones</strong></td>
                      <td><strong>SS. HH.</strong></td>
                      <td><strong>Servicios</strong></td>
                      <td><strong>Area m2</strong></td>
                      <td><strong>Direccion</strong></td>
                      <td><strong>Telefono</strong></td>
                    </tr>
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
            <p>"But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"</p>
    </div>
    </body>
    </html>

	"""
)

