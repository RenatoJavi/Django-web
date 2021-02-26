# import datetime
# import time
# dia = datetime.date.today().day
# mes = datetime.date.today().month
# año = datetime.date.today().year
# print("dia: ", dia, " | mes: ", mes, " | año: ", año)

# print(time.strftime("%H:%M"))
# siDia = time.strftime("%A")
# print(siDia)
# time.sleep(20)
# if "Saturday" == siDia:
#     print("Día de relax porque hoy es ", siDia)
# elif "Sunday" == siDia:
#     print("recuperarse")
# else:
#     print("trabaja trabaja")
palabraFinal = ""
palabra = input("ingrese una palabra: ")
# "Python"

for letra in palabra.upper():
    if letra == ("A"):
        continue
    if letra == ("E"):
        continue
    elif letra == ("I"):
        continue
    elif letra == ("O"):
        continue
    elif letra == ("U"):
        continue

    palabraFinal += letra
    print("Letra actual : " + letra.upper())
print(palabraFinal)
