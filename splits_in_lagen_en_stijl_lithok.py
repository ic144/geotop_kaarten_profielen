# selecteer een nieuwe groep, dan komen de nieuwe lagen allemaal daarin
# script om te gebruiken in QGIS

# lees de laag in
layerName = 'geotop_lithok'
lyr = QgsProject.instance().mapLayersByName(layerName)[0]

pcolor = []
pcolor.append(QgsColorRampShader.ColorRampItem(0, QColor("#c7c7c7"), '0 - Antropogeen'))
pcolor.append(QgsColorRampShader.ColorRampItem(1, QColor("#9e4f41"), '1 - Organisch materiaal (veen)'))
pcolor.append(QgsColorRampShader.ColorRampItem(2, QColor("#009100"), '2 - Klei'))
pcolor.append(QgsColorRampShader.ColorRampItem(3, QColor("#c1cf5b"), '3 - Kleiig zand, zandige klei en leem'))
pcolor.append(QgsColorRampShader.ColorRampItem(5, QColor("#ffff00"), '5 - Zand fijn (63 - 150 micrometer)'))
pcolor.append(QgsColorRampShader.ColorRampItem(6, QColor("#f2de05"), '6 - Zand midden (150 - 300 micrometer)'))
pcolor.append(QgsColorRampShader.ColorRampItem(7, QColor("#e8c517"), '7 - Zand grof (300 -2000 micrometer)'))
pcolor.append(QgsColorRampShader.ColorRampItem(8, QColor("#d9a521"), '8 - Grind'))
pcolor.append(QgsColorRampShader.ColorRampItem(9, QColor("#5e5eff"), '9 - Schelpen'))

# voor elke band
for band in range(1, lyr.bandCount()+1):
    lyrClone = lyr.clone()
    # stel de gebruikte band in
    renderer = QgsPalettedRasterRenderer(lyrClone.dataProvider(), band, qgis.core.QgsPalettedRasterRenderer.colorTableToClassData(pcolor))
    lyrClone.setRenderer(renderer)
    # verander de naam van de laag
    ok = -15 # Aanpassen als de range verandert
    lyrClone.setName(f'GeoTOP lithok NAP {(band - 1) / 2 + ok} m') 
    # voeg een kloon van de laag toe
    QgsProject.instance().addMapLayer(lyrClone)