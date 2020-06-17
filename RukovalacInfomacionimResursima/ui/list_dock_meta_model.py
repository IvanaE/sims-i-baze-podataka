from PySide2.QtCore import QAbstractListModel, Qt


class ListDockMetaModel(QAbstractListModel):

    metaModelHandler = None

    def __init__(self, parent = None):
        QAbstractListModel.__init__(self, parent)

    def init(self, metaModelHandler):
        self.metaModelHandler = metaModelHandler

    def data(self, index, role):

        if self.metaModelHandler == None:
            return None

        if role == Qt.DisplayRole:
            return self.metaModelHandler.metaModels[index.row()].name

    def rowCount(self, index):

        if self.metaModelHandler == None:
            return 0

        return len(self.metaModelHandler.metaModels)