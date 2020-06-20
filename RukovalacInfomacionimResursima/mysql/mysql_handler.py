from os import path
import pickle
import pymysql

from serijska.data_handler import DataHandler


class MySqlHandler(DataHandler):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.key = self.model.metaModel.key
        self.data = []
        self.connection = None


    def load_data(self):


        self.connection = pymysql.connect(host='lockalhost', user='root',
                                          db='projekat', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

        try:
            with self.connection.cursor() as cursor:
                cursor.execute('SELECT * FROM ' + self.model.dataSource)
                self.data = cursor.fetchall()
        finally:
            self.connection.close()

    def get_one(self, id):

        self.connection = pymysql.connect(host='lockalhost', user='root',
                                          db='projekat', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

        try:
            with self.connection.cursor() as cursor:
                cursor.execute('SELECT * FROM ' + self.model.dataSource + ' WHERE ' +
                               self.key + ' = ' + id)
                return cursor.fetchone()
        finally:
            self.connection.close()
            return None

    def get_all(self):
        return self.data

    def insert(self, obj):
        self.connection = pymysql.connect(host='lockalhost', user='root',
                                          db='projekat', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

        try:
            with self.connection.cursor() as cursor:

                query = 'INSERT INTO ' + self.model.dataSource + '(' + ''

                for key in obj:
                    query += key + ','

                query = query[:-1]
                query = query + ') VALEUS ('

                for key in obj:
                    query += obj[key] + ','

                query = query[:-1]
                query = query + ')'

                cursor.execute(query)
                self.connection.commit()
        finally:
            self.connection.close()
            return None

    def edit(self, obj):
        self.connection = pymysql.connect(host='lockalhost', user='root',
                                          db='projekat', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

        try:
            with self.connection.cursor() as cursor:

                query = 'UPDATE ' + self.model.dataSource + 'SET '

                for key in obj:
                    query += key + ' = ' + obj[key] + ','

                query = query[:-1]
                query = query + ' WHERE ' + self.key + ' = ' + obj[self.key]

                cursor.execute(query)
        finally:
            self.connection.close()
            return None

    def insert_many(self, list):

        for item in list:
            self.insert(item)

    def delete_one(self, obj):
        self.connection = pymysql.connect(host='lockalhost', user='root',
                                          db='projekat', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

        try:
            with self.connection.cursor() as cursor:

                query = 'DELETE FROM ' + self.model.dataSource + ' WHERE ' + self.key + ' = ' + obj[self.key]

                cursor.execute(query)
        finally:
            self.connection.close()
            return None






