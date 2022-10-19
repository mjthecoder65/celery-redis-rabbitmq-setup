import time
from celery import Celery, shared_task
import requests

worker = Celery(__name__, broker="amqp://guest:guest@rabbitmq:5672/", backeend="redis://localhost:6379")


# This task will be executed by celery worker.
@worker.task(name="create_task")
def create_task(task_type: str):
    time.sleep(int(task_type) * 10)
    return True



# Fetching users.
@worker.task(name="fetch_posts")
def fetch_posts():
    # Simulate task that is going to take a long time.
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    return res.json()
