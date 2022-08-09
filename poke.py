import os
import requests
import pypokedex
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from Template.principal import *


class Pokedex(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_search.clicked.connect(self.search_name)

    def pokeimg(self, id):
        if not os.path.exists('img/'+str(id)+'.png'):
            if id < 10:
                link = f'https://assets.pokemon.com/assets/cms2/img/pokedex/full/00{id}.png'
                f = open(str(id) + ".png", "wb")
                response = requests.get(link)
                f.write(response.content)
                f.close()
                os.rename(str(id)+".png", 'img/'+str(id) + ".png")
            elif id > 9 and id < 100:
                link = f'https://assets.pokemon.com/assets/cms2/img/pokedex/full/0{id}.png'
                f = open(str(id) + ".png", "wb")
                response = requests.get(link)
                f.write(response.content)
                f.close()
                os.rename(str(id) + ".png", 'img/' + str(id) + ".png")
            elif id > 99:
                link = f'https://assets.pokemon.com/assets/cms2/img/pokedex/full/{id}.png'
                f = open(str(id) + ".png", "wb")
                response = requests.get(link)
                f.write(response.content)
                f.close()
                os.rename(str(id) + ".png", 'img/' + str(id) + ".png")

    def poke_Type(self, pokemon):
        if isinstance(pokemon, int):
            type = pypokedex.get(dex=pokemon)
        elif isinstance(pokemon, str):
            type = pypokedex.get(name=pokemon)
        if len(type.types) == 1:
            self.lbl_type1.setText(type.types[0].title())
            self.lbl_type1.setGeometry(130, 50, 131, 61)
            match type.types[0]:
                case 'grass':
                    self.lbl_type1.setStyleSheet('background-color: rgba(154,203,80,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'poison':
                    self.lbl_type1.setStyleSheet('background-color: rgba(185,127,201,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'fire':
                    self.lbl_type1.setStyleSheet('background-color: #fd7d24; padding-bottom:5px; color:white; '
                                                 'border-radius:30px;')
                case 'normal':
                    self.lbl_type1.setStyleSheet('background-color: rgba(164,172,175,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'fighting':
                    self.lbl_type1.setStyleSheet('background-color: #d46622; padding-bottom:5px; color:white; '
                                                 'border-radius:30px;')
                case 'flying':
                    self.lbl_type1.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, '
                                                 'y2:1, stop:0.460227 rgba(60, 195, 235, 255), stop:0.471591 rgba('
                                                 '187, 188, 187, 255)); padding-bottom:5px; color:white; '
                                                 'border-radius:30px;')
                case 'water':
                    self.lbl_type1.setStyleSheet('background-color: #4592c4; padding-bottom:5px; color:white; '
                                                 'border-radius:30px;')
                case 'eletric':
                    self.lbl_type1.setStyleSheet('background-color: rgba(238,213,53,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'rock':
                    self.lbl_type1.setStyleSheet('background-color: rgba(163,140,33,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'bug':
                    self.lbl_type1.setStyleSheet('background-color: rgba(114,159,63,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'psychic':
                    self.lbl_type1.setStyleSheet('background-color: rgba(243,102,185,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'ice':
                    self.lbl_type1.setStyleSheet('background-color: rgba(81,196,231,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'ground':
                    self.lbl_type1.setStyleSheet('background-color: qlineargradient(spread:pad, '
                                                 'x1:0, y1:0, x2:0, y2:1, stop:0.477273 rgba(247, 222, 63, 255), '
                                                 'stop:0.488636 rgba(171, 152, 66, 255)); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'fairy':
                    self.lbl_type1.setStyleSheet('background-color: rgba(253,185,233,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'steel':
                    self.lbl_type1.setStyleSheet('background-color: rgba(158,182,183,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'dragon':
                    self.lbl_type1.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, '
                                                 'y2:1, stop:0.505 rgba(241, 110, 87, 255), stop:0.511364 rgba(83, '
                                                 '164, 207, 255)); padding-bottom:5px;color:white;border-radius:30px;')
                case 'dark':
                    self.lbl_type1.setStyleSheet('background-color: rgba(112,112,112,255); padding-bottom:5px; '
                                                 'border-radius:30px;')
                case 'ghost':
                    self.lbl_type1.setStyleSheet('background-color: rgba(123,98,163,255); padding-bottom:5px; '
                                                 'border-radius:30px;')
                case _:
                    print('error')
            self.lbl_type2.hide()

        elif len(type.types) == 2:
            self.lbl_type1.setText(type.types[0].title())
            match type.types[0]:
                case 'grass':
                    self.lbl_type1.setStyleSheet('background-color: rgba(154,203,80,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'poison':
                    self.lbl_type1.setStyleSheet('background-color: rgba(185,127,201,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'fire':
                    self.lbl_type1.setStyleSheet('background-color: #fd7d24; padding-bottom:5px; color:white; '
                                                 'border-radius:30px;')
                case 'normal':
                    self.lbl_type1.setStyleSheet('background-color: rgba(164,172,175,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'fighting':
                    self.lbl_type1.setStyleSheet('background-color: #d46622; padding-bottom:5px; color:white; '
                                                 'border-radius:30px;')
                case 'flying':
                    self.lbl_type1.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, '
                                                 'y2:1, stop:0.460227 rgba(60, 195, 235, 255), stop:0.471591 rgba('
                                                 '187, 188, 187, 255)); padding-bottom:5px; color:white; '
                                                 'border-radius:30px;')
                case 'water':
                    self.lbl_type1.setStyleSheet('background-color: #4592c4; padding-bottom:5px; color:white; '
                                                 'border-radius:30px;')
                case 'eletric':
                    self.lbl_type1.setStyleSheet('background-color: rgba(238,213,53,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'rock':
                    self.lbl_type1.setStyleSheet('background-color: rgba(163,140,33,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'bug':
                    self.lbl_type1.setStyleSheet('background-color: rgba(114,159,63,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'psychic':
                    self.lbl_type1.setStyleSheet('background-color: rgba(243,102,185,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'ice':
                    self.lbl_type1.setStyleSheet('background-color: rgba(81,196,231,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'ground':
                    self.lbl_type1.setStyleSheet('background-color: background-color: qlineargradient(spread:pad, '
                                                 'x1:0, y1:0, x2:0, y2:1, stop:0.477273 rgba(247, 222, 63, 255), '
                                                 'stop:0.488636 rgba(171, 152, 66, 255)); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'fairy':
                    self.lbl_type1.setStyleSheet('background-color: rgba(253,185,233,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'steel':
                    self.lbl_type1.setStyleSheet('background-color: rgba(158,182,183,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'dragon':
                    self.lbl_type1.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, '
                                                 'y2:1, stop:0.505 rgba(241, 110, 87, 255), stop:0.511364 rgba(83, '
                                                 '164, 207, 255)); padding-bottom:5px;color:white;border-radius:30px;')
                case 'dark':
                    self.lbl_type1.setStyleSheet('background-color: rgba(112,112,112,255); padding-bottom:5px; '
                                                 'border-radius:30px; color: white;')
                case 'ghost':
                    self.lbl_type1.setStyleSheet('background-color: rgba(123,98,163,255); padding-bottom:5px; '
                                                 'border-radius:30px; color: white;')
                case _:
                    print('error')

            self.lbl_type2.setText(type.types[1].title())
            match type.types[1]:
                case 'grass':
                    self.lbl_type2.setStyleSheet('background-color: rgba(154,203,80,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'poison':
                    self.lbl_type2.setStyleSheet('background-color: rgba(185,127,201,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'fire':
                    self.lbl_type2.setStyleSheet('background-color: #fd7d24; padding-bottom:5px; color:white; '
                                                 'border-radius:30px;')
                case 'normal':
                    self.lbl_type2.setStyleSheet('background-color: rgba(164,172,175,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'fighting':
                    self.lbl_type2.setStyleSheet('background-color: #d46622; padding-bottom:5px; color:white; '
                                                 'border-radius:30px;')
                case 'flying':
                    self.lbl_type2.etStyleSheet('background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, '
                                                'y2:1, stop:0.460227 rgba(60, 195, 235, 255), stop:0.471591 rgba('
                                                '187, 188, 187, 255)); padding-bottom:5px; color:white; '
                                                'border-radius:30px;')
                case 'water':
                    self.lbl_type2.setStyleSheet('background-color: #4592c4; padding-bottom:5px; color:white; '
                                                 'border-radius:30px;')
                case 'eletric':
                    self.lbl_type2.setStyleSheet('background-color: rgba(238,213,53,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'rock':
                    self.lbl_type2.setStyleSheet('background-color: rgba(163,140,33,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'bug':
                    self.lbl_type2.setStyleSheet('background-color: rgba(114,159,63,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'psychic':
                    self.lbl_type2.setStyleSheet('background-color: rgba(243,102,185,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'ice':
                    self.lbl_type2.setStyleSheet('background-color: rgba(81,196,231,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'ground':
                    self.lbl_type2.setStyleSheet('background-color: background-color: qlineargradient(spread:pad, '
                                                 'x1:0, y1:0, x2:0, y2:1, stop:0.477273 rgba(247, 222, 63, 255), '
                                                 'stop:0.488636 rgba(171, 152, 66, 255)); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'fairy':
                    self.lbl_type2.setStyleSheet('background-color: rgba(253,185,233,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'steel':
                    self.lbl_type2.setStyleSheet('background-color: rgba(158,182,183,255); padding-bottom:5px; '
                                                 'color:white; border-radius:30px;')
                case 'dragon':
                    self.lbl_type2.setStyleSheet('background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, '
                                                 'y2:1, stop:0.505 rgba(241, 110, 87, 255), stop:0.511364 rgba(83, '
                                                 '164, 207, 255)); padding-bottom:5px;color:white;border-radius:30px;')
                case 'dark':
                    self.lbl_type2.setStyleSheet('background-color: rgba(112,112,112,255); padding-bottom:5px; '
                                                 'border-radius:30px; color:white;')
                case 'ghost':
                    self.lbl_type2.setStyleSheet('background-color: rgba(123,98,163,255); padding-bottom:5px; '
                                                 'border-radius:30px; color: white;')
                case _:
                    print('error')

    def abilities_poke(self, pokemon):
        abilities_list = None
        if isinstance(pokemon, str):
            abilities_list = pypokedex.get(name=f'{pokemon}')
        elif isinstance(pokemon, int):
            abilities_list = pypokedex.get(dex=pokemon)
        powers = ""
        count_nohidden = 0
        for i in abilities_list.abilities:
            if not i.is_hidden:
                powers += i.name + ' '
                count_nohidden += 1
                if count_nohidden > 1:
                    powers = powers.replace(' ', ',')
                    powers = powers.replace(f'{i.name},', f' {i.name}')
            self.lbl_abiliti.setText(powers)
        for i in abilities_list.abilities:
            if i.is_hidden:
                self.label_9.setText(i.name)
            else:
                self.label_9.setText('None')

    def poke_description(self, pokemon):
        if isinstance(pokemon, int):
            p = pypokedex.get(dex=pokemon)
            self.lbl_id.setText(str(p.dex))
            self.label.setText(p.name.title())
            self.lbl_hp_value.setText(str(p.base_stats.hp))
            self.Qpb_hp.setValue(p.base_stats.hp)
            self.lbl_atk_value.setText(str(p.base_stats.attack))
            self.Qpb_attack.setValue(p.base_stats.attack)
            self.lbl_defense.setText(str(p.base_stats.defense))
            self.Qpb_defense.setValue(p.base_stats.defense)
            self.lbl_spatk.setText(str(p.base_stats.sp_atk))
            self.Qpb_spatk.setValue(p.base_stats.sp_atk)
            self.lbl_spdef.setText(str(p.base_stats.sp_def))
            self.Qpb_spdef.setValue(p.base_stats.sp_def)
            self.lbl_spd.setText(str(p.base_stats.speed))
            self.Qpb_spd.setValue(p.base_stats.speed)
            self.lbl_total_status.setText(str(p.base_stats.hp + p.base_stats.attack + p.base_stats.defense +
                                              p.base_stats.sp_atk + p.base_stats.sp_def + p.base_stats.speed))
            self.pokeimg(int(p.dex))
            self.lbl_pokeimg.setGeometry(10,10,475,431)
            self.frame.adjustSize()
            self.lbl_pokeimg.setPixmap(QtGui.QPixmap('img/'+str(p.dex)+'.png'))
        elif isinstance(pokemon, str):
            p = pypokedex.get(name=f'{pokemon}')
            self.lbl_id.setText(str(p.dex))
            self.label.setText(p.name.title())
            self.lbl_hp_value.setText(str(p.base_stats.hp))
            self.Qpb_hp.setValue(p.base_stats.hp)
            self.lbl_atk_value.setText(str(p.base_stats.attack))
            self.Qpb_attack.setValue(p.base_stats.attack)
            self.lbl_defense.setText(str(p.base_stats.defense))
            self.Qpb_defense.setValue(p.base_stats.defense)
            self.lbl_spatk.setText(str(p.base_stats.sp_atk))
            self.Qpb_spatk.setValue(p.base_stats.sp_atk)
            self.lbl_spdef.setText(str(p.base_stats.sp_def))
            self.Qpb_spdef.setValue(p.base_stats.sp_def)
            self.lbl_spd.setText(str(p.base_stats.speed))
            self.Qpb_spd.setValue(p.base_stats.speed)
            self.lbl_total_status.setText(str(p.base_stats.hp + p.base_stats.attack + p.base_stats.defense +
                                              p.base_stats.sp_atk + p.base_stats.sp_def + p.base_stats.speed))
            self.pokeimg(int(p.dex))
            self.lbl_pokeimg.setGeometry(10, 10, 475, 431)
            self.frame.adjustSize()
            self.lbl_pokeimg.setPixmap(QtGui.QPixmap('img/' + str(p.dex) + '.png'))
        else:
            error = QMessageBox()
            error.setIcon(QMessageBox.Warning)
            error.setMinimumSize(600, 1000)
            error.setText('Por favor digite um nome de um pouco que deseja')
            error.setWindowTitle('Pokemon invalido')
            error.setStandardButtons(QMessageBox.Ok)
            error.exec()

    def search_name(self):
        self.poke_Type(self.lineEdit.text())
        self.abilities_poke(self.lineEdit.text())
        self.poke_description(self.lineEdit.text())


    def next_anime(self):
        pass

