usuario = input ("Digite seu nome: ") 
nota_1 = float (input("Digite sua nota: "))
nota_2 = float (input( "Digite sua nota: "))
nota_3 = float (input("Digte sua nota: "))
media = (nota_1 + nota_2 + nota_3)/3
print (f'{usuario}sua media é {media}')
if media > 7.5:
    print ('aprovado')
elif media >=5 and media <7.5:
    print ('recuperacao')
elif media >=0 and media<5:
    print ('reprovado')
else:
    print('nota invalida')
    