diaSemana = input ('digite o dia da semana')

match diaSemana.lower():
  case "segunda" | "terca" | "quarta" | "quinta":
    print ("dia da semana")
  case "sexta":
      print ("sextouuuuuu")
  case "sabado" | "domingo":
      print ("fim de semana ")
  case _:
       print ("dia incorreto")        