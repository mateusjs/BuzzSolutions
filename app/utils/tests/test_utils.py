from typing import List

from app.utils.tests.conftest import ModelMock
from app.utils.utils import (get_suggestion_response_from_dict,
                             model_list_to_dict)


def test_model_list_to_dict(model_mock: ModelMock):
    result = model_list_to_dict(model_mock)

    assert isinstance(result, list)
    assert len(result) == 2

    assert result[0] == {"id": 1, "name": "Item 1"}
    assert result[1] == {"id": 2, "name": "Item 2"}


def test_get_suggestion_response_from_dict(input_data: List[dict]):
    result = get_suggestion_response_from_dict(input_data)

    expected_output = {
        "suggestions": [
            {
                "latitude": 40.7128,
                "longitude": -74.0060,
                "name": "New York",
                "score": 0.95,
            },
            {
                "latitude": 34.0522,
                "longitude": -118.2437,
                "name": "Los Angeles",
                "score": 0.85,
            },
        ]
    }

    assert result == expected_output
