from iharp_query_executor.get_raster_api import GetRasterExecutor

variable = "2m_temperature"
start_datetime = "2023-01-01 00:00:00"
end_datetime = "2023-12-31 23:00:00"
temporal_resolution = "year"
temporal_aggregation = "mean"
# inbound area
max_lat = 84
min_lat = 59
min_lon = -10
max_lon = -74

spatial_resolution = 1
spatial_aggregation = "mean"
aggregation = "max"
geojson_file = "../data/tri.geojson"


raster = GetRasterExecutor(
    variable=variable,
    start_datetime=start_datetime,
    end_datetime=end_datetime,
    temporal_resolution=temporal_resolution,
    temporal_aggregation=temporal_aggregation,
    min_lat=min_lat,
    max_lat=max_lat,
    min_lon=min_lon,
    max_lon=max_lon,
    spatial_resolution=spatial_resolution,
    spatial_aggregation=spatial_aggregation,
    aggregation=aggregation,
)

print(raster.execute())