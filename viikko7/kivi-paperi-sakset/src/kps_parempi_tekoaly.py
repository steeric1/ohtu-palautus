from kps_tekoaly import KPSTekoaly
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPSTekoaly):
    def __init__(self):
        self._tekoaly = TekoalyParannettu(10)
        self._tekoalyn_siirto = None

    def _toisen_siirto(self, ekan_siirto):
        on_ensimmainen_siirto = self._tekoalyn_siirto is None
        self._tekoalyn_siirto = self._tekoaly.anna_siirto()
        
        if not on_ensimmainen_siirto:
            self._tekoaly.aseta_siirto(ekan_siirto)

        return self._tekoalyn_siirto
