import pymysql

connection = None

try:
    connection = pymysql.connect(
        host="localhost",
        user="sql_helper",
        password="PoojaSql@2026",
        database="sql_query_helper1"
    )

    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM employees")
        total = cursor.fetchone()[0]

    print("MySQL connection successful!")
    print("Total employees:", total)

except pymysql.MySQLError as error:
    print("Connection error:", error)

finally:
    if connection is not None:
        connection.close()
