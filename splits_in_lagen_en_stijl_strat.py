# selecteer een nieuwe groep, dan komen de nieuwe lagen allemaal daarin
# script om te gebruiken in QGIS

# lees de laag in
layerName = 'geotop_Almere_Pampus_-50_5_strat'
lyr = QgsProject.instance().mapLayersByName(layerName)[0]

pcolor = []
pcolor.append(QgsColorRampShader.ColorRampItem(1000, QColor("#c8c8c8"), "Antropogene afzettingen, opgebrachte grond"))
pcolor.append(QgsColorRampShader.ColorRampItem(1005, QColor("#6e6e6e"), "Antropogene afzettingen, esdekken"))
pcolor.append(QgsColorRampShader.ColorRampItem(1010, QColor("#84582c"), "Formatie van Nieuwkoop, Laagpakket van Griendtsveen"))
pcolor.append(QgsColorRampShader.ColorRampItem(1045, QColor("#b45a14"), "Formatie van Nieuwkoop, Laag van Nij Beets"))
pcolor.append(QgsColorRampShader.ColorRampItem(1020, QColor("#ffffa0"), "Formatie van Naaldwijk, Laagpakket van Schoorl"))
pcolor.append(QgsColorRampShader.ColorRampItem(1030, QColor("#98dc75"), "Formatie van Naaldwijk, Laagpakket van Walcheren (gedeelte boven NAZA)"))
pcolor.append(QgsColorRampShader.ColorRampItem(1040, QColor("#feb738"), "Formatie van Naaldwijk, Laagpakket van Zandvoort"))
pcolor.append(QgsColorRampShader.ColorRampItem(1050, QColor("#98dc75"), "Formatie van Naaldwijk, Laagpakket van Walcheren, gelegen onder Formatie van Naaldwijk, Laagpakket van Zandvoort"))
pcolor.append(QgsColorRampShader.ColorRampItem(1060, QColor("#aafff5"), "Formatie van Echteld (gedeelte buiten NIHO)"))
pcolor.append(QgsColorRampShader.ColorRampItem(1070, QColor("#aafff5"), "Formatie van Echteld (gedeelte boven NIHO)"))
pcolor.append(QgsColorRampShader.ColorRampItem(1080, QColor("#009d9b"), "Formatie van Naaldwijk, Laagpakket van Wormer, Laag van Bergen"))
pcolor.append(QgsColorRampShader.ColorRampItem(1085, QColor("#448a70"), "Kreekrak Formatie (gedeelte boven NIHO)"))
pcolor.append(QgsColorRampShader.ColorRampItem(1090, QColor("#d08228"), "Formatie van Nieuwkoop, Hollandveen Laagpakket"))
pcolor.append(QgsColorRampShader.ColorRampItem(1095, QColor("#feb738"), "Formatie van Naaldwijk, Laagpakket van Zandvoort (gedeelte onder NIHO)"))
pcolor.append(QgsColorRampShader.ColorRampItem(1100, QColor("#3fa54c"), "Formatie van Naaldwijk, Laagpakket van Wormer"))
pcolor.append(QgsColorRampShader.ColorRampItem(1110, QColor("#3fa54c"), "Formatie van Naaldwijk, laagpakketten van Wormer en Zandvoort"))
pcolor.append(QgsColorRampShader.ColorRampItem(1120, QColor("#bdb76b"), "Formatie van Naaldwijk, Laagpakket van Wormer, Laag van Velsen"))
pcolor.append(QgsColorRampShader.ColorRampItem(1125, QColor("#448a70"), "Kreekrak Formatie (gedeelte onder NIHO)"))
pcolor.append(QgsColorRampShader.ColorRampItem(1130, QColor("#982f0a"), "Formatie van Nieuwkoop, Basisveen Laag"))
pcolor.append(QgsColorRampShader.ColorRampItem(2000, QColor("#69c864"), "Formatie van Naaldwijk"))
pcolor.append(QgsColorRampShader.ColorRampItem(2010, QColor("#aafff5"), "Formatie van Echteld"))
pcolor.append(QgsColorRampShader.ColorRampItem(2020, QColor("#d08228"), "Formatie van Nieuwkoop"))
pcolor.append(QgsColorRampShader.ColorRampItem(2030, QColor("#448a70"), "Kreekrak Formatie"))
pcolor.append(QgsColorRampShader.ColorRampItem(3000, QColor("#ffffbe"), "Formatie van Boxtel, Laagpakket van Kootwijk"))
pcolor.append(QgsColorRampShader.ColorRampItem(3010, QColor("#bebe00"), "Formatie van Boxtel, Laagpakket van Singraven"))
pcolor.append(QgsColorRampShader.ColorRampItem(3011, QColor("#bebe00"), "Formatie van Boxtel Laagpakket van Singraven (bovenste deel)"))
pcolor.append(QgsColorRampShader.ColorRampItem(3020, QColor("#ffff50"), "Formatie van Boxtel, Laagpakket van Wierden"))
pcolor.append(QgsColorRampShader.ColorRampItem(3012, QColor("#ffff82"), "Formatie van Boxtel Laagpakket van Singraven (onderste deel)"))
pcolor.append(QgsColorRampShader.ColorRampItem(3025, QColor("#ffff50"), "Formatie van Boxtel, laagpakketten van Wierden en Kootwijk"))
pcolor.append(QgsColorRampShader.ColorRampItem(3030, QColor("#ffff50"), "Formatie van Boxtel, laagpakketten van Wierden, Singraven en Kootwijk"))
pcolor.append(QgsColorRampShader.ColorRampItem(3040, QColor("#e1e182"), "Formatie van Boxtel, Laagpakket van Delwijnen"))
pcolor.append(QgsColorRampShader.ColorRampItem(3045, QColor("#e1e182"), "Formatie van Boxtel, laagpakketten van Delwijnen en Kootwijk"))
pcolor.append(QgsColorRampShader.ColorRampItem(3050, QColor("#ffcd00"), "Formatie van Boxtel, Laagpakket van Schimmert"))
pcolor.append(QgsColorRampShader.ColorRampItem(3060, QColor("#e1be00"), "Formatie van Boxtel, Laagpakket van Liempde"))
pcolor.append(QgsColorRampShader.ColorRampItem(3090, QColor("#ebcd00"), "Formatie van Boxtel, Laagpakket van Best"))
pcolor.append(QgsColorRampShader.ColorRampItem(3100, QColor("#ffeb00"), "Formatie van Boxtel"))
pcolor.append(QgsColorRampShader.ColorRampItem(4000, QColor("#560000"), "Formatie van Kreftenheye, Laag van Wijchen"))
pcolor.append(QgsColorRampShader.ColorRampItem(4010, QColor("#b03060"), "Formatie van Kreftenheye en Formatie van Boxtel, Laagpakket van Delwijnen"))
pcolor.append(QgsColorRampShader.ColorRampItem(4020, QColor("#880000"), "Formatie van Kreftenheye, Laagpakket van Zutphen"))
pcolor.append(QgsColorRampShader.ColorRampItem(4030, QColor("#b03060"), "Formatie van Kreftenheye, gelegen onder de Eem Formatie"))
pcolor.append(QgsColorRampShader.ColorRampItem(4040, QColor("#9c122e"), "Formatie van Kreftenheye, Laagpakket van Twello"))
pcolor.append(QgsColorRampShader.ColorRampItem(4050, QColor("#b03060"), "Formatie van Kreftenheye"))
pcolor.append(QgsColorRampShader.ColorRampItem(4055, QColor("#81697b"), "Formatie van Beegden, Laagpakket van Oost-Maarland"))
pcolor.append(QgsColorRampShader.ColorRampItem(4060, QColor("#aa9bb4"), "Formatie van Beegden, Laag van Wijchen"))
pcolor.append(QgsColorRampShader.ColorRampItem(4070, QColor("#a08c9b"), "Formatie van Beegden, Laag van Rosmalen"))
pcolor.append(QgsColorRampShader.ColorRampItem(4080, QColor("#c8c8ff"), "Formatie van Beegden"))
pcolor.append(QgsColorRampShader.ColorRampItem(4085, QColor("#988b00"), "Formatie van Koewacht (kleiige top)"))
pcolor.append(QgsColorRampShader.ColorRampItem(4090, QColor("#aca92b"), "Formatie van Koewacht"))
pcolor.append(QgsColorRampShader.ColorRampItem(4100, QColor("#89431e"), "Formatie van Woudenberg"))
pcolor.append(QgsColorRampShader.ColorRampItem(4110, QColor("#d2ff73"), "Eem Formatie"))
pcolor.append(QgsColorRampShader.ColorRampItem(4120, QColor("#d2ff73"), "Formatie van Woudenberg en Eem Formatie"))
pcolor.append(QgsColorRampShader.ColorRampItem(5000, QColor("#ff7f50"), "Formatie van Drente"))
pcolor.append(QgsColorRampShader.ColorRampItem(5010, QColor("#eb611e"), "Formatie van Drente, Laagpakket van Gieten"))
pcolor.append(QgsColorRampShader.ColorRampItem(5020, QColor("#9c9c9c"), "Door landijs gestuwde afzettingen"))
pcolor.append(QgsColorRampShader.ColorRampItem(5030, QColor("#fafad2"), "Formatie van Drachten"))
pcolor.append(QgsColorRampShader.ColorRampItem(5040, QColor("#a9a357"), "Formatie van Urk, Laagpakket van Tynje"))
pcolor.append(QgsColorRampShader.ColorRampItem(5050, QColor("#ee82ee"), "Formatie van Peelo"))
pcolor.append(QgsColorRampShader.ColorRampItem(5060, QColor("#bdb76b"), "Formatie van Urk"))
pcolor.append(QgsColorRampShader.ColorRampItem(5070, QColor("#cd5c5c"), "Formatie van Sterksel"))
pcolor.append(QgsColorRampShader.ColorRampItem(5080, QColor("#daa520"), "Formatie van Appelscha"))
pcolor.append(QgsColorRampShader.ColorRampItem(5090, QColor("#ffe4b5"), "Formatie van Stramproy"))
pcolor.append(QgsColorRampShader.ColorRampItem(5100, QColor("#ffff00"), "Formatie van Peize"))
pcolor.append(QgsColorRampShader.ColorRampItem(5110, QColor("#ffa500"), "Formatie van Waalre"))
pcolor.append(QgsColorRampShader.ColorRampItem(5120, QColor("#ffcc00"), "Formatie van Peize en Formatie van Waalre"))
pcolor.append(QgsColorRampShader.ColorRampItem(5130, QColor("#87ceeb"), "Formatie van Maassluis"))
pcolor.append(QgsColorRampShader.ColorRampItem(5140, QColor("#bc8f8f"), "Kiezeloöliet Formatie"))
pcolor.append(QgsColorRampShader.ColorRampItem(5150, QColor("#769d27"), "Formatie van Oosterhout"))
pcolor.append(QgsColorRampShader.ColorRampItem(5160, QColor("#ec79c1"), "Formatie van Inden"))
pcolor.append(QgsColorRampShader.ColorRampItem(5170, QColor("#996600"), "Formatie van Ville"))
pcolor.append(QgsColorRampShader.ColorRampItem(5180, QColor("#6cbc96"), "Formatie van Breda"))
pcolor.append(QgsColorRampShader.ColorRampItem(5185, QColor("#666410"), "Formatie van Veldhoven"))
pcolor.append(QgsColorRampShader.ColorRampItem(5190, QColor("#9a4ea3"), "Rupel Formatie, Laagpakket van Boom"))
pcolor.append(QgsColorRampShader.ColorRampItem(5200, QColor("#b87bee"), "Rupel Formatie"))
pcolor.append(QgsColorRampShader.ColorRampItem(5210, QColor("#5090c2"), "Formatie van Tongeren, Laagpakket van Zelzate, Laag van Watervliet"))
pcolor.append(QgsColorRampShader.ColorRampItem(5220, QColor("#4681a9"), "Formatie van Tongeren, Laagpakket van Goudsberg"))
pcolor.append(QgsColorRampShader.ColorRampItem(5230, QColor("#5a9fdb"), "Formatie van Tongeren"))
pcolor.append(QgsColorRampShader.ColorRampItem(5240, QColor("#ba928d"), "Formatie van Dongen, Laagpakket van Asse"))
pcolor.append(QgsColorRampShader.ColorRampItem(5250, QColor("#ceb0bf"), "Formatie van Dongen, Laagpakket van Ieper"))
pcolor.append(QgsColorRampShader.ColorRampItem(5260, QColor("#d8bfd8"), "Formatie van Dongen"))
pcolor.append(QgsColorRampShader.ColorRampItem(5270, QColor("#d02090"), "Formatie van Landen"))
pcolor.append(QgsColorRampShader.ColorRampItem(5280, QColor("#b22222"), "Formatie van Heijenrath"))
pcolor.append(QgsColorRampShader.ColorRampItem(5290, QColor("#d2691e"), "Formatie van Houthem"))
pcolor.append(QgsColorRampShader.ColorRampItem(5300, QColor("#ffa066"), "Formatie van Maastricht"))
pcolor.append(QgsColorRampShader.ColorRampItem(5310, QColor("#f5deb3"), "Formatie van Gulpen"))
pcolor.append(QgsColorRampShader.ColorRampItem(5320, QColor("#15994f"), "Formatie van Vaals"))
pcolor.append(QgsColorRampShader.ColorRampItem(5330, QColor("#98e7cd"), "Formatie van Aken"))
pcolor.append(QgsColorRampShader.ColorRampItem(6000, QColor("#76933c"), "Formatie van Echteld (geulafzettingen generatie A)"))
pcolor.append(QgsColorRampShader.ColorRampItem(6005, QColor("#76933c"), "Formatie van Beegden, Laagpakket van Oost-Maarland (geulafzettingen generatie A)"))
pcolor.append(QgsColorRampShader.ColorRampItem(6010, QColor("#76933c"), "Formatie van Naaldwijk, Laagpakket van Walcheren (geulafzettingen generatie A)"))
pcolor.append(QgsColorRampShader.ColorRampItem(6020, QColor("#76933c"), "Formatie van Naaldwijk, Laagpakket van Wormer (geulafzettingen generatie A)"))
pcolor.append(QgsColorRampShader.ColorRampItem(6100, QColor("#66cdab"), "Formatie van Echteld (geulafzettingen generatie B)"))
pcolor.append(QgsColorRampShader.ColorRampItem(6110, QColor("#66cdab"), "Formatie van Naaldwijk, Laagpakket van Walcheren (geulafzettingen generatie B)"))
pcolor.append(QgsColorRampShader.ColorRampItem(6120, QColor("#66cdab"), "Formatie van Naaldwijk, Laagpakket van Wormer (geulafzettingen generatie B)"))
pcolor.append(QgsColorRampShader.ColorRampItem(6200, QColor("#aac4ff"), "Formatie van Echteld (geulafzettingen generatie C)"))
pcolor.append(QgsColorRampShader.ColorRampItem(6210, QColor("#aac4ff"), "Formatie van Naaldwijk, Laagpakket van Walcheren (geulafzettingen generatie C)"))
pcolor.append(QgsColorRampShader.ColorRampItem(6220, QColor("#aac4ff"), "Formatie van Naaldwijk, Laagpakket van Wormer (geulafzettingen generatie C)"))
pcolor.append(QgsColorRampShader.ColorRampItem(6300, QColor("#6699cd"), "Formatie van Echteld (geulafzettingen generatie D)"))
pcolor.append(QgsColorRampShader.ColorRampItem(6310, QColor("#6699cd"), "Formatie van Naaldwijk, Laagpakket van Walcheren (geulafzettingen generatie D)"))
pcolor.append(QgsColorRampShader.ColorRampItem(6320, QColor("#6699cd"), "Formatie van Naaldwijk, Laagpakket van Wormer (geulafzettingen generatie D)"))
pcolor.append(QgsColorRampShader.ColorRampItem(6400, QColor("#1b65af"), "Formatie van Echteld (geulafzettingen generatie E)"))
pcolor.append(QgsColorRampShader.ColorRampItem(6410, QColor("#1b65af"), "Formatie van Naaldwijk, Laagpakket van Walcheren (geulafzettingen generatie E)"))
pcolor.append(QgsColorRampShader.ColorRampItem(6420, QColor("#1b65af"), "Formatie van Naaldwijk, Laagpakket van Wormer (geulafzettingen generatie E)"))


# voor elke band
for band in range(1, lyr.bandCount()+1):
    lyrClone = lyr.clone()
    # stel de gebruikte band in
    renderer = QgsPalettedRasterRenderer(lyrClone.dataProvider(), band, qgis.core.QgsPalettedRasterRenderer.colorTableToClassData(pcolor))
    lyrClone.setRenderer(renderer)
    # verander de naam van de laag
    lyrClone.setName(f'Almere Pampus Strat NAP {(band - 1) / 2 - 50}')
    # voeg een kloon van de laag toe
    QgsProject.instance().addMapLayer(lyrClone)