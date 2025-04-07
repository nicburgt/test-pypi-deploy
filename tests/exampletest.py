import pytest

# A basic test function that always passes
def test_always_passes() -> None:
    assert True

# Another test function that also always passes
def test_addition() -> None:
    assert 2 + 2 == 4

# A simple function to test if a string is non-empty
def test_string_non_empty() -> None:
    my_string = "Hello, pytest!"
    assert bool(my_string)

# A test with a condition that always evaluates to true
def test_is_true() -> None:
    assert (5 > 3)