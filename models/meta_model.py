from models.meta_data import MetaData


class MetaModel:
    def __init__(self, id, name, key, metadata = []):
        self.id = id
        self.name = name
        self.metadata = metadata
        self.key = key

    def addMetaData(self):

        self.metadata.append(MetaData())