# Treehouse Techdegree-Project-10
> Todo API with Flask

## Project Description

A fellow student of yours in the Full Stack JavaScript Techdegree has just taken the Angular Basics course and has a pretty nice working Angular.js Todo app. They went a little farther and used the ng-resource plugin which allows the application to work automatically using RESTful practices. However, they don’t have experience yet on the server side of things. But you do. Can you help them out?

## Installing / Getting started

### With virtual env

```shell
pip install -r requirements.txt
```

### With Pipenv

> Installs from Pipfile.lock

```shell
pipenv install
```

### Run the server

```shell
python app.py
```

## Testing Coverage

There are 3 different test files to cover specific parts of the code.
Run each file on it's own and check for coverage to get accurate results.

### Test the app.py file

1. Run the tests

```shell
coverage run -m tests.test_app
```

2. Get a report

```shell
coverage report *.py
```

3. For a html report:

```shell
coverage html *.py
```

### Test the models.py file

1. Run the tests

```shell
coverage run -m tests.test_models
```

2. Get a report

```shell
coverage report *.py
```

3. For a html report:

```shell
coverage html *.py
```

### Test the todos.py file

1. Run the tests

```shell
coverage run -m tests.test_todos
```

2. Get a report

```shell
coverage report resources/*.py
```

3. For a html report:

```shell
coverage html resources/*.py
```