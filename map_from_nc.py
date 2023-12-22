import xarray as xr
import rioxarray as rio
import matplotlib.pyplot as plt


# write direct to geotiff
try:
    nc = xr.open_dataset('./output/geotop.nc')
    nc.to_netcdf('output1.nc')
    nc.rio.to_raster(r'output1.tiff')
except Exception as e:
    print(e)

# make a new DataArray with all data
try:
    data = nc['lithok'].data
    xrd = nc['xrd'].data
    yrd = nc['yrd'].data
    z = nc['z'].data
    da = xr.DataArray(data, dims=('z', 'y', 'x'), coords={'x': xrd, 'y': yrd})
    da.to_netcdf('output2.nc')
    da.rio.to_raster('output2.tiff')
except Exception as e:
    print(e)

# make a new DataArray with one layer
try:
    data = nc['lithok'].data[0]
    xrd = nc['xrd'].data
    yrd = nc['yrd'].data
    z = nc['z'].data
    da = xr.DataArray(data, dims=('yrd', 'xrd'), coords={'xrd': xrd, 'yrd': yrd})
    da.to_netcdf('output3.nc')
    da.rio.to_raster('output3.tiff')
except Exception as e:
    print(e)

# transpose
try:
    ncT = nc.transpose()
    ncT.to_netcdf('output4.nc')
    ncT.rio.to_raster('output4.tiff')
except Exception as e:
    print(e)

# transpose and make a new DataArray
try:
    ncT = nc.transpose()
    data = ncT['lithok'].data
    xrd = ncT['xrd'].data
    yrd = ncT['yrd'].data
    z = ncT['z'].data
    da = xr.DataArray(data, dims=('z', 'y', 'x'), coords={'x': xrd, 'y': yrd})
    da.to_netcdf('output5.nc')
    da.rio.to_raster('output5.tiff')
except Exception as e:
    print(e)

