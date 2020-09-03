# python -m pytest test_file.py

import project.fibonacci as fib # pylint: disable=import-error

def test_function():
    assert fib.fib_recursive(15) == 987