from data_source_handler.mysql_handler import MySqlHandler
from data_source_handler.seq_handler import SeqHandler
from data_source_handler.serial_handler import SerialHandler
from data_source_type import DataSourceType

class DataSourceHandlerFactory:

    def getHandler(self, type):

        if type == DataSourceType.SERIAL:
            return SerialHandler()
        if type == DataSourceType.SEQ:
            return SeqHandler()
        if type == DataSourceType.MYSQL:
            return MySqlHandler()
