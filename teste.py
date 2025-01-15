I = [-2,-3,-4,-5,-6,-7]
S = list('ciaociao')


def funzione_7(lista):
  changes = 0
  list = []

  for i in range(len(lista)):
    if type(lista[i]) == int:
        if i % 2 == 0:
            lista[i] *= -1
            list.append(lista[i])
            changes += 1
        else:
           list.append(lista[i])

    else:
        valore = str(lista[i])
        if i % 2 == 0:
            list.append(valore.capitalize())
            changes += 1
        else:
            list.append(valore)

  print(changes)
  print(list)
      

funzione_7(I)
funzione_7(S)
