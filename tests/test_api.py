from fastapi.testclient import TestClient
from app.main import api

client = TestClient(api)


def test_api_should_get_a_calendar_response():
    # Act
    response = client.get("/calendar?start_date=2023-01-01&end_date=2023-01-02")

    # Assert
    assert response.status_code == 200
    assert len(response.json()) == 48
