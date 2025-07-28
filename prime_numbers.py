import math
import time


def time_measuring(other_fun, num):
    start_time = time.perf_counter()
    other_fun(num)
    return time.perf_counter() - start_time


def check(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            print("To nie jest liczba pierwsza")
            break
        if i == int(math.sqrt(number)):
            print("To jest liczba pierwsza")


try:
    user_number = int(input("Podaj liczbę do sprawdzenia: "))
    print(f"Czas wykonania działania to: {time_measuring(check, user_number)} sekundy.")
except ValueError:
    print("To nie jest liczba!")
