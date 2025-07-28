import random
import time


WINS_TIMES = 3

"""
rock -> 1
paper -> 2
scissors -> 3
"""

print("Gra kamień, papier, nożyce. Ten kto wygra 3 razy jest zwycięzcą.")

user_wins_times = 0
computer_wins_times = 0
game_runs = True

try:
    while game_runs:
        computer = random.randint(1, 3)
        user = int(
            input("Wybierz jedną z trzech możliwości: 1.Kamień 2.Papier 3.Nożyce:\n")
        )
        print(f"Komputer wybrał: {computer}")
        time.sleep(1)

        if computer == user:
            print("Remis")
        elif computer - user == -1 or computer - user == 2:
            user_wins_times += 1
            print("Punkt dla użytkownika")
        else:
            computer_wins_times += 1
            print("Punkt dla komputera")

        if user_wins_times == WINS_TIMES or computer_wins_times == WINS_TIMES:
            game_runs = False

    if computer_wins_times > user_wins_times:
        print("Komputer wygrał")
    else:
        print("Użytkownik wygrał")

except ValueError:
    print("Nieznana wartość")
