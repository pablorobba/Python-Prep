import sys 
import os
if len(sys.argv) == 4:
    archivo = open('clase09_ej2.csv', 'a')
    import datetime
    hoy = datetime.datetime.now()
    marca_de_tiempo = int(datetime.datetime.timestamp(hoy))
    
    humedad = sys.argv[1]
    temperatura = sys.argv[2]
    lluvia = sys.argv[3]
    
    if (lluvia == "True") or (lluvia == "False"): #por si ponen un parametro que es distinto a T o F
        linea = str(marca_de_tiempo) + ',' + temperatura + ',' + humedad + ',' + lluvia #funcion para poner en linea las otras funciones que se van a imprir
        archivo.write(linea + "\n")
        archivo.close()
    else:
        lluvia = input("Debes escribir 'True' si llueve o 'False' si no")
        linea = str(marca_de_tiempo) + ',' + temperatura + ',' + humedad + ',' + lluvia
        archivo.write(linea + "\n")
        archivo.close()
else:
    print("ERROR: Tenes que dar 3 parameros, que sean 1)humedad 2)temperatura 3)si llueve o no") 
    print("por ejemplo: '26 85 True'")
    
    
