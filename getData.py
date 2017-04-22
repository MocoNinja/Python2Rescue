#! /usr/bin/python3

import sys
import csv

def acortar(palabra, patron):
    caracteresBorrar = len(patron) + 2 # el patron lleva pegados : y dos espacios de forma fija
    return palabra[caracteresBorrar:]


nombreArchivo = sys.argv.__getitem__(1)

etiquetas = ['MatCodig', 'MatNumSe', 'MatNumMe', 'MatNumCo', 'MatCant', 'MatTipo', 'MatDescr', 'MatMarca', 'MatLocal', '$UpdatedBy', '$Revisions', 'Observaciones']
print("Leyendo datos del archivo: ", nombreArchivo)
camposEsperados = len(etiquetas)


with open('output.txt', 'w') as archivoSalida:
    with open(nombreArchivo, 'r') as archivoAbierto:
        campoActual = 1
        for line in archivoAbierto:
            lineaActual = ""
            lineaActual += archivoAbierto.readline()
            for i in etiquetas:
                if i in lineaActual:
                    textoTratado = acortar(lineaActual, i)
                    archivoSalida.write("#Fichero" + str(campoActual))
                    campoActual += 1
                    archivoSalida(i + textoTratado)
