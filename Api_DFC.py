inicio = input("Desea empezar con la actividad, indique Si para comenzar, NO para finalizar programa.n\Ingrese su respuesta = ").lower()
print("")
while inicio != "no":
    try:
        print("Tiene a sus dispoision 4 opciones, indique que actividad desea ejecutar")
        print("Opción 1 = Jugar a “piedra, papel, tijera” compitiendo contra la computadora.")
        print("Opción 2 = Adivinar un número compitiendo contra la computadora.")
        print("Opción 3 = Tirar un dado.")
        print("Opción 4 = Graficar una función matemática.")
        print("Escriba con numero la acitiviad que desea realizar")
        print("")
        actividad = int(input("Ingrese la opcion deseada = "))
        if actividad == 1:
            print("Usted eligió la opción 1  Jugar a “piedra, papel, tijera” compitiendo contra la computadora.")
        elif actividad == 2:
            print("Usted eligiió la opción 2 Adivinar un número compitiendo contra la computadora")
        elif actividad == 3:
            print("Usted eligió la opción 3 Adivinar un número compitiendo contra la computadora.")
        elif actividad == 4:
            print("Usted elegió la opcion 4 Graficar una función matemática.")
            print("")
        inicio = input("Desea continuar con una alguna otra actividad SI/NO= ").lower()
        if inicio == "no":
            break
    except:
        print("Solo debe ingresar numeros")
        print("")
       



print("Usted seleciono la opcion NO. Se finaliza actividad")

