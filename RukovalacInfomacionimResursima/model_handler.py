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

        file = open('c:\\Users\\vasaandja\\Desktop\\N-7\\sims-bp-2019-version5g1-V7\models.txt', 'w')

        for model in self.models:
            print(model.metaModel)
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

        file = open('c:\\Users\\vasaandja\\Desktop\\N-7\\sims-bp-2019-version5g1-V7\models.txt', 'r')

        for line in file.readlines():
            data = line.strip().split('|')

            if len(data) == 0:
                break

            metaModel = self.metaModelHandler.findMetaModel(data[3])
            self.models.append(Model(data[0], metaModel,
                                     self.getDataSourceType(data[2]), data[1]))

        file.close()

        for model in self.models:
            print(model)
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