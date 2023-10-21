from datetime import datetime
import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base


@pytest.fixture
def client() -> TestClient:
    client = TestClient(app)
    return client


@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:")

    Base.metadata.create_all(engine)

    SessionClass = sessionmaker(bind=engine)
    session = SessionClass()

    yield session

    session.close()
    Base.metadata.drop_all(engine)


from app.models.geoname import GeoName


@pytest.fixture
def geoname_db_objects(db_session: sessionmaker) -> None:
    ny = {
        "longitude": -74.0143100,
        "admin4_code": None,
        "feature_class": "P",
        "population": 49708,
        "feature_code": "PPL",
        "elevation": 53,
        "geoname_id": 5106292,
        "country_code": "US",
        "dem": 56,
        "cc2": None,
        "timezone": "America\\New_York",
        "latitude": 40.7878800,
        "admin1_code": "NJ",
        "modification_date": datetime.strptime("2011-05-14", "%Y-%m-%d").date(),
        "name": "West New York",
        "asciiname": "West New York",
        "admin2_code": "17.0",
        "alternatenames": 'Vehst N"ju Jork,Vest NJujork,nyw ywrk ghrby, nywjrsy,Вест Њујорк,Вэст Нью Йорк,نیو یورک غربی، نیوجرسی',
        "admin3_code": None,
    }
    london = {
        "geoname_id": 4517009,
        "name": "London",
        "asciiname": "London",
        "alternatenames": None,
        "latitude": 39.8864500,
        "longitude": -83.4482500,
        "feature_class": "P",
        "feature_code": "PPLA2",
        "country_code": "US",
        "cc2": None,
        "admin1_code": "OH",
        "admin2_code": "97.0",
        "admin3_code": None,
        "admin4_code": None,
        "population": 9904,
        "elevation": 321,
        "dem": 321,
        "timezone": "America\\New_York",
        "modification_date": datetime.strptime("2011-05-14", "%Y-%m-%d").date(),
    }
    db_session.add(GeoName(**ny))
    db_session.add(GeoName(**london))
    db_session.commit()
