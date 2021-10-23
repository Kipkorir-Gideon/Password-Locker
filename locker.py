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