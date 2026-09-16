from personnage import personnage

class mage(personnage):
    def __init__(self, pseudo: str, niveau: int = 1):
        if niveau == 1:
            calcul_pv = 1 * 5 + 10
            calcul_init = 1 * 6 + 4
            self.__mana = 1 * 5
            super().__init__(pseudo, 1, calcul_pv, calcul_init)
        else:
            calcul_pv = niveau * 5 + 10
            calcul_init = niveau * 6 + 4
            self.__mana = niveau * 5
            super().__init__(pseudo, niveau, calcul_pv, calcul_init)

    @property
    def mana(self) -> int:
        return self.__mana

    @mana.setter
    def mana(self, m: int):
        self.__mana = m

    def degats(self) -> int:
        if self.__mana >= 4:
            self.__mana -= 4
            return self.niveau + 3
        else:
            return self.niveau