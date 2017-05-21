#!/usr/include/python2.7
import cgi
import cgitb; cgitb.enable()

print("Content-Type: text/html\n")

print ("""
    <html>
    <head>
    <TITLE>CGI script ! Python</TITLE>
    </head>
    <body>
	"""
)

print ("<ul>")
for i in range(0,10):
	print ("<li>"+str(i)+"</li>")
print ("<ul>")


print("""
	<form action="recibe.py" method="post" name="miform">
		nombre:
		<input type="text" maxlength="10" size="10" name="nombre"><br>
		apellido:
		<input type="text" maxlength="10" size="10" name="apellido"><br>


		musica favorita:
		<input type="checkbox" name="musica" value="rock" checked>Rock
		<input type="checkbox" name="musica" value="pop" checked>Pop
		<input type="checkbox" name="musica" value="heavy">Heavy
		<input type="checkbox" name="musica" value="tecno">Tecno<br>



		<input type="submit" name="enviar" value="enviar"><br>
	</form>

""")
print("""
	<h1>Hola</h1>
    <img src="asd.jpg">
    </body>
    </html>
	"""
)
