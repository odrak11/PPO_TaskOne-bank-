# klasa Client odpowiada za przechowywanie danych o konkretnym kliencie i dziedziczy po klasie Person
from Person import Person
from Account import Account

class Client(Person):
    def __init__(self, name, account):
        super().__init__(name)
        self.account = account

    # metoda get_account zwraca obiekt klasy Account
    def get_account(self):
        return self.account
        
    def __str__(self):
        return f"Client({self.name}, {self.account})"
        