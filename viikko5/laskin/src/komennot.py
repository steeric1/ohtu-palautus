class BinaariOperaatio:
    def __init__(self, sovellus, syote_funktio, suorita_funktio):
        self._sovellus = sovellus
        self._syote_funktio = syote_funktio
        self._suorita_funktio = suorita_funktio

    def suorita(self):
        try:
            syote = int(self._syote_funktio())
        except:
            return

        self._suorita_funktio(syote)

class Summa(BinaariOperaatio):
    def __init__(self, sovellus, syote_funktio):
        super().__init__(sovellus, syote_funktio, sovellus.plus)

class Erotus(BinaariOperaatio):
    def __init__(self, sovellus, syote_funktio):
        super().__init__(sovellus, syote_funktio, sovellus.miinus)
        
class Nollaus:
    def __init__(self, sovellus):
        self._sovellus = sovellus

    def suorita(self):
        self._sovellus.nollaa()

class Kumoa:
    def __init__(self, sovellus):
        self._sovellus = sovellus

    def suorita(self):
        pass