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
IN = form.getfirst("in","empty")
 
print ("hola que tal",IN)
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
cursor3=db.cursor()
if (usuario!='empty'):
    sql="Select * From administradores where user='%s'" % (usuario)
    cursor.execute(sql)
    resultado=cursor.fetchall()
    sql2="Select * From inmobiliarias where users='%s'" % (usuario)
    cursor2.execute(sql2)
    resultado2=cursor2.fetchall()
    sql2="Select * From inmobiliarias where id='%i'" % (int(IN))
    cursor3.execute(sql2)
    resultado3=cursor2.fetchall()
else:
    resultado=""
    resultado2=""
    resultado3=""
cursor.close()
cursor2.close() 
cursor3.close()

booleano=[0,0,0,0,0,0,0,0,0]
if(resultado3!=""):
    if(usuario=="empty"):
        usuario=resultado3[0][1]
    if(password=="empty"):
        password=resultado3[0][2]
    if(codigo=="empty"):
        codigo=resultado3[0][3]
    if(nombre=="empty"):
        nombre=resultado3[0][4]
    if(ruc=="empty"):
        ruc=resultado3[0][5]
    if(email=="empty"):
        email=resultado3[0][6]
    if(direccion=="empty"):
        direccion=resultado3[0][7]
    if(telefono=="empty"):
        telefono=resultado3[0][8]
    if(celular=="empty"):
        celular=resultado3[0][9]


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
    #insertar.execute("insert into inmobiliarias values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (usuario,password,codigo,nombre,ruc,email,direccion,telefono,celular))
    insertar.execute("UPDATE inmobiliarias SET users='%s', password='%s', codigo='%s', nombre='%s', ruc='%s', email='%s', direccion='%s', telefono='%s', celular='%s' WHERE inmobiliarias.id = '%i'"%(usuario,password,codigo,nombre,ruc,email,direccion,telefono,celular,int(IN)))
    print("<center><p>Datos Actualizados</p></center>")
    db.commit()
    insertar.close()


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
                <li><a href="_inmob.py">Inmobiliaria</a></li>
                <li><a>Panel de Control</a></li>
                <li><a>Archivos</a></li>
                <li><a href="../../python/_main.py">Cerrar Sesion</a></li>
            </ul>
        </nav>
    </header>
    <section class="main">
        <div id = "barra">
            <p>Escritorio</p>
            <ul>
                <li><a href="_form_inmob.py">Registre un Inmueble</a></li>
                <li><a href="Update_dats.py?in=%i">"""%(int(IN))+"""Actualizar Datos</a></li>
""")

men = ["Multimedias","Paginas","Comentarios","Ventas","Alquiler","Apariencia","Interesados","Herramientas","Ajustes"];
func.printba(men,IN)

print("""</section>
        <center><h1 >Ingrese los datos a actualizar</h1></center>
        <div id="inmobiliaria"><form action="Update_dats.py?in=%i" method = "post"  class='contacto'>"""%(int(IN))+"""<div><label>Usuario:</label><input type="text" name = "usuario"></div>""")
if (booleano[0]==0 or usuario=='empty'):
    print("<p>*ejm: angel111</p>")
print("""            
            <div><label>Password:</label><input type="text" name = "password"></div>""")
if (booleano[1]==0 or password=='empty'):
     print("<p>*ejm: angeAG@123</p>")
print("""
           <div><label>Codigo:</label><input type="text" name = "codigo"></div>""")
if (booleano[2]==0 or codigo=='empty'):
    print("<p>*ejm: ASD-362728</p>")
print("""
            <div><label>Nombre:</label><input type="text" name = "nombre"></div>""")
if (booleano[3]==0 or nombre=='empty'):
    print("<p>*ejm: angel111</p>")
print("""
            <div><label>RUC:</label><input type="text" name = "ruc"></div>""")
if (booleano[4]==0 or ruc=='empty'):
    print("<p>*ejm: 23456789876  max: 11 dig.</p>")
print("""
            <div><label>Email:</label><input type="text" name = "email"></div>""")
if (booleano[5]==0 or email=='empty'):
    print("<p>*ejm: angel@gmail.com</p>")
print("""
            <div><label>Direccion:</label><input type="text" name="direccion"></input><br /></div>
            """)
if (booleano[5]==0 or direccion=='empty'):
    print("<p>*ejm: plaza cesamo</p>")
print("""
            <div><label>Telefono:</label><input type="text" name="telefono"></input><br /></div>
            """)
if (booleano[5]==0 or telefono=='empty'):
    print("<p>*ejm: 054-948372</p>")
print("""
            <div><label>Celular:</label><input name="celular"></input><br /></div>
            """)        
if (booleano[5]==0 or celular=='empty'):
    print("<p>*ejm: 054-948372</p>")   
print("""
            <div><input type="submit"  name="value" value= Actualizar></div>
        </form> </div>""")

print("""
    <footer>
        <p> Maldonado-Cutipa-Ttito - sws.com</p>
    </footer>

    </body>
</html>""")

