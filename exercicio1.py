# façam um scrip que leia do usuario, seu nome,
# 3 notas e calculem a media, monstrem resultado
usuario = input ("Digite seu nome: ") 
nota_1 = float (input("Digite sua nota: "))
nota_2 = float (input( "Digite sua nota: "))
nota_3 = float (input("Digte sua nota: "))
media = (nota_1 + nota_2 + nota_3)/3
print (f'{usuario}sua media é {media}')
