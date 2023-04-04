
import random

# Открываем файл с данными и создаем словарь стран и столиц
with open("countries.txt", "r") as file:
    countries = dict(line.strip().split("-") for line in file)

# Создаем функцию для отображения столицы или названия страны
def display_capital_or_country():
    name = input("Sisestage riigi või pealinna nimi: ").title()
    if name in countries:
        print(countries[name])
    else:
        answer = input(f"{name} sõnastikust puudu. Kas soovite selle lisada? (y/n) ")
        if answer == "y":
            capital = input(f"Sisestage kapital {name}: ").title()
            if capital:
                countries[name] = capital.title()
                with open("countries.txt", "a") as file:
                    file.write(f"\n{name}-{capital.title()}")
                print(f"{name} lisatud sõnastikku.")
            else:
                print("Kapital on sisestamata.")
        else:
            print("")

# Создаем функцию для исправления ошибки в словаре
def correct_error():
    name = input("Sisestage parandamiseks riigi või pealinna nimi: ").title()
    if name in countries:
        capital = input(f"Sisestage jaoks uus kapital {name}: ").title()
        if capital:
            countries[name] = capital.title()
            with open("countries.txt", "w") as file:
                for country, capital in countries.items():
                    file.write(f"{country}-{capital}\n")
            print(f"Kapitali jaoks {name} muudetud {capital.title()}.")
        else:
            print("Kapital on sisestamata.")
    else:
        print(f"{name} pole sõnastikus.")

# Создаем функцию для проверки знаний
def test_your_knowledge():
    total = 0
    correct = 0
    for i in range(10):
        name = random.choice(list(countries.keys()))
        capital = countries[name]
        answer = input(f"Riigi pealinna nimi {name}: ").title()
        if answer:
            total += 1
            if answer == capital:
                print("sa vastasid õigesti.")
                correct += 1
            else:
                print(f"Sa vastasid valesti. Õige vastus: {capital}.")
    if total > 0:
        print(f"Sa võitsid {correct} iz {total} ({correct/total*100:.2f}%).")
    else:
        print("Sõnastikus pole riike.")

# бесконечный цикл для работы приложения
while True:
    command = input("Sisestage käsk (country/correct/test/exit): ")
    if command == "country":
        display_capital_or_country()
    elif command == "correct":
        correct_error()
    elif command == "test":
        test_your_knowledge()
    elif command == "exit":
        break
    else:
        print("Kehtetu käsk. proovi uuesti.") 