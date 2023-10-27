from typing import List
from app.models.geolocation import GeoLocation


class GeonameScorer:
    def __init__(self, query_location: GeoLocation, geonames: List[dict]):
        self.query_location = query_location
        self.geonames = geonames

    def calculate_score(self):
        pass
