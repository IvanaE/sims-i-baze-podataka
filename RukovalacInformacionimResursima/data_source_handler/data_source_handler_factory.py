from data_source_type import DataSourceType
from data_source_handler.serial_handler import SerialHandler
from data_source_handler.seq_handler import SeqHandler

class DataSourceHandlerFactory:

    def getHandler(self, type):

        if type == DataSourceType.SERIAL:
            return SerialHandler()
        if type == DataSourceType.SEQ:
            return SeqHandler()