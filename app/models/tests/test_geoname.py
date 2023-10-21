import pytest
from sqlalchemy.orm import Session, sessionmaker

from app.models.geoname import GeoName  # Importe a classe GeoName


class TestGeoname:
    def test_geoname_columns(self, db_session: sessionmaker):
        columns = GeoName.__table__.columns.keys()
        expected_columns = [
            "geoname_id",
            "name",
            "asciiname",
            "alternatenames",
            "latitude",
            "longitude",
            "feature_class",
            "feature_code",
            "country_code",
            "cc2",
            "admin1_code",
            "admin2_code",
            "admin3_code",
            "admin4_code",
            "population",
            "elevation",
            "dem",
            "timezone",
            "modification_date",
        ]

        assert set(columns) == set(expected_columns)
