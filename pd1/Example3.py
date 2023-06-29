import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


# EXAMPLE 3 - INSERT INTO TABLE

import datetime as dt

record = {
    'OrderDate': '2020-12-16',
    'Region': 'Central',
    'Rep': 'Johnson2',
    'Item': 'post-it-notes2',
    'Units': 220,
    'UnitCost': 2.5,
    'Total': 220 * 2.5,
}


def insert_new_record(record):
    try:
        db_name = 'tests'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """INSERT INTO abcreport ({}) VALUES ('{}', '{}', '{}', '{}', {}, {}, {})""".format(
            ', '.join(record.keys()),
            record['OrderDate'],
            record['Region'],
            record['Rep'],
            record['Item'],
            record['Units'],
            record['UnitCost'],
            record['Total'],
        )
        cur.execute(query)
        db_connection.commit()  # VERY IMPORTANT, otherwise, rows would not be added or reflected in the DB!
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    print("Record added to DB")


def main():
    # get_all_records()
    # get_all_records_for_rep('Morgan')
    insert_new_record(record)


if __name__ == '__main__':
    main()

