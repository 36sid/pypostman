from PyQt6.QtCore import QThread, pyqtSignal
from core.client import send_request

class RequestWorker(QThread):
    finished = pyqtSignal(dict)

    def __init__(self, method, url, headers=None, body=None):
        super().__init__()
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body

    def run(self):
        result = send_request(self.method, self.url, self.headers, self.body)
        self.finished.emit(result)