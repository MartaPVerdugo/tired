""" Send tired message whenever the time is 0 and 30 minutes past the hour."""
import datetime
import time

time_now = datetime.datetime.now().time()


def tired():
    tired_message = "I'm tired, go away"
    print(tired_message)


while 00 <= time_now.minute < 30:
    print(time_now.minute)
    time.sleep(3)
    tired()
