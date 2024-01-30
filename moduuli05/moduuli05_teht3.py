input_number = int(input("Syötä numero: "))
is_prime = True

for i in range(2, input_number//2):
    if input_number % i == 0:
        print(f"Pienin löydetty tekijä: {i}")
        is_prime = False
        break

if is_prime == True and input_number != 4:
    print(f"Syöttämäsi numero {input_number} on alkuluku!")
else:
    print(f"Syöttämäsi numero {input_number} ei ole alkuluku!")
