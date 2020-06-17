class Model:
    def __init__(self, name, metaModel, dataSourceType, dataSource, data = []):
        self.name = name
        self.metaModel = metaModel
        self.dataSourceType = dataSourceType
        self.dataSource = dataSource
        self.data = data