from unittest.mock import patch
from core.collection_runner import run_collection

def test_request_passes_on_200():
    mock_result = {
        "status_code": 200,
        "elapsed_ms": 143,
        "body": {"id": 1},
        "error": None
    }

    collection = {
        "name": "Test Collection",
        "requests": [
            {
                "name": "Get todo",
                "method": "GET",
                "url": "https://fake-url.com",
                "headers": {},
                "body": None
            }
        ]
    }

    with patch("core.collection_runner.send_request", return_value=mock_result):
        results = run_collection(collection)

    assert results[0]["passed"] == True
    assert results[0]["status_code"] == 200

def test_request_passes_on_400():
    mock_result = {
        "status_code": 400,
        "elapsed_ms": 143,
        "body": {},
        "error": None
    }

    collection = {
        "name": "Test Collection",
        "requests": [
            {
                "name": "Get todo",
                "method": "GET",
                "url": "https://fake-url.com",
                "headers": {},
                "body": None
            }
        ]
    }

    with patch("core.collection_runner.send_request", return_value=mock_result):
        results = run_collection(collection)

    assert results[0]["passed"] == False
    assert results[0]["status_code"] == 400