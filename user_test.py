import unittest
import pyperclip
from user import User


class TestUser(unittest.TestCase):
    '''
    Test class that defines class behaviors
    '''

    def setUp(self):
        '''
        Set up to run before each test case.
        '''
        self.new_user = User('Yuri', 'Gagari', 'yuri3607')
    
    def test__init__(self):
        '''
        Test for checking if the initialization is well done
        '''
        self.assertEqual(self.new_user.first_name, 'Yuri')
        self.assertEqual(self.new_user.last_name, 'Gagari')
        self.assertEqual(self.new_user.password, 'yuri3607')
    
    def test_save_user(self):
        '''
		Test to check if the new users information is saved into the users list
		'''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)