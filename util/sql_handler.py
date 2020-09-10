from util.file_handler import FileHandler
import json
import mysql.connector


def get_connection(new_user, new_password, new_host, new_database):
    return mysql.connector.connect(user= new_user, password=new_password,
                                        host=new_host,
                                        database=new_database)

class SqlHandler(FileHandler):
    def __init__(self, table, key, metapath):
        super().__init__()
        try:
            self.table = table
            self.key = key
            self.metapath = metapath

            with open(self.metapath, "rb") as metadata:
                db_metadata = json.load(metadata)

            self.connection = get_connection(db_metadata["user"], db_metadata["password"], db_metadata["host"], db_metadata["database"])
            self.cursor = self.connection.cursor()
            self.data = self.load_data()
            self.column_names = self.cursor.column_names

        except mysql.connector.Error as err: 
            self.connection.close()

    def __exit__(self, type__, value, traceback):
        self.close()

    def __enter__(self):
        return self

    def complete(self):
        self.__complete = True

    def close(self):
        if self.connection:
            try:
                if self.__complete:
                    self.connection.commit()
                else:
                    self.connection.rollback()
            except Exception as e:
                raise Exception()
            finally:
                try:
                    self.connection.close()
                except Exception as e:
                    raise Exception()

    
    def get_one(self, id):
        try:
            self.cursor.execute("SELECT * FROM "+ self.table +" WHERE " + self.key + " = " + id)
            result = self.cursor.fetchall() 
            self.connection.commit()
            return result
        except mysql.connector.Error as err:
            pass


    def load_data(self):
        return self.get_all()

    def get_all(self):
        try:
            self.cursor.execute("SELECT * FROM  " + self.table)
            result = self.cursor.fetchall() 
            self.connection.commit()
            return result
        except mysql.connector.Error as err:
            pass
    
    def edit(self, obj, col, value):
        try:
            self.cursor.execute("UPDATE " + self.table + " SET " + col + " = '" + value + "' WHERE " + self.key + " = '" + str(obj[0]) + "'")
            self.connection.commit()

        except mysql.connector.Error as err:
            pass
            self.connection.rollback()
            self.connection.close()

    def insert(self, obj):
        try:
            inserted = self.cursor.execute("INSERT INTO " + self.table + " values " + " ( '" + "','".join(obj) + "' )")
            self.connection.commit()
            return inserted
        except mysql.connector.Error as err:

            self.connection.rollback()
            self.connection.close()

            raise err

    def insert_many(self, obj):
        for i in obj:
            self.insert(i)

    def delete_one(self, id):
        try:
            self.cursor.execute("DELETE FROM " + self.table + " WHERE " + self.key + " = '" + str(id) + "'")
            self.connection.commit()
        except mysql.connector.Error as err:
            self.connection.rollback()
            self.connection.close()

    
    def save(self, obj):
        pass