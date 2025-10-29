import random
import fractions
import sys
from fractions import Fraction
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

app = QApplication()


punkty = 0
print("Wybierz liczbę od 1 do 5")
próby = random.randint(3, 6)
for wygrana in range(próby):
    #Użytkownik podaje liczbę
    liczba = int(input("Podaj liczbę: "))
    #losowa wygrywająca liczba
    import random
    wygrana = random.randint(1, 5)

    if liczba == wygrana:
        print("Wygrałeś!")
        punkty += 1
    else:
        if liczba > wygrana:
            print("Przegrałeś,za dużo, wygrywająca liczba to:")
        elif liczba < wygrana:
            print("Przegrałeś, za mało, wygrywająca liczba to:")
    print(wygrana)
#zapisujemy wynik wygranych w postaci ułamka zwykłego\
x = Fraction(punkty, próby)
print("Ilość twoich punktów to", x)
