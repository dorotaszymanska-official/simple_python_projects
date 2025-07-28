def celsius_to_fahrenheit(degrees):
    return (9 * degrees / 5) + 32


def fahrenheit_to_celsius(degrees):
    return (degrees - 32) * 5 / 9


print("Witam w konwerterze temperatury!")

while True:
    try:
        user_number = float(input("Podaj temperaturę: "))
        temperature_unit = input(
            "Podaj jednostkę: c - stopnie Celsjusza, f - stopnie Fahrenheita: "
        )
        if temperature_unit == "c":
            print(
                f"Temperatura w stopniach Fahrenheita wynosi: {celsius_to_fahrenheit(user_number)}"
            )
            break
        elif temperature_unit == "f":
            print(
                f"Temperatura w stopniach Celsjusza wynosi: {fahrenheit_to_celsius(user_number)}"
            )
            break
        else:
            print("Nie rozpoznano odpowiedniego znaku")
    except ValueError:
        print("Podaj liczbę kretynie!")
