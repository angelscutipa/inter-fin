#!C:\Python34\python
import cgi
import cgitb; cgitb.enable()
import func
import mysql.connector

print("Content-Type: text/html\n")
db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='inmobiliaria')
							 
print("""
        <!DOCTYPE html>
        <html lang="en" >
        <head>
                <title>Login</title>
                <meta charset="UTF-8">
                <link href="../css/style_de.css" rel="stylesheet" type="text/css" media="screen">
                <script type="text/javascript" src="http://www.google.com/jsapi?key=CODIGO-PERSONAL"></script>
        </head>
        <body>""")
							
form = cgi.FieldStorage() # se instancia solo una vez
usuario= form.getfirst('usuario', 'empty')
password= form.getfirst('password', 'empty')

cursor=db.cursor()
if (usuario!='empty'):
    sql="Select * From administradores where user='%s'" % (usuario)
    cursor.execute(sql)
    resultado=cursor.fetchall()
else:
    resultado="";
cursor.close()  
print ("""
    <div id="portada">
            <a href="_main.py"><img src="../sws/icono.png" alt="Obra de K. Haring" width="40" height="40"></a>
            <div id="header">""")
func.portada()
print("""    </div>
             </div>""")

print("""
	<center><div id="_login"><form action="login.py" method="post" name="miform">
                <fieldset>
                <h2>Usuario</h2> 
		<input type="text" placeholder="Ingrese su nombre" name="usuario"/><br>
		<h2>Password</h2> 
		<input type="password" placeholder="Ingrese su password" name="password"/><br>""")
if (resultado!=""):
    for registro in resultado:
        resultado=resultado;
    if(registro[2]==password):
        print("""
        <h1>que caraasdbshf </h1>
        <input type="submit" name="value" value=ingresar>""")
else:
    print("""
    <h1>hola comoestas </h1>
    <a href="diseno.py"><input type="submit" name="value" value=ingresar></a>""")
			

print("""
		</fieldset>
	</form></div></center>""")   

print ("""</body>
          </html>""")
db.close()
