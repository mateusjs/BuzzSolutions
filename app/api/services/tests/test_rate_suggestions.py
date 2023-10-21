from typing import List
from unittest.mock import Mock, patch

import pytest
from geopy.distance import geodesic
from app.api.services.rate_suggestions import RateSuggestions
from app.models.geolocation import GeoLocation


class TestRateSuggestions:
    @patch("app.api.services.rate_suggestions.RateSuggestions._sort_by_score")
    @patch("app.api.services.rate_suggestions.RateSuggestions._get_score_by_distance")
    def test_calculate_distance(
        self,
        get_score_by_distance_mock: Mock,
        sort_by_score_mock: Mock,
        geonames_data: List[dict],
    ):
        RateSuggestions(
            query_location=GeoLocation(latitude=40.8000, longitude=-74.0060),
            geonames=geonames_data,
        ).calculate_distance()

        get_score_by_distance_mock.assert_called_once
        sort_by_score_mock.assert_called_once

    @patch("app.api.services.rate_suggestions.RateSuggestions._sort_by_score")
    @patch("app.api.services.rate_suggestions.RateSuggestions._get_score_by_distance")
    @patch("app.api.services.rate_suggestions.geodesic")
    def test_calculate_distance_error(
        self,
        geodesic_mock: Mock,
        get_score_by_distance_mock: Mock,
        sort_by_score_mock: Mock,
    ):
        with pytest.raises(Exception):
            RateSuggestions(
                query_location=GeoLocation(latitude=40.8000, longitude=-74.0060),
                geonames=None,
            ).calculate_distance()

        geodesic_mock.assert_not_called
        get_score_by_distance_mock.assert_not_called
        sort_by_score_mock.assert_not_called

    @pytest.mark.parametrize(
        "distance, max_distance, expected_score",
        [(12, 12, 0.0), (13, 12, 0.08), (14, 12, 0.17), (1, 12, 0.92)],
    )
    def test_get_score_by_distance(
        self, distance, max_distance, expected_score, geonames_data: List[dict]
    ):
        geonames_data[0]["distance"] = distance
        geonames_data[1]["distance"] = distance
        RateSuggestions(
            query_location=GeoLocation(latitude=40.8000, longitude=-74.0060),
            geonames=geonames_data,
        )._get_score_by_distance(max_distance)

        assert geonames_data[0]["score"] == expected_score
        assert geonames_data[1]["score"] == expected_score

    def test_get_score_by_distance_error(self):
        with pytest.raises(Exception):
            RateSuggestions(
                query_location=GeoLocation(latitude=40.8000, longitude=-74.0060),
                geonames=None,
            )._get_score_by_distance(0)

    @pytest.mark.parametrize(
        "geonames, expected_scores",
        [
            ([], []),
            (
                [
                    {"latitude": 37.12898, "longitude": -84.08326, "score": 0.8},
                    {"latitude": 38.93345, "longitude": -76.54941, "score": 0.9},
                    {"latitude": 39.88645, "longitude": -83.44825, "score": 0.7},
                ],
                [0.9, 0.8, 0.7],
            ),
            (
                [
                    {"latitude": 37.12898, "longitude": -84.08326, "score": 0.7},
                    {"latitude": 38.93345, "longitude": -76.54941, "score": 0.9},
                    {"latitude": 39.88645, "longitude": -83.44825, "score": 0.8},
                ],
                [0.9, 0.8, 0.7],
            ),
        ],
    )
    def test_sort_by_score(self, geonames, expected_scores):
        rate_suggestions = RateSuggestions(
            query_location=GeoLocation(0, 0), geonames=geonames
        )

        rate_suggestions._sort_by_score()

        for geo_name, expected_score in zip(rate_suggestions.geonames, expected_scores):
            assert geo_name["score"] == expected_score

    def test_sort_by_score(self):
        geonames = [
            {"latitude": 37.12898, "longitude": -84.08326},
            {"latitude": 38.93345, "longitude": -76.54941, "score": 0.9},
            {"latitude": 39.88645, "longitude": -83.44825, "score": 0.8},
        ]
        rate_suggestions = RateSuggestions(
            query_location=GeoLocation(0, 0), geonames=geonames
        )

        with pytest.raises(Exception):
            rate_suggestions._sort_by_score()
