# code om GeoTOP data op te halen
# en een netcdf te produceren die in QGIS ingelezen kan worden als kaartlaag

import xarray as xr
import numpy as np
from netCDF4 import Dataset


# geef coördinaten op in RD van linksonder en rechtsboven
links = [115000,481200]
rechts = [125000,493600]
diepte = [-15, 5]

def x_van_rd_naar_geotop(x):
    # voor GeoTop v1.5 (anders dan v1.4!!)
    # x: waarde tussen 0 en 2645, in RD is dat 13600 en 278200
    # je kan een range opgeven door [xStart:stapgrootte:xEnd]
    return (x - 13_600) / 100

def y_van_rd_naar_geotop(y):
    # voor GeoTop v1.5 (anders dan v1.4!!)
    # y: waarde tussen 0 en 2810, in RD is dat 338500 en 619600
    return (y - 338_500) / 100

def z_van_nap_naar_geotop(z):
    # voor GeoTop v1.5 (anders dan v1.4!!)
    # z: waarde tussen 0 en 312, in NAP is dat -50 en 106,5
    return (z - -50) * 2

# RD omzetten naar GeoTOP coördinaten
xGTStart = x_van_rd_naar_geotop(links[0])
xGTEnd = x_van_rd_naar_geotop(rechts[0])
yGTStart = y_van_rd_naar_geotop(links[1])
yGTEnd = y_van_rd_naar_geotop(rechts[1])
zGTMin = z_van_nap_naar_geotop(diepte[0])
zGTMax = z_van_nap_naar_geotop(diepte[1])
# de API wil hele getallen
xStart = int(xGTStart)
yStart = int(yGTStart)
xEnd = int(xGTEnd) + 1
yEnd = int(yGTEnd) + 1
zMin = int(zGTMin)
zMax = int(zGTMax)


for geoType in ['lithok', 'strat']: 

    # naam van uitvoerbestand
    fileOut = f'./output/geotop_{geoType}.nc'

    # haal data op
    url = f'https://www.dinodata.nl/opendap/GeoTOP/geotop.nc?{geoType}[{xStart}:1:{xEnd}][{yStart}:1:{yEnd}][{zMin}:1:{zMax}]'

    ds = xr.open_dataset(url)

    lons = np.linspace(int(links[0]), int(rechts[0]) + 100, int((rechts[0] - links[0]) / 100) + 2)
    lats = np.linspace(int(links[1]), int(rechts[1]) + 100, int((rechts[1] - links[1]) / 100) + 2)
    depths = np.linspace(diepte[0], diepte[1], int((diepte[1] - diepte[0]) * 2 + 1))
    datas = ds[geoType].data

    # maak een netcdf
    ncfile = Dataset('./output/temp.nc', 'w')
    # dimensies moeten lat, lon heten, anders opent het niet in QGis
    # mogen wel in RD of ander coördinatensysteem zijn
    lat_dim = ncfile.createDimension('lat', len(lats))
    lon_dim = ncfile.createDimension('lon', len(lons))
    depth_dim = ncfile.createDimension('depth', len(depths))
    data_dim = ncfile.createDimension(geoType, None)

    lat = ncfile.createVariable('lat', np.float32, ('lat',))
    lat.units = 'm'
    lat.long_name = 'y RD'
    lon = ncfile.createVariable('lon', np.float32, ('lon',))
    lon.units = 'm'
    lon.long_name = 'x RD'
    depth = ncfile.createVariable('depth', np.float64, ('depth'))
    depth.units = 'm'
    depth.long_name = 'depth'
    data = ncfile.createVariable(geoType, np.float64, ('lon', 'lat', 'depth'))
    data.units = 'm'
    data.long_name = geoType

    lat[:] = lats
    lon[:] = lons
    depth[:] = depths
    data[:] = datas

    ncfile.title = f'GeoTOP {geoType}'
    ncfile.close()

    # er moet een transpose worden gedaan om x en y om te wisselen
    ds = xr.open_dataset('./output/temp.nc')
    ds = ds.transpose()
    ds.to_netcdf(fileOut)
    ds.close()