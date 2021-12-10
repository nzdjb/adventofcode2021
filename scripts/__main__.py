from typing import Text
from unittest import TestLoader, TextTestRunner
from os import path

def unittest():
    suite = TestLoader().discover(path.join(path.dirname(path.abspath(__file__)), '..'))
    TextTestRunner().run(suite)
