from PySide2.QtCore import QAbstractListModel, Qt


class ListDockModel(QAbstractListModel):

    modelHandler = None

    def __init__(self, parent = None):
        QAbstractListModel.__init__(self, parent)

    def init(self, modelHandler):
        self.modelHandler = modelHandler

    def data(self, index, role):

        if self.modelHandler == None:
            return None

        if role == Qt.DisplayRole:
            return self.modelHandler.models[index.row()].name

    def rowCount(self, index):

        if self.modelHandler == None:
            return 0

        return len(self.modelHandler.models)