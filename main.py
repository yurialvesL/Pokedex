import sys
from poke import *
from PyQt5.QtWidgets import QApplication

qt = QApplication(sys.argv)
poke = Pokedex()
poke.poke_Type(152)
poke.poke_description(152)
poke.abilities_poke(152)
poke.show()
sys.exit(qt.exec())

