#!C:\Python27\python
import cgi
import cgitb; cgitb.enable()
import re

print("Content-Type: text/html\n")

form = cgi.FieldStorage() # se instancia solo una vez
verificar = form.getfirst('verificar', 'empty')
#^[^0-9A-Z]*$
if re.match("[A-Z]{3}-[0-9]{6}$",verificar):        
    print ('cumple patron')

else:
    print ('no cumple patron')


# Para evitar script injection

print ("""
    <html>
    <head>
    <TITLE>CGI script ! Python</TITLE>
    </head>
    <body>
	"""
)
print("""
	<form action="formulario.py" method="post" name="miform">

		<input type="text" name="verificar"/>
		
		<input type="submit" name="enviar" value="verificar">
	</form>
    </body>
    </html>
	"""
)

