import psycopg2
#from dotenv import load_dotenv
#import os

connection = psycopg2.connect(
    database="dbname", user="username", password="pass", host="hostname", port=5432
)
