import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from guerrier import guerrier
from mage import mage
from joueur import joueur

if __name__ == "__main__":
    try:
        print("--- test du combat entre classes heritees ---")
        g1 = guerrier("ilkan", 3)
        m1 = mage("lucas", 3)

        print(g1)
        print(m1)

        print("\ndebut du combat :")
        g1.combat(m1)

        print("\n--- test de la classe joueur ---")
        j1 = joueur("mama", 3)
        j1.ajouterpersonnage(g1)
        j1.ajouterpersonnage(m1)

        # C'est ici qu'il fallait changer "gandalf" par "lucas" !
        trouve = j1.getpersonnagepseudo("lucas")
        print("personnage trouve par pseudo :", trouve)

    except Exception as e:
        print("erreur detectee :", e)
    else:
        print("\nfin du programme")