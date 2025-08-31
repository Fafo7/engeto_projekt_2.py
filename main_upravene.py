"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Filip Trepáň
email: filip.trepan@gmail.com
"""
import time
import random

oddelovac = "=" * 30


def generuj_cislo() -> str:
    """Generuje náhodné 4-místné číslo (řetězec bez opakování číslic)."""
    cislice = random.sample("0123456789", 4)
    if cislice[0] == "0":  # zajistí, že první číslice není nula
        cislice[0], cislice[1] = cislice[1], cislice[0]
    return ''.join(cislice)


def kontrola_vstupu(uzivatel: str) -> bool:
    """
    Ověří, zda uživatel zadal platné 4místné číslo:
    - pouze číslice,
    - délka 4,
    - nezačíná nulou,
    - neobsahuje opakující se číslice.
    """
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
    """Vrátí počet číslic na správném místě (bulls)."""
    return sum(1 for h, u in zip(hadane_cislo, uzivatel) if h == u)


def cows(hadane_cislo: str, uzivatel: str) -> int:
    """Vrátí počet číslic, které se shodují, ale nejsou na správném místě (cows)."""
    return sum(
        min(hadane_cislo.count(c), uzivatel.count(c)) for c in set(uzivatel)
    )


def vypis_vysledku(spravne_na_mieste: int, spravne_cislo: int) -> None:
    """Vypíše počet bulls a cows oddělený čárkou."""
    print(
        f"{spravne_na_mieste} bull" + ("s" if spravne_na_mieste != 1 else ""),
        f"{spravne_cislo} cow" + ("s" if spravne_cislo != 1 else ""), sep=", "
    )


def hraj_jednu_hru():
    """Spustí jednu hru Bulls and Cows včetně počítadla pokusů a času."""
    hadane_cislo = generuj_cislo()
    pokusy = 0
    start_time = time.time()
    # print(hadane_cislo)  # DEBUG: zobrazí hádané číslo

    uzivatel = input("Enter a 4-digit number: ")

    while True:
        if not kontrola_vstupu(uzivatel):
            uzivatel = input("Zadej platné číslo: ")
            continue

        pokusy += 1
        bull_count = bulls(hadane_cislo, uzivatel)
        cow_count = cows(hadane_cislo, uzivatel) - bull_count
        vypis_vysledku(bull_count, cow_count)

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


def main():
    """Spustí úvodní zprávu a řídí hlavní smyčku hry."""
    print("Hi there!")
    print(oddelovac)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(oddelovac)

    while True:
        hraj_jednu_hru()
        nova_hra = input("Do you want to play again? (y/n): ").lower()
        if nova_hra != 'y':
            print("Thank you for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()