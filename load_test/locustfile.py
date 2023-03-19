import random
from locust import HttpUser, task, between

class JSONPlaceholderUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def fetch_post(self):
        post_id = random.randint(1, 100)
        self.client.get(f"/posts/{post_id}")
