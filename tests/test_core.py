import pytest
from regexlibrary.core import contains_digit

def test_contains_digit_true():
    assert contains_digit("abc123") is True

def test_contains_digit_false():
    assert contains_digit("abcdef") is False
