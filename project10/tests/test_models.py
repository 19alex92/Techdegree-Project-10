import unittest

from models import Todo
import app


class TestTodoModel(unittest.TestCase):

    # Helper methods
    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        self.todo = Todo.create(name='Test todo task')

    def tearDown(self):
        query = Todo.delete().where(Todo.name == self.todo.name)
        query.execute()

    # Tests
    def test_todo_creation(self):
        '''Tests if the database is working'''
        todo = self.todo
        self.assertTrue(isinstance(todo, Todo))


if __name__ == "__main__":
    unittest.main()
