from PySide2.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout


class LoginForm(QDialog):

    def __init__(self, loginOk, userHandler, parent=None):
        super(LoginForm, self).__init__(parent)

        self.loginOk = loginOk
        self.userHandler = userHandler

        # Create widgets
        self.name = QLineEdit("Username")
        self.password = QLineEdit("Password")
        self.button = QPushButton("ok")

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.name)
        layout.addWidget(self.password)

        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.ok)

    def ok(self):

        user = self.userHandler.getUser(self.name.text(), self.password.text())

        if user != None:
            self.loginOk(user)
