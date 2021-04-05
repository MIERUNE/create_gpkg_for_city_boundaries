import glob
from pathlib import Path

import geopandas as gpd
import pandas as pd

zip_path_list = [Path(l) for l in glob.glob("./*.zip")]

town_gdf = pd.concat([
    gpd.read_file("zip://" + str(zipfile))
    for zipfile in zip_path_list
]).pipe(gpd.GeoDataFrame)

town_gdf["AREA_CODE"] = town_gdf['PREF'].str.cat(town_gdf['CITY'])
city_gdf = town_gdf.dissolve(by="AREA_CODE", as_index=False)
pref_gdf = city_gdf.dissolve(by="PREF", as_index=False)

pref_gdf.to_file("boundary.gpkg", layer='pref', driver="GPKG")
city_gdf.to_file("boundary.gpkg", layer='city', driver="GPKG")
town_gdf.to_file("boundary.gpkg", layer='town', driver="GPKG")
