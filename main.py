
import random

nera_laimetojo = True
lygiosios = False


pries_zmogu = False
pries_kompiuteri = False
pries_lengvakomp = False
meniu = True

def pagrindinis_meniu():
    global meniu
    global pries_zmogu
    global pries_lengvakomp
    global pries_kompiuteri
    pries_zmogu = False
    pries_kompiuteri = False
    pries_lengvakomp = False
    meniu = True
    while meniu:
        nuline_poz()
        try:
            input_b = int(input(
                f"***Kryžiukai nuliukai***\n1. Prieš žmogų\n2. Prieš kompiuterį\n3. Išeiti (bet kuriuo metu įvedus end, būsite grąžintas čia)\n___Įveskite pasirinkimą: "))
            if input_b >= 4 or input_b < 1:
                print("Neteisingas pasirinkimas, pasirinkite prieš ką žaisite.")
                continue

            elif input_b == 1:
                pries_zmogu = True

                break

            elif input_b == 2:
                input_c = int(
                    input(f"Pasirinkite priešininko stiprumą: \n1. lengvas\n2. normalus\n___Įveskite pasirinkimą: "))
                if input_c == 2:
                    pries_kompiuteri = True
                    break
                if input_c == 1:
                    pries_lengvakomp = True
                    break

            elif input_b == 3:
                pries_zmogu = False
                pries_kompiuteri = False
                pries_lengvakomp = False
                meniu = False
                break

        except:
            print("Neteisingas pasirinkimas, pasirinkite prieš ką žaisite.")
            continue
def nuline_poz():
    global verte
    global pozicijos
    global pseudoturncount
    pseudoturncount = 0
    verte = {"a1": 2,
             "a2": 1,
             "a3": 2,
             "b1": 1,
             "b2": 3,
             "b3": 1,
             "c1": 2,
             "c2": 1,
             "c3": 2}

    pozicijos = {"a1": "*",
                 "a2": "*",
                 "a3": "*",
                 "b1": "*",
                 "b2": "*",
                 "b3": "*",
                 "c1": "*",
                 "c2": "*",
                 "c3": "*"}


#tikrina ar laimėta
def tikrink(pozicijos):
    global nera_laimetojo
    global lygiosios

    ivedimai = len(uzimti)
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
        elif (pozicijos["a1"] != pozicijos["a3"]) and (pozicijos["a1"] != pozicijos["c3"]) and (pozicijos["a1"] != pozicijos["c1"]) and (pozicijos["a2"] != pozicijos["c2"]) and (pozicijos["b1"] != pozicijos["b3"]) and (pozicijos["c1"] != pozicijos["c3"]) and (pozicijos["a3"] != pozicijos["c3"]) and (pozicijos["c1"] != pozicijos["a3"]):
            print("Laimėti neįmanoma!!!")
            nera_laimetojo = False
            break
        elif ivedimai == 9:
            print("Niekas nelaimėjo, visi langeliai išnaudoti!")
            nera_laimetojo = False
            break
        else:
            break

#normalaus sunkumo pasirinkimas
def pasirinkimas(vertes_sarasas):
    maxverte = max(vertes_sarasas.values())
    for key, value in vertes_sarasas.items():
        if value == maxverte:
            return key

def lengvas_pasirinkimas(vertes_sarasas):
    galimi_variantai = []
    for key, value in vertes_sarasas.items():
        if value > 0:
            galimi_variantai.append(key)
    l_pasirinkimas = random.choice(galimi_variantai)
    return l_pasirinkimas

verte = {"a1": 2,
         "a2": 1,
         "a3": 2,
         "b1": 1,
         "b2": 3,
         "b3": 1,
         "c1": 2,
         "c2": 1,
         "c3": 2}

