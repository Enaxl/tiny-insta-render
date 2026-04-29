from locust import HttpUser, task, between
import random

class TinyInstaUser(HttpUser):
    wait_time = between(0.5, 1.5)

    @task
    def view_timeline(self):
        user_id = random.randint(0, 999)
        self.client.get(f"/api/timeline?user=test1_user{user_id}&limit=20")
