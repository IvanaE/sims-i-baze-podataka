from meta_data import MetaData


class MetaModel:
    def __init__(self, id, name, metadata = []):
        self.id = id
        self.name = name
        self.metadata = metadata

    def addMetaData(self):

        self.metadata.append(MetaData())