import os
import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.users = {}
                for line in file:
                    email, password, name, created = line.strip().split(";")
                    self.users[email] = (password, name, created)
        else:
            self.users = {}

    def get_user(self, email):
        return self.users.get(email)

    def add_user(self, email, password, name):
        created = str(datetime.datetime.now())
        self.users[email] = (password, name, created)
        with open(self.filename, "a") as file:
            file.write(email + ";" + password + ";" + name + ";" + created + "\n")
