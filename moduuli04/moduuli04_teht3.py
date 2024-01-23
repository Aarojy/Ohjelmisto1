user_input = input("Syötä numero tai tyhjä merkkijono: ")
min_value = int(user_input)
max_value = int(user_input)

while user_input != "":
    if int(user_input) < min_value:
        min_value = int(user_input)
    if int(user_input) > max_value:
        max_value = int(user_input)
    user_input = input("Syötä numero tai tyhjä merkkijono: ")

print(f"Suurin syöttämäsi arvo oli: {max_value}")
print(f"Pienin syöttämäsi arvo oli: {min_value}")
