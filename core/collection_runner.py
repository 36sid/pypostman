from core.client import send_request

def run_collection(collection):
    results = []

    for request in collection["requests"]:
        result = send_request(
            method=request["method"],
            url=request["url"],
            headers=request.get("headers"),
            body=request.get("body")
        )

        passed = (
            result["status_code"] is not None and
            200 <= result["status_code"] < 300
        )

        results.append({
            "name": request["name"],
            "method": request["method"],
            "url": request["url"],
            "status_code": result["status_code"],
            "elapsed_ms": result["elapsed_ms"],
            "passed": passed,
            "error": result["error"]
        })

    return results