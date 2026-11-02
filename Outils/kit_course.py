"""Pièces du jeu de course : barrière de ville et portique de départ."""
from pathlib import Path

from geo import Maille

SORTIE = Path(r"E:\Minecraft\Claude Unreal Engine\PalmeraBay\Art\Modeles\Mobilier")
ROUGE = (0.7, 0.04, 0.04)
BLANC = (0.86, 0.85, 0.82)
NOIR = (0.03, 0.03, 0.035)


def barriere():
    """Dix-huit mètres de blocs de béton peints en rouge et blanc, le long de X."""
    m = Maille()
    for i in range(6):
        x0 = -9.0 + i * 3.0
        couleur = ROUGE if i % 2 == 0 else BLANC
        m.boite("peint", x0 + 0.03, x0 + 2.97, -0.42, 0.42, 0.0, 0.22, 1.0, "xXyYZ", couleur)
        m.boite("peint", x0 + 0.03, x0 + 2.97, -0.24, 0.24, 0.22, 1.05, 1.0, "xXyYZ", couleur)
    return m


def arche():
    """Portique au-dessus de la route, avec un damier d'arrivée (la route suit Y local)."""
    m = Maille()
    for x in (-9.2, 9.2):
        m.boite("metal", x - 0.22, x + 0.22, -0.22, 0.22, 0.0, 6.4)
    m.boite("metal", -9.4, 9.4, -0.3, 0.3, 6.0, 6.5)
    for i in range(24):
        for j in range(3):
            couleur = BLANC if (i + j) % 2 == 0 else NOIR
            x0 = -9.0 + i * 0.75
            m.boite("peint", x0, x0 + 0.75, -0.32, 0.32, 6.5 + j * 0.3, 6.8 + j * 0.3, 1.0, "yY", couleur)
    # Damier au sol, légèrement au-dessus de la chaussée
    for i in range(20):
        for j in range(4):
            couleur = BLANC if (i + j) % 2 == 0 else NOIR
            x0 = -8.0 + i * 0.8
            y0 = -0.8 + j * 0.4
            m.boite("peint", x0, x0 + 0.8, y0, y0 + 0.4, 0.0, 0.015, 1.0, "Z", couleur)
    return m


if __name__ == "__main__":
    for nom, m in {"SM_Barriere": barriere(), "SM_Arche": arche()}.items():
        m.ecrire_glb(SORTIE / f"{nom}.glb")
        print(nom, m.triangles(), flush=True)
