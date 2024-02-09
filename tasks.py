import schedule
import time
import requests

def make_request():
    requests.get("https://aws-https-midleware.onrender.com/")
    print(f"Wake Up! - {time.ctime()}")

schedule.every().minute.do(make_request)

while True:
    schedule.run_pending()
    time.sleep(1)
