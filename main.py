import sys
from poke import *
from PyQt5.QtWidgets import QApplication

qt = QApplication(sys.argv)
poke = Pokedex()
poke.poke_Type(1)
poke.poke_description(1)
poke.abilities_poke(1)
poke.show()
sys.exit(qt.exec())

