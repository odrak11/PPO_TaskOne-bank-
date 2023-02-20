# klasa Person jest klasą przetrzymującą podstawowe dane o osobie
class Person:
    def __init__(self, name):
        self.name = name

    # metoda get_name zwraca imię i nazwisko osoby
    def get_name(self):
        return self.name

    def __str__(self):
        return self.name