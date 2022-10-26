def anoBisiesto(year):
    bisiesto = year % 4
    if bisiesto == 0:
        print("Este año es bisiesto")
    
    else:
        print("Este año NO es bisiesto")

anoBisiesto(2022)