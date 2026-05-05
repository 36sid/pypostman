import json
import os
from datetime import datetime

HISTORY_FILE = "data/history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            content = f.read()
            if not content.strip():
                return []
            return json.loads(content)
    else:
        return []

def save_request(method, url, result):
    history = load_history()
    entry = {
        "method" : method,
        "url" : url,
        "status_code" : result["status_code"],
        "elapsed_ms" : result["elapsed_ms"],
        "timestamp" : datetime.now().isoformat(),
        "body" : result["body"]
    }
    history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def delete_history():
    history = []
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)