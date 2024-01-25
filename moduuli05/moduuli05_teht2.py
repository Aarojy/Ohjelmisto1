new_number = 0
list_of_numbers = []

new_number = input("Syötä numero: ")
while new_number != "":
    list_of_numbers.append(int(new_number))
    new_number = input("Syötä uusi numero: ")

if len(list_of_numbers) >= 5:
     amount_of_numbers_to_print = 5
else:
     amount_of_numbers_to_print = len(list_of_numbers)

print(f"Syötit {len(list_of_numbers)} numeroa. Tulostetaan syöttämistäsi numeroista {amount_of_numbers_to_print} suurinta järjestyksessä suurimasta pienimpään:")

list_of_numbers.sort(reverse=True)
for i in range(amount_of_numbers_to_print):
    print(list_of_numbers[i])
