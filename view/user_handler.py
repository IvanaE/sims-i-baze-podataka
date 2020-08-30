from PySide2.QtCore import QDir

from models.user import User


class UserHandler:
    def __init__(self):
        self.users = []
        self.user = None
        self.load()


    def load(self):

        self.users = []

        file = open(QDir.currentPath() + '/data/users.txt', 'r')

        for line in file.readlines():
            data = line.strip().split('|')

            if len(data) == 0:
                break

            self.users.append(User(data[0], data[1], data[2], data[3], data[4]))

        file.close()

    def save(self):

        file = open(QDir.currentPath() + '/data/users.txt', 'w')

        for user in self.users:
            file.write(str(user.firstName) + '|' + user.lastName + '|' + user.username + '|'
                       + user.password + '|' + user.type + '\n')

        file.close()

    def getUser(self, username, password):

        for user in self.users:

            if user.username == username and user.password == password:
                return user

        return None
