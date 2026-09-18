class personnage:
    def __init__(self, pseudo: str, niveau: int = 1, pv: int = None, initiative: int = None):
        if not isinstance(pseudo, str) or len(pseudo) == 0:
            raise ValueError("pseudo invalide")
        if niveau < 1:
            raise ValueError("niveau invalide")

        self.__pseudo = pseudo
        self.__niveau = niveau

        
        self.__pv = niveau if pv is None else pv
        self.__initiative = niveau if initiative is None else initiative

    @property
    def pseudo(self) -> str:
        return self.__pseudo

    @property
    def niveau(self) -> int:
        return self.__niveau

    @property
    def pv(self) -> int:
        return self.__pv

    @pv.setter
    def pv(self, valeur: int):
        self.__pv = valeur

    @property
    def initiative(self) -> int:
        return self.__initiative

    def degats(self) -> int:
        return self.__niveau

    def attaque(self, autre):
        if self.__initiative > autre.initiative:
            autre.pv -= self.degats()
            if autre.pv > 0: self.pv -= autre.degats()
        elif autre.initiative > self.__initiative:
            self.pv -= self.degats()
            if self.pv > 0: autre.pv -= self.degats()
        else:
            autre.pv -= self.degats()
            self.pv -= self.degats()

    def soigner(self):
        self.__pv = self.__niveau

    def combat(self, autre):
        while self.__pv > 0 and autre.pv > 0:
            self.attaque(autre)
            print(f"{self.__pseudo} (pv: {self.__pv}) vs {autre.pseudo} (pv: {autre.pv})")

    
    def __eq__(self, autre) -> bool:
        if isinstance(autre, personnage): return self.__pseudo == autre.pseudo
        return False

    def __str__(self) -> str:
        return f"personnage:[{self.__pseudo}; niv:{self.__niveau}; pv:{self.__pv}; init:{self.__initiative}]"
