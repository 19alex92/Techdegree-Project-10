import unittest

import app


class TestApp(unittest.TestCase):

    # Helper methods
    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    # Tests
    def test_my_todos(self):
        '''Tests if the hompage loads correctly'''
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
