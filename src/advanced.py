"""Joins, copies, and merges from the advanced section."""

from __future__ import annotations

import pandas as pd

from src.pandas_structures import create_employee_dataframe


def inner_join_example() -> pd.DataFrame:
    """Inner join example from the article."""
    left = pd.DataFrame({"A": ["A0", "A1", "A2", "A3"]})
    right = pd.DataFrame({"B": ["B2", "B3", "B6", "B7"]}, index=[2, 3, 6, 7])
    return left.join(right, how="inner")


def deep_copy_dataframe(df: pd.DataFrame | None = None) -> pd.DataFrame:
    """Deep copy so mutations do not affect the source frame."""
    source = create_employee_dataframe() if df is None else df
    return source.copy(deep=True)
