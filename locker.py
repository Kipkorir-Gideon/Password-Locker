from user import User
from credentials import Credentials

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

def remove_user(user):
    '''
    A method to remove saved user
    '''
    User.remove_user()

def checks_user(user_name, password):
    '''
    A method to check user if it exists
    '''
    checking_user = Credentials.check_user(user_name, password)
    return checking_user

def generate_password():
    '''
    A method to generate password
    '''
    generate_pass = Credentials.generate_password()
    return generate_pass

def create_credentials(user_name, account_name, password):
    '''
    A method to create user credentials
    '''
    new_credential = Credentials(user_name, account_name, password)
    return new_credential

def save_credentials(credentials):
    '''
    A method to save new credentials
    '''
    Credentials.save_credential(credentials)

def display_credentials(user_name):
    '''
    A method to display user's credential
    '''
    return Credentials.display_credentials(user_name)

def copy_credentials(account_name):
    '''
    A method to copy credentials
    '''
    return Credentials.copy_credentials(account_name)


def main():
    print(' ')
    print('Hi, Welcome to Password_Locker app.')
    while True:
        print('Use the following codes to use the app: \n ca - Create an Account \n li - Log In \n ex - Exit')
        short_code = input('Enter your option: ').lower().strip()
        if short_code == 'ca':
            print('Create a new account.')
            first_name = input('Enter your first name: ').strip()
            last_name = input('Enter your last name: ').strip()
            password = input('Enter your password: ').strip()
            save_user(create_user(first_name, last_name, password))
            print(' ')
            print(f'Account created. \n First name: {first_name} \n Last name: {last_name} \n Password: {password}')

        