year = int(input("Ilmoita vuosiluku: "))

if year % 100 == 0 and year % 400 == 0:
    print(f'Ilmoittamasi vuosi "{year}" on karkausvuosi')
elif year % 4 == 0 and year % 100 != 0:
    print(f'Ilmoittamasi vuosi "{year}" on karkausvuosi')
else:
    print(f'Ilmoittamasi vuosi "{year}" ei ole karkausvuosi')
