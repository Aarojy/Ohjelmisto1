from math import pi
def price_per_squaremeter(diameter_cm, price):
    diameter_m = diameter_cm * 0.01
    area = pi * (diameter_m/2)**2
    return price/area

if __name__ == '__main__':

    pizza1_diameter_cm = float(input("Syötä pizzan 1 halkaisija senttimetreinä: "))
    pizza1_price = float(input("Syötä pizzan 1 hinta euroina: "))

    pizza2_diameter_cm = float(input("Syötä pizzan 2 halkaisija senttimetreinä: "))
    pizza2_price = float(input("Syötä pizzan 2 hinta euroina: "))

    print(f"Pizzan 1 hinta on: {price_per_squaremeter(pizza1_diameter_cm,pizza1_price):.2f} euroa/neliömetri.")
    print(f"Pizzan 2 hinta on: {price_per_squaremeter(pizza2_diameter_cm, pizza2_price):.2f} euroa/neliömetri.")

    if price_per_squaremeter(pizza1_diameter_cm,pizza1_price) == price_per_squaremeter(pizza2_diameter_cm, pizza2_price):
        print("Pizzan 1 ja 2 antavat yhtä suuren vastineen rahalle.")
    elif price_per_squaremeter(pizza1_diameter_cm,pizza1_price) < price_per_squaremeter(pizza2_diameter_cm, pizza2_price):
        print("Pizzan 1 antaa paremman vastineen rahalle.")
    else:
        print("Pizzan 2 antaa paremman vastineen rahalle.")