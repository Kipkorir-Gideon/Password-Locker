class User:
    '''
    class that generate an instance of User
    '''

    user_list = [] # An empty list to store users

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def save_user(self):
        '''
        Method to save a created instance
        '''
        User.user_list.append(self)

    def remove_user(self):
        '''
        A method to delete a saved user
        '''
        User.user_list.remove(self)
        