# -*- coding: utf-8 -*-
import os
import datetime
import logging
import codecs

LOG_PATH = 'log'

def init_logger(logger_name='logger'):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
    
    # stream
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    if not os.path.exists(LOG_PATH):
        os.makedirs(LOG_PATH)

    # file
    log_date = datetime.date.today().strftime('%Y%m%d')
    file_name = f'./{LOG_PATH}/{log_date}.log'
    if not os.path.exists(file_name):
        with codecs.open(file_name, 'w', 'utf-8') as f:
            f.write('')

    fh = logging.FileHandler(filename=file_name)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger

APP_LOGGER = init_logger()
DB_LOGGER = init_logger('db_logger')