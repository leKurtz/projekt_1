# hlavicka

# projekt_1.py: první projekt do Engeto Online Python Akademie
# autor: Theodor Vysušil
# email: vysusil.theodor@gmail.com

#tady bude začínat můj kód

# Registrovaní uživatelé a jejich hesla
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Přihlášení uživatele
username = input("username: ")
password = input("password: ")

# Ověření přihlašovacích údajů
if username in users and users[username] == password:
    print("Welcome to the app,", username)

    print("We have 3 texts to be analyzed.")
    text = input("Enter a number btw. 1 and 3 to select: ")

else:
    print("unregistered user, terminating the program..")