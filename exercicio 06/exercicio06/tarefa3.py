def calcular_media (nota1, nota2, nota3):  
    return (nota1+nota2+nota3 )/3  

def calcular_aprovacao ():
    media = calcular_media (nota1, nota2, nota3)
    
    
    if media >=7:
        return "aprovado"
    else:
        return "reprovado"
    
    
nota1 = float (input("digitar sua nota: "))
nota2 = float (input("digitar sua nota: "))
nota3 = float (input("digitar sua nota: "))
#media = calcular_media (nota1, nota2, nota3)
#print (media)
print (calcular_aprovacao())