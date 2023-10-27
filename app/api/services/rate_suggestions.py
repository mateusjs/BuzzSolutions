from typing import List
from geopy.distance import geodesic
from app.api.services.geoname_scorer import GeonameScorer

class RateSuggestions(GeonameScorer):
    def calculate_score(self):
        max_distance = float("-inf")
        for geo_name in self.geonames:
            geo_name_coords = (geo_name.get("latitude"), geo_name.get("longitude"))
            query_coords = (self.query_location.latitude, self.query_location.longitude)
            distance = geodesic(query_coords, geo_name_coords).km
            if distance > max_distance:
                max_distance = distance
            geo_name["distance"] = distance
        self._get_score_by_distance(max_distance)
        self._sort_by_score()
        return self.geonames

    def _get_score_by_distance(self, max_distance: float):
        for geo_name in self.geonames:
            geo_name["score"] = round(abs(1 - (geo_name["distance"] / max_distance)), 2)

    def _sort_by_score(self):
        self.geonames = sorted(self.geonames, key=lambda x: x["score"], reverse=True)
