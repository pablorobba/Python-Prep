#modulo3.py
class Modulo3:
    def __init__(self,lista):
        self.lista= lista
   
    def convierte_celsius_farenheit_kelvin(self,entrada, salida):
        for i in self.lista:
            print(i, entrada , "son en", salida, 
                  self.___convierte_celsius_farenheit_kelvin
                  (i,entrada,salida), salida)
        
    def factorial(self):
        for i in self.lista:
            print("el factorial de", i, "es", self.___factorial(i)) 
            
               
    def ___factorial(self,numero):
            
        '''''Devuelve el factorial de un numero'''
            
        if type(numero) != int:
                return("tenes que poner un numero")    
            
        if(numero < 0):
                return("tenes que poner un entero no negativo")
            
        if (numero <= 1):
                return 1    
                
        else:
            numero = numero * self.___factorial(numero - 1)
            return numero
            
    def ___convierte_celsius_farenheit_kelvin(self, valor, entrada, salida) :
    
        '''Formula que convierte entre distintos tipos de escala de grados. 
            Para su funcionamiento, se la debe llamar y dar una entrada 
            con la escala de grados a convertir, el valor a convertir, 
            y la escala a la que se desea convertir. 
            Por ejemplo: "convierte_celsius_farenheit_kelvin
            ("celsius", 1, "kelvin")"'''
            
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
    
    def numero_que_más_se_repite(self,menor):
        ''' devuelve el que más se repite y cuántas veces lo hace'''
        numeros_unicos =[]
        numero_de_repes = []
        if len(self.lista) == 0:
            print("lista sin numeros")
            return None
        
        if (menor):
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)
            
        for e in self.lista:
            if e in numeros_unicos:
                i = numeros_unicos.index(e)
                numero_de_repes[i] += 1
            else:
                numeros_unicos.append(e)
                numero_de_repes.append(1)

        minimo = numeros_unicos[0]
        maximo = numero_de_repes[0]
        
        for i in range(len(numeros_unicos)):
            if numero_de_repes[i] > maximo:
                minimo = numeros_unicos[i]
                maximo = numero_de_repes[i]
        return minimo, maximo
    
    def si_es_primo(self):
        for i in self.lista:
            primo = True
            if i % 2 == 0:
                primo = False
                print(i, "no es primo")
            else:
                print(i, "es primo")