from netCDF4 import Dataset
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm, LinearSegmentedColormap
from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd
from shapely.geometry import LineString, Point, Polygon
from shapely.ops import split
import xarray as xr
import rioxarray as rio
import json


# profiellijn in RD
profiellijnen_rd = {
    'Zuidoost': LineString(((125323.6,482461.7), (126614.7,480186.9)))
}

punten_rd = {
    'Weesperstraat 430':  Point(122273.54,486202.08)
}

# dieptebereik in m tov NAP
z_nap = [-25, 1]
# type data dat je wil hebben
# lithok is zand, klei, veen enz
# strat is formaties e.d.
geo_type = 'lithok'  # 'strat' 

def x_van_rd_naar_geotop(x):
    # voor GeoTop v1.5 (anders dan v1.4!!)
    # x: waarde tussen 0 en 2645, in RD is dat 13600 en 278200
    # je kan een range opgeven door [x_start:stapgrootte:x_end]
    return (x - 13_600) / 100

def y_van_rd_naar_geotop(y):
    # voor GeoTop v1.5 (anders dan v1.4!!)
    # y: waarde tussen 0 en 2810, in RD is dat 338500 en 619600
    return (y - 338_500) / 100

def z_van_nap_naar_geotop(z):
    # voor GeoTop v1.5 (anders dan v1.4!!)
    # z: waarde tussen 0 en 312, in NAP is dat -50 en 106,5
    return (z - -50) * 2

def min_max_coords(profiellijn, idx):
    # bepalen van gebied waarvoor data opgehaald moet worden
    coords = [punt[idx] for punt in profiellijn.coords]
    start = min(coords)
    end = max(coords)
    return start, end

def haal_data(x_gt_start, y_gt_start, x_gt_end, y_gt_end, z_gt_min, z_gt_max, geo_type, geom_type):
    if geom_type == 'lijn' or geom_type == 'vlak':
        add = 1
    elif geom_type == 'punt':
        add = 0

    # de API wil hele getallen
    x_start = int(x_gt_start)
    y_start = int(y_gt_start)
    x_end = int(x_gt_end) + add
    y_end = int(y_gt_end) + add
    z_min = int(z_gt_min)
    z_max = int(z_gt_max)

    url = f'https://www.dinodata.nl/opendap/GeoTOP/geotop.nc?{geo_type}[{x_start}:1:{x_end}][{y_start}:1:{y_end}][{z_min}:1:{z_max}]'

    nc = Dataset(url)
    return nc

def maak_raster_polygons(x_gt_start, x_gt_end, y_gt_start, y_gt_end):
    # maak de rasterpolygons
    x_raster = np.arange(int(x_gt_start), int(x_gt_end) + 1, 1)
    y_raster = np.arange(int(y_gt_start), int(y_gt_end) + 1, 1)

    # zet de rasterpunten om in polygonen
    rasterpolygons = []
    for x in x_raster: 
        for y in y_raster:
            rasterpolygons.append(Polygon(((x,y), (x+1, y), (x+1, y+1), (x, y+1), (x,y))))
    rasterpolygons = np.array(rasterpolygons)
    rasterpolygons.shape = (len(x_raster), len(y_raster))

    return rasterpolygons

def haal_relevante_data_lijn(rasterpolygons, profiel_lijn, nc):
    # haal de benodigde data uit de netcdf op basis van de profiellijn en polygonen
    profielstukken = [] # onderverdeling van het profiel in stukken. Deze wordt niet gebruikt, maar kan handig zijn als je iets anders wil dan een profiel zoals nu
    lithok = [] # de grondopbouw
    eindpunten = [] # eindpunten van lijnstukken voor plotraster
    for i, row in enumerate(rasterpolygons):
        for j, polygon in enumerate(row):
            lijnstukken = split(profiel_lijn, polygon)
            for lijnstuk in lijnstukken.geoms:
                if lijnstuk.within(polygon):
                    profielstukken.append(lijnstuk)
                    lithok.append(pd.DataFrame(nc[geo_type][i,j,:]))
                    eindpunten.append(profiel_lijn.project(lijnstuk.interpolate(1, normalized=True)))

    # sorteren van lithok en profielstukken
    sort_tuples = sorted(zip(eindpunten, lithok, profielstukken))
    eindpunten, lithok, profielstukken = [t[0] for t in sort_tuples], [t[1] for t in sort_tuples], [t[2] for t in sort_tuples]

    # maak een dataframe van de data tbv de plot
    lithok = pd.concat(lithok, axis=1)

    # voeg het beginpunt toe voor het plotten
    eindpunten.insert(0, 0)
    # de schaal is 1:100, reken weer terug naar werkelijke afstanden
    eindpunten = [punt * 100 for punt in eindpunten]

    return eindpunten, lithok, profielstukken



