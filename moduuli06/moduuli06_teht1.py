import random
def dice_roll():
    return random.randint(1,6)

if __name__ == '__main__':

    rolled_number = dice_roll()
    times_rolled = 1
    print(rolled_number)

    while rolled_number != 6:
        times_rolled += 1
        rolled_number = dice_roll()
        print(f"Heitit noppaa ja sait silmäluvuksi {rolled_number}:n")

    print(f"\nHeitit noppaa {times_rolled} kertaa ennen kuin heitit 6:n!")
