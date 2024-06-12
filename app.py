# write 'hello world' to the console
import random

def jugar_ronda(opcion_jugador, opcion_oponente):
    if opcion_jugador == opcion_oponente:
        return 0  # Empate
    elif (opcion_jugador == "rock" and opcion_oponente == "scissors") or \
         (opcion_jugador == "scissors" and opcion_oponente == "paper") or \
         (opcion_jugador == "paper" and opcion_oponente == "rock"):
        return 1  # Jugador gana
    else:
        return -1  # Jugador pierde

def main():
    opciones = ["rock", "paper", "scissors"]
    puntuacion = 0
    puntuacion_oponente = 0
    rondas_jugadas = 0

    while True:
        eleccion_jugador = input("Elige rock, paper o scissors: ").lower()
        if eleccion_jugador not in opciones:
            print("Opción no válida. Por favor, elige de nuevo.")
            continue

        eleccion_oponente = random.choice(opciones)
        print(f"El oponente eligió: {eleccion_oponente}")

        resultado = jugar_ronda(eleccion_jugador, eleccion_oponente)
        rondas_jugadas += 1
        if resultado == 0:
            print("Es un empate.")
        elif resultado == 1:
            print("Ganaste!")
            puntuacion += 1
        else:
            print("Perdiste.")
            puntuacion_oponente += 1
        
        jugar_de_nuevo = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_de_nuevo != "s":
            break

    print(f"Tu puntuación final es: {puntuacion}")
    print(f"IA puntuación final es: {puntuacion_oponente}")
    print(f"Número de rondas jugadas: {rondas_jugadas}")

if __name__ == "__main__":
    main()