usuario = input ("digite seu nome:")
altura = float (input("digite sua altuta:"))
peso = float (input("digite seu peso:"))
IMC = peso / (altura**2)
if IMC >=0 and IMC < 18.5:
    print ( 'abaixo do peso')
elif IMC >=18.5 and peso < 25:
    print ('peso normal')
elif IMC >=25 and peso < 30:
    print ('acima do peso')
elif IMC >=30:
    print ('velorio')
else:
    print('vai fazer DIETA')