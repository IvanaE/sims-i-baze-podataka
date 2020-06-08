from data_source_type import DataSourceType
from model import Model


class ModelHandler:
    def __init__(self, metaModelHandler):
        self.models = []
        self.metaModelHandler = metaModelHandler

    def addModel(self, name, source, sourceType, metaModel):

        self.models.append(Model(name, metaModel, sourceType, source))

    def save(self):

        file = open('c:\\Users\\vasaandja\\Desktop\\Nada-4\\sims-bp-2019-version5g1\models.txt', 'w')

        for model in self.models:
            print(model.metaModel)
            file.write(model.name + '|' + model.dataSource + '|' + str(model.dataSourceType)
                       + '|' + str(model.metaModel.id) + '\n')

        file.close()



    def load(self):

        file = open('c:\\Users\\vasaandja\\Desktop\\Nada-4\\sims-bp-2019-version5g1\models.txt', 'r')

        for line in file.readlines():
            data = line.strip().split('|')

            if len(data) == 0:
                break

            metaModel = self.metaModelHandler.findMetaModel(data[3])
            self.models.append(Model(data[0], metaModel,
                                     self.getDataSourceType(data[2]), data[1]))

        file.close()

    def getDataSourceType(self, type):

        if type == 'DataSourceType.SEQ':
            return DataSourceType.SEQ
        if type == 'DataSourceType.SERIAL':
            return DataSourceType.SERIAL

        return DataSourceType.MYSQL

    def delete(self, model):

        self.models.remove(model)