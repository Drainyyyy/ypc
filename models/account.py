class Account:
    def __init__(self, username: str, password: str, admin: bool = False):
        self.username = username
        self.password = password
        self.admin = admin
