from core.client import send_request

result = send_request("GET", "https://jsonplaceholder.typicode.com/todos/1")
print(result)