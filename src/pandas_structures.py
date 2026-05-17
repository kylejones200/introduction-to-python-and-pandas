"""Pandas Series and DataFrame creation."""

from __future__ import annotations

import pandas as pd

EMPLOYEE_RECORDS: dict[str, list] = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 34, 29, 32],
    "City": ["New York", "Paris", "Berlin", "London"],
}

ADDITIONAL_EMPLOYEES = [
    {"Name": "Tom", "Age": 25, "City": "Tokyo"},
    {"Name": "Emma", "Age": 31, "City": "Sydney"},
]


def create_series_from_list() -> pd.Series:
    """Series from a list with a custom index."""
    return pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])


def create_series_from_dict() -> pd.Series:
    """Series from a dictionary."""
    return pd.Series({"a": 100, "b": 200, "c": 300})


def create_employee_dataframe() -> pd.DataFrame:
    """Employee DataFrame from the article."""
    return pd.DataFrame(EMPLOYEE_RECORDS)


def create_employee_dataframe_from_records() -> pd.DataFrame:
    """DataFrame built from a list of dictionaries."""
    return pd.DataFrame(ADDITIONAL_EMPLOYEES)


def library_versions() -> dict[str, str]:
    """Report versions used at the start of the article."""
    import numpy as np

    return {
        "pandas": pd.__version__,
        "numpy": np.__version__,
    }
