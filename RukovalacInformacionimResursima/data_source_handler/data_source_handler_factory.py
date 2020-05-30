from data_source_handler.serial_handler import SerialHandler
from data_source_type import DataSourceType

class DataSourceHandlerFactory:

    def getHandler(self, type):

        if type == DataSourceType.SERIAL:
            return SerialHandler()