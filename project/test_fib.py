# python -m pytest
import fibonacci as fib # pylint: disable=import-error

def test_function():
    assert fib.fib_r(15) == 987