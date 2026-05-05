# PyPostman

A lightweight API client built with Python and PyQt6. Send HTTP requests, inspect responses, and track request history — all from a native desktop UI.

---

## Features

- Send HTTP requests — GET, POST, PUT, DELETE, PATCH
- Set custom request headers via a key-value table
- Send JSON request bodies
- Pretty-printed JSON responses
- Request history saved locally
- Threaded requests — UI stays responsive while waiting for a response

## Tech Stack

- **UI** — PyQt6
- **HTTP** — requests
- **Testing** — pytest
- **CI** — GitHub Actions


## Getting Started

**1. Clone the repo**

```bash
git clone https://github.com/36sid/postman-clone.git
cd postman-clone
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv

# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the app**

```bash
python main.py
```

## Running Tests

```bash
pytest tests/ -v
```

## CI

Every push to any branch triggers a GitHub Actions workflow that installs dependencies and runs the full test suite.

