numMes = int (input('Digite o numero correspodente do mes'))
match numMes:
      case 1 :
          textoMes = 'JANEIRO'
      case 2:
          textoMes = 'FEVEREIRO'
      case 3:  
          textoMes = 'MARÇO'
      case 4:
          textoMes = 'ABRIL' 
       case _:
           print ("dados incorretos")    
              