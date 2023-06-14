from locust import HttpUser, task, between
import json
from sample import generate_text
import fire

class PerformanceTests(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def stress_test(self):
        res = self.client.post("/generate-text", json={"start": "london"})
        print(res.text)

def use_model(start):
    output_text = generate_text(start)
    for i in output_text:
        print(i)
        print("\n\n")

if __name__ == "__main__":
    fire.Fire(use_model)

    
