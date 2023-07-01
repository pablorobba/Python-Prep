def numero_que_más_se_repite(lista):
    ''' devuelve el que más se repite y cuántas veces lo hace'''
    repetientes = []
    repetidos =[]
    if len(lista) == 0:
        print("lista sin numeros")
        return None
        
    else:
        for cuanto_se_repite in lista:
            cuanto_se_repite = lista.count(cuanto_se_repite)
            repetientes.append(cuanto_se_repite)
            repetientes.sort()
            
        if cuanto_se_repite:            
            repetidos.append((max(set(lista), key = lista.count)))
            repetidos.append(repetientes[-1])
    return repetidos
        
   
i = [1,1,1,5,1,1,1,1,1,9,9,1,4,9,9,5,9,9,5,9,9,9,9,9,9,9,4,5,5,5,5,5,5,5,5,5,5,
     5,5,5,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]
print(numero_que_más_se_repite(i))



def convierte_celsius_farenheit_kelvin(entrada, valor, salida) :
    
    '''Formula que convierte entre distintos tipos de escala de grados. 
    Para su funcionamiento, se la debe llamar y dar una entrada con la escala de 
    grados a convertir, el valor a convertir, y la escala a la que se desea 
    convertir. 
    Por ejemplo: "convierte_celsius_farenheit_kelvin("celsius", 1, "kelvin")"'''
    
    if type(valor) != int:
        print("tenes que dar un numero")
        
    else:
    
        if entrada == "celsius" and salida == "celsius":
            valor_convertido = int(valor)           
        if entrada == "celsius" and salida == "farenheit":
            valor_convertido = ((int(valor) * 9/5) + 32)            
        if entrada == "celsius" and salida == "kelvin":
            valor_convertido = (int(valor) + 273.15)
    
        if entrada == "farenheit" and salida == "farenheit":
            valor_convertido = valor            
        if entrada == "farenheit" and salida == "celsius":
            valor_convertido = (int(valor) - 32) * 5/9       
        if entrada == "farenheit" and salida == "kelvin":
            valor_convertido = 5/9 * (int(valor) -32) + 273.15
        
        if entrada == "kelvin" and salida == "kelvin":
            valor_convertido = valor            
        if entrada == "kelvin" and salida == "farenheit":
            valor_convertido = 1.8 * (int(valor) - 273.15) + 32            
        if entrada == "kelvin" and salida == "celsius":
            valor_convertido = int(valor) - 273.15
                                    
    return valor_convertido

lista = ["farenheit", "celsius", "kelvin"]
for e in range(0,3):
    for i in range (0,3):
        for h in range(0,4):
            print("el valor de", h ,"en",lista[e],"a",lista[i], "es",  
                convierte_celsius_farenheit_kelvin(lista[e],h,lista[i]))


            
def numero_que_más_se_repite(lista):
    ''' devuelve el que más se repite y cuántas veces lo hace'''
    numeros_unicos =[]
    numero_de_repes = []
    if len(lista) == 0:
        print("lista sin numeros")
        return None

    for e in lista:
        if e in numeros_unicos:
            i = numeros_unicos.index(e)
            numero_de_repes[i] += 1
        else:
            numeros_unicos.append(e)
            numero_de_repes.append(1)
    print("numeros unicos:", numeros_unicos)
    print("numeros repes:", numero_de_repes)
    
    minimo = numeros_unicos[0]
    maximo = numero_de_repes[0]
    
    for i in range(len(numeros_unicos)):
        if numero_de_repes[i] > maximo:
            minimo = numeros_unicos[i]
            maximo = numero_de_repes[i]
    return minimo, maximo        
    
lista = [1,1,3,3,3,3]
numero_que_más_se_repite(lista)



from collections import Counter

lista = [1,2,3,4,4,4,4,4,5,6,7]

cuantas = Counter(lista)
cantidad_de_repes = cuantas.most_common(1)[0][1]
más_comun = cuantas.most_common(1)[0][0]

print ("el numero que más se repite es " + str(más_comun)
       + ", en un total de", cantidad_de_repes, "veces")