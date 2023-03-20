import mysql.connector

SQL_HOST = "sql7.freesqldatabase.com"
DATABASE_USER = "sql7606287"
DATABASE_PASSWORD = "kGMMHFUyl6"
DATABASE_NAME = "sql7606287"
TABLE_NAME = 'users'

mail_user = ''
SQL_QUERY = f'SELECT * FROM {TABLE_NAME} WHERE mail="{mail_user}";'


def request(sql_req, result = False):
    try:
        with mysql.connector.connect(host=SQL_HOST,
                                         user=DATABASE_USER,
                                         password=DATABASE_PASSWORD,
                                         database=DATABASE_NAME
                                         ) as con:
            # cursor object
            cursor = con.cursor()
            # execute query
            cursor.execute(sql_req)
            if result:
                query_result = cursor.fetchall()
                return query_result

    except Exception as err:
        print("Error: ", err)
        return False
