import random


MINIMUM = 1
MAX_TRIES = 5

game_mode_message = "Wybierz tryb gry, wprowadzając odpowiednią liczbę:\n1.Użytkownik zgaduje liczbę\n2.Komputer zgaduje liczbę\n"

level_message = """Wybierz poziom, wprowadzając przyporządkowaną mu liczbę:\n
1.Łatwy (zakres: 1-10)\n2.Średni (zakres: 1-100)\n3.Trudny (zakres: 1-1000)\n"""


def set_level(level):
    if level == 1:
        return 10
    elif level == 2:
        return 100
    elif level == 3:
        return 1000
    else:
        return 0


def user_mode(user_answer, max_tries):
    print("Zgadnij liczbę. Powodzenia!")
    computer_number = random.randint(MINIMUM, set_level(user_answer))
    tries = max_tries
    while tries >= 0:
        message = f"To jest próba nr. {max_tries + 1 - tries}. Wybierz liczbę od z zakresu od {MINIMUM} do {set_level(user_answer)}:\n"
        user_number = int(input(message))
        if user_number == computer_number:
            print("Liczba odgadnięta. Wygrana")
            break
        elif user_number > computer_number:
            print("Twoja liczba jest za duża")
            tries -= 1
        elif user_number < computer_number:
            print("Twoja liczba jest za mała")
            tries -= 1
        else:
            return
        if tries <= 0:
            print("Użytkownik przegrał!")
            break


def computer_mode(user_answer, max_tries):

    user_number = int(
        input(
            f"Komputer zgaduje. Wybierz liczbę z zakresu od {MINIMUM} do {set_level(user_answer)}:\n"
        )
    )
    tries = max_tries
    low_range = MINIMUM
    high_range = set_level(user_answer)

    while tries >= 0:
        print(f"To jest próba nr. {max_tries + 1 - tries} komputera.")
        computer_number = random.randint(low_range, high_range)
        print(f"Liczba wybrana przez komputer to: {computer_number}")
        user_reaction = int(
            input(
                "Jeśli komputer zgadł, wpisz 1. Jeśli liczba podana przez komputer jest za mała - wciśnij 2. Jeśli jest za duża - wciśnij 3."
            )
        )
        if user_reaction == 1:
            print("Komputer wygrał!")
            break
        elif user_reaction == 2:
            tries -= 1
            low_range = computer_number
        elif user_reaction == 3:
            tries -= 1
            high_range = computer_number
        else:
            print("Brak reakcji")
        if tries <= 0:
            print("Komputer przegrał!")
            break


try:
    user_choice = int(input(level_message))
    mode = int(input(game_mode_message))

    if mode == 1:
        user_mode(user_choice, MAX_TRIES)
    elif mode == 2:
        computer_mode(user_choice, MAX_TRIES)
    else:
        print("Nie ma takiego trybu!!!")
except ValueError:
    print("Niewłaściwy znak!!!")
except NameError:
    print("Niewłaściwy poziom!!!")
