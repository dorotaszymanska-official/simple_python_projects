while True:
    try:
        number1 = input("Wpisz pierwszą liczbę: ")
        sign = input("Podaj znak: ")
        number2 = input("Wpisz drugą liczbę: ")
        if sign == ":":
            sign = "/"
        print(eval(f"{number1} {sign} {number2}"))
        break
    except ZeroDivisionError:
        print("Nie można dzielić przez 0 !!! Spróbuj jeszcze raz")
    except NameError:
        print("Podaj liczbę. Spróbuj jeszcze raz")
    except SyntaxError:
        print("Podaj znak działania matematycznego")
