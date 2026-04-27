from unittest.mock import patch, MagicMock
from core.client import send_request

def test_successful_get_request():
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.headers = {"Content-Type": "application/json"}
    mock_response.json.return_value = {"id": 1, "title": "todo"}
    mock_response.elapsed.total_seconds.return_value = 0.143

    with patch("core.client.requests.request", return_value=mock_response):
        result = send_request("GET", "https://fake-url.com")

    assert result["error"] is None
    assert result["status_code"] == 200
    assert result["body"] == {"id": 1, "title": "todo"}