import string
import random
import pyperclip

from user import User

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

    def generate_password(size=10, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        Method to generate password
        '''
        generate_pass = ''.join(random.choice(char) for _ in range(size))
        return generate_pass

    @classmethod
    def check_user(cls, first_name, password):
        '''
        A method to check if account matches password
        '''
        current_user = ''
        for user in User.user_list:
            if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
            return current_user

    @classmethod
    def display_credentials(cls, user_name):
        '''
        A method to display credentials saved
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return user_credentials_list

    @classmethod
    def find_by_account_name(cls, account_name):
        '''
        A method to find credentials by the name of the account
        '''
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def copy_credentials(cls, account_name):
        '''
        A method to copy credentials
        '''
        copy_credential = Credentials.find_by_account_name(account_name)
        return pyperclip.copy(copy_credential.password)

