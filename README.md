# Ejercicio Newspaper3k

Utilizando el paquete newspaper3k se pide escribir una librería en un archivo ej1.py (un archivo de python llamado ej1) que implemente una función que reciba una URL de un artículo periodístico y devuelva un diccionario que contenga la cantidad de veces que apareció cada palabra en el texto.

La función debe llamarse body, por lo que la librería podría ser testeada con el siguiente código:

import ej1

url="https://www.nytimes.com/2016/08/07/education/edlife/kenneth-goldsmith-on-wasting-time-on-the-internet.html"

x=ej1.body(url)

for key,value in x.items():

    print("La cantidad de veces que aparece la palabra {} es {}".format(key,value))

Todos los caracteres deberán ser pasados a minúscula. Cualquier caracter que no sea una letra se considera separador de palabras. No se deberán contabilizar los string vacíos.
