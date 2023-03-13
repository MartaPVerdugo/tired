""" Send tired message whenever the time is 0 and 30 minutes past the hour."""
import datetime


def check_tired():
    time_now = datetime.datetime.now().time()
    if 00 <= time_now.minute < 30:
        return True
