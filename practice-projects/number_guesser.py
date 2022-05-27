from datetime import datetime
import time
import random
import os
from number_guesser_user import User

def game(game_mode):
        while True:
            game_user = User()
            if game_mode == 5:
                while True:
                    os.system('cls')
                    print("Estadisticas de adivinador".upper())
                    print("\n------------------------------------")
                    print("Nivel:",          str(game_user.level))
                    print("------------------------------------")
                    print("Puntaje maximo:", str(game_user.max_score))
                    print("------------------------------------")
                    print("Mejor tiempo:",   str(game_user.best_time), "segundos")
                    print("------------------------------------")
                    print("Victorias:",      str(game_user.wins))
                    print("------------------------------------")
                    stadistics_desicion = input("\nDigita la letra -y- para volver al menu, escribe cualquier otra cosa para salir del programa: ").replace(" ","").lower()
                    os.system('cls')
                    if stadistics_desicion != "y":
                        print("gracias por jugar!")
                        break
                    if stadistics_desicion == "y":
                        game_mode = int(input(MENU).replace(" ",""))
                        os.system('cls')
                        if game_mode != 5:
                            break
            if game_mode == 5:
                break            
            if game_mode == 1:
                limite = 51
                lives = 11
                mode = "facil"
                points_base = 50
            if game_mode == 2:
                limite = 101
                lives = 11
                mode = "normal"
                points_base = 150                
            if game_mode == 3:
                limite = 101
                lives = 6
                mode = "dificil"
                points_base = 600
            if game_mode == 4:
                limite = 201
                lives = 6     
                mode = "muy dificil"
                points_base = 1400
            cpu_number = random.randint(1,limite)
            print("Has elegido el modo", mode, "por lo tanto tienes", str(lives-1), "vidas y la cpu ha elegido un numero del 1 al", str(limite-1))                
            user_election = int(input("elige tu primer numero: ").replace(" ",""))
            start_time = datetime.utcnow()
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
                with open("./number_of_wins.txt", "r",encoding="UTF-8") as nnowbu:
                    for num in nnowbu:
                        number_of_guessed_wins = int(num)
                        with open("./number_of_wins.txt", "w", encoding="UTF-8") as nnowbuwa:
                            nnowbuwa.write(str(number_of_guessed_wins + 1))
                            game_user.total_wins(number_of_guessed_wins + 1)
                            break
                os.system('cls')
                print("------------------------------------------------------------------------------------")
                print("el numero de la CPU es", str(cpu_number))
                print("------------------------------------------------------------------------------------")
                time.sleep(2)
                end_time = datetime.utcnow()
                total_time = end_time - start_time
                total_time = round(total_time.total_seconds(),None)
                total_points = round(points_base * 10000 / total_time,None)
                print("felicidades, has obtenido", str(total_points), "puntos")
                print("------------------------------------------------------------------------------------")
                time.sleep(2)
                with open("./max-score.txt", "r", encoding="UTF-8") as ms:
                    for i in  ms:
                        if total_points > int(i):
                            game_user.new_max_score(total_points)
                            print("Enorabuena!, has conseguido un nuevo puntaje maximo")
                            print("------------------------------------------------------------------------------------")
                            with open("./max-score.txt", "w", encoding="UTF=8") as nms:
                                nms.write(str(total_points))
                            time.sleep(2)
                            break    
                        if total_points <= int(i):
                            print("tu puntaje maximo es de", str(i), "de puntos, intenta superarlo la proxima vez")
                            print("------------------------------------------------------------------------------------")
                            time.sleep(2)
                            break
                with open("./user_points.txt", "r", encoding="UTF=8") as up:
                    for i in up:
                        new_user_points_saved = int(i) + total_points
                        with open("./user_points.txt", "w", encoding="UTF-8") as np:
                            np.write(str(new_user_points_saved))     
                            with open("./level.txt", "r", encoding="UTF-8") as rulful:
                                for i in rulful:
                                    limit_level = 1000000 * ((int(i)+1)*(int(i)+1))
                                    if new_user_points_saved >= limit_level:
                                        with open("./level.txt", "w", encoding="UTF-8") as nulig:
                                            nulig.write(str(int(i)+1))
                                            print("Increible!, has subido a nivel", str(int(i)+1),", eres todo un adivinador!")
                                            print("------------------------------------------------------------------------------------")
                                            time.sleep(3.5)
                                            with open("./level.txt", "r", encoding="UTF-8") as frfi:
                                                for _ in frfi:
                                                    game_user.new_level(int(_))
                                    else:
                                        time.sleep(1)
                                        print("necesitas", str(limit_level -new_user_points_saved), "puntos más para subir a nivel", str(int(i)+1))
                                        print("------------------------------------------------------------------------------------")
                                        time.sleep(3)
                                        break       
                            break                 
                print("tu partida a durado", str(total_time), "segundos")
                print("------------------------------------------------------------------------------------")
                with open("./best-time.txt", "r", encoding="UTF-8") as bt:
                    for i in  bt:
                        if total_time < int(i):
                            game_user.new_best_time(total_time)
                            time.sleep(2)
                            print("Enorabuena!, has conseguido un nuevo mejor tiempo de partida")
                            print("------------------------------------------------------------------------------------")
                            with open("./best-time.txt", "w", encoding="UTF=8") as nbt:
                                nbt.write(str(total_time))
                            break    
                        if total_time >= int(i):
                            time.sleep(2)
                            print("tu mejor tiempo es de", str(i), "segundos, intenta mejorarlo la proxima vez")
                            print("------------------------------------------------------------------------------------")
                            break 
                time.sleep(2)
                game_mode = input(MENU2).replace(" ","")
                if game_mode.isalpha() or int(game_mode) > 5 or int(game_mode) < 1:
                    print("gracias por jugar!")
                    time.sleep(3)
                    break
                game_mode = int(game_mode)
                os.system('cls')        
            elif lives == 0:
                os.system('cls')
                print("------------------------------------------------------------------------------------")
                print("el numero de la CPU era", str(cpu_number))
                print("------------------------------------------------------------------------------------")
                time.sleep(2)
                end_time = datetime.utcnow()
                total_time = end_time - start_time
                total_time = round(total_time.total_seconds(),None)
                total_points = round(points_base * 10000 / total_time,None)
                print("lo siento, has perdido y por lo tanto has obtenido 0 puntos")
                print("------------------------------------------------------------------------------------")
                time.sleep(1)
                print("gracias por jugar, tu partida a durado", str(total_time), "segundos")
                print("------------------------------------------------------------------------------------")
                time.sleep(2)
                game_mode = input(MENU3).replace(" ","")
                if game_mode.isalpha() or int(game_mode) > 5 or int(game_mode) < 1:
                    print("gracias por jugar!")
                    time.sleep(3)
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
            print("no puedes poner texto ni espacios vacíos")
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
Solo puedes digitar los números:

