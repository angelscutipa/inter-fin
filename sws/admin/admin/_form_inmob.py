#!C:\Python34\python
import cgi
import cgitb; cgitb.enable()
import mysql.connector
import re

print("Content-Type: text/html\n")

db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='inmobiliaria')

form = cgi.FieldStorage()
codigo = form.getfirst('codigo','empty')
direccion = form.getfirst('direccion', 'empty')
referencia = form.getfirst('referencia','empty')
precio = form.getfirst('precio','empty')
superficieTotal = form.getfirst('superficieTotal' , 'empty')
superficieConstruida = form.getfirst('superficieConstruida' , 'empty')
descripcion = form.getfirst('descripcion','empty')
tipo_id = form.getfirst('tipo_id','empty')
inmobiliaria_id = form.getfirst('inmobiliaria_id','empty')


booleano=[0,0,0,0,0,0,0,0,0]

if re.match("[A-Z]{3}-[0-9]{6}-[0-9]{3}",codigo):        
    booleano[0]=1;
if re.match("[a-zA-Z]|[0-9]",direccion):
    booleano[1]=1;
if re.match("[a-zA-Z]|[0-9]",referencia):        
    booleano[2]=1;
if re.match("[+-]?\d+(\.\d+|[eE][+-]?\d+)?",precio):        
    booleano[3]=1;
if re.match("[+-]?\d+(\.\d+|[eE][+-]?\d+)?",superficieTotal):        
    booleano[4]=1;
if re.match("[+-]?\d+(\.\d+|[eE][+-]?\d+)?",superficieConstruida):        
    booleano[5]=1;
if re.match("[a-zA-Z]|[0-9]",descripcion):        
    booleano[6]=1;
if re.match("",tipo_id):        
    booleano[7]=1;
if re.match("",inmobiliaria_id):        
    booleano[8]=1;



if(booleano[0]==1 and booleano[1]==1 and booleano[2]==1 and booleano[3]==1 and booleano[4]==1 and booleano[5]==1 and booleano[6]==1 and booleano[7]==1 and booleano[8]==1):
    insertar = db.cursor()
    insertar.execute("insert into inmuebles values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (codigo,direccion,referencia,precio,superficieTotal,superficieConstruida,descripcion,tipo_id,inmobiliaria_id))
    db.commit()
    print("ID de ultimos registros insertado: %s<br>" % insertar.lastrowid)
    insertar.close()

print("""
    <!DOCTYPE html>
   <html lang="en">
    <head>
        <title>Inmuebles</title>
         <meta charset="UTF-8">
        <link rel='stylesheet' href="../css/formulario.css"></link>
    </head> 
    """)

print("""
    <body>
     <header>
        <nav>
        <ul>
        <li><a href="_inmob.py">Inmobiliaria</a></li>
        <li><a href="">Panel de Control</a></li>
        <li><a href="">Archivos</a></li>
        <li><a href="../../python/_main.py">Cerrar Sesion</a></li>
        <ul>
        </nav>
    </header>

         
""")

print("""
        <h1 >Registro de Inmueble</h1>
        <div id="inmobiliaria"><form action="_form_inmob.py" method = "post"  class='contacto'>
    
            <div><label>Codigo:</label><input type="text" name = "codigo"></div>""")
if (booleano[0]==0 or codigo=='empty'):
    print("<p>*campo obligatorio ejm: ABC-051116-001</p>")
print("""            
            <div><label>Direccion:</label><input type="text" name = "direccion"></div>""")
if (booleano[1]==0 or direccion=='empty'):
     print("<p>*campo obligatorio ejm: Calle ejemplo N: xx")
print("""
            <div><label>Referencia:</label><textarea id="message" class="input" name="referencia" rows="7" cols="30"></textarea></div>""")

print("""
            <div><label>Precio:</label><input type="text" name = "precio"></div>""")
if (booleano[3]==0 or precio=='empty'):
    print("<p>*campo obligatorio ejm: 123.123")
print("""
            <div><label>Superficie Total:</label><input type="text" name = "superficieTotal"></div>""")
if (booleano[4]==0 or superficieTotal=='empty'):
    print("<p>*campo obligatorio ejm: 123.123") 
print("""
            <div><label>Superficie construida:</label><input type="text" name = "superficieConstruida"></div>""")
if (booleano[5]==0 or superficieConstruida=='empty'):
    print("<p>*campo obligatorio ejm: 123.123")

print("""
            <div><label>Descripcion:</label><textarea id="message" class="input" name="descripcion" rows="7" cols="30"></textarea><br /></div>
            """)
            
if (booleano[6]==0 or descripcion=='empty'):
    print("<p>.</p>")


print("""
            <div><label>Tipo_id:</label><select name="tipo_id">
               <option value="1">opcion</option> 
               <option value="2">opcion2 </option> 
              
            </select>""")


if (booleano[7]==0 or tipo_id=='empty'):
    print("<p>.</p>")





print("""
            <div><label>Inmobiliaria_id:</label><select name="inmobiliaria_id">
               <option value="1">opcion </option> 
               <option value="2">opcion2 </option> 
               
            </select></div>
            """)
if(booleano[8]==0 or inmobiliaria_id=='empty'):
    print("<p>.</p>")


print("""

            <div><input type="submit"  name="value" value= Registrarse></div>
        </form> </div>""")

print("""
    <footer>
        <p> Maldonado-Cutipa-Ttito - sws.com</p>
    </footer>

    </body>
</html>""")
