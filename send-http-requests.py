import requests
import time

ALB_URL = "http://ecs-demo-alb-1268306410.ap-southeast-1.elb.amazonaws.com"

def simulate_traffic():
    while True:
        try:
            response = requests.get(ALB_URL)
            if response.status_code == 200:
                print("Request successful")
            else:
                print(f"Request failed with status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

if __name__ == "__main__":
    while True:
        simulate_traffic()
        time.sleep(0.01)  # Adjust the interval as needed
