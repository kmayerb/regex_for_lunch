import re

def contains_digit(text):
    """Return True if the string contains a digit."""
    return bool(re.search(r'\d', text))
