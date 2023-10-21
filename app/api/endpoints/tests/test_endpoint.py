from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException
from fastapi.exceptions import ResponseValidationError
from fastapi.testclient import TestClient


class TestEndpoint:
    @patch("app.api.endpoints.suggestion_endpoint.get_suggestion_response_from_dict")
    @patch("app.api.services.rate_suggestions.RateSuggestions.calculate_distance")
    @patch("app.api.endpoints.suggestion_endpoint.model_list_to_dict")
    @patch("app.api.repository.geoname_repository.GeoNameRepository.filter_geonames")
    def test_get_suggestions(
        self,
        filter_geonames_mock: Mock,
        model_list_to_dict_mock: Mock,
        calculate_distance_mock: Mock,
        get_suggestion_response_from_dict_mock: Mock,
        client: TestClient,
        geoname_db_objects,
    ):
        get_suggestion_response_from_dict_mock.return_value = {
            "suggestions": [
                {
                    "latitude": 14,
                    "longitude": -4,
                    "name": "NY",
                    "score": 1,
                }
            ]
        }
        params = {"q": "New York", "latitude": 40.7128, "longitude": -74.0060}
        response = client.get("/suggestions", params=params)
        assert response.status_code == 200
        assert filter_geonames_mock.assert_called_once
        assert model_list_to_dict_mock.assert_called_once
        assert calculate_distance_mock.assert_called_once
        assert get_suggestion_response_from_dict_mock.assert_called_once

    @patch("app.api.endpoints.suggestion_endpoint.get_suggestion_response_from_dict")
    @patch("app.api.services.rate_suggestions.RateSuggestions.calculate_distance")
    @patch("app.api.endpoints.suggestion_endpoint.model_list_to_dict")
    @patch("app.api.repository.geoname_repository.GeoNameRepository.filter_geonames")
    def test_get_suggestions_without_params(
        self,
        filter_geonames_mock: Mock,
        model_list_to_dict_mock: Mock,
        calculate_distance_mock: Mock,
        get_suggestion_response_from_dict_mock: Mock,
        client: TestClient,
        geoname_db_objects,
    ):
        filter_geonames_mock.return_value = None
        params = {"q": "New York"}
        response = client.get("/suggestions", params=params)
        assert response.status_code == 200
        assert response.json() == {"suggestions": []}
        assert filter_geonames_mock.assert_called_once
        assert model_list_to_dict_mock.assert_not_called
        assert calculate_distance_mock.assert_not_called
        assert get_suggestion_response_from_dict_mock.assert_not_called

    @patch("app.api.repository.geoname_repository.GeoNameRepository.filter_geonames")
    def test_get_suggestions_with_errors(
        self,
        filter_geonames_mock: Mock,
        client: TestClient,
        geoname_db_objects,
    ):
        filter_geonames_mock.return_value = "None"
        params = {"q": "New York"}
        response = client.get("/suggestions", params=params)
        assert response.status_code == 500
        assert response.json() == {"detail": "Internal server error"}
