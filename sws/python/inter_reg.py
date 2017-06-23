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

form = cgi.FieldStorage() # se instancia solo una vez
correo = form.getfirst('correo', 'empty')
password = form.getfirst('password', 'empty')
nombre = form.getfirst('nombre', 'empty')
celular = form.getfirst('celular', 'empty')

IN= form.getfirst('in', 'empty')


cursor=db.cursor()
if (correo!='empty'):
    sql="Select * From interesado where email='%s'" % (correo)
    cursor.execute(sql)
    resultado=cursor.fetchall()
else:
    resultado=""
cursor.close()

func.inicio()
print ("""
    </head> 
    <body>
    <div id="portada">
            <a href="_main.py"><img src="../sws/icono.png" alt="Obra de K. Haring" width="40" height="40"></a>
            <div id="header">""")
func.portada()

booleano=[0,0,0,0]

if re.match("^.*@.*.com$",correo):        
    booleano[0]=1;
if re.match("[0-9A-Za-z]",nombre):        
    booleano[1]=1;
if re.match("^.*[A-Z]{2,}.*[\~\@;:\^_]{1}.*$",password):
    booleano[2]=1;
if re.match("^[0-9]{3}-[0-9]{9}$",celular):        
    booleano[3]=1;

if(len(resultado)==0 and booleano[0]==1 and booleano[1]==1 and booleano[2]==1 and booleano[3]==1):
    insertar = db.cursor()
    insertar.execute("insert into interesado values(null,'%s','%s','%s','%s')" % (correo,password,nombre,celular))
    db.commit()
    print ("<br><h2>Exitoso</h2><br>")
    insertar.close()
    print("""<meta http-equiv="refresh" content = "0, url=_design.py?in=%i">"""%(int(IN)))

print("""
        <center><h1 id="bienve">Bienvenido ingrese sus datos por favor...</h1></center>
        <div id="inmobiliaria"><form method="post" name="miform">
                
        <input type="text" placeholder="Ingrese su Correo" name="correo"/><br>""")
if (booleano[0]==0 or correo=='empty'):
    print("<p>*campo obligatorio ejm: angel.cutipa@ucsp.com</p>")
print("""
    
        <input type="password" placeholder="Ingrese su Contrasena" name="password"/><br>""")
if (booleano[1]==0 or password=='empty'):
    print("<p>*campo obligatorio ejm: angeAG@123</p>")
print("""
        <input type="text" placeholder="Ingrese su nombre" name="nombre"/><br>""")
        
if (booleano[2]==0 or nombre=='empty'):
    print("<p>*campo obligatorio ejm: Angel</p>")
print("""
        <input type="text" placeholder="Ingrese su N celular" name="celular"/><br>""")
if (booleano[3]==0 or celular=='empty'):
    print("<p>*campo obligatorio ejm: 054-959654475</p>")
print("""
        <center><input type="submit" name="value" value=Registrarse></center>
    </form></div>""")



print ("""</body>
          </html>""")