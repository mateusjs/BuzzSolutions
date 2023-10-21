import pytest
from app.api.repository.geoname_repository import GeoNameRepository


class TestGeonameRepository:
    @pytest.mark.parametrize(
        "filters, expected_length",
        [
            ({"q": "London", "latitude": 37.0, "longitude": -82.0}, 1),
            ({"q": "New york", "latitude": 37.0, "longitude": -72.0}, 1),
            ({"q": "London", "latitude": 45.0, "longitude": -82.0}, 0),
            ({"q": "New york", "latitude": 45.0, "longitude": -75.0}, 0),
        ],
    )
    def test_filter_geonames(
        self, filters, expected_length, geoname_db_objects, db_session
    ):
        repo = GeoNameRepository(db_session)
        results = repo.filter_geonames(**filters)

        assert isinstance(results, list)
        assert len(results) == expected_length
        if results:
            assert results[0].name.lower().find(filters["q"])
            assert results[0].latitude >= filters["latitude"]
            assert results[0].longitude <= filters["longitude"]

    def test_filter_geonames_with_error(
        self,
    ):
        filters = {"q": "New york", "latitude": 45.0, "longitude": -75.0}
        with pytest.raises(AttributeError):
            repo = GeoNameRepository(None)
            results = repo.filter_geonames(**filters)
