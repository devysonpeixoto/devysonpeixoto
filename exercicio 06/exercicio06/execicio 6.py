lista = [1,2,3,4,5,6,7,8,9]
lista2 = [7,8,12,17]
lista.append (10) #add um elemento ao final da lista.
lista.insert (5,3) #add um elemento espeicifico da lista (indice, valor).
lista.extend (lista2) #add todos os elementos ao final da lista.

lista.remove (2) # remove a primeira ocorrencia de um valor especifico.


# remove e retorna o elemento de indice especifico (ou o ultimo se estiver vazio).
elemento = lista.pop() #remove o ultimo elemento e guardar na vareavel.
print (elemento) # saida numero 9.
print (lista) # saida - [1,2,3,4,5,6,7,8].

elemento = lista.pop (3) #remove o elemento de indice 3.
print (elemento) #saida - 4.
print (lista) # saida - [1,2,3,,5,6,7,8,9].

del lista[7] #remove o elemento de indice 7.
lista.clear () #remove a lista toda.

#Slicing - fatiamneto da lista - é feito sobre os indices. 
print (lista[1:4]) # saida [2,3,4,5]
print (lista[:3])  # saida [1,2,3]
print (lista[2:])  # saida [3,4,5,6,7,8,9]
print (lista[:])   # saida [1,2,3,4,5,6,7,8,9]
print (lista[::4]) # saida [1,5,9]




print (lec(lista))   #saida 9 
#retorna a lista ordenada decrescente
lista.sort (
    print (lista) (reverse = True))
print (lista) #saida [9,8,7,6,5,4,3,2,1] inverte a ordem dos elementos da lista.
lista.reverse()
print (lista)  #saida [9,8,7,6,5,4,3,2,1] retorna o indece da primeira ocorrencia de uma valor.
print (lista.index(5))  #saida 4 retorna o numero de ocorrenciade um valor.
lista3 = [1,1,2,2,3]  #saida - 2 

#verificaçao de existencia

print (3 in lsita) #saida -True
print (0 in lista) # saida - False