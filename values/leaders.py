from storage.leaders_storage import LeadersStorage

from data.leader import Leader

# Лидеры
_Alexandr_Makedonia = Leader('Александр', 'Македония', 0, is_banned=True)
_Alieanora_England = Leader('Алиенора Аквитанская (Англия)', 'Англия', 1)
_Alieanora_France = Leader('Алиенора Аквитанская (Франция)', 'Франция', 2)
_Amanitore = Leader('Аманиторе', 'Нубия', 3)
_Ambiotriks = Leader('Амбиорикс', 'Галлия', 4)
_Vasilii_II = Leader('Василий II', 'Византия (Россия 2)', 5)
_viktoria = Leader('Виктория', 'Англия', 6)
_Vilgelmina = Leader('Вильгельмина', 'Нидерланды', 7)
_Gandi = Leader('Ганди', 'Индия', 8)
_Gilgamesh = Leader('Гильгамеш', 'Шумер', 9)
_Gorgo_Grece = Leader('Горго', 'Греция', 10)
_Javarman = Leader('Джайаварман VII', 'Кхмеры', 11)
_Jhon_Cartin = Leader('Джон Кэртин', 'Австралия', 12, is_banned=True)
_Didona = Leader('Дидона', 'Финикия', 13)
_Ekatetina_Medichi_Velikolepnaya = Leader('Екатерина Медичи (Великолепная)', 'Франция', 14)
_Juan_III = Leader('Жуан III', 'Португалия', 15)
_Ish_vak = Leader('Иш-Вак-Чан-Ахав', 'Майя', 16)
_Kir = Leader('Кир II', 'Персия', 17)
_Cleopatra = Leader('Клеопатра', 'Египет', 18)
_Kristina_I = Leader('Кристина', 'Швеция', 20)
_Kupe = Leader('Купе', 'Маори', 21)
_Lautaro = Leader('Лаутаро', 'Мапуче', 22)
_Mansa_Musa = Leader('Манса Муса', 'Мали', 23)
_Matiash_I = Leader('Матьяш I', 'Венгрия', 24)
_Mvembda = Leader('Мвемба а Нзинга', 'Конго', 25)
_Menelik2 = Leader('Менелик II', 'Эфиопия', 26)
_Montesuma = Leader('Монтесума', 'Ацтеки', 27)
_Peter_the_Great = Leader('Пётр Великий', 'Россия', 28)
_PoundMaker = Leader('Паундмейкер', 'Кри', 29)
_Pochatok = Leader('Пачакутек', 'Инки', 30)
_Pedru_II = Leader('Педру II', 'Бразилия', 31)
_Perikl = Leader('Перикл', 'Греция', 32)
_Robert_Brus = Leader('Роберт Брюс', 'Шотландия', 33)
_Saladin = Leader('Саладин (Визирь)', 'Аравия', 34)
_Simon_Bolivar = Leader('Симон Боливар', 'Колумбия', 35)
_Sondok = Leader('Сондок', 'Корея', 36, is_banned=True)
_Suleiman = Leader('Сулейман (Кануни)', 'Османы', 37)
_Tamara = Leader('Тамара', 'Грузия', 38)
_Rusvelt_Progressive = Leader('Теодор Рузвельт (Прогрессивист)', 'США', 39)
_Rusvelt_Vsadnik = Leader('Теодор Рузвельт (Мужественный всадник)', 'США', 40)
_Tomiris = Leader('Томирис', 'Скифия', 41)
_Trayan = Leader('Траян', 'Рим', 42)
_Tribuhvana = Leader('Трибхувана', 'Индонезия', 43)
_Wilfried_Lorie = Leader('Уилфрид Лорье', 'Канада', 44)
_Filipp_2 = Leader('Филипп II', 'Испания', 45)
_Friedrich_Barbarossa = Leader('Фридрих Барбаросса', 'Германия', 46)
_Hammurapi = Leader('Хаммурапи', 'Вавилон', 47, is_banned=True)
_Harald = Leader('Харальд Суровый', 'Норвегия', 48)
_Hojo_Tokimune = Leader('Ходзё Токимунэ', 'Япония', 49)
_Hubilai_Mongol = Leader('Хубилай (Монголия)', 'Монголия', 50)
_Hubilau_China = Leader('Хубилай (Китай)', 'Китай', 51)
_Tin_Huan = Leader('Цинь Шихуанди (Небесный Мандат)', 'Китай', 52)
_Chaka = Leader('Чака', 'Зулусы', 53)
_Chandaragupta = Leader('Чандрагупта', 'Индия', 54)
_Chingishan = Leader('Чингисхан', 'Монголия', 55)
_Chieu_Vietnam = Leader('Чьеу Тхи Чинь', 'Вьетнам', 56)
_Yadviga = Leader('Ядвига', 'Польша', 57)
_Ekaterina_Medichi_Black_Queen = Leader('Екатерина Медичи (Чёрная королева)', 'Франция', 58)
_Wu_Zeitian = Leader('У Цзетянь', 'Китай', 59)
_Tokugawa = Leader('Токугава', 'Япония', 60)
_Suleiman_muhtesem = Leader('Сулейман (Muhteşem)', 'Османы', 61)
_Abraham_Linkoln = Leader('Авраам Линкольн', 'США', 62, is_banned=True)
_Nader_shah = Leader('Надер Шах', 'Персия', 63)
_Nzinga_Mbandi = Leader('Нзинга Мбанди', 'Конго', 64)
_Cesar = Leader('Юлий Цезарь', 'Рим', 65, is_banned=True)
_Tin_Huan_unifier = Leader('Цинь Шихуанди (Освободитель)', 'Китай', 66)
_Saladin_sultan = Leader('Саладин (Султан)', 'Аравия', 67)
_Yongle = Leader('Юнлэ', 'Китай', 68)
# 19 id свободен, его можно занять. Раньше там стоял константин острожский


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
    _Yongle
])
