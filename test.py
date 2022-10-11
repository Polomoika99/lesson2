import sys

def test_format_simple():
    str1 = 'Hello, {}! {}'
    str2 = str1.format('world', 123)
    assert str2 == 'Hello, world! 123'