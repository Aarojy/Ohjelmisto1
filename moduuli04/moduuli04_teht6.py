import random

number_of_points = int(input("Syötä käytettävien pisteiden lukumäärä: "))
dots_inside = 0

i = 1
while i <= number_of_points:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x ** 2 + y ** 2 <= 1:
        dots_inside += 1

    i += 1

calculated_pi = dots_inside / number_of_points*4
print(calculated_pi)