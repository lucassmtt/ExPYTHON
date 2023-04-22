import pymysql
import dotenv
import os

dotenv.load_dotenv('.env')

connection = pymysql.connect(
    host=os.environ['MYSQL_USER'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_HOST'],
)

with connection:
    with connection.cursor() as cursor:
        # apply the SQL
        ...
    