from datetime import datetime
import time
import random
import os

def game(game_mode):
        while True:
            if game_mode == 1:
                limite = 51
                lives = 11
                mode = "facil"
            if game_mode == 2:
                limite = 101
                lives = 11
                mode = "normal"
            if game_mode == 3:
                limite = 101
                lives = 6
                mode = "dificil"
            if game_mode == 4:
                limite = 201
                lives = 6     
                mode = "muy dificil"
            cpu_number = random.randint(1,limite)
            print("Has elegido el modo", mode, "por lo tanto tienes", str(lives-1), "vidas y la cpu ha elegido un numero del 1 al", str(limite-1))                
            user_election = int(input("elige tu primer numero: ").replace(" ",""))
            os.system('cls')
            while user_election != cpu_number:
                lives -= 1
                if user_election > cpu_number and lives > 0:
                    print("elegiste el numero", str(user_election))
                    print("te quedan", str(lives), "vidas")
                    user_election = int(input("el numero es menor, intenta de nuevo: "))
                    os.system('cls')
                elif user_election < cpu_number and lives > 0:
                    print("elegiste el numero", str(user_election))
                    print("te quedan", str(lives), "vidas")
                    user_election = int(input("el numero es mayor, intenta de nuevo: "))
                    os.system('cls')    
                if lives == 0:
                    break              
            if user_election == cpu_number:
                os.system('cls')
                print("el numero de la CPU es", str(cpu_number))
                game_mode = input(MENU2).replace(" ","")
                if game_mode.isalpha() or int(game_mode) > 4 or int(game_mode) < 1:
                    print("gracias por jugar!")
                    break
                game_mode = int(game_mode)
                os.system('cls')        
            elif lives == 0:
                os.system('cls')
                print("el numero de la CPU era", str(cpu_number))
                game_mode = input(MENU3).replace(" ","")
                if game_mode.isalpha() or int(game_mode) > 4 or int(game_mode) < 1:
                    print("gracias por jugar")
                    break
                game_mode = int(game_mode)
                os.system('cls')


def run():
    while True:
        try:
            os.system('cls')
            player_mode = int(input(MENU))
            os.system('cls')
            game(player_mode)
            break
        except ValueError:
            os.system('cls')
            print("no puedes poner texto ni espacios vacios")
            value_error_message = input("si quieres continuar con el programa escribe la letra -y-, escribe cualquier otra cosa para salir: ").replace(" ","").lower()    
            if value_error_message != "y":
                print("gracias por jugar")
                break
        except UnboundLocalError:
            os.system('cls') 
            value_error_message = input(MENU4).replace(" ","").lower()    
            if value_error_message != "y":
                print("gracias por jugar")
                break   

MENU4 = """
solo puedes digitar los numeros:

1-facil
2-normal
3-dificil
4-muy dificil

si quieres continuar con el programa escribe la letra -y-, escribe cualquier otra cosa para salir: """


MENU2 ="""
Felicidades, ganaste!,

si quieres seguir jugando escribe el numero de la dificultad en que quieres jugar
                                         
1-facil
2-normal
3-dificil
4-muy dificil
                                         
escribe cualquier otra cosa para salir del programa: """


MENU3 = """
Lo siento, perdiste!,

si quieres seguir jugando escribe el numero de la dificultad en que quieres jugar
                                         
1-facil
2-normal
3-dificil
4-muy dificil
                                         
escribe cualquier otra cosa para salir del programa: """



MENU = """
Bienvenido a NumberGuesser V1.0

-----------------------------------------------------------------------

El juego en donde debes adivinar el numero que piense la CPU

Ahora, adivinador ¿estas listo para comenzar?

-----------------------------------------------------------------------

Elige tu dificultad:

1-facil
2-normal
3-dificil
4-muy dificil

digita el numero de la dificultad en la que deseas jugar
(1,2,3,4): """



if __name__ == "__main__":
    run()