#!/usr/bin/python
# -*- coding: utf-8 -*-

fich=open("/etc/passwd","r")
num_usuarios=fich.readlines()
print "El numero de usuarios de este ordenador es: " + str(len(num_usuarios))
fich.close()

# Primera parte hecha

dicc = {}

fich=open("/etc/passwd","r")

for user in num_usuarios:
    
    conf = user.split(":");
    username = conf[0]
    shell = conf[-1][:-1]
    print "El usuario: *" + username + "* utiliza la shell: " + shell
    dicc[username] = shell
    #dicc[conf=0]  = conf[-1][:-1]

print "Comprobamos la clave y el valor de root"
print "root", dicc["root"]
print "Ahora evitamos la excepcion que nos da imaginario al no estar en nuestro diccionario"
try:
    print "*imaginario*", dicc["imaginario"]
except KeyError:
    print ("no se encuentra la clave en el diccionario") 
fich.close()
