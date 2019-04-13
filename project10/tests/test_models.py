import unittest

from models import Todo
import app


class TestTodoModel(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        self.todo = Todo.create(name='Test todo task')

    def tearDown(self):
        query = Todo.delete().where(Todo.name == self.todo.name)
        query.execute()

    def test_todo_creation(self):
        todo = self.todo
        self.assertTrue(isinstance(todo, Todo))


if __name__ == "__main__":
    unittest.main()
