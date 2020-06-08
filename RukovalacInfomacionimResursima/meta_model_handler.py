from meta_data import MetaData
from meta_model import MetaModel

class MetaModelHandler:
    def __init__(self):
        self.metaModels = []

    def load(self):

        self.metaModels = []

        file = open('c:\\Users\\Ica\\Desktop\\sims-i-baze-podataka\\RukovalacInformacionimResursima\\metaModels.txt', 'r')

        for line in file.readlines():
            data = line.strip().split('|')

            if len(data) == 0:
                break

            self.metaModels.append(MetaModel(data[0], data[1], []))

        file.close()

        file = open('c:\\Users\\Ica\\Desktop\\sims-i-baze-podataka\\RukovalacInformacionimResursima\\metaData.txt', 'r')

        for line in file.readlines():
            data = line.strip().split('|')

            if len(data) == 0:
                break

            metaModel = self.findMetaModel(data[5])

            if metaModel == None:
                continue

            metaModel.metadata.append(MetaData(data[0], data[1], data[2], data[3], data[4]))


        file.close()

    def save(self):

        file = open('c:\\Users\\Ica\\Desktop\\sims-i-baze-podataka\\RukovalacInformacionimResursima\\metaModels.txt', 'w')

        for model in self.metaModels:
            file.write(model.id + '|' + model.name + '\n')

        file.close()

        file = open('c:\\Users\\Ica\\Desktop\\sims-i-baze-podataka\\RukovalacInformacionimResursima\\metaData.txt', 'w')

        for model in self.metaModels:

            for data in model.metadata:
                file.write(data.id + '|' + data.name + '|' + data.columnName + '|' + data.type + '|'
                           + str(data.index) + '|' + model.id + '\n')

        file.close()

    def findMetaModel(self, id):

        for model in self.metaModels:

            if model.id == id:
                return model

        return None

    def __str__(self):
        result = ''

        for model in self.metaModels:
            result += 'MetaMode:' + model.name + '\n'
            result += 'MetaData: \n'
            for data in model.metadata:
                result += 'name: ' + data.name + '\n'

        return result