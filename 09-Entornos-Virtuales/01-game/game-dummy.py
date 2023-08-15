# -*- coding: utf-8 -*-

#Importamos las librerías a emplear
import random


def computer_choice():

    #Valor aleatorio para el algoritmo
    computer = random.choice(options)
    return computer


def user_choice():

    #Valor elegido por nosotros
    user = str(input("Selecciona: piedra, papel o tijera:\n"))
    user = user.lower()
    
    if user in options:
        return user
    else:
        raise Exception("Tu elección no es válida. Elige de nuevo.")


def run_game():

    #Inicio del juego
    rounds = 3
    user_win = 0
    computer_win = 0

    print("*" * 15)
    print("¡El juego empieza AHORA!.")
    print("*" * 15)
    
    while True:

        computer = computer_choice()
        user = user_choice()
        
        print(f"{user} vs {computer}, ")
            

        if user == computer:

            rounds -= 1
            print(f"""

            Tie!
            You have both picked {user}
            {rounds} remaining.

            """)


        if (user == "tijera" and computer == "papel") or (user == "piedra" and computer == "tijera") or (user == "papel" and computer == "piedra"):
        
            rounds -= 1
            user_win += True

            print(f"""
            
            You have won this round!
            {user} beats {computer}!
            {rounds} remaining.

            """)


        if (computer == "tijera" and user == "papel") or (computer == "piedra" and user == "tijera") or (computer == "papel" and user == "piedra"):
    
            rounds -= 1
            computer_win += True
            
            print(f"""
            
            You have lost this round.
            {computer} beats {user}!
            {rounds} remaining.

            """)

        
        if rounds <= 0:
            if user_win == computer_win:
                print("Es un empate.")
                break
            if computer_win > user_win:
                print(f"El ganador es la máquina con: {computer_win} puntos.")
                break
            if computer_win < user_win:
                print(f"¡Felicidades! Tú eres el ganador con: {user_win} puntos!")
                break


if __name__ == "__main__":
    # Global choice options.
    options = ("piedra", "papel", "tijera")
    run_game()

