# Codigo de la actividad asincrona semana 09 Fundamentos De Programación

# Mensaje de bienvenida.

print("\n\t*************************")
print("\t*Bienvenid@ al programa.*")
print("\t*************************")

# Ingresar datos del usuario desde teclado.
name = input("\nIngrese su nombre por favor (solo nombre no apellido) -> ")
apellidos = input("Ingrese su apellido por favor (solo su apellido) -> ")
edad = int(input("Ingrse su edad por favor -> "))
sexo = input("Ingrese su sexo por favor -> ").lower()

# Estructura condicional.

# Sexo masculino.
if sexo == "masculino" or sexo == "m" or sexo == "hombre":
   # Concatenación de los datos del usuario.
    print(f"\nEl nombre del usuario es {name} {apellidos}, tiene {edad} años de edad y es de sexo masculino.\n")

    # Estructura de la condición anidada
    if edad >= 0 and edad <= 2:
        print("El usuario es un niño y se encuentra en la etapa de bebé.")
    elif edad >= 3 and edad <= 5:
        print("El usuario es un niño y se encuentra en la etapa de infancia.")
    elif edad >= 6 and edad <= 11:
        print("El usuario es un niño y se encuentra en la etapa de niñes.")
    elif edad >= 12 and edad <= 18:
        print("El usuario es un joven y se encuentra en la etapa de adolescencia.")
    elif edad >= 19 and edad <= 26:
        print("El usuario es un hombre y se encuentra en la etapa de juventud.")
    elif edad >= 27 and edad <= 40:
        print("El usuario es un hombre y se encuentra en la etapa de adultez joven.")
    elif edad >= 41 and edad <= 55:
        print("El usuario es un señor y se encuentra en la etapa de adultez.")
    elif edad >= 56 and edad <= 65:
        print("El usuario es un señor y se encuentra en la etapa de persona mayor.")
    elif edad >= 66:
        print("El usuario es un abuelo y se encuentra en la etapa de vejez.")
    
    else:
        print("Asegurate de escribir correctamente tu edad solo con numeros ejemplo: 20.")

    # Calculado si la edad del usuario es par o impar.
    parOImp = edad % 2

    if parOImp == 0:
        print(f"\nLa edad del usuario ({edad} años) es un número par.")

    else:
        print(f"\nLa edad del usuario ({edad} años) es un número impar.")

# Sexo femenino.
elif sexo == "femenino" or sexo == "f" or sexo == "mujer":
    # Concatenación de los datos del usuario.
    print(f"\nEl nombre del usuario es {name} {apellidos}, tiene {edad} años de edad y es de sexo femenino.\n")

    # Estructura de la condición anidada
    if edad >= 0 and edad <= 2:
        print("La usuario es una niña y se encuentra en la etapa de bebé.")
    elif edad >= 3 and edad <= 5:
        print("La usuario es una niña y se encuentra en la etapa de infancia.")
    elif edad >= 6 and edad <= 11:
        print("La usuario es una niña y se encuentra en la etapa de niñes.")
    elif edad >= 12 and edad <= 18:
        print("La usuario es una joven y se encuentra en la etapa de adolescencia.")
    elif edad >= 19 and edad <= 26:
        print("La usuario es una mujer y se encuentra en la etapa de juventud.")
    elif edad >= 27 and edad <= 40:
        print("La usuario es una mujer y se encuentra en la etapa de adultez joven.")
    elif edad >= 41 and edad <= 55:
        print("La usuario es una señora y se encuentra en la etapa de adultez.")
    elif edad >= 56 and edad <= 65:
        print("La usuario es una señora y se encuentra en la etapa de persona mayor.")
    elif edad >= 66:
        print("La usuario es una abuela y se encuentra en la etapa de vejez.")
    
    else:
        print("Asegurate de escribir correctamente tu edad solo con numeros ejemplo: 20.\n")

    parOImp = edad % 2

    # Calculado si la edad del usuario es par o impar.
    if parOImp == 0:
        print(f"\nLa edad de la usuario ({edad} años) es un número par.")

    else:
        print(f"\nLa edad de la usuario ({edad} años) es un número impar.")

else:
    print("Asegurate de escribir correctamente tu sexo, ya sea maculino o femenino.\n")

print("\nFin del programa.\n")