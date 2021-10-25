import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
        '''
        Test that checks credentials behavior.
        '''
        
        def setUp(self):
	        '''
		    Function to test creation of  an account's credentials before each test
		    '''
	        self.new_credential = Credentials('Yuri', 'twitter', 'yuri3607')

        def test__init__(self):
            '''
            Test to check if initialization or creation is well done.
            '''
            self.assertEqual(self.new_credential.user_name, 'Yuri')
            self.assertEqual(self.new_credential.account_name, 'twitter')
            self.assertEqual(self.new_credential.password,'yuri3607')
        
        
        def test_save_credentials(self):
            '''
            Test to check if the newly created credentials are saved correctly
            '''
            self.new_credential.save_credential()
            twitter = Credentials('Yuri', 'twitter', 'yuri3607')
            twitter.save_credential()
            self.assertEqual(len(Credentials.credentials_list),2)
            
        def tearDown(self):
            '''
            method to clear the details list after every test.
            '''
            Credentials.credentials_list = []
            
        def test_display_credentials(self):
            '''
            Test to check if the display credentials method, display the correct credentials
            '''
            self.new_credential.save_credential()
            twitter = Credentials('gidalios', 'twitter', 'yuri3607')
            twitter.save_credential()
            self.assertEqual(len(Credentials.display_credentials(twitter.user_name)), 1)
            
            
        def test_find_by_account_name(self):
            '''
            Test to check if the copy credential method the correct details
            '''

            self.new_credential.save_credential()
            twitter = Credentials('Yuri', 'twitter', 'yuri3607')
            twitter.save_credential()
            credential_exist = Credentials.find_by_account_name('twitter')
            self.assertTrue(credential_exist, twitter)


if __name__ == '__main__':
	unittest.main()