def haal_data_lijn(profiellijn_rd, z_nap, geo_type):
    # bepaal min en max x, y, z in RD voor opvragen data
    xRdStart, xRdEnd = min_max_coords(profiellijn_rd, 0)
    yRdStart, yRdEnd = min_max_coords(profiellijn_rd, 1)
    z_nap_min, z_nap_max = min(z_nap), max(z_nap)
    
    # zet min en max x om van RD naar geotop
    x_gt_start = x_van_rd_naar_geotop(xRdStart)
    x_gt_end = x_van_rd_naar_geotop(xRdEnd)
    # zet min en max y om van RD naar geotop
    y_gt_start = y_van_rd_naar_geotop(yRdStart)
    y_gt_end = y_van_rd_naar_geotop(yRdEnd)
    # zet min en max z om van NAP naar geotop
    z_gt_min = z_van_nap_naar_geotop(z_nap_min)
    z_gt_max = z_van_nap_naar_geotop(z_nap_max)


    # profiellijn in geotop raster coordinaten
    profiel_lijn = LineString([(x_van_rd_naar_geotop(punt[0]), y_van_rd_naar_geotop(punt[1])) for punt in profiellijn_rd.coords])

    # haal data op
    nc = haal_data(x_gt_start, y_gt_start, x_gt_end, y_gt_end, z_gt_min, z_gt_max, geo_type, 'lijn')

    return nc, x_gt_start, x_gt_end, y_gt_start, y_gt_end, z_nap_min, z_nap_max, profiel_lijn


def haal_data_punt(puntRd, z_nap, geo_type):
    # zet de x, y en z-coördinaten om van RD naar GeoTop
    xGT = x_van_rd_naar_geotop(puntRd.x)
    yGT = y_van_rd_naar_geotop(puntRd.y)
    z_nap_min, z_nap_max = min(z_nap), max(z_nap)
    z_gt_min = z_van_nap_naar_geotop(z_nap_min)
    z_gt_max = z_van_nap_naar_geotop(z_nap_max)

    nc = haal_data(xGT, yGT, xGT, yGT, z_gt_min, z_gt_max, geo_type, 'punt')

    return nc, xGT, yGT, z_nap_min, z_nap_max

def plot(geo_type, z_nap_min, z_nap_max, nc, x_gt_start, x_gt_end, y_gt_start, y_gt_end, profiel_lijn, locatie, profiellijn_rd, profiel_type):
        # lees de tabellen in met materialen en kleuren van BRO
        if geo_type == 'lithok':
            lithoklasse = pd.read_excel('./REF_GTP_LITHO_CLASS.xlsx')
        elif geo_type == 'strat':
            lithoklasse = pd.read_excel('./REF_GTP_STR_UNIT.xlsx')

        for legenda in [lithoklasse]: #, stratEenheid
            legenda['kleur'] = legenda.apply(lambda row: [row['RED_DEC'] / 255, row['GREEN_DEC'] / 255, row['BLUE_DEC'] / 255, 1], axis=1)

        # array met z-waarden om te gebruiken op de y-as van de plot
        stap = 0.5
        zs = np.arange(z_nap_min - stap, z_nap_max + stap, stap)

        rasterpolygons = maak_raster_polygons(x_gt_start, x_gt_end, y_gt_start, y_gt_end)

        eindpunten, lithok, profielstukken = haal_relevante_data_lijn(rasterpolygons, profiel_lijn, nc)


        # kleurenschaal op basis van tabel van BRO
        aanwezig = lithok.values
        aanwezig = [item for sublist in aanwezig for item in sublist]
        aanwezig = set(aanwezig)

        lithoklasse = lithoklasse[lithoklasse['VOXEL_NR'].isin(aanwezig)]

        cmap = ListedColormap(lithoklasse['kleur'])
        bounds = lithoklasse['VOXEL_NR'].values
        labels = lithoklasse['DESCRIPTION'].values
        norm = BoundaryNorm(bounds, cmap.N)

        sorted_bounds_labels = sorted(zip(bounds, labels))
        bounds, labels = np.array([t[0] for t in sorted_bounds_labels]), np.array([t[1] for t in sorted_bounds_labels])

        len_lab = len(labels)
        # prepare normalizer
        ## Prepare bins for the normalizer
        norm_bins = bounds + 0.5
        norm_bins = np.insert(norm_bins, 0, np.min(norm_bins) - 1.0)
        ## Make normalizer and formatter
        norm = BoundaryNorm(norm_bins, len_lab, clip=True)
        fmt = FuncFormatter(lambda x, pos: labels[norm(x)])

        # Plot figure
        fig = plt.figure(figsize=[profiellijn_rd.length/30, 10])

        diff = norm_bins[1:] - norm_bins[:-1]
        tickz = norm_bins[:-1] + diff / 2

        # maak de plot
        im = plt.pcolormesh(eindpunten, zs, lithok, cmap=cmap, norm=norm, shading='flat')
        cb = plt.colorbar(im, format=fmt, ticks=tickz)
        plt.title(f'{locatie} {geo_type}')
        plt.savefig(f'./output/{profiel_type}_{geo_type}_{locatie}.svg')
        plt.savefig(f'./output/{profiel_type}_{geo_type}_{locatie}.png')
        plt.close()

        nc.close()