1-facil
2-normal
3-dificil
4-muy difícil
-------------------------------------------
5-estadisticas
-------------------------------------------

si quieres continuar con el programa escribe la letra -y-, escribe cualquier otra cosa para salir: """


MENU2 ="""
Felicidades, ¡ganaste!,

si quieres seguir jugando escribe el número de la dificultad en que quieres jugar
                                         
1-facil
2-normal
3-dificil
4-muy difícil

o accede a tus estadísticas con el numero 5
                                         
escribe cualquier otra cosa para salir del programa: """


MENU3 = """
Lo siento, ¡perdiste!,

si quieres seguir jugando escribe el número de la dificultad en que quieres jugar
                                         
1-facil
2-normal
3-dificil
4-muy difícil

o accede a tus estadísticas con el numero 5
                                         
escribe cualquier otra cosa para salir del programa: """



MENU = """
Bienvenido a NumberGuesser V1.0

-----------------------------------------------------------------------

El juego en donde debes adivinar el número que piense la CPU

Ahora, adivinador ¿estás listo para comenzar?

-----------------------------------------------------------------------

Elige tu dificultad:

1-facil
2-normal
3-dificil
4-muy difícil

:Entre mayor sea la dificultad y entre menor sea el tiempo que tardes en adivinar el numero 
:Mayor será tu puntaje

----------------------------------------------------------------------

:Puedes digitar el número 5 para ver tus estadísticas

----------------------------------------------------------------------

digita el número de la dificultad en la que deseas jugar

(1,2,3,4) o accede a tus estadísticas(5): """



if __name__ == "__main__":
    run()