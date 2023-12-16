import random
import sys




def pagrindinis_meniu():  # pagrindinis meniu
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


uzimti = []     # uzimti sąrašas - tie langeliai kurie užimti žaidimo metu


def zaidimo_pradzia():  # žaidimo vizualizacija

    return print("", "   ", "1", "2", "3", "\n", " ", "/-------", "\n", "A", "|", pozicijos["a1"], pozicijos["a2"],
                 pozicijos["a3"],
                 "\n", "B", "|", pozicijos["b1"], pozicijos["b2"], pozicijos["b3"], "\n", "C", "|", pozicijos["c1"],
                 pozicijos["c2"], pozicijos["c3"])


w1 = {"a1": "*", "a2": "*", "a3": "*"}  #w1-w8 yra "win conditions", naudojami apskaičiuoti normalaus AI ėjimus
w2 = {"b1": "*", "b2": "*", "b3": "*"}
w3 = {"c1": "*", "c2": "*", "c3": "*"}
w4 = {"a1": "*", "c1": "*", "b1": "*"}
w5 = {"a2": "*", "b2": "*", "c2": "*"}
w6 = {"a3": "*", "b3": "*", "c3": "*"}
w7 = {"a1": "*", "b2": "*", "c3": "*"}
w8 = {"a3": "*", "b2": "*", "c1": "*"}
ww = {1: w1, 2: w2, 3: w3, 4: w4, 5: w5, 6: w6, 7: w7, 8: w8}


verte = {"a1": 2,  # pradinės vertės; vidurinis > kampiniai > visi kiti
         "a2": 1,
         "a3": 2,
         "b1": 1,
         "b2": 5,
         "b3": 1,
         "c1": 2,
         "c2": 1,
         "c3": 2}

pozicijos = {"a1": "*",     #pozicijų sąrašas, naudojamas ir vizualizacijai, ir kitur
             "a2": "*",
             "a3": "*",
             "b1": "*",
             "b2": "*",
             "b3": "*",
             "c1": "*",
             "c2": "*",
             "c3": "*"}

laimejimai = {"X": 0,       #laimėjimu sekimas
              "0": 0}



def nuline_poz():  # žaidimo nulinė pozicija, naudojama tada kai žaidimas baigiasi, prieš pradedant dar vieną žaidimą
    global verte
    global pozicijos
    global uzimti
    global w1, w2, w3, w4, w5, w6, w7, w8
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

    for x in ww.keys():
        for key in ww[x].keys():
            ww[x][key] = "*"

    w1 = {"a1": "*", "a2": "*", "a3": "*"}
    w2 = {"b1": "*", "b2": "*", "b3": "*"}
    w3 = {"c1": "*", "c2": "*", "c3": "*"}
    w4 = {"a1": "*", "c1": "*", "b1": "*"}
    w5 = {"a2": "*", "b2": "*", "c2": "*"}
    w6 = {"a3": "*", "b3": "*", "c3": "*"}
    w7 = {"a1": "*", "b2": "*", "c3": "*"}
    w8 = {"c3": "*", "b2": "*", "a1": "*"}



def tikrink(pozicijos):  # tikrina ar laimėta, ar lygiosios ir pnš

    ivedimai = len(uzimti)

    if (pozicijos["a1"] == pozicijos["a2"] == pozicijos["a3"]) and (pozicijos["a3"] != "*"):
        print(f"{pozicijos["a1"]} laimėjo!")
        laimejimai[pozicijos["a1"]] += 1
        zaidimo_pradzia()
        pagrindinis_meniu()
    elif (pozicijos["b1"] == pozicijos["b2"] == pozicijos["b3"]) and (pozicijos["b3"] != "*"):
        print(f"{pozicijos["b1"]} laimėjo!")
        laimejimai[pozicijos["b1"]] += 1
        zaidimo_pradzia()
        pagrindinis_meniu()
    elif (pozicijos["c1"] == pozicijos["c2"] == pozicijos["c3"]) and (pozicijos["c3"] != "*"):
        print(f"{pozicijos["c1"]} laimėjo!")
        laimejimai[pozicijos["c1"]] += 1
        zaidimo_pradzia()
        pagrindinis_meniu()
    elif (pozicijos["a1"] == pozicijos["b2"] == pozicijos["c3"]) and (pozicijos["c3"] != "*"):
        print(f"{pozicijos["a1"]} laimėjo!")
        laimejimai[pozicijos["a1"]] += 1
        zaidimo_pradzia()
        pagrindinis_meniu()
    elif (pozicijos["a3"] == pozicijos["b2"] == pozicijos["c1"]) and (pozicijos["c1"] != "*"):
        print(f"{pozicijos["c1"]} laimėjo!")
        laimejimai[pozicijos["c1"]] += 1
        zaidimo_pradzia()
        pagrindinis_meniu()
    elif (pozicijos["a1"] == pozicijos["b1"] == pozicijos["c1"]) and (pozicijos["c1"] != "*"):
        print(f"{pozicijos["a1"]} laimėjo!")
        laimejimai[pozicijos["a1"]] += 1
        zaidimo_pradzia()
        pagrindinis_meniu()
    elif (pozicijos["a2"] == pozicijos["b2"] == pozicijos["c2"]) and (pozicijos["c2"] != "*"):
        print(f"{pozicijos["a2"]} laimėjo!")
        laimejimai[pozicijos["a2"]] += 1
        zaidimo_pradzia()
        pagrindinis_meniu()
    elif (pozicijos["a3"] == pozicijos["b3"] == pozicijos["c3"]) and (pozicijos["b3"] != "*"):
        print(f"{pozicijos["a3"]} laimėjo!")
        laimejimai[pozicijos["a3"]] += 1
        zaidimo_pradzia()
        pagrindinis_meniu()
    elif (pozicijos["a1"] != pozicijos["a3"]) and (pozicijos["a1"] != pozicijos["c3"]) and (
            pozicijos["a1"] != pozicijos["c1"]) and (pozicijos["a2"] != pozicijos["c2"]) and (
            pozicijos["b1"] != pozicijos["b3"]) and (pozicijos["c1"] != pozicijos["c3"]) and (
            pozicijos["a3"] != pozicijos["c3"]) and (pozicijos["c1"] != pozicijos["a3"]):
        print("Laimėti neįmanoma!!!")
        zaidimo_pradzia()
        pagrindinis_meniu()
    elif ivedimai == 9:
        print("Niekas nelaimėjo, visi langeliai išnaudoti!")
        zaidimo_pradzia()
        pagrindinis_meniu()


