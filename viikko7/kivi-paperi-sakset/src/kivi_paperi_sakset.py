from tuomari import Tuomari


class KiviPaperiSakset:
    def pelaa(self):
        self._tuomari = Tuomari()

        while self._vuoro():            
            print(self._tuomari)

        print("Kiitos!")
        print(self._tuomari)

    def _vuoro(self):
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
        self._viimeistele_vuoro()
        
        return self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ekan_siirto):
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

    def _viimeistele_vuoro(self):
        pass

