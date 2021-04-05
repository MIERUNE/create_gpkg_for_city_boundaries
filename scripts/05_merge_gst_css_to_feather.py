import geopandas as gpd

gdf = gpd.read_file("merge_boundary.gpkg", layer="add_system_number")

gdf["GST_CSS_NAME"] = gdf['GST_NAME'].str.cat(gdf['CSS_NAME'], na_rep="")

dissolve_key = ["GST_CSS_NAME", "system_number"]
city_boundary = gdf.dissolve(by=dissolve_key, as_index=False)

city_boundary.to_feather("merge_city_boundary.feather")
city_boundary.to_file("merge_city_boundary.gpkg", layer="merge_city_boundary", driver="GPKG")
