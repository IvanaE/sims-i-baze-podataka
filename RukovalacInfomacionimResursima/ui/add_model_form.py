from PySide2.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QComboBox

from data_source_type import DataSourceType


class AddModelForm(QDialog):

    def __init__(self, metaModelHandler, addModelOk, parent=None):
        super(AddModelForm, self).__init__(parent)

        self.metaModelHandler = metaModelHandler
        self.addModelOk = addModelOk

        # Create widgets
        self.name = QLineEdit("Name")
        self.source = QLineEdit("Source")
        self.button = QPushButton("ok")

        self.sourceTypeCB = QComboBox()
        self.sourceTypeCB.addItems(['Sequential', 'Serial'])

        self.metaModelCB = QComboBox()


        if self.metaModelHandler is not None:
            for metaModel in self.metaModelHandler.metaModels:
                self.metaModelCB.addItem(metaModel.name)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.name)
        layout.addWidget(self.source)
        layout.addWidget(self.sourceTypeCB)
        layout.addWidget(self.metaModelCB)

        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.ok)

    def ok(self):
        self.addModelOk(self.name.text(), self.source.text(),
                        str(self.sourceTypeCB.currentText()), str(self.metaModelCB.currentText()))