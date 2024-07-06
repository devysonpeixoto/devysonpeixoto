anos_nasc = [1979, 1985, 1989, 1994, 1979, 1985,]
idades = []
ano_atual = 2024 
adicionar_ano_nascimento = lambda 
for ano in  anos_nasc:
     #print (ano)
     idades.append (ano_atual - ano)
#for idade in idades:
   #print (idade)
print (max (idades))
print (min (idades))
idades.sort(reverse = True)
print (idades)
    
          