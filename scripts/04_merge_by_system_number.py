import geopandas as gpd

merge_boundary_gdf = gpd.read_file(
    "../data/merge_boundary.gpkg", layer="add_system_number"
)

plane_rectangular_gdf = merge_boundary_gdf.dissolve(by="system_number", as_index=False)
necessary_columns = ["system_number", "geometry"]
plane_rectangular_gdf = plane_rectangular_gdf[necessary_columns]

plane_rectangular_gdf.to_file(
    "../data/merge_boundary.gpkg", layer="plane_rectangular", driver="GPKG"
)
