class User:
    '''
    class that generate an instance of User
    '''

    user_list = [] # An empty list to store users

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password