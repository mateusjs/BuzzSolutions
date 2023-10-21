from typing import List

import pytest


class ModelMock:
    def __init__(self, id, name):
        self.id = id
        self.name = name


@pytest.fixture
def model_mock() -> ModelMock:
    return [ModelMock(1, "Item 1"), ModelMock(2, "Item 2")]


@pytest.fixture
def input_data() -> List[dict]:
    return [
        {"latitude": 40.7128, "longitude": -74.0060, "name": "New York", "score": 0.95},
        {
            "latitude": 34.0522,
            "longitude": -118.2437,
            "name": "Los Angeles",
            "score": 0.85,
        },
    ]
