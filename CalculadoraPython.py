print("simple calculator")
input_first_number = float(input("Digite o primeiro número: "))
print(f"ok,seu numero e:{input_first_number}")  

input_second_number = float(input("Digite o segundo número: "))
print(f"ok,seu segundo numero e:{input_second_number}") 

input_character = int(input("Digite o numero do caractere para calcular(1 = +)(2 = -)(3 = *)(4 = /): "))



def calculo(n1,n2,caractere):
        
        if caractere == 1:
         resultado = n1 + n2
         print(f"a soma entre {n1} e {n2} e:{resultado}" )
        elif caractere == 2:
         resultado = n1 - n2
         print(f"a subtração entre {n1} e {n2} e:{resultado}" )
        elif caractere == 3:
         resultado = n1 * n2
         print(f"a multiplicação entre {n1} e {n2} e:{resultado}" )
        elif caractere == 4:
         resultado = n1 / n2
         print(f"a divisão entre {n1} e {n2} e:{resultado}" )
calculo(input_first_number,input_second_number,input_character)