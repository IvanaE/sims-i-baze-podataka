from PySide2.QtCore import QDir

from data_source_type import DataSourceType
from model import Model
from sekvencijalna.sequential_file_handler import SequentialFileHandler
from serijska.serial_file_handler import SerialFileHandler


class ModelHandler:
    def __init__(self, metaModelHandler):
        self.models = []
        self.metaModelHandler = metaModelHandler

    def addModel(self, name, source, sourceType, metaModel):

        self.models.append(Model(name, metaModel, sourceType, source))

    def save(self):

        file = open(QDir.currentPath() + '/models.txt', 'w')

        for model in self.models:
            file.write(model.name + '|' + model.dataSource + '|' + str(model.dataSourceType)
                       + '|' + str(model.metaModel.id) + '\n')

        file.close()

        for model in self.models:
            if model.dataSourceType == DataSourceType.SERIAL:
                handler = SerialFileHandler(model)
                handler.save()
            elif model.dataSourceType == DataSourceType.SEQ:
                handler = SequentialFileHandler(model)
                handler.save()

    def load(self):

        file = open(QDir.currentPath() + '/models.txt', 'r')

        for line in file.readlines():
            data = line.strip().split('|')

            if len(data) == 0:
                break

            metaModel = self.metaModelHandler.findMetaModel(data[3])
            self.models.append(Model(data[0], metaModel,
                                     self.getDataSourceType(data[2]), data[1]))

        file.close()

        for model in self.models:
            if model.dataSourceType == DataSourceType.SERIAL:
                handler = SerialFileHandler(model)
                handler.load_data()
                model.data = handler.get_all()
            elif model.dataSourceType == DataSourceType.SEQ:
                handler = SequentialFileHandler(model)
                handler.load_data()
                model.data = handler.get_all()

    def getDataSourceType(self, type):

        if type == 'DataSourceType.SEQ':
            return DataSourceType.SEQ
        if type == 'DataSourceType.SERIAL':
            return DataSourceType.SERIAL

        return DataSourceType.MYSQL

    def delete(self, model):

        self.models.remove(model)

    def getModelFromFile(self, fileName, type):

        for model in self.models:

            if model.dataSource == fileName and type == model.dataSourceType:
                return model

        return None

    def getModelWithName(self, name):

        for model in self.models:

            if model.name == name:
                return model

        return None