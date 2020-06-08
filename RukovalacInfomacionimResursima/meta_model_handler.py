from meta_data import MetaData
from meta_model import MetaModel

class MetaModelHandler:
    def __init__(self):
        self.metaModels = []

    def load(self):

        self.metaModels = []

        file = open('c:\\Users\\vasaandja\\Desktop\\Nada-4\\sims-bp-2019-version5g1\metaModels.txt', 'r')

        for line in file.readlines():
            data = line.strip().split('|')

            if len(data) == 0:
                break

            self.metaModels.append(MetaModel(data[0], data[1], []))

        file.close()

        file = open('c:\\Users\\vasaandja\\Desktop\\Nada-4\\sims-bp-2019-version5g1\metaData.txt', 'r')

        for line in file.readlines():
            data = line.strip().split('|')

            if len(data) == 0:
                break

            metaModel = self.findMetaModel(data[4])

            if metaModel == None:
                continue

            metaModel.metadata.append(MetaData(data[0], data[1], data[2], data[3]))


        file.close()

    def save(self):

        file = open('c:\\Users\\vasaandja\\Desktop\\Nada-4\\sims-bp-2019-version5g1\metaModels.txt', 'w')

        for model in self.metaModels:
            file.write(str(model.id) + '|' + model.name + '\n')

        file.close()

        file = open('c:\\Users\\vasaandja\\Desktop\\Nada-4\\sims-bp-2019-version5g1\metaData.txt', 'w')

        for model in self.metaModels:

            for data in model.metadata:
                file.write(data.name + '|' + data.columnName + '|' + data.type + '|'
                           + str(data.index) + '|' + str(model.id) + '\n')

        file.close()

    def findMetaModel(self, id):

        for model in self.metaModels:

            if model.id == id:
                return model

        return None

    def generateId(self):

        self.id = 1

        for model in self.metaModels:

            if int(model.id) > self.id:
                self.id = int(model.id)

        return self.id + 1

    def addMetaModel(self, name):

        self.metaModels.append(MetaModel(self.generateId(), name, []))

    def delete(self, metaModel):

        self.metaModels.remove(metaModel)

    def __str__(self):
        result = ''

        for model in self.metaModels:
            result += 'MetaMode:' + model.name + '\n'
            result += 'MetaData: \n'
            for data in model.metadata:
                result += 'name: ' + data.name + '\n'

        return result