#!C:\Python34\python
import cgi
import cgitb; cgitb.enable()
import mysql.connector

print("Content-Type: text/html\n")

db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='inmobiliaria')


form = cgi.FieldStorage() # se instancia solo una vez
estado = form.getfirst('estado', 'empty')
print("aksjdgfjadgfjasdgfjadsgfjhadsgfjasdgfjashdgf",estado)