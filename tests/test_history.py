import unittest.mock
from unittest.mock import patch
from core.history import load_history, save_request, delete_history

def test_load_empty_history():
    with patch("os.path.exists", return_value=False):
        result = load_history()
    assert result == []

def test_save_and_load():
    mock_result = {
        "status_code": 200,
        "elapsed_ms": 143,
        "body": {"id": 1}
    }
    with patch("builtins.open", unittest.mock.mock_open()):
        with patch("json.load", return_value=[]):
            with patch("json.dump") as mock_dump:
                save_request("GET", "https://fake.com", mock_result)
                assert mock_dump.called

def test_delete_history():
    mock_open_instance = unittest.mock.mock_open()
    with patch("builtins.open", mock_open_instance):
        with patch("json.dump") as mock_dump:
            delete_history()
            mock_dump.assert_called_with([], mock_open_instance(), indent=2)