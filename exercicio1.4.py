anoAtual = 2024
anoNascimento = int (input("digite o ano q que nasceu"))
idade = anoAtual - anoNascimento20241

podevotar = True if idade >=16 else False
if podevotar:
    print('parabens')
else:
    print ('va va va')