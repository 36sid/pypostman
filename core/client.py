import requests

def send_request(method, url, headers=None, body=None, params=None):
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=body,
            params=params
        )
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
        return {
            "status_code": None,
            "headers": None,
            "body": None,
            "elapsed_ms": None,
            "error": f"Request failed: {type(e).__name__}"
        }
    return {
        "status_code": response.status_code,
        "headers": dict(response.headers),
        "body": response.json() if "application/json" in response.headers.get("Content-Type", "") else response.text,
        "elapsed_ms": response.elapsed.total_seconds() * 1000,
        "error": None
    }