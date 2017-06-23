#!C:\Python34\python

import cgi
import cgitb; cgitb.enable()
import mysql.connector

print("Content-Type: text/html\n")

db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='sws')
							 
							
form = cgi.FieldStorage() # se instancia solo una vez
usuario = form.getfirst('usuario', 'empty')
password = form.getfirst('password', 'empty')
			
			
"""			
if(usuario !='empty' and password != 'empty'):
	consulta=db.cursor()
	cursor.execute("SELECT * FROM administradores where user = '%s'" % (usuario))
	resultado = cursor.fetchall()
	if(len(resultado) == 0):
		insertar = db.cursor()
		insertar.execute("insert into administradores values(null,'%s','%s')" % (usuario,password))
		db.commit()
		print ("ID de ultimo registro insertado: %s<br>" % insertar.lastrowid)
		insertar.close()
	else:
		print("ya existe")
		"""

if(usuario !='empty' and password != 'empty'):
	consulta = db.cursor()
	consulta.execute("SELECT * FROM administradores WHERE user = '%s'" % (usuario));
	resultado = consulta.fetchall()
	print(resultado)
	print(resultado[0][2])
	print ("tamaño: %s<br>" % len(resultado))
							  
print ("""
    <html>
    <head>
    <TITLE>CGI script ! Python</TITLE>
    </head>
    <body>
	"""
)

print("""
	<form action="prueba.py" method="post" name="miform">
		usuario:
		<input type="text" maxlength="10" size="10" name="usuario"><br><br>
		password:
		<input type="password" name="password" size="15" maxlength="10"><br>
		
		<input type="submit" name="enviar" value="enviar"><br>
	</form>
""")

print("""	
	</body>
</html>
""")