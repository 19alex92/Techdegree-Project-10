from flask import Blueprint, abort

from flask_restful import (Resource, Api, reqparse, fields,
                           url_for, marshal, marshal_with)

import models


todo_fields = {
    'id': fields.Integer,
    'name': fields.String,
}


def todo_or_404(id):
    try:
        todo = models.Todo.get(models.Todo.id == id)
    except models.Todo.DoesNotExist:
        abort(404)
    else:
        return todo


class ToDoList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            required=True,
            help='No ToDo title provided',
            location=['form', 'json']
        )

    def get(self):
        return [marshal(todo, todo_fields)
                for todo in models.Todo.select()]

    @marshal_with(todo_fields)
    def post(self):
        args = self.reqparse.parse_args()
        todo = models.Todo.create(**args)
        return (todo, 201, {
            'Location': url_for('resources.todo.todo', id=todo.id)
        })


class ToDo(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            required=True,
            help='No ToDo title provided',
            location=['form', 'json']
        )

    @marshal_with(todo_fields)
    def get(self, id):
        return todo_or_404(id)

    @marshal_with(todo_fields)
    def put(self, id):
        args = self.reqparse.parse_args()
        query = models.Todo.update(**args).where(models.Todo.id == id)
        query.execute()
        return (models.Todo.get(models.Todo.id == id), 200,
                {'Location': url_for('resources.todo.todo', id=id)})

    def delete(self, id):
        query = models.Todo.delete().where(models.Todo.id == id)
        query.execute()
        return '', 204, {'Location': url_for('resources.todo.todos')}


todo_api = Blueprint('resources.todo', __name__)
api = Api(todo_api)
api.add_resource(
    ToDoList,
    '/todos',
    endpoint='todos'
)
api.add_resource(
    ToDo,
    '/todos/<int:id>',
    endpoint='todo'
)
