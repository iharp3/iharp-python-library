from iharp_query_executor.get_geojson_executor import GeoJsonExecutor

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

spatial_resolution = 0.25
spatial_aggregation = "mean"
aggregation = "max"
geojson_file = "./data/tri.geojson"


geojson = GeoJsonExecutor(
    variable=variable,
    start_datetime=start_datetime,
    end_datetime=end_datetime,
    temporal_resolution=temporal_resolution,
    min_lat=min_lat,
    max_lat=max_lat,
    min_lon=min_lon,
    max_lon=max_lon,
    spatial_resolution=spatial_resolution,
    aggregation=aggregation,
    geojson_file=geojson_file
)

print(geojson.execute())