from typing import List


def model_list_to_dict(model_list: List[object]) -> List[dict]:
    return [model.__dict__ for model in model_list]


def get_suggestion_response_from_dict(data: dict) -> dict:
    new_data = {"suggestions": []}
    for item in data:
        new_data["suggestions"].append(
            {
                "latitude": item.get("latitude"),
                "longitude": item.get("longitude"),
                "name": item.get("name"),
                "score": item.get("score"),
            }
        )
    return new_data
