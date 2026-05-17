"""Core Python syntax and types demonstrated in the article."""

from __future__ import annotations


def hello_world() -> str:
    """Classic hello-world example."""
    return "Hello World"


def demonstrate_types() -> dict[str, type]:
    """Return types for the basic Python data types from the article."""
    name = "Alice"
    age = 30
    height = 5.9
    fruits = ["apple", "banana", "cherry"]
    person = {"name": "Alice", "age": 30}
    return {
        "name": type(name),
        "age": type(age),
        "height": type(height),
        "fruits": type(fruits),
        "person": type(person),
    }


def adult_label(age: int) -> str:
    """If-else example from the article."""
    if age >= 18:
        return "You are an adult."
    return "You are a minor."


def list_fruits(fruits: list[str]) -> list[str]:
    """For-loop example: return fruits in order."""
    return [fruit for fruit in fruits]


def count_with_while(limit: int) -> list[int]:
    """While-loop example: count from 0 up to limit - 1."""
    values: list[int] = []
    count = 0
    while count < limit:
        values.append(count)
        count += 1
    return values
