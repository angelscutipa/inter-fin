#!/usr/include/python2.7
import cgi
import cgitb; cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage() # se instancia solo una vez
nombre = form.getfirst('nombre', 'empty')
apellido = form.getfirst('apellido', 'empty')
musica = form.getlist("musica")

# Para evitar script injection
nombre = cgi.escape(nombre)

print ("""
    <html>
    <head>
    <TITLE>CGI script ! Python</TITLE>
    </head>
    <body>
"""
)
print ('Nombre: ', nombre , '<br>')
print ('Apellido: ', apellido , '<br>')
print (musica)
print ("""
    </body>
    </html>
"""
)
