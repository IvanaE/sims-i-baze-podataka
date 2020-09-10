import mysql.connector

class MysqlConnection:
    __instance = None
    @staticmethod
    def getInstance():
        if MysqlConnection.__instance == None:
            MysqlConnection()
        return MysqlConnection.__instance

    def __init__(self):
        if MysqlConnection.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.cnx = mysql.connector.connect(user='root', password='',
                                               host='localhost',
                                               database='visokoskolska_ustanova_test')


            MysqlConnection.__instance = self


