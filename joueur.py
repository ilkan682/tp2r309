from personnage import personnage

class joueur:
    def __init__(self, nom: str, max_perso: int):
        if not isinstance(nom, str) or max_perso <= 0:
            raise ValueError("parametres joueur invalides")
        self.__nom = nom
        self.__max_perso = max_perso
        self.__personnages = []

    @property
    def nom(self) -> str:
        return self.__nom

    def ajouterpersonnage(self, p: personnage) -> bool:
        if len(self.__personnages) < self.__max_perso:
            self.__personnages.append(p)
            return True
        return False

    def getpersonnagenumero(self, index: int) -> personnage:
        return self.__personnages[index]

    def getpersonnagepseudo(self, pseudo: str) -> personnage:
        for p in self.__personnages:
            if p.pseudo == pseudo:
                return p
        return None

    def getpersonnageobjet(self, persomal) -> personnage:
        for p in self.__personnages:
            if p == persomal:
                return p
        return None

    def supprimerpersonnagenumero(self, index: int):
        if 0 <= index < len(self.__personnages):
            self.__personnages.pop(index)

    def supprimerpersonnagepseudo(self, pseudo: str):
        for p in self.__personnages:
            if p.pseudo == pseudo:
                self.__personnages.remove(p)
                break

    def supprimerpersonnageobjet(self, persomal):
        if persomal in self.__personnages:
            self.__personnages.remove(persomal)