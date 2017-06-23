#!C:\Python34\python
import cgi
import cgitb; cgitb.enable()
import mysql.connector
db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='inmobiliaria')

print("Content-Type: text/html\n")

form = cgi.FieldStorage() # se instancia solo una vez
q = form.getfirst('q', 'empty')

if(q=="venta" or q=="alquiler"):
	cursor=db.cursor()
	sql="Select * From tipos where nombre like '%s'" % (q);
	cursor.execute(sql)
	resultado=cursor.fetchall()
	sql="Select * From inmuebles where tipo_id like '%s'" % (resultado[0][0]);
	cursor.execute(sql)
	resultado2=cursor.fetchall()
	if(len(resultado2) == 0):
		print("No hay resultado tipo<b>",q,"</b>");
	else:
		for resul in resultado2:
			cursor=db.cursor()
			sql="Select * From imagenes where inmueble_id='%d'" % (int(resul[0]))
			cursor.execute(sql)
			resultado3=cursor.fetchall()
			print("<ul>")
			print ("""<center><div class="res"><a href="_design.py?in=%i">"""%(resul[0])+"""<li>"""+"""<img src='%s' alt="">"""%(resultado3[0][2])+resul[11]+"</li></a></div></center>")
			print("</ul>")
	cursor.close()   

elif(q != "empty"):
	cursor=db.cursor()
	sql="Select count(*) as num From inmuebles where nombre like '%s'" % (q);
	cursor.execute(sql)
	resultado=cursor.fetchall()
	
	if(resultado[0][0] == 0):
		print("No hay resultado<b>",q,"</b>");
	else:
		q="%"+q+"%"
		sql="Select * From inmuebles where nombre like '%s'" % (q);
		cursor.execute(sql)
		resultado=cursor.fetchall()
		
		for i in range(0,len(resultado)):
			cursor=db.cursor()
			sql="Select * From imagenes where inmueble_id='%d'" % (int(resultado[i][0]))
			cursor.execute(sql)
			resultado3=cursor.fetchall()
			print("<ul>")
			print ("""<div class="res"><a href="_design.py?in=%i">"""%(resultado[i][0])+"""<li>"""+"""<img src='%s' alt="">"""%(resultado3[0][2])+resultado[i][11]+"</li></a></div>")
			print("</ul>")
	cursor.close()   
	
