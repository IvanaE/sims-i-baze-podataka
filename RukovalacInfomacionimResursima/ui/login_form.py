from PySide2.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout


class LoginForm(QDialog):

    def __init__(self, loginOk, parent=None):
        super(LoginForm, self).__init__(parent)

        self.loginOk = loginOk

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

        if self.name.text() == 'admin' and self.password.text() == 'admin':
            self.loginOk()