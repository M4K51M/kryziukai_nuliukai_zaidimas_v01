import os
# import system
import time


# os.system("cls") panaudosime ekrano valymui
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# zaidimo_laukas = list(range(1, 10))
laukeliai = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}


def zaidimo_laukas_tinklelis():
    cls()
    print("\u2554\u2550\u2550\u2550\u2564\u2550\u2550\u2550\u2564\u2550\u2550\u2550\u2557")
    # for i in zaidimo_laukas(9):
    print("\u2551", laukeliai[7], "\u2502", laukeliai[8], "\u2502", laukeliai[9], "\u2551")
    print("\u255F\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2563")
    print("\u2551", laukeliai[4], "\u2502", laukeliai[5], "\u2502", laukeliai[6], "\u2551")
    print("\u255F\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2563")
    print("\u2551", laukeliai[1], "\u2502", laukeliai[2], "\u2502", laukeliai[3], "\u2551")
    print("\u255A\u2550\u2550\u2550\u2567\u2550\u2550\u2550\u2567\u2550\u2550\u2550\u255D")
    # print("\u2551", "X", "\u2502", "0", "\u2502", "O", "\u2551")
    # print("\u255A\u2550\u2550\u2550\u2567\u2550\u2550\u2550\u2567\u2550\u2550\u2550\u255D")


# def laukelio_ivedimas():
def laukelio_ivedimas(pasirinktas_laukelis):
    while True:
        laukelis = input(f"Pasirinkite laisvą norimą laukelį (nuo 1 iki 9):")
        # laukelis = input(f"Pasirinkite laisvą norimą laukelį (nuo 1 iki 9):"  + pasirinktas_laukelis)
        if not (laukelis in "123456789"):
            print("Neteisingai įvestas laukelis, įveskite dar kartą laisvą laukelio numerį nuo 1 iki 9: ")
            continue
        laukelis = int(laukelis)
        # if str(zaidimo_laukas_tinklelis[laukelis]) in "XO":
        if str(laukeliai[laukelis]) == "X" or str(laukeliai[laukelis]) == "O":
            print("Šitas laukelis jau užimtas, pasirinkite kitą LAISVĄ laukelį: ")
            continue
        laukeliai[laukelis] = pasirinktas_laukelis
        break


def tikrinam_laimejimo_kombinacija():
    if (laukeliai[1] == laukeliai[2] == laukeliai[3] or laukeliai[4] == laukeliai[5] == laukeliai[6] or laukeliai[7] ==
            laukeliai[8] == laukeliai[9]):
        return True
    elif (laukeliai[1] == laukeliai[4] == laukeliai[7] or laukeliai[2] == laukeliai[5] == laukeliai[8] or laukeliai[
        3] == laukeliai[6] == laukeliai[9]):
        return True
    elif (laukeliai[1] == laukeliai[5] == laukeliai[9] or laukeliai[3] == laukeliai[5] == laukeliai[7]):
        return True
    else:
        return False


def main():
    ejimo_numeris = 0
    while True:
        cls()
        zaidimo_laukas_tinklelis()
        # laukelio_ivedimas()
        if ejimo_numeris % 2 == 0:
            # return "X"
            laukelio_ivedimas("X")
        else:
            laukelio_ivedimas("O")
        if ejimo_numeris > 3:
            laimetojas = tikrinam_laimejimo_kombinacija()
            if laimetojas:
                zaidimo_laukas_tinklelis()
                if ejimo_numeris % 2 == 0:
                    print("Žaidėjas 1 (X) laimėjo!")
                elif ejimo_numeris % 2 == 1:
                    print("Žaidėjas 2 (O) laimėjo!")
                # print(laimetojas, "Laimėjo!")
                break
        ejimo_numeris += 1
        if ejimo_numeris > 8:
            zaidimo_laukas_tinklelis()
            print("Deja, bet niekas nelaimėjo.")
            break


def pause():
    programPause = input("Paspauskite <ENTER> pabaigti programos vykdymą...")


main()
pause()
# time.sleep(10)

# zaidimo_laukas_tinklelis()
# laukelio_ivedimas()
# tikrinam_laimejimo_kombinacija()
