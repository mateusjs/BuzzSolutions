from typing import List

from geopy.distance import geodesic

from app.models.geolocation import GeoLocation


class RateSuggestions:
    def __init__(self, query_location: GeoLocation, geonames: List[dict]):
        self.query_location = query_location
        self.geonames = geonames

    def calculate_distance(self):
        try:
            max_distance = float("-inf")
            for geo_name in self.geonames:
                geo_name_coords = (geo_name.get("latitude"), geo_name.get("longitude"))
                query_coords = (
                    self.query_location.latitude,
                    self.query_location.longitude,
                )
                distance = geodesic(query_coords, geo_name_coords).km
                if distance > max_distance:
                    max_distance = distance
                geo_name["distance"] = distance
            self._get_score_by_distance(max_distance)
            self._sort_by_score()
            return self.geonames
        except Exception as e:
            raise e

    def _get_score_by_distance(self, max_distance: float):
        try:
            for geo_name in self.geonames:
                geo_name["score"] = round(
                    abs(1 - (geo_name["distance"] / max_distance)), 2
                )
        except Exception as e:
            raise e

    def _sort_by_score(self):
        try:
            self.geonames = sorted(
                self.geonames, key=lambda x: x["score"], reverse=True
            )
        except Exception as e:
            raise e
