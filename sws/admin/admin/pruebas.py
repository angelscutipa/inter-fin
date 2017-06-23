import re

cadena=input("ingrese: ")

print("letra: ",cadena)


if(re.match(".*[A-Z]{2,}.*[\~\@;:\^_]{1,}.*",cadena)):
	print("ok")

else:
        print("mal")


#debe contener por lo menos dos letras mayúsculas y un caracter que no sea letra ni número.
