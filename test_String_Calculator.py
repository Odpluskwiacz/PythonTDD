
from String_Calculator import add


def test_empty_string_returns_zero():
    assert add("") == "0"

def test_one_number_returns_itself():
    assert add("1") == "1"

def test_two_numbers_returns_sum():
    assert add("1.1,2.2") == "3.3"

def test_many_numbers():
    assert add("1,2,3,4.5") == "10.5"

def test_newline_separator():
    assert add("1\n2,3") == "6.0"

def test_invalid_newline_separator():
    assert add("175.2, \n35") == "Number expected ale '\\n' znalezion na pozycji 6."

def test_missing_number_at_end():
    assert add("1,3,") == "Number expected but EOF found."

def test_custom_separator():
    assert add("//;\n1;2") == "3.0"
    assert add("//sep\n2sep3") == "5.0"

def test_custom_separator_with_wrong_separator():
    assert add("//|\n1|2,3") == "'|' expected but ',' found at position 3."

def test_negative_numbers():
    assert add("-1,2") == "Negative not allowed : -1"
    assert add("2,-4,-5") == "Negative not allowed : -4, -5"

def test_multiple_errors():
    assert add("-1,,2") == "Negative not allowed : -1\nNumber expected but ',' found at position 3."
    assert add("-1,,-2") == "Negative not allowed : -1\nNumber expected but ',' found at position 3.\nNegative not allowed : -2"

