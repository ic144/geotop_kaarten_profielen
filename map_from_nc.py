import xarray as xr
import rioxarray as rio

# writing direct to tiff does not work
try:
    nc = xr.open_dataset('./output/geotop.nc')
    print(nc)
    nc.rio.to_raster(r'output.tiff')
except Exception as e:
    print(e)

# making a new DataArray does not work either
try:
    data = nc['lithok'].data
    xrd = nc['xrd'].data
    yrd = nc['yrd'].data
    z = nc['z'].data
    xray = xr.DataArray(data, dims=('z', 'y', 'x'), coords={'x': xrd, 'y': yrd})
    nc.rio.to_raster(r'output.tiff')
except Exception as e:
    print(e)
