class OperacionesMatematicas:
    
    
    def __init__(self) -> None:
        pass
    
    
    def factorial(self,numero):
        if (numero > 1):
            numero = numero * self.factorial(numero - 1)
        return numero
    
        
    def primos(self,numero):
        primos = True
        for i in range(2,numero):
            if i % numero == 0:
                primos = False
                break
        return primos
    
    
    def par_impar (self,numero):
        si_es_par = ""
        if numero % 2 == 0:
            si_es_par = (f"{numero} es par")
        else:
            print(numero, "es impar")
            si_es_par = (f"{numero} es par")
        return si_es_par
    
    
    def más_repetidos (self,lista,menor = True):
        
        from collections import Counter            
        contador = Counter(lista)
        
        if menor:
            másrepetido = contador.most_common(1)[0][0]
            cuantas_veces = contador.most_common(1)[0][1]
        else:
            másrepetido = contador.most_common(2)[1][0]
            cuantas_veces = contador.most_common(2)[1][1]   
        
        
        retornado = f"el más repetido es {másrepetido}, en un total de {cuantas_veces}"
        
        return retornado
        
         
print(OperacionesMatematicas().primos(9))
print(OperacionesMatematicas().factorial(9))
print(OperacionesMatematicas().par_impar(8))
print(OperacionesMatematicas().más_repetidos([1,2,3,4,5,5,5,4,4,4]))