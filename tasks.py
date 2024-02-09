import schedule
import time
import requests

def wake_up_task():
    requests.get("https://aws-https-midleware.onrender.com/")
    print(f"Wake Up! - {time.ctime()}")

schedule.every(30).seconds.do(wake_up_task)

while True:
    schedule.run_pending()
    time.sleep(1)