#vertės tikrinimas normalaus sunkumo pasirinkimui
def vertes_tikrinimas(verte, poziciju_sarasas):
    for key, value in verte.items():
        if key in uzimti:
            verte[key] = -100

    if poziciju_sarasas["a2"] == "0" and (poziciju_sarasas["a1"] != "X" and poziciju_sarasas["a3"] != "X"):
        verte["a1"] = verte["a1"] + 2
        verte["a3"] = verte["a3"] + 2


    if (poziciju_sarasas["a1"] == "0" or poziciju_sarasas["a3"] == "0") and (poziciju_sarasas["a1"] != "X" and poziciju_sarasas["a2"] != "X" and poziciju_sarasas["a3"] != "X"):

        verte["a1"] = verte["a1"] + 2
        verte["a2"] = verte["a2"] + 3
        verte["a3"] = verte["a3"] + 2

    if (poziciju_sarasas["c1"] == "0" or poziciju_sarasas["c3"] == "0") and (poziciju_sarasas["c1"] != "X" and poziciju_sarasas["c2"] != "X" and poziciju_sarasas["c3"] != "X"):

        verte["c1"] += 2
        verte["c2"] += 3
        verte["c3"] += 2

    if (poziciju_sarasas["b1"] == "0" or poziciju_sarasas["b3"] == "0") and (poziciju_sarasas["b1"] != "X" and poziciju_sarasas["b2"] != "x" and poziciju_sarasas["b3"] != "X"):

        verte["b1"] += 2
        verte["b3"] += 2

    if (poziciju_sarasas["a1"] == "0" or poziciju_sarasas["c1"] == "0") and (poziciju_sarasas["a1"] != "X" and poziciju_sarasas["b1"] != "X" and poziciju_sarasas["c1"] != "X"):

        verte["a1"] += 2
        verte["b1"] += 3
        verte["c1"] += 2

    if (poziciju_sarasas["a2"] == "0" or poziciju_sarasas["c2"] == "0") and (poziciju_sarasas["a2"] != "X" and poziciju_sarasas["b2"] != "X" and poziciju_sarasas["c2"] != "X"):

        verte["a2"] += 2
        verte["c2"] += 2

    if (poziciju_sarasas["a3"] == "0" or poziciju_sarasas["c3"] == "0") and (poziciju_sarasas["a3"] != "X" and poziciju_sarasas["b3"] != "X" and poziciju_sarasas["c3"] != "X"):

        verte["a3"] += 2
        verte["b3"] += 3
        verte["c3"] += 2

    if poziciju_sarasas["b2"] == "0" and (poziciju_sarasas["a1"] != "X" and poziciju_sarasas["c3"] != "X"):

        verte["a1"] += 3
        verte["c3"] += 3

    if poziciju_sarasas["b2"] == "0" and (poziciju_sarasas["a3"] != "X" and poziciju_sarasas["c1"] != "X"):

        verte["a3"] += 3
        verte["c1"] += 3

    if ((poziciju_sarasas["a1"] == "X" or poziciju_sarasas["a3"] == "X") and poziciju_sarasas["a2"] == "X") or (poziciju_sarasas["a1"] == "X" and poziciju_sarasas["a3"] == "X"):

        verte["a1"] += 10
        verte["a2"] += 10
        verte["a3"] += 10

    if ((poziciju_sarasas["b1"] == "X" or poziciju_sarasas["b3"] == "X") and  poziciju_sarasas["b2"] == "X") or (poziciju_sarasas["b1"] == "X" and poziciju_sarasas["b3"] == "X"):

        verte["b1"] += 10
        verte["b2"] += 10
        verte["b3"] += 10

    if ((poziciju_sarasas["c1"] == "X" or poziciju_sarasas["c3"] == "X") and poziciju_sarasas["c2"] == "X") or (poziciju_sarasas["c1"] == "X" and poziciju_sarasas["c3"] == "X"):

        verte["c1"] += 10
        verte["c2"] += 10
        verte["c3"] += 10

    if ((poziciju_sarasas["a1"] == "X" or poziciju_sarasas["c1"] == "X") and poziciju_sarasas["b1"] == "X") or (poziciju_sarasas["a1"] == "X" and poziciju_sarasas["c1"] == "X"):

        verte["a1"] += 10
        verte["b1"] += 10
        verte["c1"] += 10

    if ((poziciju_sarasas["a2"] == "X" or poziciju_sarasas["c2"] == "X") and poziciju_sarasas["b2"] == "X") or (
            poziciju_sarasas["a2"] == "X" and poziciju_sarasas["c2"] == "X"):

        verte["a2"] += 10
        verte["b2"] += 10
        verte["c2"] += 10

    if ((poziciju_sarasas["a3"] == "X" or poziciju_sarasas["c3"] == "X") and poziciju_sarasas["b3"] == "X") or (
            poziciju_sarasas["a3"] == "X" and poziciju_sarasas["c3"] == "X"):

        verte["a3"] += 10
        verte["b3"] += 10
        verte["c3"] += 10

    if poziciju_sarasas["b2"] == "X" and (poziciju_sarasas["a1"] == "X" or poziciju_sarasas["c3"] == "X"):

        verte["a1"] += 10
        verte["c3"] += 10

    if poziciju_sarasas["b2"] == "X" and (poziciju_sarasas["a3"] == "X" or poziciju_sarasas["c1"] == "X"):

        verte["a3"] += 10
        verte["c1"] += 10

uzimti = []


pozicijos = {"a1": "*",
             "a2": "*",
             "a3": "*",
             "b1": "*",
             "b2": "*",
             "b3": "*",
             "c1": "*",
             "c2": "*",
             "c3": "*"}

