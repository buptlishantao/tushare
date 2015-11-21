import sys
import time
import datetime

def get_today_str():
    today = datetime.date.today()
    return today.strftime("%Y-%m-%d")


if __name__ == '__main__':
    print get_today_str()


