#!C:\Python34\python

import cgi
import cgitb; cgitb.enable()
import mysql.connector

print("Content-Type: text/html\n")

db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='inmobiliaria')
							 
							
form = cgi.FieldStorage() # se instancia solo una vez
usuario = form.getfirst('usuario', 'empty')
password = form.getfirst('password', 'empty')

if(usuario !='empty' and password != 'empty'):
	consulta = db.cursor()
	consulta.execute("SELECT * FROM administradores where user = '%s'" % (usuario))
	resultado_ad = consulta.fetchall()
	
	consulta.execute("SELECT * FROM inmobiliarias where users = '%s'" % (usuario))
	resultado_in = consulta.fetchall()

	if(len(resultado_ad)==0 and len(resultado_in)==0):
		print("""<center>No existe ningun usuario</center>""")
	elif(len(resultado_ad)!=0):
		if(resultado_ad[0][2]==password):
			print(""" <meta http-equiv="refresh" content = "0, url=admin/_admin.py?in=%i">"""%(resultado_ad[0][0]))
		else:
			print("""<center>No existe ningun usuario</center>""")
	elif(len(resultado_in)!=0):
		if(resultado_in[0][2]==password):
			print(""" <meta http-equiv="refresh" content = "0, url=admin/_inmob.py?in=%i">"""%(resultado_in[0][0]))
		else:
			print("""<center>No existe ningun usuario</center>""")

print("""
	<html>
	<head>
		<title>Administrador</title>
		<meta charset="utf-8">
        <link rel="shortcut icon" type="image/x-icon" href="../sws/icono.png">
        <link rel="stylesheet" href="css/style_log.css"
	</head>
	<body>
		<form action="_index.py" method="post" name="miform">
			<h2>SWS</h2>
    		<input type="text" placeholder="Usuario" name="usuario"/><br>
    		<input type="password" placeholder="Password" name="password"/><br>
			<input type="submit" value="Log in" id="but">
		</form>
	</body>
	</html>
""")
