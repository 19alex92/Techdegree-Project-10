import unittest

import app
from models import Todo


class TestToDoList(unittest.TestCase):

    # Helper methods
    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def tearDown(self):
        query = Todo.delete().where(Todo.name == 'Test todo task')
        query.execute()

    # Tests
    def test_ToDoList_get_valid(self):
        '''Tets the get all tasks endpoint'''
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_ToDoList_get_invalid(self):
        '''Tests for status code 404 when invalid URI'''
        response = self.app.get('/todo')
        self.assertEqual(response.status_code, 404)

    def test_ToDoList_post_valid(self):
        '''Tests the post endpoint'''
        body = {'name': 'Test todo task'}
        response = self.app.post('/api/v1/todos', data=body,
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 201)

    def test_ToDoList_post_invalid(self):
        '''Tests for status code 404 when invalid URI'''
        body = {'name': 'Test todo task'}
        response = self.app.post('/api/v1/todo', data=body,
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 404)


class TestToDo(unittest.TestCase):

    # Helper methods
    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        self.todo = Todo.create(name='Test todo task')

    def tearDown(self):
        query = Todo.delete().where(Todo.name == self.todo.name)
        query.execute()
        query = Todo.delete().where(Todo.name == 'Test todo task test')
        query.execute()

    # Tests
    def test_ToDo_get_valid(self):
        '''Tests the get a specific task endpoint'''
        response = self.app.get(f'/api/v1/todos/{self.todo.id}')
        self.assertEqual(response.status_code, 200)

    def test_ToDo_get_invalid(self):
        '''Tests for status code 404 when invalid URI'''
        response = self.app.get(f'/api/v1/todo/{self.todo.id}')
        self.assertEqual(response.status_code, 404)

    def test_ToDo_put_valid(self):
        '''Tests the put endpoint'''
        json_data = {'name': 'Test todo task test'}
        response = self.app.put(f'/api/v1/todos/{self.todo.id}',
                                data=json_data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_ToDo_put_invalid(self):
        '''Tests for status code 404 when invalid URI'''
        json_data = {'name': 'Test todo task test'}
        response = self.app.put(f'/api/v1/todo/{self.todo.id}',
                                data=json_data, follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_ToDo_delete_valid(self):
        '''Tests the delete endpoint'''
        response = self.app.delete(f'/api/v1/todos/{self.todo.id}')
        self.assertEqual(response.status_code, 204)

    def test_ToDo_delete_invalid(self):
        '''Tests for status code 404 when invalid URI'''
        response = self.app.delete(f'/api/v1/todo/{self.todo.id}')
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
