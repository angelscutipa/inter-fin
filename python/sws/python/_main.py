#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
import func

print("Content-Type: text/html\n")

func.menu()

print("""
			</nav>
    		<div class = "logotipo">
    			<img src="../sws/1.jpg" id="imagen" alt="">
	      		<div id="spa">
	      			<h2>Busca tu Inmueble al mejor Precio</h2>
     				<ul>
	   					<li><a>Seleccione</a></li>
	   					<li><a>Clase</a></li>
	   					<li><a>Departamento-Zona</a></li>
	    			</ul>
	    			<h4>Casas de Playa | Casas de Campo | Alquiler Turistas</h4>
	    		</div>
	    		<div id="lo">
	    			<img src="../sws/icono.png" alt="">
	    		</div>
    		</div>
    		<div id="asd"><h1>Alquiler y Venta de Inmuebles</h1></div>
    	</header>	

    	<section class="main"> <!-- empty section -->
			<div id="ar"><h3>SWS-CORP.</h3></div>
			<div class="articles">
			"""
			)

desc = ["Alquiler de Casa Vacia Urb. El Golf", "Alquiler de Casa Vacia Los Cantaros", "Venta de Casa Urb. La Perla", "Alquiler de Casa Las Castellanas ", "Remate - Venta de Terreno Chancay", "Venta de Terreno Urb. Santa Maria", "Alquiler de Casa Vacia Urb. El Golf ", "Alquiler de Casa Vacia Los Cantaros", "Venta de Casa Urb. La Perla", "Alquiler de Casa Las Castellanas ", "Remate - Venta de Terreno Chancay", "Venta de Terreno Urb. Santa Maria"];
imagen = ["../sws/foto1.jpg"];
print("<ul>")
for i in range(0,len(desc)):
	print ("<li>"+"""<a href="diseno.py"><img src="../sws/foto1.jpg" alt=""></a>"""+str(desc[i])+"</li>")
	#print(<img src=str(imagen[i]) alt="">)
print("</ul>")

print("""
			</div>
	
			<aside>
				<p>
					Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis.
				</p>
			</aside>

		</section>

		<footer>
			<p> Maldonado-Cutipa-Ttito - sws.com</p>
		</footer>
	</body>
</html>

"""
)
