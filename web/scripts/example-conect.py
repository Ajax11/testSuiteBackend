import psycopg2

# from dotenv import load_dotenv
# import os

connection = psycopg2.connect(
    database="dbname", user="username", password="pass", host="hostname", port=5432
)

DATABASE_PASSWORD_TRIPLET = "SuperSecret123!"
SECRET_KEY = "django-insecure-1234567890abcdefghijklmn"
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


SECRET_KEY = "Tango-insecure-%fhf@r@7i_@j^9$s!_-fy="
