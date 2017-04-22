import sys

nombreArchivo = sys.argv.__getitem__(1)
etiquetas = ['MatCodig:  ', 'MatNumSe:  ', 'MatNumMe:  ', 'MatNumCo:  ', 'MatCant:  ', 'MatTipo:  ', 'MatDescr:  ', 'MatMarca:  ', 'MatLocal:  ', '$UpdatedBy:  ', '$Revisions:  ']
# Cambiar estas etiquetas por las pertinentes según lo hablado con Merche
alias = ['Et1:','Et2:','Et3:','Et4:','Et5:','Et6:','Et7','Et8:','Et9:','Et10:','Et11:']

def crearArchivo(nombre):
    nombre += ".txt"
    archivoDestino = open(nombre, 'w')
    archivoDestino.write("## File successfully created!\n\n")
    archivoDestino.close()
def escribirLinea(linea):
    linea += "\n"
    archivoDestino = open(nombreArhivo + '.txt','a')
    archivoDestino.write(linea)
    archivoDestino.close()
nombreArhivo = "prueba"
crearArchivo(nombreArhivo)


archivoOrigen = open(nombreArchivo, 'r')
for line in archivoOrigen:
    resultado = ""
    for i in range (0, len(etiquetas)):
        lineaLeida = line.strip('\n')
        if not (lineaLeida == '\n'):
            for i in etiquetas:
                if i in lineaLeida:
                    resultado += alias[etiquetas.index(i)]
                    resultado += lineaLeida.strip(i)
                    resultado +=';'
            line = next(archivoOrigen)
    escribirLinea(resultado)