pseudoturncount = 0


pagrindinis_meniu()



while pries_zmogu:
    while nera_laimetojo:
        print("", "   ", "1", "2", "3", "\n", " ", "/-------",  "\n", "A","|", pozicijos["a1"], pozicijos["a2"], pozicijos["a3"],
        "\n", "B", "|", pozicijos["b1"], pozicijos["b2"], pozicijos["b3"], "\n", "C", "|", pozicijos["c1"], pozicijos["c2"], pozicijos["c3"])
        # print("pries zmogu")
        tikrink(pozicijos)

        if nera_laimetojo == False:
            break
        elif pseudoturncount % 2 == 0:
            tikrink(pozicijos)
            pseudoturncount += 1
            input_a = input("X ėjimas: ")
            try:
                if input_a == "end":
                    pagrindinis_meniu()
                elif (pozicijos[input_a] == "X" or pozicijos[input_a] == "0") or (input_a not in pozicijos):
                    print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
                    pseudoturncount += 1

                else:
                    pozicijos[input_a] = "X"
            except:
                print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
                pseudoturncount += 1

        elif nera_laimetojo:
            tikrink(pozicijos)
            pseudoturncount += 1
            input_a = input("0 ėjimas: ")
            try:
                if input_a == "end":
                    pagrindinis_meniu()
                elif (pozicijos[input_a] == "X" or pozicijos[input_a] == "0") or (input_a not in pozicijos):
                    print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
                    pseudoturncount += 1

                else:
                    pozicijos[input_a] = "0"
            except:
                print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
                pseudoturncount += 1

        else:
            break


while pries_kompiuteri:
    while nera_laimetojo:
        vertes_tikrinimas(verte, pozicijos)
        print("", "   ", "1", "2", "3", "\n", " ", "/-------",  "\n", "A" ,"|", pozicijos["a1"], pozicijos["a2"], pozicijos["a3"],
              "\n", "B", "|", pozicijos["b1"], pozicijos["b2"], pozicijos["b3"], "\n", "C", "|", pozicijos["c1"], pozicijos["c2"], pozicijos["c3"])
        tikrink(pozicijos)


        if nera_laimetojo == False:
            break
        elif pseudoturncount % 2 == 0:
            pseudoturncount += 1
            input_a = input("X ėjimas: ")
            try:
                if input_a == "end":
                    pagrindinis_meniu()
                elif (pozicijos[input_a] == "X" or pozicijos[input_a] == "0") or (input_a not in pozicijos):
                    print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
                    pseudoturncount += 1

                else:
                    uzimti.append(input_a)
                    verte[input_a] = 0
                    pozicijos[input_a] = "X"
            except:
                print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
                pseudoturncount += 1

        elif nera_laimetojo:
            tikrink(pozicijos)
            pseudoturncount += 1
            vertes_tikrinimas(verte, pozicijos)
            pasirinkimas1 = pasirinkimas(verte)
            uzimti.append(pasirinkimas1)
            pozicijos[pasirinkimas1] = "0"
            verte[pasirinkimas1] = 0

        else:
            break


while pries_lengvakomp:
    while nera_laimetojo:
        vertes_tikrinimas(verte, pozicijos)
        print("", "   ", "1", "2", "3", "\n", " ", "/-------",  "\n", "A" ,"|", pozicijos["a1"], pozicijos["a2"], pozicijos["a3"],
              "\n", "B", "|", pozicijos["b1"], pozicijos["b2"], pozicijos["b3"], "\n", "C", "|", pozicijos["c1"], pozicijos["c2"], pozicijos["c3"])
        tikrink(pozicijos)


        if nera_laimetojo == False:
            break
        elif pseudoturncount % 2 == 0:
            pseudoturncount += 1
            input_a = input("X ėjimas: ")
            try:
                if input_a == "end":
                    pagrindinis_meniu()

                elif (pozicijos[input_a] == "X" or pozicijos[input_a] == "0") or (input_a not in pozicijos):
                        print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
                        pseudoturncount += 1

                else:
                    uzimti.append(input_a)
                    verte[input_a] = 0
                    pozicijos[input_a] = "X"
            except:
                print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
                pseudoturncount += 1

        elif nera_laimetojo:
            tikrink(pozicijos)
            pseudoturncount += 1
            vertes_tikrinimas(verte, pozicijos)
            pasirinkimas2 = lengvas_pasirinkimas(verte)
            uzimti.append(pasirinkimas2)
            pozicijos[pasirinkimas2] = "0"
            verte[pasirinkimas2] = 0

        else:
            break


