import schedule
import time

def make_request():
    print("Wake Up!")

schedule.every().minute.do(make_request)

while True:
    schedule.run_pending()
    time.sleep(1)
