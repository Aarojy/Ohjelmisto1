import random

number_of_dice = int(input("Syötä arpakuutioiden lukumäärä: "))
sum_of_rolled_numbers = 0

for i in range(number_of_dice):
    sum_of_rolled_numbers += random.randint(1,6)

print(f"Heitit {number_of_dice} noppaa. Heittämiesi noppien silmälukujen summa on: {sum_of_rolled_numbers}")