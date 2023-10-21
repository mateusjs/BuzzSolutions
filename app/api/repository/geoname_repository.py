from typing import List

from sqlalchemy import and_, or_
from sqlalchemy.orm import Session

from app.models.geoname import GeoName


class GeoNameRepository:
    def __init__(self, session: Session):
        self.session = session

    def filter_geonames(self, **filters) -> List[GeoName]:
        try:
            query = self.session.query(GeoName)

            filter_conditions = []

            if filters.get("q"):
                filter_conditions.append(
                    or_(
                        GeoName.name.ilike(f'%{filters["q"]}%'),
                        GeoName.asciiname.ilike(f'%{filters["q"]}%'),
                        GeoName.alternatenames.ilike(f'%{filters["q"]}%'),
                    )
                )
            if filters.get("latitude"):
                filter_conditions.append(GeoName.latitude >= filters["latitude"])
            if filters.get("longitude"):
                filter_conditions.append(GeoName.longitude <= filters["longitude"])

            if filter_conditions:
                query = query.filter(and_(*filter_conditions))

            return query.all()
        except Exception as e:
            print(f"Error when filtering geonames: {e}")
            raise e
