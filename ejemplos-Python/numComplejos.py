import time

c0 = int(input("ingresar número entero que no sea negativo y que no sea cero : "))
pasos = 0
while c0 != 1:
    if (c0 % 2) == 0:
       # print("es parr")
        pasos += 1
        c0 /= 2
        print("# pasos: ", pasos, " nuevo valor par: ", c0)

    else:
        #print("es impar")
        pasos += 1
        c0 = 3 * c0 + 1
        time.sleep(5)
        print("pasos : ", pasos, " Nuevo valor impar: ", c0)
