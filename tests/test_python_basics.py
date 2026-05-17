from src.python_basics import (
    adult_label,
    count_with_while,
    demonstrate_types,
    hello_world,
    list_fruits,
)


def test_hello_world():
    assert hello_world() == "Hello World"


def test_demonstrate_types():
    types = demonstrate_types()
    assert types["name"] is str
    assert types["age"] is int
    assert types["height"] is float
    assert types["fruits"] is list
    assert types["person"] is dict


def test_adult_label():
    assert "adult" in adult_label(18)
    assert "minor" in adult_label(10)


def test_list_fruits():
    assert list_fruits(["apple", "banana"]) == ["apple", "banana"]


def test_count_with_while():
    assert count_with_while(3) == [0, 1, 2]
