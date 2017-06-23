#!C:\Python34\python
import cgi
import cgitb; cgitb.enable()
import mysql.connector


print("Content-Type: text/html\n")
db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='inmobiliaria')


form = cgi.FieldStorage() # se instancia solo una vez
correo = form.getfirst('correo', 'empty')
password= form.getfirst('password', 'empty')
consulta=form.getfirst('consulta','empty')

IN = form.getfirst("in","empty")

if (correo!="empty" and password!="empty"):
    cursor=db.cursor()
    sql="Select * From interesado where email like '%s'" % (correo);
    cursor.execute(sql)
    resultado=cursor.fetchall()
    if(len(resultado)==0):
        print("""<br><center><div style="background-color: #FF0000">No hay un usuario con el correo: <b>""",correo,"</b></div>");
        print("""<a href="inter_reg.py?in=%i">"""%(int(IN))+"""<h3>Registrarse aqui</h3></a>""")
    else:
        pass_tem=resultado[0][2]
        if(pass_tem==password):
            id_interesado=resultado[0][0]
            _interes = db.cursor()
            _interes.execute("insert into interes values(null,'%s','%d','%s','nos')" % (id_interesado,int(IN),consulta))
            db.commit()
            print("""<br><center><div style="background-color: #4CAF50">Solicitud enviada</div><center>""")
            _interes.close()
        else:
            print("""<br><center><div style="width: 100px; background-color: #FFD500;">Contraseña incorrecta</div>""")
            
    cursor.close()


