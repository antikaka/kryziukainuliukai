
import random
import sys

nera_laimetojo = True

def pagrindinis_meniu(): #pagrindinis meniu
    global nera_laimetojo
    nuline_poz()

    while True:
        input_c = input(
            "***Kryžiukai nuliukai***\n1. Prieš žmogų\n2. Prieš kompiuterį\n3. Rodyti šios sesijos rezultatus\n4. Išeiti \n----Bet kuriuo metu įvedus 'end', būsite grąžintas čia----\n___Įveskite pasirinkimą: "
        )

        if input_c == "1":
            pries_zmogu()
            break
        elif input_c == "2":
            input_b = input(
                "Pasirinkite priešininko stiprumą:\n1. lengvas\n2. normalus\n___Įveskite pasirinkimą: ")
            if input_b == "1":
                pries_lengvakomp()
                break
            elif input_b == "2":
                pries_kompiuteri()
                break
        elif input_c == "3":
            print(f"X žaidėjo pergalės: {laimejimai["X"]}\n0 žaidėjo pergalės: {laimejimai["0"]}")
            continue
        elif input_c == "4":
            sys.exit()
        else:
            print("Netinkamas pasirinkimas. Bandykite dar kartą.")


uzimti = []

def zaidimo_pradzia(): #žaidimo vizualizacija

    tikrink(pozicijos)
    return print("", "   ", "1", "2", "3", "\n", " ", "/-------", "\n", "A", "|", pozicijos["a1"], pozicijos["a2"],
                 pozicijos["a3"],
                 "\n", "B", "|", pozicijos["b1"], pozicijos["b2"], pozicijos["b3"], "\n", "C", "|", pozicijos["c1"],
                 pozicijos["c2"], pozicijos["c3"])

def nuline_poz(): #žaidimo nulinė pozicija, naudojama tada kai žaidimas baigiasi
    global verte
    global pozicijos
    global uzimti
    verte["a1"] = 2
    verte["a2"] = 1
    verte["a3"] = 2
    verte["b1"] = 1
    verte["b2"] = 3
    verte["b3"] = 1
    verte["c1"] = 2
    verte["c2"] = 1
    verte["c3"] = 2

    pozicijos = {"a1": "*",
                 "a2": "*",
                 "a3": "*",
                 "b1": "*",
                 "b2": "*",
                 "b3": "*",
                 "c1": "*",
                 "c2": "*",
                 "c3": "*"}
    uzimti = []


