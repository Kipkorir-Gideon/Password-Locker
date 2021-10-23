class Credentials:
    '''
    A class for creating user credentials
    '''
    credentials_list = [] # An empty list for storing credentials

    def __init__(self, user_name, account_name, password):
        self.user_name = user_name
        self.account_name = account_name
        self.password = password

    def save_credential(self):
        '''
        A method to save a created credential
        '''
        Credentials.credentials_list.append(self)

    def remove_credential(self):
        '''
        A method to remove saved credential
        '''
        Credentials.credentials_list.remove(self)

