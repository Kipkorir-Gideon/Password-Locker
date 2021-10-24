from user import User
from credentials import Credentials
import random

def create_user(first_name, last_name, password):
    '''
    a method to create a user account
    '''
    new_user = User(first_name, last_name, password)
    return new_user

def save_user(user):
    '''
    A method to save a user
    '''
    User.save_user(user)

def checks_user(user_name, password):
    '''
    A method to check user if it exists
    '''
    checking_user = Credentials.check_user(user_name, password)
    return checking_user