def pasirinkimas(vertes_sarasas):  # normalaus sunkumo AI pasirinkimas iš vertės sąrašo
    maxverte = max(vertes_sarasas.values())
    for key, value in vertes_sarasas.items():
        if value == maxverte:
            return key


def lengvas_pasirinkimas(
        vertes_sarasas):  # lengvo sunkumo AI pasirinkimas, irgi iš vertės sąrašo, bet neatsižvelgiant į pačią vertę, o tik į tai kokie žingsniai yra galimi
    galimi_variantai = []
    for key, value in vertes_sarasas.items():
        if value > 0:
            galimi_variantai.append(key)
    l_pasirinkimas = random.choice(galimi_variantai)
    return l_pasirinkimas

def vertes_korekcija(kas_eina, ejimas): # v2 normalaus lygio AI, tikrina kuri iš pergalių (win condition) yra artima
    for key, value in verte.items():    # v2 nuo praeito dar skiriasi tuo, kad atsižvelgia į tai kieno ėjimas prieš tai buvo
        if key in uzimti:               # patikra vyksta po X (priešininko) ir po 0 (kompiuterio) ėjimų
            verte[key] = -1000

    if list(pozicijos.values()).count("X") > list(pozicijos.values()).count("0"):
        for num in range(1, 9):
            if ejimas in ww[num]:
                ww[num][ejimas] = kas_eina
            if (list(ww[num].values()).count("X") > 1) and (list(ww[num].values()).count("0") == 0):
                temp_w = ww[num].copy()
                for key, value in temp_w.items():
                    # print(f"mano ejimas, radau du X, pridedu 200 prie {verte[key]}")
                    verte[key] += 200

    if list(pozicijos.values()).count("X") == list(pozicijos.values()).count("0"):
        for num in range(1, 9):
            if ejimas in ww[num]:
                ww[num][ejimas] = kas_eina
            if (list(ww[num].values()).count("0") > 1) and (list(ww[num].values()).count("X") == 0):
                temp_w = ww[num].copy()
                for key, value in temp_w.items():
                    # print(f"prieso ejimas, radau du 0, pridedu 200 prie {verte[key]}")
                    verte[key] += 200


    for num in range(1,9):
        if ejimas in ww[num]:
            ww[num][ejimas] = kas_eina
        if (list(ww[num].values()).count("0") > 1) and (list(ww[num].values()).count("X") == 0):
            temp_w = ww[num].copy()
            for key, value in temp_w.items():
                # print(f"radau du 0, pridedu 20 prie {verte[key]}")
                verte[key] += 20

        if (list(ww[num].values()).count("X") > 1) and (list(ww[num].values()).count("0") == 0):
            temp_w = ww[num].copy()
            for key, value in temp_w.items():
                # print(f"radau du X, pridedu 10 prie {verte[key]}")
                verte[key] += 10

        if (list(ww[num].values()).count("0") > 0) and (list(ww[num].values()).count("X") == 0):
            temp_w = ww[num].copy()
            for key, value in temp_w.items():
                # print(f"radau 0, pridedu 3 prie {verte[key]}")
                verte[key] += 3

        if (list(ww[num].values()).count("0") > 0) and (list(ww[num].values()).count("X") == 1):
            temp_w = ww[num].copy()
            for key, value in temp_w.items():
                verte[key] -= 1


def lengvojo_verte(verte):  #naudojamas lengvojo sunkumo AI ėjimams nuspręsti
    for key, value in verte.items():
        if key in uzimti:
            verte[key] = -1000



def pries_zmogu():  # pats žaidimas, antras žaidėjas žmogus
    while True:
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
        else:
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



def pries_kompiuteri():  # pats žaidimas, antras žaidėjas normalaus sunkumo kompiuteris
    while True:
        tikrink(pozicijos)
        # print(verte)
        if len(uzimti) % 2 == 0:
            zaidimo_pradzia()
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
                vertes_korekcija("X", input_a)

        else:
            tikrink(pozicijos)
            pasirinkimas1 = pasirinkimas(verte)
            uzimti.append(pasirinkimas1)
            print(f"Kompiuterio ėjimas: {pasirinkimas1}")
            pozicijos[pasirinkimas1] = "0"
            verte[pasirinkimas1] = 0
            vertes_korekcija("0", pasirinkimas1)



def pries_lengvakomp():  # pats žaidimas, antras žaidėjas lengvo sunkumo (atsitiktinis) kompiuteris
    while True:
        tikrink(pozicijos)
        lengvojo_verte(verte)

        if len(uzimti) % 2 == 0:
            zaidimo_pradzia()
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

        else:
            tikrink(pozicijos)
            lengvojo_verte(verte)
            pasirinkimas2 = lengvas_pasirinkimas(verte)
            print(f"Kompiuterio ėjimas: {pasirinkimas2}")
            uzimti.append(pasirinkimas2)
            pozicijos[pasirinkimas2] = "0"
            verte[pasirinkimas2] = 0


pagrindinis_meniu()
