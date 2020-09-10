import sys
from app import App
from util.mysql_connection import MysqlConnection

if __name__ == "__main__":
    try:
        MysqlConnection.getInstance()
    except Exception as e:
        print(e)
    
    app = App()
    app.start()

    sys.exit(app.exec_())
