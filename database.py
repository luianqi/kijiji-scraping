import psycopg2
from decouple import config


def openConnection():
    connection = psycopg2.connect(
        host=config("host"),
        database=config("database"),
        user=config("user"),
        password=config("password"),
    )

    return connection


def closeConnection(connection):
    connection.close()


def insertData(connection, ads, tableName):
    title = ads[0].replace("'", "")
    location = ads[1].replace("'", "")
    date = ads[2]
    description = ads[3].replace("'", "")
    beds = ads[4]
    picture = ads[5]
    price = ads[6]
    currency = ads[7]

    cursor = connection.cursor()
    insertSql = f"""
    insert into {tableName}(title, location, date, description, beds, picture, price, currency)
    values('{title}', '{location}', '{date}', '{description}', '{beds}', '{picture}', '{price}', '{currency}')
    """
    cursor.execute(insertSql)
    connection.commit()
