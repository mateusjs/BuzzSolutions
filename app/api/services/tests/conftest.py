from typing import List
import pytest


@pytest.fixture
def geonames_data() -> List[dict]:
    return [
        {
            "latitude": 40.7128,
            "longitude": -134.0060,
            "name": "New York",
        },
        {
            "latitude": 34.0522,
            "longitude": -118.2437,
            "name": "Los Angeles",
        },
    ]
