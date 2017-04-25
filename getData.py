# -*- coding: <utf-8> -*-

from sys import argv

nombreArchivo = argv.__getitem__(1)
if len(argv) == 3:
    nombreArchivoDestino = argv.__getitem__(2)
    if nombreArchivoDestino.find(".txt") == -1:
        nombreArchivoDestino += ".txt"
else:
    nombreArchivoDestino = "output.txt"

etiquetas = ['MatCodig:  ', 'MatNumSe:  ', 'MatNumMe:  ', 'MatNumCo:  ', 'MatCant:  ', 'MatTipo:  ', 'MatDescr:  ', 'MatMarca:  ', 'MatLocal:  ', '$UpdatedBy:  ', '$Revisions:  ']
alias = ['Et1:','Et2:','Et3:','Et4:','Et5:','Et6:','Et7','Et8:','Et9:','Et10:','Et11:']

def crearArchivo(nombre):
    nombre += ".txt"
    archivoDestino = open(nombreArchivoDestino, 'w')
    archivoDestino.write("## File successfully created!\n\n")
    archivoDestino.write("## Formato: ")
    texto = ""
    for etiqueta in etiquetas:
        texto = texto + etiqueta + ";"
    archivoDestino.write(texto.strip("\n"))
    archivoDestino.close()
def escribirLinea(linea):
    archivoDestino = open(nombreArchivoDestino,'a')
    linea += "\n"
    archivoDestino.write(linea)
    archivoDestino.close()
crearArchivo(nombreArchivo)
archivoOrigen = open(nombreArchivo, 'r')
for line in archivoOrigen:
    resultado = ""
    for i in range (0, len(etiquetas)):
        lineaLeida = line.strip('\r\n')
        if not (lineaLeida == '\n'):
            for i in etiquetas:
                if i in lineaLeida:
                    #resultado += alias[etiquetas.index(i)]
                    resultado += lineaLeida.strip(i)
                    resultado +=';'
                    line = next(archivoOrigen)
    escribirLinea(resultado)
