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

print("""
        <!DOCTYPE html>
        <html lang="en" >
        <head>
                <title>Formulario</title>
                <meta charset="UTF-8">
                <link href="../css/style_de.css" rel="stylesheet" type="text/css" media="screen">
                <script type="text/javascript" src="http://www.google.com/jsapi?key=CODIGO-PERSONAL"></script>
        </head>
        <body>""")

form = cgi.FieldStorage() # se instancia solo una vez
usuario = form.getfirst('usuario', 'empty')
password = form.getfirst('password', 'empty')
codigo = form.getfirst('codigo', 'empty')
nombre = form.getfirst('nombre', 'empty')
ruc = form.getfirst('ruc', 'empty')
email = form.getfirst('email', 'empty')
direccion = form.getfirst('direccion', 'empty')
telefono = form.getfirst('telefono', 'empty')
celular = form.getfirst('celular', 'empty')

cursor=db.cursor()
cursor2=db.cursor()
if (usuario!='empty'):
    sql="Select * From administradores where user='%s'" % (usuario)
    cursor.execute(sql)
    resultado=cursor.fetchall()
    sql2="Select * From inmobiliarias where users='%s'" % (usuario)
    cursor2.execute(sql2)
    resultado2=cursor2.fetchall()
else:
    resultado=""
    resultado2=""
cursor.close()
cursor2.close() 

booleano=[0,0,0,0,0,0,0,0,0]

if re.match("[0-9a-z]{1,}$",usuario):        
    booleano[0]=1;
if re.match("^.*[A-Z]{2,}.*[\~\@;:\^_]{1}.*$",password):
    booleano[1]=1;
if re.match("[A-Z]{3}-[0-9]{6}$",codigo):        
    booleano[2]=1;
if re.match("[0-9A-Za-z]",nombre):        
    booleano[3]=1;
if re.match("[0-9]{0,11}$",ruc):        
    booleano[4]=1;
if re.match("^.*@.*.com$",email):        
    booleano[5]=1;
if re.match("[a-zA-Z0-9]",direccion):        
    booleano[6]=1;
if re.match("^[0-9]{3}-[0-9]{6}$",telefono):        
    booleano[7]=1;
if re.match("^[0-9]{3}-[0-9]{9}$",celular):        
    booleano[8]=1;

if(len(resultado)==0 and len(resultado2)==0 and booleano[0]==1 and booleano[1]==1 and booleano[2]==1 and booleano[3]==1 and booleano[4]==1 and booleano[5]==1 and booleano[6]==1 and booleano[7]==1 and booleano[8]==1):
	insertar = db.cursor()
	insertar.execute("insert into inmobiliarias values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (usuario,password,codigo,nombre,ruc,email,direccion,telefono,celular))
	db.commit()
	print ("ID de ultimo registro insertado: %s<br>" % insertar.lastrowid)
	insertar.close()
print ("""
    <div id="portada">
            <a href="_main.py"><img src="../sws/icono.png" alt="Obra de K. Haring" width="40" height="40"></a>
            <div id="header">""")
func.portada()
print("""    </div>
             </div>""")

print("""
    <center><h1 id="bienve">Bienvenido ingrese sus datos por favor...</h1></center>
	<div id="inmobiliaria"><form action="for_reg.py" method="post" name="miform">
                
		<input type="text" placeholder="Ingrese Nombre de Usuario" name="usuario"/><br>""")
if (booleano[0]==0 or usuario=='empty'):
    print("<p>*campo obligatorio ejm: angel111</p>")
print("""
	
		<input type="text" placeholder="Ingrese su Contrasena" name="password"/><br>""")
if (booleano[1]==0 or password=='empty'):
    print("<p>*campo obligatorio ejm: angeAG@123</p>")
print("""
		
		<input type="text" placeholder="Codigo" name="codigo"/><br>""")
if (booleano[2]==0 or codigo=='empty'):
    print("<p>*campo obligatorio ejm: ASD-362728</p>")
print("""
		<input type="text" placeholder="Ingrese su nombre" name="nombre"/><br>""")
if (booleano[3]==0 or nombre=='empty'):
    print("<p>*campo obligatorio ejm: angel111</p>")
print("""
		
		<input type="text" placeholder="Ingrese su N RUC" name="ruc"/><br>""")
if (booleano[4]==0 or ruc=='empty'):
    print("<p>*campo obligatorio ejm: 23456789876  max: 11 dig.</p>")
print("""
		
		<input type="text" placeholder="Ingrese su email" name="email"/><br>""")
if (booleano[5]==0 or email=='empty'):
    print("<p>*campo obligatorio ejm: angel@gmail.com</p>")
print("""
		
		<input type="text" placeholder="Ingrese su direccion" name="direccion"/><br>""")
if (booleano[6]==0 or direccion=='empty'):
    print("<p>*campo obligatorio ejm: plaza cesamo</p>")
print("""
		
		<input type="text" placeholder="Ingrese su telefono" name="telefono"/><br>""")
if (booleano[7]==0 or telefono=='empty'):
    print("<p>*campo obligatorio ejm: 054-948372</p>")
print("""
		
		<input type="text" placeholder="Ingrese su celular" name="celular"/><br>""")
if (booleano[8]==0 or celular=='empty'):
    print("<p>*campo obligatorio ejem: 051-950887373</p>")

print("""
		<center><input type="submit" name="value" value=Registrarse></center>
	</form></div>""")

print ("""</body>
          </html>""")
