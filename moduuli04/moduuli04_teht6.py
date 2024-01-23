import random

number_of_points = int(input("Syötä käytettävien pisteiden lukumäärä: "))
dots_outside = 0
dots_inside = 0

i = 1
while i <= number_of_points:
    x = random.random()
    y = random.random()
    if x ** 2 + y ** 2 <= 1:
        dots_inside += 1
    else:
        dots_outside += 1

    i += 1

calculated_pi = dots_inside / (dots_inside + dots_outside)*4
print(calculated_pi)