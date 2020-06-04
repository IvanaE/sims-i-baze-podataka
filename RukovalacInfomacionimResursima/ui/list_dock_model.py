from PySide2.QtCore import QAbstractListModel, Qt


class ListDockModel(QAbstractListModel):

    models = None

    def __init__(self, parent = None):
        QAbstractListModel.__init__(self, parent)

    def init(self, models):
        self.models = models

    def data(self, index, role):

        if self.models == None:
            return None

        if role == Qt.DisplayRole:
            return self.models[index.row()].name

    def rowCount(self, index):

        if self.models == None:
            return 0

        return len(self.models)