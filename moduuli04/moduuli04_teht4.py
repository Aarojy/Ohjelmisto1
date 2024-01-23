import random

right_number = random.randint(1,10)

player_guess = int(input("Arvaa numero väliltä 1-10: "))

while player_guess != right_number:
    if player_guess > right_number:
        print(f"Arvaamasi numero: {player_guess} on suurempi kuin oikea numero.")
    else:
        print(f"Arvaamasi numero: {player_guess} on pienempi kuin oikea numero.")
    player_guess = int(input("Arvaa uusi numero väliltä 1-10: "))

print(f"Arvasit oikean numeron {right_number}!")

