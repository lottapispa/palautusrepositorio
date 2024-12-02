import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    joukko.lisaa_alkio(1)
    joukko.lisaa_alkio(2)
    joukko.lisaa_alkio(3)
    joukko.lisaa_alkio(2)

    print(joukko.muuta_lista_kokonaisluvuiksi())


if __name__ == "__main__":
    main()
