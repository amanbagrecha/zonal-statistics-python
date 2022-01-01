from glob import glob
import rasterio
import geopandas as gpd
from rasterstats import zonal_stats
import pandas as pd

allraster = glob(".modis-ndvi/*tif")

listcol =[]
for i in allraster:
    with rasterio.open(i) as src:
        scrs = src.crs
        vinput = gpd.read_file("featureCollection.gpkg").to_crs(crs = scrs)
        stats = zonal_stats(vinput, i, stats = 'mean', geojson_out = True, nodata = -999)
        raster_sts = [i['properties']['mean'] for i in stats]
        listcol.append(raster_sts)

print(pd.DataFrame(listcol))