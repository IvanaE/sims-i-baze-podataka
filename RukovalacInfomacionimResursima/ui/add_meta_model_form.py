from PySide2.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout


class AddMetaModelForm(QDialog):

    def __init__(self, metaModelHandler, addMetaModelOk, parent=None):
        super(AddMetaModelForm, self).__init__(parent)

        self.metaModelHandler = metaModelHandler
        self.addMetaModelOk = addMetaModelOk

        # Create widgets
        self.name = QLineEdit("Name")
        self.button = QPushButton("ok")

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.name)

        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.ok)

    def ok(self):
        self.addMetaModelOk(self.name.text())