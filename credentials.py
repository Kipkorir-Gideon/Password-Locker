class Credentials:
    '''
    A class for creating user credentials
    '''
    credentials_list = [] # An empty list for storing credentials

    def __init__(self, user_name, account_name, password):
        self.user_name = user_name
        self.account_name = account_name
        self.password = password

