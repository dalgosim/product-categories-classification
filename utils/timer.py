# -*- coding: utf-8 -*-
import time
import datetime
import random

def random_sleep(min_delay=0.1):
    time.sleep(min_delay + random.randrange(1, 9)/10)

def get_now(time_format='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.now().strftime(time_format)

def str2date(str_date, date_format='%Y-%m-%d'):
    if isinstance(str_date, str):
        return datetime.datetime.strptime(str_date, date_format)
    else:
        return str_date

def date2str(_date, date_format='%Y-%m-%d'):
    return _date.strftime(date_format)

def get_yesterday(time_format='%Y-%m-%d %H:%M:%S'):
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    return yesterday.strftime(time_format)

def get_now_hour():
    return datetime.datetime.now().hour

def add_date(str_date, delta_day, date_format='%Y-%m-%d'):
    _date = str2date(str_date, date_format)
    if delta_day > 0:
        _date = _date + datetime.timedelta(days=delta_day)
    else:
        _date = _date - datetime.timedelta(days=abs(delta_day))
    return _date.strftime(date_format)