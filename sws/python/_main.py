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
cursor=db.cursor()
sql="Select * From inmuebles where tipo_id=1"
cursor.execute(sql)
resultado=cursor.fetchall()
sql="Select * From inmuebles where tipo_id=2"
cursor.execute(sql)
resultado2=cursor.fetchall()

func.menu()

print("""<script type="text/javascript" src="jquery.min.js"></script> 
<script type="text/javascript"> 
$(document).ready(function() {
   $("#buscador").submit(function() {
	 q = $(this).parent().find("input");
	 $(this).parent().find(".show").html("");
	 if(q.val() == ""){
		q.focus();
	 }else{
		getData(q.val());
	 }
	 return false;
   });
 });

function getData(valor){
        $.ajax({
                data:  {"q":valor},
                url:   'buscar.py',
                type:  'get',
                beforeSend: function () {
                        $("#buscador.msn").html("Procesando, espere por favor...");
                },
                success:  function (response) {
						$("#buscador .msn").html("");
                        $("#buscador .show").html(response);
                }
        });
}
</script>
</head> """)

#print(resultado[0][2])

print("""
    <body>
        <header>
            <nav>
                <ul>
                    <li><a href="_main.py">SWS</a></li>
                    <li><a href="_main.py">Inmuebles</a></li>""")
me = ["Venta","Alquiler","Servicios","Blog"];
func.printba(me)
print("""<li><a href="for_reg.py">Registrate</a></li>
		<li><a href="../admin/_index.py">Ingresar</a></li>""")
		
print("""		</ul>
			</nav>
    		<div class = "logotipo">
    				<form method="post" id="buscador" >
    					<input placeholder="Ingrese inmuebles, tipo: venta o alquiler" type="text" class="buscado">
    					<button>Buscar</button>
    					<div class="msn"></div>
						<div class="show"></div>
    				</form>
    			<img src="../sws/1.jpg" id="imagen" alt="">
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
imagen = ["../sws/foto1.jpg"];

print("<ul>")
for i in range(0,len(resultado)):
	cursor=db.cursor()
	sql="Select * From imagenes where inmueble_id='%d'" % (int(resultado[i][0]))
	cursor.execute(sql)
	resultado3=cursor.fetchall()
	print ("""<a href="_design.py?in=%i">"""%(resultado[i][0])+"""<li>"""+"""<img src='%s' alt="">"""%(resultado3[0][2])+resultado[i][11]+"</li></a>")
	#print(<img src=str(imagen[i]) alt="">)
print("</ul>")

imagen = ["../sws/foto1.jpg"];

print("<ul>")
for i in range(0,len(resultado2)):
	cursor=db.cursor()
	sql="Select * From imagenes where inmueble_id='%d'" % (int(resultado2[i][0]))
	cursor.execute(sql)
	resultado3=cursor.fetchall()
	print ("""<a href="_design.py?in=%i">"""%(resultado2[i][0])+"""<li>"""+"""<img src='%s' alt="">"""%(resultado3[0][2])+resultado2[i][11]+"</li></a>")
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
