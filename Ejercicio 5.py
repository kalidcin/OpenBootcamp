while True:
    try:
        peso = float(input('Ingresa tu peso: '))
        estatura = float(input('Introduce tu estatura en metros: '))

        imc = peso / (estatura * estatura)
        print("El indice de masa corporal es: ", round(imc, 2))
        break
    except ValueError:
        print('Introduce un valor valido')