import mysql.connector


class Database:
    def __init__(self, host, user, password, database_name):
        self.connection = mysql.connector.connect(
            host=host,
            port=3306,
            user=user,
            database=database_name,
            password=password
        )
        self.cursor = self.connection.cursor()

    def query(self, sql, data):
        """
        Return a table of items selected by the query.
        :param sql:
        :param data:
        :return rows:
        """
        self.cursor.execute(sql, data)
        rows = self.cursor.fetchall()
        self.cursor.close()
        return rows

    def insert(self, sql, data):
        self.cursor.execute(sql, data)
        self.connection.commit()

    def close_all(self):
        self.cursor.close()
        self.connection.close()
