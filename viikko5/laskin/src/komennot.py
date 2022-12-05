class Summa:
    def __init__(self, sovellus, syote_funktio):
        self._sovellus = sovellus
        self._syote_funktio = syote_funktio

    def suorita(self):
        try:
            syote = int(self._syote_funktio())
        except:
            return

        self._sovellus.plus(syote)

class Erotus:
    def __init__(self, sovellus, syote_funktio):
        self._sovellus = sovellus
        self._syote_funktio = syote_funktio

    def suorita(self):
        try:
            syote = int(self._syote_funktio())
        except:
            return

        self._sovellus.miinus(syote)
        
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