from typing import List, Union

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.repository.geoname_repository import GeoNameRepository
from app.api.services.rate_suggestions import RateSuggestions
from app.core.database import get_db
from app.models.geolocation import GeoLocation
from app.utils.utils import get_suggestion_response_from_dict, model_list_to_dict

router = APIRouter()


from fastapi import HTTPException


@router.get("/")
async def get_suggestions(
    q: str,
    latitude: str = None,
    longitude: str = None,
    db: Session = Depends(get_db),
) -> dict:
    try:
        latitude = float(latitude) if latitude else None
        longitude = float(longitude) if longitude else None

        geoname_repo = GeoNameRepository(db)

        filters = {"q": q, "latitude": latitude, "longitude": longitude}
        geonames = geoname_repo.filter_geonames(**filters)
        if not geonames:
            return {"suggestions": []}
        result = RateSuggestions(
            query_location=GeoLocation(latitude=latitude, longitude=longitude),
            geonames=model_list_to_dict(geonames),
        ).calculate_distance()

        return get_suggestion_response_from_dict(result)
    except Exception as e:
        print(f"Error when getting suggestions: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
