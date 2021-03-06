import os
from decouple import config

DEBUG = True

# Database
if DEBUG:
    SERVER = 'localhost'
    DATABASE_NAME = 'postgres'
    USERNAME = 'postgres'
    PASSWORD = '1234'
    PORT = '5432'
else:
    SERVER = 'taplock.app'
    DATABASE_NAME = 'cdos'
    USERNAME = 'cdos'
    PASSWORD = '1234'
    #PASSWORD = config('PROD_DB_PASSWORD')
    PORT = '5432'

DATABASE_CONNECTION = f'postgresql://{USERNAME}:{PASSWORD}@{SERVER}:{PORT}/{DATABASE_NAME}'


