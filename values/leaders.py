from storage.leaders_storage import LeadersStorage

from data.leader import Leader

import values.nations as nation

# Лидеры
_Alexandr_Makedonia = Leader('Александр', nation._Makedonia, is_banned=True)
_Alieanora_England = Leader('Алиенора Аквитанская (Англия)', nation._England)
_Alieanora_France = Leader('Алиенора Аквитанская (Франция)', nation._France)
_Amanitore = Leader('Аманиторе', nation._Nubia)
_Ambiotriks = Leader('Амбиорикс', nation._Gallia)
_Vasilii_II = Leader('Василий II', nation._Byzantium)
_viktoria = Leader('Виктория', nation._England)
_Vilgelmina = Leader('Вильгельмина', nation._Niderlands)
_Gandi = Leader('Ганди', nation._India)
_Gilgamesh = Leader('Гильгамеш', nation._Shumer)
_Gorgo_Grece = Leader('Горго', nation._Grece)
_Javarman = Leader('Джайаварман VII', nation._Khmers)
_Jhon_Cartin = Leader('Джон Кэртин', nation._Australia, is_banned=True)
_Didona = Leader('Дидона', nation._Finikia)
_Ekatetina_Medichi_Velikolepnaya = Leader('Екатерина Медичи (Великолепная)', nation._France)
_Juan_III = Leader('Жуан III', nation._Portugalia)
_Ish_vak = Leader('Иш-Вак-Чан-Ахав', nation._Maya)
_Kir = Leader('Кир II', nation._Persia)
_Cleopatra = Leader('Клеопатра', nation._Egypt)
_Kristina_I = Leader('Кристина', nation._Shwetsia)
_Kupe = Leader('Купе', nation._Maori)
_Lautaro = Leader('Лаутаро', nation._Mapuche)
_Mansa_Musa = Leader('Манса Муса', nation._Mali)
_Matiash_I = Leader('Матьяш I', nation._Vengria)
_Mvembda = Leader('Мвемба а Нзинга', nation._Kongo)
_Menelik2 = Leader('Менелик II', nation._Efiop)
_Montesuma = Leader('Монтесума', nation._Atstek)
_Peter_the_Great = Leader('Пётр Великий', nation._Russia)
_PoundMaker = Leader('Паундмейкер', nation._Kri)
_Pochatok = Leader('Пачакутек', nation._Inki)
_Pedru_II = Leader('Педру II', nation._Brazil)
_Perikl = Leader('Перикл', nation._Grece)
_Robert_Brus = Leader('Роберт Брюс', nation._Scotland)
_Saladin = Leader('Саладин (Визирь)', nation._Aravia)
_Simon_Bolivar = Leader('Симон Боливар', nation._Kolumbia)
_Sondok = Leader('Сондок', nation._Korea, is_banned=True)
_Suleiman = Leader('Сулейман (Кануни)', nation._Osman)
_Tamara = Leader('Тамара', nation._Gruzia)
_Rusvelt_Progressive = Leader('Теодор Рузвельт (Прогрессивист)', nation._USA)
_Rusvelt_Vsadnik = Leader('Теодор Рузвельт (Мужественный всадник)', nation._USA)
_Tomiris = Leader('Томирис', nation._Skifia)
_Trayan = Leader('Траян', nation._Rome)
_Tribuhvana = Leader('Трибхувана', nation._Indonesia)
_Wilfried_Lorie = Leader('Уилфрид Лорье', nation._Canada)
_Filipp_2 = Leader('Филипп II', nation._Spain)
_Friedrich_Barbarossa = Leader('Фридрих Барбаросса', nation._German)
_Hammurapi = Leader('Хаммурапи', nation._Babylon, is_banned=True)
_Harald = Leader('Харальд Суровый (Конунг)', nation._Norway)
_Hojo_Tokimune = Leader('Ходзё Токимунэ', nation._Japan)
_Hubilai_Mongol = Leader('Хубилай (Монголия)', nation._Mongolia)
_Hubilau_China = Leader('Хубилай (Китай)', nation._China)
_Tin_Huan = Leader('Цинь Шихуанди (Небесный Мандат)', nation._China)
_Chaka = Leader('Чака', nation._Zulus)
_Chandaragupta = Leader('Чандрагупта', nation._India)
_Chingishan = Leader('Чингисхан', nation._Mongolia)
_Chieu_Vietnam = Leader('Чьеу Тхи Чинь', nation._Vietnam)
_Yadviga = Leader('Ядвига', nation._Polsha)
_Ekaterina_Medichi_Black_Queen = Leader('Екатерина Медичи (Чёрная королева)', nation._France    )
_Wu_Zeitian = Leader('У Цзетянь', nation._China)
_Tokugawa = Leader('Токугава', nation._Japan)
_Suleiman_muhtesem = Leader('Сулейман (Muhteşem)', nation._Osman)
_Abraham_Linkoln = Leader('Авраам Линкольн', nation._USA, is_banned=True)
_Nader_shah = Leader('Надер Шах', nation._Persia)
_Nzinga_Mbandi = Leader('Нзинга Мбанди', nation._Kongo)
_Cesar = Leader('Юлий Цезарь', nation._Rome, is_banned=True)
_Tin_Huan_unifier = Leader('Цинь Шихуанди (Освободитель)', nation._China)
_Saladin_sultan = Leader('Саладин (Султан)', nation._Aravia)
_Yongle = Leader('Юнлэ', nation._China)
_Ramses = Leader('Рамзес II', nation._Egypt)
_Cleopatra_Ptolematic = Leader('Клеопатра (династия Птолемеев)', nation._Egypt)
_Sundiata_Keita = Leader('Сундиата Кейта', nation._Mali)
_Teodora = Leader('Феодора', nation._Byzantium)
_Sejong = Leader('Sejong', nation._Korea, is_banned=True)
_Ludwig = Leader('Людвиг II', nation._German)
_Elizabeth = Leader('Елизавета I', nation._England)
_Victoria = Leader('Виктория (Эпоха пара)', nation._England)
_Harald_Varangian = Leader('Харальд Суровый (Варяг)', nation._Norway)


