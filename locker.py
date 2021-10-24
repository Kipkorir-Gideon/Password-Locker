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
    User.remove_user(user)

def checks_user(first_name, password):
    '''
    A method to check user if it exists
    '''
    checking_user = Credentials.check_user(first_name, password)
    return checking_user

def display_user():
    '''
    Method to display saved users
    '''
    return User.user_list

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

def check_credential(account_name):
    '''
    Method to check existence of credential
    '''
    return Credentials.credential_exist(account_name)

def display_credentials(user_name):
    '''
    A method to display user's credential
    '''
    return Credentials.display_credentials(user_name)

def delete_credentials(account_name):
    
    '''
    Method to delete credentials
    '''
    Credentials.delete_credentials(account_name)

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

        elif short_code == 'li':
            print(' ')
            print('Enter your account details to log in.')
            user_name = input('Enter your first name: ').strip()
            password = str(input('Enter your password: '))
            user_exist = checks_user(user_name, password)
            if user_exist == user_name:
                print(' ')
                print(f'Welcome {user_name}. What do you want to do?')
                print(' ')
                while True:
                    print('Choose from the codes below: \n cc - Create credential \n dc - display credentials \n dl - Delete credential \n cp - Copy password \n ex - Exit')
                    short_code = input('Enter code: ').lower().strip()
                    if short_code == 'cc':
                        print(' ')
                        print('Enter credentials: ')
                        accout_name = input('Enter account name: ').strip()
                        while True:
                            print(' ')
                            print('Choose an option for password: \n ep - An existing password \n gp - Generate password \n ex - Exit')
                            pass_option = input('Enter your option: ').lower().strip()
                            if pass_option == 'ep':
                                print(' ')
                                password = input('Enter your password: ').strip()
                                break
                            elif pass_option == 'gp':
                                password = generate_password()
                                break
                            elif pass_option == 'ex':
                                break
                            else:
                                print('Wrong option. Try again.')
                        save_credentials(create_credentials(user_name, accout_name, password))
                        print(' ')
                        print(f'Credentials created; \n Account name: {accout_name} \n Password: {password}')
                        print(' ')

                    elif short_code == 'dc':
                        print(' ')
                        if display_credentials(user_name):
                            print('List of your credentials.')
                            print(' ')
                            for credentials in display_credentials(user_name):
                                print(f'Account name: {credentials.account_name} \n Password: {credentials.password}')
                            print(' ')
                        else:
                            print(' ')
                            print('No credentials yet.')
                            print(' ')
                    elif short_code == 'dl':
                        print(' ')
                        print('Enter the account name of credential you want to delete')
                        credential_name = input()
                        if check_credential(credential_name):
                            delete_credential = delete_credential(accout_name)
                            print(' ')
                            print(f'Credentials for {accout_name} deleted successfully.')
                        else:
                            print(' ')
                            print('No credentials found!')
                            
                    elif short_code == 'cp':
                        print(' ')
                        chosen_account = input('Enter account to copy password from: ')
                        copy_credentials(chosen_account)
                        print(' ')

                    elif short_code == 'ex':
                        print(' ')
                        print(f'Goodbye {user_name}')
                        break

                    else:
                        print('Wrong option. Try again.')
            else:
                print('Wrong details. Try again or create account.')

        elif short_code == 'ex':
            break

        else:
            print(' ')
            print('Wrong option. Try again.')


if __name__ == '__main__':
    main()