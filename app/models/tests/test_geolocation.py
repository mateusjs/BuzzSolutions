from app.models.geolocation import GeoLocation


class TestGeolocation:
    def test_geolocation_init(self):
        latitude = 40.7128
        longitude = -74.0060
        geolocation = GeoLocation(latitude, longitude)

        assert geolocation.latitude == latitude
        assert geolocation.longitude == longitude
