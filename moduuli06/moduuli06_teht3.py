def gallons_to_litres(gallons):
    return gallons * 3.785

if __name__ == '__main__':

    how_many_gallons = float(input("Syötä bensiinin määrä gallonoina: "))
    print(gallons_to_litres(how_many_gallons))
