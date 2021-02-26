bloques = int(input("Ingrese el número de bloques:"))
altura = 0
while bloques >= 0:
    altura += 1
    print("contador", altura)
    bloques -= altura
  #  if bloques >= 0:
    print("me quedan : ", bloques)
    if bloques < 0:
        print("hace falta : ", bloques)

print("La altura de la piramide: ", altura-1)
