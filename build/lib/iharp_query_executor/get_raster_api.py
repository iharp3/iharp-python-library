import requests
import json

class GetRasterExecutor():
    def __init__(
            self, 
            variable: str, 
            start_datetime: str,
            end_datetime: str,
            temporal_resolution: str,
            temporal_aggregation: str,
            min_lat: float,
            max_lat: float,
            min_lon: float,
            max_lon: float,
            spatial_resolution: float,
            spatial_aggregation: str,
            aggregation,
    ):
        super().__init__()
        self.variable = variable
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.temporal_resolution = temporal_resolution
        self.temporal_aggregation = temporal_aggregation
        self.min_lat = min_lat
        self.max_lat = max_lat
        self.min_lon = min_lon
        self.max_lon = max_lon
        self.spatial_resolution = spatial_resolution
        self.spatial_aggregation = spatial_aggregation
        self.aggregation = aggregation
      

    def execute(self):
        form_data = {
            "requestType": "",
            "variable": self.variable,  
            "startDateTime": self.start_datetime,
            "endDateTime": self.end_datetime,
            "temporalResolution": self.temporal_resolution,
            "temporalAggregation": self.temporal_aggregation,
            "north": self.min_lat,
            "south": self.max_lat,
            "east": self.min_lon,
            "west": self.max_lon,
            "spatialResolution": self.spatial_resolution,
            "spatialAggregation": self.spatial_aggregation,
            "aggregation": self.aggregation
        }

        url = "https://iharpv.cs.umn.edu/api/query/"
        
        response = requests.post(
            url = url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(form_data),
            verify=True
            )
        
        try:
            print("Response content:", response.json())
        except:
            print("Raw response content:", response.text)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Error:", response.status_code)
            return None