leadersStorage = LeadersStorage([
    _Alexandr_Makedonia,
    _Alieanora_England,
    _Alieanora_France,
    _Amanitore,
    _Ambiotriks,
    _Vasilii_II,
    _viktoria,
    _Vilgelmina,
    _Gandi,
    _Gilgamesh,
    _Gorgo_Grece,
    _Javarman,
    _Jhon_Cartin,
    _Didona,
    _Ekatetina_Medichi_Velikolepnaya,
    _Juan_III,
    _Ish_vak,
    _Kir,
    _Cleopatra,
    _Kristina_I,
    _Kupe,
    _Lautaro,
    _Mansa_Musa,
    _Matiash_I,
    _Mvembda,
    _Menelik2,
    _Montesuma,
    _Peter_the_Great,
    _PoundMaker,
    _Pochatok,
    _Pedru_II,
    _Perikl,
    _Robert_Brus,
    _Saladin,
    _Simon_Bolivar,
    _Sondok,
    _Suleiman,
    _Tamara,
    _Rusvelt_Progressive,
    _Rusvelt_Vsadnik,
    _Tomiris,
    _Trayan,
    _Tribuhvana,
    _Wilfried_Lorie,
    _Filipp_2,
    _Friedrich_Barbarossa,
    _Hammurapi,
    _Harald,
    _Hojo_Tokimune,
    _Hubilai_Mongol,
    _Hubilau_China,
    _Tin_Huan,
    _Chaka,
    _Chandaragupta,
    _Chingishan,
    _Chieu_Vietnam,
    _Yadviga,
    _Ekaterina_Medichi_Black_Queen,
    _Wu_Zeitian,
    _Tokugawa,
    _Suleiman_muhtesem,
    _Abraham_Linkoln,
    _Nader_shah,
    _Nzinga_Mbandi,
    _Cesar,
    _Tin_Huan_unifier,
    _Saladin_sultan,
    _Yongle,
    _Ramses,
    _Cleopatra_Ptolematic,
    _Sundiata_Keita,
    _Teodora,
    _Sejong,
    _Ludwig,
    _Elizabeth,
    _Victoria,
    _Harald_Varangian
])
