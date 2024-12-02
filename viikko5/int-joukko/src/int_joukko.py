class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.joukko = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluuko_alkio_joukkoon(self, alkio):
        maara = 0

        for luku in range(0, self.alkioiden_lkm):
            if alkio == self.joukko[luku]:
                maara += 1

        if maara > 0:
            return True
        else:
            return False

    def lisaa_alkio(self, alkio):
        if self.alkioiden_lkm == 0:
            self.joukko[0] = alkio
            self.alkioiden_lkm += 1
            return True
        else:
            pass

        if not self.kuuluuko_alkio_joukkoon(alkio):
            self.joukko[self.alkioiden_lkm] = alkio
            self.alkioiden_lkm += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.joukko) == 0:
                vanha_taulukko = self.joukko
                self.kopioi_lista(self.joukko, vanha_taulukko)
                self.joukko = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(vanha_taulukko, self.joukko)

            return True

        return False

    def poista_alkio(self, alkio):
        indeksi = -1
        temp_luku = 0

        for luku in range(0, self.alkioiden_lkm):
            if alkio == self.joukko[luku]:
                indeksi = luku
                self.joukko[indeksi] = 0
                break

        if indeksi != -1:
            for luku_2 in range(indeksi, self.alkioiden_lkm - 1):
                temp_luku = self.joukko[luku_2]
                self.joukko[luku_2] = self.joukko[luku_2 + 1]
                self.joukko[luku_2 + 1] = temp_luku

            self.alkioiden_lkm -= 1
            return True

        return False

    def kopioi_lista(self, lista_a, lista_b):
        for luku in range(0, len(lista_a)):
            lista_b[luku] = lista_a[luku]

    def listan_koko(self):
        return self.alkioiden_lkm

    def muuta_lista_kokonaisluvuiksi(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for luku in range(0, len(taulu)):
            taulu[luku] = self.joukko[luku]

        return taulu

    @staticmethod
    def yhdiste(lista_a, lista_b):
        joukko = IntJoukko()
        a_taulu = lista_a.muuta_lista_kokonaisluvuiksi()
        b_taulu = lista_b.muuta_lista_kokonaisluvuiksi()

        for luku in range(0, len(a_taulu)):
            joukko.lisaa_alkio(a_taulu[luku])

        for luku_2 in range(0, len(b_taulu)):
            joukko.lisaa_alkio(b_taulu[luku_2])

        return joukko

    @staticmethod
    def leikkaus(lista_a, lista_b):
        joukko = IntJoukko()
        a_taulu = lista_a.muuta_lista_kokonaisluvuiksi()
        b_taulu = lista_b.muuta_lista_kokonaisluvuiksi()

        for luku in range(0, len(a_taulu)):
            for luku_2 in range(0, len(b_taulu)):
                if a_taulu[luku] == b_taulu[luku_2]:
                    joukko.lisaa_alkio(b_taulu[luku_2])

        return joukko

    @staticmethod
    def erotus(lista_a, lista_b):
        joukko = IntJoukko()
        a_taulu = lista_a.muuta_lista_kokonaisluvuiksi()
        b_taulu = lista_b.muuta_lista_kokonaisluvuiksi()

        for luku in range(0, len(a_taulu)):
            joukko.lisaa_alkio(a_taulu[luku])

        for luku in range(0, len(b_taulu)):
            joukko.poista_alkio(b_taulu[luku])

        return joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.joukko[0]) + "}"
        else:
            tulostus = "{"
            for luku in range(0, self.alkioiden_lkm - 1):
                tulostus += str(self.joukko[luku])
                tulostus += ", "
            tulostus += str(self.joukko[self.alkioiden_lkm - 1])
            tulostus += "}"
            return tulostus
