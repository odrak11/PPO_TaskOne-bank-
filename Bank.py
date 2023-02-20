# klasa Bank jest klasą zbiorczą która umożliwia wykonanie operacji bankowych
from Client import Client
from Account import Account
from Person import Person

class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = []

    # metoda add_client dodaje klienta do listy klientów
    def add_client(self, client):
        self.clients.append(client)

    # metoda get_client zwraca dane klienta o podanym imieniu i nazwisku
    def get_client(self, name):
        for client in self.clients:
            if client.get_name() == name:
                return "Klient: " + client.get_name() + ", Stan konta: " + str(client.get_account().get_balance()) + " zł"
        return "Brak klienta o takich danych."

    # metoda deposit_money dodaje podaną kwotę do stanu konta klienta o podanym imieniu i nazwisku
    def deposit_money(self, name, amount):
        for client in self.clients:
            if client.get_name() == name:
                client.get_account().deposit(amount)
                return "Dodano pieniądze na konto"
        return "Brak klienta o takich danych."

    # metoda delete_client usuwa klienta o podanym imieniu i nazwisku
    def delete_client(self, name):
        for client in self.clients:
            if client.get_name() == name:
                self.clients.remove(client)
                return "Klient został usunięty."
        return "Brak klienta o takich danych."
    

    def __str__(self):
       return f"Bank({self.name}, {self.clients})"