for locatie, profiellijn_rd in profiellijnen_rd.items():
    print(locatie)
    for geo_type in ['lithok', 'strat']:
        nc, x_gt_start, x_gt_end, y_gt_start, y_gt_end, z_nap_min, z_nap_max, profiel_lijn = haal_data_lijn(profiellijn_rd, z_nap, geo_type)
        plot(geo_type, z_nap_min, z_nap_max, nc, x_gt_start, x_gt_end, y_gt_start, y_gt_end, profiel_lijn, locatie, profiellijn_rd, 'lijn')

for locatie, puntRd in punten_rd.items():
    print(locatie)
    for geo_type in ['lithok', 'strat']:
        nc, xGT, yGT, z_nap_min, z_nap_max = haal_data_punt(puntRd, z_nap, geo_type)
        plot(geo_type, z_nap_min, z_nap_max, nc, xGT, xGT+0.01, yGT, yGT+0.01, LineString(((xGT, yGT), (xGT+0.01, yGT+0.01))), locatie, LineString(((puntRd.x, puntRd.y), (puntRd.x+10, puntRd.y+10))), 'punt')


for locatie, profiellijn_rd in profiellijnen_rd.items():
    print(locatie)
    for geo_type in ['lithok', 'strat']:
        print(geo_type)

        # haal de data op
        nc, x_gt_start, x_gt_end, y_gt_start, y_gt_end, z_nap_min, z_nap_max, profiel_lijn = haal_data_lijn(profiellijn_rd, z_nap, geo_type)

        # lees de tabellen in van BRO voor kleurschalen
        if geo_type == 'lithok':
            lithoklasse_totaal = pd.read_excel('./REF_GTP_LITHO_CLASS.xlsx')
        elif geo_type == 'strat':
            lithoklasse_totaal = pd.read_excel('./REF_GTP_STR_UNIT.xlsx')

        for legenda in [lithoklasse_totaal]: #, stratEenheid
            legenda['kleur'] = legenda.apply(lambda row: [row['RED_DEC'] / 255, row['GREEN_DEC'] / 255, row['BLUE_DEC'] / 255, 1], axis=1)

        for i, level in enumerate(np.linspace(min(z_nap), max(z_nap), nc.variables[geo_type].shape[-1])):
            print(level)
            plotData = nc.variables[geo_type][:,:,i]

            # kleurenschaal op basis van tabel van BRO
            aanwezig = np.unique(plotData)
            lithoklasse = lithoklasse_totaal[lithoklasse_totaal['VOXEL_NR'].isin(aanwezig)]

            cmap = ListedColormap(lithoklasse['kleur'])
            bounds = lithoklasse['VOXEL_NR'].values
            labels = lithoklasse['DESCRIPTION'].values

            # als er maar 1 materiaal is, dan krijg je een foutmelding, dit is voor ondiepe lagen
            if len(bounds) < 2:
                bounds = np.append(bounds, 4)
            if len(bounds) < 2:
                bounds = np.append(bounds, 5)

            norm = BoundaryNorm(bounds, cmap.N)

            sorted_bounds_labels = sorted(zip(bounds, labels))
            bounds, labels = np.array([t[0] for t in sorted_bounds_labels]), np.array([t[1] for t in sorted_bounds_labels])

            len_lab = len(labels)
            # prepare normalizer
            # Prepare bins for the normalizer
            norm_bins = bounds + 0.5
            norm_bins = np.insert(norm_bins, 0, np.min(norm_bins) - 1.0)
            # Make normalizer and formatter
            norm = BoundaryNorm(norm_bins, len_lab, clip=True)
            fmt = FuncFormatter(lambda x, pos: labels[norm(x)])

            # Plot figure
            fig = plt.figure()

            diff = norm_bins[1:] - norm_bins[:-1]
            tickz = norm_bins[:-1] + diff / 2

            x = range(int(min(profiellijn_rd.coords.xy[0])/100-1), int(max(profiellijn_rd.coords.xy[0])/100+2))
            y = range(int(min(profiellijn_rd.coords.xy[1])/100-1), int(max(profiellijn_rd.coords.xy[1])/100+2))

            im = plt.pcolormesh(x, y, plotData.T, cmap=cmap, norm=norm, shading='flat')
            cb = plt.colorbar(im, format=fmt, ticks=tickz)
            plt.title(f'{geo_type} NAP {level} m')
            plt.savefig(f'./output/{geo_type}_{level}_{locatie}.png')
            plt.close()