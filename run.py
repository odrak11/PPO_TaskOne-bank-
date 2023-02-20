
from Bank import Bank
from Client import Client
from Account import Account
from Person import Person

bank = Bank("Bank")

# po uruchomieniu aplikacji jest odrazu tworzony jeden klient
client1 = Client("Jan Kowalski", Account("Jan", 1000))
bank.add_client(client1)

# menu aplikacji umożliwiające komunikację między użytkownikiem a aplikacją
def menu():
    print("")
    print("Witaj w banku.")
    print("1. Wyświetl dane klienta")
    print("2. Dodaj klienta")
    print("3. Usuń klienta")
    print("4. Dodaj środki na konto")
    print("5. Wyjdź")
    choice = input("Wybierz opcję: ")
    print("")
    
    # wybór 1 - wyświetlenie danych klienta
    if choice == "1":
        clientname = input("Podaj imię i nazwisko klienta: ")
        print(bank.get_client(clientname))
        menu()

    # wybór 2 - dodanie klienta
    elif choice == "2":
        name = input("Podaj imię i nazwisko klienta: ")
        account = input("Podaj nazwę konta: ")
        balance = input("Podaj stan konta: ")
        client = Client(name, Account(account, balance))
        bank.add_client(client)
        print("Klient został dodany.")
        menu()

    # wybór 3 - usunięcie klienta
    elif choice == "3":
        name = input("Podaj imię i nazwisko klienta do usunięcia: ")
        print(bank.delete_client(name))
        menu()

    # wybór 4 - wpłata pieniędzy na konto
    elif choice == "4":
        name = input("Podaj imię i nazwisko klienta: ")
        amount = input("Podaj kwotę do wpłaty: ")
        print(bank.deposit_money(name, amount))
        menu()

    # wybór 5 - wyjście z aplikacji
    elif choice == "5":
        print("Dziękujemy za skorzystanie z naszych usług.")
        exit()


menu()