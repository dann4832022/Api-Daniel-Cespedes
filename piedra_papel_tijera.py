import random
class Piedra_papel_tijera:
    def __init__(self, inicio):
        self.inicio = "si"
        
    def nombre(self, nombre):
        nombre = print(f"{nombre} vs Maquina")

    def jugar(self):
        rondas = 0
        victoria_maquina = 0
        victoria_humano = 0
        empate = 0
        while True:
            
            jugador_1 = input("Seleccione una de las tres opciónes \nPiedra \nPapel \nTijera\nEscriba opción = ").lower()
            # print (f"{nombre} has seleccionado la opción = {jugador_1}")
            maquina = random.choice(["piedra", "papel", "tijera"])
            # print(f"La maquina ha seleccinado la opción = {maquina}")
            
            rondas = rondas + 1
            # Primera parte = El jugador elige la opción piedra
            if jugador_1 == "piedra" and maquina == "papel":
                print(f"{nombre} eligio piedra y la maquina eligio papel.\nGanador = Maquina")
                victoria_maquina = victoria_maquina + 1
                print("")
            elif jugador_1 == "piedra" and maquina == "tijera":
                print(f"{nombre} eligió piedra y la maquina eligió tijera.\nGanador Jugador 1")
                victoria_humano = victoria_humano + 1
                print("")
            elif jugador_1 == "piedra" and maquina == "piedra":
                print(f"Empate!!!\nAmbos jugadores elegieron Piedra")
                empate = empate + 1
            #Segunda parte = el jugador elige la opción ppapel
            elif jugador_1 == "papel" and maquina == "papel":
                print(f"Empate!!!\nAmbos jugadores elegieron Papel")
                empate = empate + 1
                print("")
            elif jugador_1 == "papel" and maquina == "tijera":
                print(f"{nombre} eligió papel y la maquina eligió tijera.\nGanador Maquina")
                victoria_maquina = victoria_maquina + 1
                print("")
            elif jugador_1 == "papel" and maquina == "piedra":
                print(f"El jugdor 1 eligió papel y la maquina eligió piedra.\nGanador jugador 1")
                victoria_humano = victoria_humano + 1
                print("")
            #Tercera parte = el jugador elige la opción tijera
            elif jugador_1 == "tijera" and maquina == "tijera":
                print(f"Empate!!!\nAmbos jugadores elegieron Tijera")
                empate = empate + 1
                print("")
            elif jugador_1 == "tijera" and maquina == "papel":
                print(f"{nombre} eligió tijera y la maquina eligió papel.\nGanador Jugador 1")
                victoria_humano = victoria_humano + 1
                print("")
            elif jugador_1 == "tijera" and maquina == "piedra":
                print(f"El jugdor 1 eligió papel y la maquina eligió piedra.\nGanador Maquina")
                victoria_maquina = victoria_maquina + 1
                print("")
            # continuar o finalizar
            continuar = input("Seleccione la tecla S para seguir jugando sino cualquier tecla == ").lower()
            if continuar != "s":
                break
        print(f"Se han jugado un total de {rondas} rondas")
       
        print(f"{nombre} has tenido un total de = {victoria_humano} partidas ganadas")
        print(f"La maquina ha obbenido un total de  {victoria_maquina} partidas ganadas")
        print(f"Hubo un total de {empate} partidas que terminaron en empates")



iniciar = input("Si desea jugar seleccione la letra S caso contrario cualquier letra = ").lower()

if iniciar == "s":
    juego = Piedra_papel_tijera(inicio = "si")
    print("Bienvenido al PIEDRA - PAPEL - TIJEA")
    nombre = input("Ingrese su nombre = ")
    juego.nombre(nombre)
    juego.jugar()
else:
    print("Hasta luego")

