# bro_profielen_kaarten

This repository was made to share a netCDF file. It is in the folder output.  
  
The data consists of:  
* xy-coordinates in rd (rd is the coordinate system of the Netherlands), 
* z-coordinates relative to mean sea level,
* lithok which is a lithology class represented by an integer between 1 and 10.
  
I would like to visualize the lithok from this netCDF file on maps, preferably via a format that allows for use in a GIS too.  
NetCDF with recognized coordinates would be good, other option could be GeoTIFF.  
  
If I open this netCDF file in QGis directly, it plots on coordinates 1-8, instead of using xrd and yrd.  
  
On reading with xarray in Python, it messes up xyz to zyx or vice versa.