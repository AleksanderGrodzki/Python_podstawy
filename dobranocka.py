import time
from pickle import GLOBAL

input("Witaj użytkowniku! \n")
print("Chcesz zagrać w grę?")
time.sleep(0.5)

if int(input("Naciśnij 1,aby zacząć "
                 "Naciśnij 0, aby wyjść\n")) == 1:
    x = int(input("Wybierz poziom trudności od 1 do 5: "))
    if x == 1:
        print("Poziom 1"
        "Powodzenia!")
    elif x == 2:
        print("Poziom 2"
        "Powodzenia!")
    elif x == 3:
        print("Poziom 3"
        "Powodzenia!")
    elif x == 4:
        print("Poziom 4"
        "Powodzenia!")
    elif x == 5:
        print("Poziom 5"
        "Powodzenia!")
else:
    print("Coś ty wybrał głupcze!")

input("Naciśnij enter, aby wyjść!")
print("Exit!")
