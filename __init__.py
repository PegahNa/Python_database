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

# EXAMPLE 2

def calc_sum(sold_items):
    sales = []

    for item in sold_items:
        sales.append(item[2])

    commission = sum(sales)
    return commission


def get_all_records_for_rep(rep_name):
    try:
        db_name = 'tests'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """SELECT Item, Units, Total FROM abcreport WHERE Rep = '{}'""".format(
            rep_name)  # note extra speechmarks around the curly brakets -- we need them!
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple

        for i in result:
            print(i)

        cur.close()

        comp = calc_sum(result)

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    print("Sum for {} is £{}".format(rep_name, comp))
    return rep_name, comp

def main():
    #get_all_records()
     get_all_records_for_rep('Morgan')
    #insert_new_record(record)


if __name__ == '__main__':
    main()