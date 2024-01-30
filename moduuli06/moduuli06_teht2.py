import random
def dice_roll(faces):
    return random.randint(1,faces)

if __name__ == '__main__':

    how_many_faces = int(input("Kuinka monta tahkoa haluat nopassa olevan? "))

    rolled_number = dice_roll(how_many_faces)
    times_rolled = 1
    print(f"Heitit noppaa ja sait silmäluvuksi {rolled_number}:n")

    while rolled_number != how_many_faces:
        times_rolled += 1
        rolled_number = dice_roll(how_many_faces)
        print(f"Heitit noppaa ja sait silmäluvuksi {rolled_number}:n")

    print(f"\nHeitit noppaa {times_rolled} kertaa ennen kuin heitit {how_many_faces}!")