verte = {"a1": 2,    #pradinės vertės; vidurinis > kampiniai > visi kiti
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

laimejimai = { "X": 0,
               "0": 0}

def tikrink(pozicijos):  #tikrina ar laimėta, ar lygiosios ir pnš


    ivedimai = len(uzimti)


    if (pozicijos["a1"] == pozicijos["a2"] == pozicijos["a3"]) and (pozicijos["a3"] != "*"):
        print(f"{pozicijos["a1"]} laimėjo!")
        laimejimai[pozicijos["a1"]] += 1
        pagrindinis_meniu()
    elif (pozicijos["b1"] == pozicijos["b2"] == pozicijos["b3"]) and (pozicijos["b3"] != "*"):
        print(f"{pozicijos["b1"]} laimėjo!")
        laimejimai[pozicijos["b1"]] += 1
        pagrindinis_meniu()
    elif (pozicijos["c1"] == pozicijos["c2"] == pozicijos["c3"]) and (pozicijos["c3"] != "*"):
        print(f"{pozicijos["c1"]} laimėjo!")
        laimejimai[pozicijos["c1"]] += 1
        pagrindinis_meniu()
    elif (pozicijos["a1"] == pozicijos["b2"] == pozicijos["c3"]) and (pozicijos["c3"] != "*"):
        print(f"{pozicijos["a1"]} laimėjo!")
        laimejimai[pozicijos["a1"]] += 1
        pagrindinis_meniu()
    elif (pozicijos["a3"] == pozicijos["b2"] == pozicijos["c1"]) and (pozicijos["c1"] != "*"):
        print(f"{pozicijos["c1"]} laimėjo!")
        laimejimai[pozicijos["c1"]] += 1
        pagrindinis_meniu()
    elif (pozicijos["a1"] == pozicijos["b1"] == pozicijos["c1"]) and (pozicijos["c1"] != "*"):
        print(f"{pozicijos["a1"]} laimėjo!")
        laimejimai[pozicijos["a1"]] += 1
        pagrindinis_meniu()
    elif (pozicijos["a2"] == pozicijos["b2"] == pozicijos["c2"]) and (pozicijos["c2"] != "*"):
        print(f"{pozicijos["a2"]} laimėjo!")
        laimejimai[pozicijos["a2"]] += 1
        pagrindinis_meniu()
    elif (pozicijos["a3"] == pozicijos["b3"] == pozicijos["c3"]) and (pozicijos["b3"] != "*"):
        print(f"{pozicijos["a3"]} laimėjo!")
        laimejimai[pozicijos["a3"]] += 1
        pagrindinis_meniu()
    elif (pozicijos["a1"] != pozicijos["a3"]) and (pozicijos["a1"] != pozicijos["c3"]) and (pozicijos["a1"] != pozicijos["c1"]) and (pozicijos["a2"] != pozicijos["c2"]) and (pozicijos["b1"] != pozicijos["b3"]) and (pozicijos["c1"] != pozicijos["c3"]) and (pozicijos["a3"] != pozicijos["c3"]) and (pozicijos["c1"] != pozicijos["a3"]):
        print("Laimėti neįmanoma!!!")

        pagrindinis_meniu()
    elif ivedimai == 9:
        print("Niekas nelaimėjo, visi langeliai išnaudoti!")

        pagrindinis_meniu()




def pasirinkimas(vertes_sarasas): #normalaus sunkumo AI pasirinkimas iš vertės sąrašo
    maxverte = max(vertes_sarasas.values())
    for key, value in vertes_sarasas.items():
        if value == maxverte:
            return key

def lengvas_pasirinkimas(vertes_sarasas): #lengvo sunkumo AI pasirinkimas, irgi iš vertės sąrašo, bet neatsižvelgiant į pačią vertę, o tik į tai kokie žingsniai yra galimi
    galimi_variantai = []
    for key, value in vertes_sarasas.items():
        if value > 0:
            galimi_variantai.append(key)
    l_pasirinkimas = random.choice(galimi_variantai)
    return l_pasirinkimas




def vertes_tikrinimas(verte, poziciju_sarasas): #galimų ėjimų vertės tikrinimas atsižvelgiant į savo ėjimus ir į priešininko ėjimus
    for key, value in verte.items():            #prioritetas skiriamas ne savo pergalės užtikrinimui, bet priešininko pralaimėjimui
        if key in uzimti:
            verte[key] = -1000

    if poziciju_sarasas["a2"] == "0" and (poziciju_sarasas["a1"] != "X" and poziciju_sarasas["a3"] != "X"):
        verte["a1"] = verte["a1"] + 2
        verte["a3"] = verte["a3"] + 2


    if (poziciju_sarasas["a1"] == "0" or poziciju_sarasas["a3"] == "0") and (poziciju_sarasas["a1"] != "X" and poziciju_sarasas["a2"] != "X" and poziciju_sarasas["a3"] != "X"):

        verte["a1"] = verte["a1"] + 5
        verte["a2"] = verte["a2"] + 3
        verte["a3"] = verte["a3"] + 5

    if (poziciju_sarasas["c1"] == "0" or poziciju_sarasas["c3"] == "0") and (poziciju_sarasas["c1"] != "X" and poziciju_sarasas["c2"] != "X" and poziciju_sarasas["c3"] != "X"):

        verte["c1"] += 5
        verte["c2"] += 3
        verte["c3"] += 5

    if (poziciju_sarasas["b1"] == "0" or poziciju_sarasas["b3"] == "0") and (poziciju_sarasas["b1"] != "X" and poziciju_sarasas["b2"] != "x" and poziciju_sarasas["b3"] != "X"):

        verte["b1"] += 5
        verte["b3"] += 5

    if (poziciju_sarasas["a1"] == "0" or poziciju_sarasas["c1"] == "0") and (poziciju_sarasas["a1"] != "X" and poziciju_sarasas["b1"] != "X" and poziciju_sarasas["c1"] != "X"):

        verte["a1"] += 5
        verte["b1"] += 2
        verte["c1"] += 5

    if (poziciju_sarasas["a2"] == "0" or poziciju_sarasas["c2"] == "0") and (poziciju_sarasas["a2"] != "X" and poziciju_sarasas["b2"] != "X" and poziciju_sarasas["c2"] != "X"):

        verte["a2"] += 5
        verte["c2"] += 5

    if (poziciju_sarasas["a3"] == "0" or poziciju_sarasas["c3"] == "0") and (poziciju_sarasas["a3"] != "X" and poziciju_sarasas["b3"] != "X" and poziciju_sarasas["c3"] != "X"):

        verte["a3"] += 5
        verte["b3"] += 3
        verte["c3"] += 5

    if poziciju_sarasas["b2"] == "0" and (poziciju_sarasas["a1"] != "X" and poziciju_sarasas["c3"] != "X"):

        verte["a1"] += 5
        verte["c3"] += 5

    if poziciju_sarasas["b2"] == "0" and (poziciju_sarasas["a3"] != "X" and poziciju_sarasas["c1"] != "X"):

        verte["a3"] += 5
        verte["c1"] += 5

    if ((poziciju_sarasas["a1"] == "X" or poziciju_sarasas["a3"] == "X") and poziciju_sarasas["a2"] == "X") or (poziciju_sarasas["a1"] == "X" and poziciju_sarasas["a3"] == "X"):

        verte["a1"] += 12
        verte["a2"] += 12
        verte["a3"] += 12

    if ((poziciju_sarasas["b1"] == "X" or poziciju_sarasas["b3"] == "X") and poziciju_sarasas["b2"] == "X") or (poziciju_sarasas["b1"] == "X" and poziciju_sarasas["b3"] == "X"):

        verte["b1"] += 12
        verte["b2"] += 12
        verte["b3"] += 12

    if ((poziciju_sarasas["c1"] == "X" or poziciju_sarasas["c3"] == "X") and poziciju_sarasas["c2"] == "X") or (poziciju_sarasas["c1"] == "X" and poziciju_sarasas["c3"] == "X"):

        verte["c1"] += 12
        verte["c2"] += 12
        verte["c3"] += 12

    if ((poziciju_sarasas["a1"] == "X" or poziciju_sarasas["c1"] == "X") and poziciju_sarasas["b1"] == "X") or (poziciju_sarasas["a1"] == "X" and poziciju_sarasas["c1"] == "X"):

        verte["a1"] += 12
        verte["b1"] += 12
        verte["c1"] += 12

    if ((poziciju_sarasas["a2"] == "X" or poziciju_sarasas["c2"] == "X") and poziciju_sarasas["b2"] == "X") or (
            poziciju_sarasas["a2"] == "X" and poziciju_sarasas["c2"] == "X"):

        verte["a2"] += 12
        verte["b2"] += 12
        verte["c2"] += 12

    if ((poziciju_sarasas["a3"] == "X" or poziciju_sarasas["c3"] == "X") and poziciju_sarasas["b3"] == "X") or (
            poziciju_sarasas["a3"] == "X" and poziciju_sarasas["c3"] == "X"):

        verte["a3"] += 12
        verte["b3"] += 12
        verte["c3"] += 12

    if poziciju_sarasas["b2"] == "X" and (poziciju_sarasas["a1"] == "X" or poziciju_sarasas["c3"] == "X"):

        verte["a1"] += 12
        verte["c3"] += 12

    if poziciju_sarasas["b2"] == "X" and (poziciju_sarasas["a3"] == "X" or poziciju_sarasas["c1"] == "X"):

        verte["a3"] += 12
        verte["c1"] += 12

    if (poziciju_sarasas["a1"] == "0" and poziciju_sarasas["c1"] == "0") and poziciju_sarasas["b1"] != "X":

        verte["b1"] += 30

    if (poziciju_sarasas["a3"] == "0" and poziciju_sarasas["c3"] == "0") and poziciju_sarasas["b3"] != "X":

        verte["b3"] += 30

    if (poziciju_sarasas["a1"] == "0" and poziciju_sarasas["a3"] == "0") and poziciju_sarasas["a2"] != "X":

        verte["a2"] += 30

    if (poziciju_sarasas["c1"] == "0" and poziciju_sarasas["c3"] == "0") and poziciju_sarasas["c2"] != "X":

        verte["c2"] += 30


def pries_zmogu():            #pats žaidimas, antras žaidėjas žmogus
    while nera_laimetojo:
        tikrink(pozicijos)
        zaidimo_pradzia()
        if len(uzimti) % 2 == 0:
            tikrink(pozicijos)
            input_a = input("X ėjimas: ")
            if input_a == "end":
                pagrindinis_meniu()
                break
            elif input_a not in pozicijos.keys():
                print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
            elif pozicijos[input_a] == "X" or pozicijos[input_a] == "0":
                print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
            else:
                pozicijos[input_a] = "X"
                uzimti.append(input_a)
        elif nera_laimetojo:
            tikrink(pozicijos)
            input_a = input("0 ėjimas: ")
            if input_a == "end":
                pagrindinis_meniu()
                break
            elif input_a not in pozicijos.keys():
                print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
            elif pozicijos[input_a] == "X" or pozicijos[input_a] == "0":
                print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
            else:
                pozicijos[input_a] = "0"
                uzimti.append(input_a)
        else:
            break

def pries_kompiuteri():      #pats žaidimas, antras žaidėjas normalaus sunkumo kompiuteris
    while nera_laimetojo:
        tikrink(pozicijos)
        #print(verte)
        if len(uzimti) % 2 == 0:
            zaidimo_pradzia()
            vertes_tikrinimas(verte, pozicijos)
            input_a = input("X ėjimas: ")
            if input_a == "end":
                pagrindinis_meniu()
                break
            elif input_a not in pozicijos.keys():
                print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
            elif pozicijos[input_a] == "X" or pozicijos[input_a] == "0":
                print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")
            else:
                uzimti.append(input_a)
                verte[input_a] = 0
                pozicijos[input_a] = "X"

        elif nera_laimetojo:
            tikrink(pozicijos)
            vertes_tikrinimas(verte, pozicijos)
            pasirinkimas1 = pasirinkimas(verte)
            uzimti.append(pasirinkimas1)
            print(f"Kompiuterio ėjimas: {pasirinkimas1}")
            pozicijos[pasirinkimas1] = "0"
            verte[pasirinkimas1] = 0
        else:
            break

def pries_lengvakomp():     #pats žaidimas, antras žaidėjas lengvo sunkumo (atsitiktinis) kompiuteris
    while nera_laimetojo:
        tikrink(pozicijos)
        zaidimo_pradzia()
        vertes_tikrinimas(verte, pozicijos)

        if len(uzimti) % 2 == 0:
            input_a = input("X ėjimas: ")
            if input_a == "end":
                pagrindinis_meniu()
                break

            elif input_a not in pozicijos.keys():

                print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")

            elif pozicijos[input_a] == "X" or pozicijos[input_a] == "0":

                print(f"Jūs pasirinkote: {input_a}, tai nėra tinkamas variantas")

            else:
                uzimti.append(input_a)
                verte[input_a] = 0
                pozicijos[input_a] = "X"

        elif nera_laimetojo:
            tikrink(pozicijos)
            vertes_tikrinimas(verte, pozicijos)
            pasirinkimas2 = lengvas_pasirinkimas(verte)
            uzimti.append(pasirinkimas2)
            pozicijos[pasirinkimas2] = "0"
            verte[pasirinkimas2] = 0

        else:
            break



pagrindinis_meniu()
