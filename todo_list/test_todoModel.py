"""
This is a unit test file which checks the functionality of the todo_model
"""

import os
from unittest import TestCase
from todo_model import Todo


class TestTodoModel(TestCase):
    def setUp(self):
        self.filename = 'test_todo_list.txt'
        self.todo = Todo
