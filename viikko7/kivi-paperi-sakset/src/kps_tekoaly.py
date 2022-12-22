from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly import Tekoaly


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self._tekoaly = Tekoaly()

    def _toisen_siirto(self, _):
        self._tekoalyn_siirto = self._tekoaly.anna_siirto()
        return self._tekoalyn_siirto

    def _viimeistele_vuoro(self):
        print(f"Tietokone valitsi: {self._tekoalyn_siirto}")
