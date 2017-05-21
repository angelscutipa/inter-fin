def menu():
	print("""
		<!DOCTYPE HTML>
		<html lang="es">
			<head>
				<meta charset="utf-8">
				<script type="text/javascript" src="../js/load.js"></script>
				<link rel="stylesheet" href="../css/style.css">
				<link rel="shortcut icon" type="image/x-icon" href="../sws/icono.png">
				<title>Alquiler y Venta de Inmuebles</title>
			</head>
			<body>
				<header>
					<nav>
	""")

	me = ["SWS","Inmuebles","Venta","Alquiler","Servicios","Blog","Registrate","Ingresar"];
	print ("<ul>")
	for i in range(0,len(me)):
		print ("<li><a>"+str(me[i])+"</a></li>")
	print ("</ul>")

def inicio():
    print("""
        <!DOCTYPE html>
        <html lang="en" >
        <head>
                <title>Caracteristicas</title>
                <meta charset="UTF-8">
                <link href="../css/style_de.css" rel="stylesheet" type="text/css" media="screen">
                <script type="text/javascript" src="http://www.google.com/jsapi?key=CODIGO-PERSONAL"></script>
        </head> """)


items=["Casas","Departamentos","Terrenos","Locales"];
service=["Empresa","Externos","Servicios"];
d_service=["Ventas","Alquiler","Proyectos","Otros"];
nosotros=["Informate","Mision","Vision","Historia"];
def servicios(items,x):
    print("<ul>")
    for i in range(0,len(items)):
        if (x==1 and i==len(items)-1):
            print("<li><a href="">"+ str(items[i])+"</a>")
            servicios(d_service,0)
            print("</li>")
        else:
            print("<li><a href="">"+ str(items[i])+ "</a></li>")
    print("</ul>")

def portada():
    lista = ["SWS","Venta","Alquiler","Proyectos","Contacto","Servicios","Nosotros","Ingresar","Registrate"];
    print("""<ul class="nav">""")
    for i in range(0, len(lista)):
        if (lista[i]=="Registrate"):
            print(""""<li><a href="for_reg.py">"""+ str(lista[i])+"</a>")
            print("</li>")
        elif (lista[i]=="Ingresar"):
            print(""""<li><a href="Login.py">"""+ str(lista[i])+"</a>")
            print("</li>")
        elif (i==1):
            print("<li><a href="">"+ str(lista[i])+"</a>")
            servicios(items,0)
            print("</li>")
        elif (i==2):
            print("<li><a href="">"+ str(lista[i])+"</a>")
            servicios(items,0)
            print("</li>")
        elif (i==5):
            print("<li><a href="">"+ str(lista[i])+"</a>")
            servicios(service,1)
            print("</li>")
        elif (i==6):
            print("<li><a href="">"+ str(lista[i])+"</a>")
            servicios(nosotros,0)
            print("</li>")
        else:
            print("<li><a href="">"+ str(lista[i])+"</a></li>")

    print("""</ul>""")

def tabla(lista):
    print("<tr>")
    for i in range(0,len(lista)):
        print("<td><strong>"+str(lista[i])+"</strong></td>")
    print("</tr>")

