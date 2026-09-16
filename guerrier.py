from personnage import personnage

class guerrier(personnage):
    def __init__(self, pseudo: str, niveau: int = 1):
        if niveau == 1:
            calcul_pv = 1 * 8 + 4
            calcul_init = 1 * 4 + 6
            super().__init__(pseudo, 1, calcul_pv, calcul_init)
        else:
            calcul_pv = niveau * 8 + 4
            calcul_init = niveau * 4 + 6
            super().__init__(pseudo, niveau, calcul_pv, calcul_init)

    def degats(self) -> int:
        return self.niveau * 2