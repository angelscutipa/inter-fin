#!C:\Python34\python

import cgi
import cgitb; cgitb.enable()
import func
import mysql.connector
import re

print("Content-Type: text/html\n")


form = cgi.FieldStorage()
IN = form.getfirst("in","empty")

print("""
	<html>
	<head>		
        <meta charset="utf-8">
        <script type="text/javascript" src="../js/load.js"></script>
        <link rel="stylesheet" href="../css/style_ad.css">
        <link rel="shortcut icon" type="image/x-icon" href="../../sws/icono.png">
        <title>Panel de Administrador</title>
	</head>
	<body>
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
            <p>Escritorio</p>
            <ul>
""")

men = ["Multimedias","Enlaces","Paginas","Comentarios","Inmuebles","Apariencia","Inmobiliarias","Herramientas","Ajustes","Otros"];
func.printba1(men,IN)

print("""
            </ul>
        </div>
        <div class="articles">
            <a href="#">
                <img src="../img/Crystal_Clear_write.gif"  width= "110" alt="edit" />
                <span>Nuevo Articulo</span>
            </a>
            <a href="#">
                <img src="../img/Crystal_Clear_file.gif"  width="110" alt="edit" />
                <span>Subir</span>
            </a>
            <a href="#">
                <img src="../img/Crystal_Clear_files.gif"  width="110" alt="edit" />
                <span>Articulos Subidos</span>
            </a>
            <a href="#">
                <img src="../img/Crystal_Clear_user.gif"  width="110" alt="edit" />
                <span>Perfil</span>
            </a>
            <a href="#">
                <img src="../img/Crystal_Clear_stats.gif" width="110" alt="edit" />
                <span>Estadisticas</span>
            </a>
            <a href="#">
                <img src="../img/Crystal_Clear_settings.gif" width="110" alt="edit" />
                <span>Ajustes</span>   
            </a>
        </div>
    </section>
    <footer>
    	<p> Maldonado-Cutipa-Ttito - sws.com</p>
    </footer>

	</body>
</html>
""")
