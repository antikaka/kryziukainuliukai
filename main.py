
nera_laimetojo = True
lygiosios = False
def tikrink(pozicijos):
    global nera_laimetojo
    global lygiosios

    ivedimai = sum(value == "X" for value in pozicijos.values()) + sum(value == "0" for value in pozicijos.values())
    while nera_laimetojo:

        if (pozicijos["a1"] == pozicijos["a2"] == pozicijos["a3"]) and (pozicijos["a3"] != "*"):
            print(f"{pozicijos["a1"]} laimėjo!")
            nera_laimetojo = False
            break
        elif (pozicijos["b1"] == pozicijos["b2"] == pozicijos["b3"]) and (pozicijos["b3"] != "*"):
            print(f"{pozicijos["b1"]} laimėjo!")
            nera_laimetojo = False
            break
        elif (pozicijos["c1"] == pozicijos["c2"] == pozicijos["c3"]) and (pozicijos["c3"] != "*"):
            print(f"{pozicijos["c1"]} laimėjo!")
            nera_laimetojo = False
            break
        elif (pozicijos["a1"] == pozicijos["b2"] == pozicijos["c3"]) and (pozicijos["c3"] != "*"):
            print(f"{pozicijos["a1"]} laimėjo!")
            nera_laimetojo = False
            break
        elif (pozicijos["a3"] == pozicijos["b2"] == pozicijos["c1"]) and (pozicijos["c1"] != "*"):
            print(f"{pozicijos["c1"]} laimėjo!")
            nera_laimetojo = False
            break
        elif (pozicijos["a1"] == pozicijos["b1"] == pozicijos["c1"]) and (pozicijos["c1"] != "*"):
            print(f"{pozicijos["a1"]} laimėjo!")
            nera_laimetojo = False
            break
        elif (pozicijos["a2"] == pozicijos["b2"] == pozicijos["c2"]) and (pozicijos["c2"] != "*"):
            print(f"{pozicijos["a2"]} laimėjo!")
            nera_laimetojo = False
            break
        elif (pozicijos["a3"] == pozicijos["b3"] == pozicijos["c3"]) and (pozicijos["b3"] != "*"):
            print(f"{pozicijos["a3"]} laimėjo!")
            nera_laimetojo = False
            break
        elif ivedimai == 9:
            print("Niekas nelaimėjo, visi langeliai išnaudoti!")
            nera_laimetojo = False
            break
        elif (pozicijos["a1"] != pozicijos["a3"]) and (pozicijos["a1"] != pozicijos["c3"]) and (pozicijos["a1"] != pozicijos["c1"]) and (pozicijos["a2"] != pozicijos["c2"]) and (pozicijos["b1"] != pozicijos["b3"]) and (pozicijos["c1"] != pozicijos["c3"]) and (pozicijos["a3"] != pozicijos["c3"]) and (pozicijos["c1"] != pozicijos["a3"]):
            print("Laimėti neįmanoma!!!")
            nera_laimetojo = False
            break
        else:
            break




pozicijos = {"a1": "*",
             "a2": "*",
             "a3": "*",
             "b1": "*",
             "b2": "*",
             "b3": "*",
             "c1": "*",
             "c2": "*",
             "c3": "*"}

x = 0


pries_zmogu = False
pries_kompiuteri = False

while True:
    try:
        input_b = int(input(f"***Kryžiukai nuliukai***\n1. Prieš žmogų\n2. Prieš kompiuterį\n___Įveskite pasirinkimą: "))
        if input_b >=3 or input_b < 1:
            print("Neteisingas pasirinkimas, pasirinkite prieš ką žaisite.")
            continue

        elif input_b == 1:
            pries_zmogu = True
            break

        elif input_b == 2:
            pries_kompiuteri = True
            break
    except:
        print("Neteisingas pasirinkimas, pasirinkite prieš ką žaisite.")
        continue

while pries_zmogu:
    while nera_laimetojo:
        print("", "   ", "1", "2", "3", "\n", " ", "/-------",  "\n", "A","|", pozicijos["a1"], pozicijos["a2"], pozicijos["a3"],
        "\n", "B", "|", pozicijos["b1"], pozicijos["b2"], pozicijos["b3"], "\n", "C", "|", pozicijos["c1"], pozicijos["c2"], pozicijos["c3"])

        tikrink(pozicijos)

        if nera_laimetojo == False:
            break
        elif x % 2 == 0:
            tikrink(pozicijos)
            x += 1
            input_a = input("X ėjimas: ")
            try:
                if (pozicijos[input_a] == "X" or pozicijos[input_a] == "0") or (input_a not in pozicijos):
                    print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
                    x += 1

                else:
                    pozicijos[input_a] = "X"
            except:
                print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
                x += 1

        elif nera_laimetojo:
            tikrink(pozicijos)
            x += 1
            input_a = input("0 ėjimas: ")
            try:
                if (pozicijos[input_a] == "X" or pozicijos[input_a] == "0") or (input_a not in pozicijos):
                    print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
                    x += 1

                else:
                    pozicijos[input_a] = "0"
            except:
                print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
                x += 1

        else:
            break







