#! /usr/bin/python3

import sys
import csv

def acortar(palabra, 13):
	return line[13:]
nombreArchivo = sys.argv.__getitem__(1)

etiquetas = ['MatCodig', 'MatNumSe', 'MatNumMe', 'MatNumCo', 'MatCant', 'MatTipo', 'MatDescr', 'MatMarca', 'MatLocal', '$UpdatedBy', '$Revisions', 'Observaciones']
print("Leyendo datos del archivo: ", nombreArchivo)
camposEsperados = 12

# quitar caracteres palabra + 1 + 2

with open('eggs.csv', 'w', newline='') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=' ', quotechar=';', quoting=csv.QUOTE_MINIMAL)
	with open(nombreArchivo, 'r') as archivoAbierto:
		numeroActual = "1"
		for line in archivoAbierto:
			lineaActual = ""
			lineaActual += archivoAbierto.readline()
			for i in etiquetas:
				if i in lineaActual:
					spamwriter.writerow("#Fichero" + numeroActual)
					spamwriter.writerow(i + lineaActual)
			#spamwriter.writerow(etiquetas.__getitem__(0) + archivoAbierto.readline())
