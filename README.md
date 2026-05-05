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

## Project Structure

```
postman-clone/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── core/
│   ├── client.py         # HTTP engine
│   └── history.py        # request history
│
├── ui/
│   ├── main_window.py    # root window and layout
│   ├── request_panel.py  # request input panel
│   └── worker.py         # background thread for HTTP calls
│
├── tests/
│   ├── test_client.py
│   └── test_history.py
│
├── data/
│   └── history.json      # auto-generated, gitignored
│
├── main.py
├── requirements.txt
└── DEV_NOTES.md
```

## Getting Started

**1. Clone the repo**

```bash
git clone https://github.com/your-username/postman-clone.git
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

