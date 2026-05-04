import json
from ui.worker import RequestWorker
from core.client import send_request
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QComboBox, QPushButton, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyPostman")
        self.setFixedSize(800, 600)

         # central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # top bar
        top_bar = QHBoxLayout()
        self.method_dropdown = QComboBox()
        self.method_dropdown.addItems(["GET", "POST", "PUT", "DELETE", "PATCH"])
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL...")
        self.send_button = QPushButton("Send")
        top_bar.addWidget(self.method_dropdown)
        top_bar.addWidget(self.url_input)
        top_bar.addWidget(self.send_button)

        # response area
        self.response_area = QTextEdit()
        self.response_area.setReadOnly(True)
        self.response_area.setPlaceholderText("Response will appear here...")

        # add to main layout
        main_layout.addLayout(top_bar)
        main_layout.addWidget(self.response_area)

        self.send_button.clicked.connect(self.handle_send)
    
    def handle_send(self):
        self.send_button.setEnabled(False)
        self.send_button.setText("Sending...")

        method = self.method_dropdown.currentText()
        url = self.url_input.text()

        self.worker = RequestWorker(method, url)
        self.worker.finished.connect(self.display_response)
        self.worker.start()

    def display_response(self, result):
        if result["error"]:
            self.response_area.setText(f"Error: {result['error']}")
        else:
            body = result["body"]
            if isinstance(body, dict) or isinstance(body, list):
                formatted_body = json.dumps(body, indent=2)
            else:
                formatted_body = body

            self.response_area.setText(
                f"Status: {result['status_code']}\n"
                f"Time: {result['elapsed_ms']:.0f}ms\n\n"
                f"{formatted_body}"
            )

        self.send_button.setEnabled(True)
        self.send_button.setText("Send")