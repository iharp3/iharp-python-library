from iharp_query_executor.get_find_area_api import GetFindAreaExecutor


variable = "2m_temperature"
start_datetime = "2020-01-01 00:00:00"
end_datetime = "2023-12-31 23:00:00"
temporal_resolution = "year"
temporal_aggregation = "mean"
# inbound area
min_lat = 75.0 #84
max_lat = 80.0 #59
min_lon = -50.0 #-10
max_lon = -25.0 #-74

# Greenland, throws error "Your request is too large"
# max_lat = 85.0
# min_lat = 60.0
# min_lon = -70.0
# max_lon = -10.0

spatial_resolution = 0.25
spatial_aggregation = "mean"
aggregation = "max"
filter_predicate = ">"
filter_value = 263
geojson_file = "../data/tri.geojson"


fa = GetFindAreaExecutor(
    variable=variable,
    start_datetime=start_datetime,
    end_datetime=end_datetime,
    min_lat=min_lat,
    max_lat=max_lat,
    min_lon=min_lon,
    max_lon=max_lon,
    spatial_resolution=spatial_resolution,
    aggregation=aggregation,
    filter_predicate=filter_predicate,
    filter_value=filter_value
)

print(fa.execute())