class Account:
    """A model for the users account.

        This class gives all data for the account of a user.

        :param username: self-explaining
        :param password: self-explaining
        :param uid: The unique unambiguous identifier for the user
        :param admin: Indicates if the account is an administrator for the chat
        :param accepted: Indicates if the account got accepted for joining the chat by a chat admin
        :param banned: self-explaining
        :type username: str
        :type uid: int
        :type password: str
        :type admin: bool
        :type accepted: bool
        :type banned: bool
        """
    # TODO encrypt password/make as hash

    def __init__(self, username: str, password: str, uid: int, admin: bool = False, accepted: bool = False, banned: bool = False):
        self.username = username
        self.password = password
        self.uid = uid
        self.admin = admin
        self.accepted = accepted
        self.banned = banned

    def __str__(self):
        return self.username

    def ban(self):
        """Set the ban status of the user to True. This won't allow the user to join the chat anymore."""
        self.banned = True

    def unban(self):
        """Set the ban status of the user to False. This will revoke the ban."""
        self.banned = False

    def accept(self):
        """Accept the user for joining the chat"""
        self.accepted = True

    def decline(self):
        """Set the banned status of the user to True and the accepted status will remain on False."""
        self.banned = True
