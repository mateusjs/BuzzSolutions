from sqlalchemy import (BigInteger, Column, Date, Float, Integer, Numeric,
                        String)

from app.models import Base


class GeoName(Base):
    __tablename__ = "geoname"
    geoname_id = Column(BigInteger, primary_key=True, index=True, unique=True)
    name = Column(String(200))
    asciiname = Column(String(200))
    alternatenames = Column(String(5000))
    latitude = Column(Numeric(10, 7))
    longitude = Column(Numeric(10, 7))
    feature_class = Column(String(1))
    feature_code = Column(String(10))
    country_code = Column(String(2))
    cc2 = Column(String(60))
    admin1_code = Column(String(20))
    admin2_code = Column(String(80))
    admin3_code = Column(String(20))
    admin4_code = Column(String(20))
    population = Column(BigInteger)
    elevation = Column(Integer)
    dem = Column(Integer)
    timezone = Column(String(40))
    modification_date = Column(Date)
