# klasa Account odpowiada za przechowywanie danych o konkretnym koncie oraz umożliwia podstawowe operacje na nim
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    # metoda get_name zwraca nazwę konta
    def get_name(self):
        return self.name

    # metoda get_balance zwraca stan konta
    def get_balance(self):
        return self.balance

    # metoda deposit dodaje podaną kwotę do stanu konta
    def deposit(self, amount):
        self.balance += amount
        
    def __str__(self):
        return f"Account({self.name}, {self.balance})"