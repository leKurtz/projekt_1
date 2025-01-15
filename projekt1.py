# projekt_1.py: první projekt do Engeto Online Python Akademie

# author: Theodor Vysušil
# email: vysusil.theodor@gmail.com

# TADY ZACINA KOD

TEXTS = [
    """
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
    """At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.""",
]

separator = "-" * 40

# PRIHLASENI

accesses = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

username = input("username: ")
password = input("password: ")

if username in accesses and accesses[username] == password:
    print("Welcome to the app", username)
    print(separator)
else:
    print("unregistered user, terminating the program..")
    exit()

# VYBER TEXTU

print("We have 3 texts to be analyzed.")
print(separator)

choose_text = input("Enter a number btw. 1 and 3 to select: ")
print(separator)

if not choose_text.isdigit():
    print("You must choose a number!")
    exit()
    
elif int(choose_text) not in range (1, 4):
    print("You can choose only 1, 2 or 3!")
    exit()

# ANALYZA TEXTU

selected_text = TEXTS[int(choose_text) -1]

words = selected_text.split()
word_count = len(words)

title_count = sum(1 for word in words if word.istitle())
upper_count = sum(1 for word in words if word.isupper())
lower_count = sum(1 for word in words if word.islower())
numeric_count = sum(1 for word in words if word.isdigit())
numeric_sum = sum(int(word) for word in words if word.isdigit())

print("There are", word_count, "words in the selected text.")
print("There are", title_count, "titlecase words.")
print("There are", upper_count, "uppercase words.")
print("There are", lower_count, "lowercase words.")
print("There are", numeric_count, "numeric strings")
print("There are of all the numbers", numeric_sum)
print(separator)

# GRAF

print("{:<3}| {:<13}|{:>3}".format("LEN", "OCCURRENCES", "NR."))
print(separator)


length_counts = {}
for word in words:
    length = len(word.strip(".,!_:;"))
    length_counts[length] = length_counts.get(length, 0) + 1

for length in sorted(length_counts):
    count = length_counts[length]
    print(f"{length:>3}|{'*' * count:<14}|{count:<3}")


