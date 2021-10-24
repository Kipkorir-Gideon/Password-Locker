class User:
    '''
    class that generate an instance of User
    '''

    user_list = [] # An empty list to store users

    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
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
        