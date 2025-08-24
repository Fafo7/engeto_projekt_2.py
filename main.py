"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Filip Trepáň
email: filip.trepan@gmail.com
"""
import time
import random
oddelovac = "=" * 30

def generuj_cislo() -> str:
    """Generuje náhodné 4-místné číslo jako řetězec."""
    cislice = random.sample("0123456789", 4)
    if cislice[0] == "0":  # Zajistí, že první číslice není nula
        # Aktualizace: prohodí první dvě číslice
        cislice[0], cislice[1] = cislice[1], cislice[0]
    return ''.join(cislice)

def kontrola_vstupu(uzivatel) -> bool:
    """Zkontroluje, zda uživatel zadal platné číslo."""
    if not uzivatel.isdigit():
        print("Zadejte celé číslo.")
        return False
    if len(uzivatel) != 4:
        print("Číslo musí mít čtyři cifry.")
        return False
    if uzivatel[0] == "0":
        print("Číslo nesmí začínat nulou.")
        return False
    if len(set(uzivatel)) != len(uzivatel):
        print("Číslo nesmí obsahovat opakující se cifry.")
        return False
    return True

def bulls(hadane_cislo: str, uzivatel: str) -> int:
    """Zkontroluje, kolik čísel je správně na správném místě.
    """
    hadane = str(hadane_cislo)
    uzivatel = str(uzivatel)
    spravne_na_mieste = sum(
        1 for i in range(min(len(hadane), 
                             len(uzivatel))) if hadane[i] == uzivatel[i])
    return spravne_na_mieste

def cows(hadane_cislo: str, uzivatel: str) -> int:
    """Zkontroluje, kolik čísel je správně, ale nemusí být na správném místě.
    """
    hadane = str(hadane_cislo)
    uzivatel = str(uzivatel)
    spravne_cislo = sum(
        min(hadane.count(c), uzivatel.count(c)) for c in set(uzivatel))
    return spravne_cislo

def vypis_vysledku(spravne_na_mieste: int, spravne_cislo: int) -> None:
    """Vypíše výsledek kontroly.
        bull = správné číslo na správném místě
        cow = správné číslo, ale na špatném místě"""
    print(
        f"{spravne_na_mieste} bull" + ("s" if spravne_na_mieste != 1 else ""),
        f"{spravne_cislo} cow" + ("s" if spravne_cislo != 1 else ""), sep=", "
    )

# Úvodní zpráva
print("Hi there!")
print(oddelovac)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(oddelovac)

# Hlavní herní smyčka
while True:
    # Generování náhodného čísla a počítadlo pokusů
    hadane_cislo = generuj_cislo()
    pokusy = 0
    start_time = time.time()
    # Debug: odkomentujte následující řádek pro zobrazení hádaného čísla
    # print(hadane_cislo)  
    uzivatel = input("Enter a 4-digit number: ")

    while True:
        if not kontrola_vstupu(uzivatel):
            uzivatel = input("Zadej platné číslo: ")
            continue

        pokusy += 1
        bull_count = bulls(hadane_cislo, uzivatel)
        cow_count = cows(hadane_cislo, uzivatel) - bull_count
        vypis_vysledku(bull_count, cow_count)
        # Kontrola, zda uživatel uhodl číslo
        if bull_count == 4:
            end_time = time.time()
            total_time = end_time - start_time
            minuty, sekundy = divmod(total_time, 60)
            print(oddelovac)
            print(
                f"Correct, you've guessed the right number {hadane_cislo}\n"
                f"in {pokusy} guesses!"
            )
            print(
                f"Time taken: {int(minuty)} minute" + ("s" if minuty != 1 else ""),  
                f"and {int(sekundy)} second" + ("s" if sekundy != 1 else "")                
            )
            print(oddelovac)
            print("That's amazing!")
            break
        else:
            print(oddelovac)
            uzivatel = input(">>> ")
    # Hra pokračuje, dokud uživatel nechce skončit
    while True:
        nova_hra = input("Do you want to play again? (y/n): ").lower()
        if nova_hra in ('y', 'n'):
            break
        print("Please enter 'y' for yes or 'n' for no.")    
    if nova_hra != 'y':
        print("Thank you for playing! Goodbye!")
        break