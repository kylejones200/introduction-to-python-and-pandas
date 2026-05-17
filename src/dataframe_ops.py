"""Selecting, filtering, grouping, and transforming DataFrames."""

from __future__ import annotations

import pandas as pd

from src.pandas_structures import create_employee_dataframe

DEFAULT_SALARIES = [50_000, 60_000, 55_000, 65_000]


def select_and_query(df: pd.DataFrame | None = None) -> dict[str, pd.DataFrame | pd.Series]:
    """Column, row, and query selections from the article."""
    frame = create_employee_dataframe() if df is None else df.copy()
    return {
        "ages": frame["Age"],
        "row_by_label": frame.loc[[0]],
        "row_by_position": frame.iloc[[0]],
        "age_over_30": frame.query("Age > 30"),
    }


def add_salary_and_filter(
    df: pd.DataFrame | None = None,
    salaries: list[int] | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Add a salary column, filter high earners, then drop salary."""
    frame = create_employee_dataframe() if df is None else df.copy()
    pay = salaries if salaries is not None else DEFAULT_SALARIES
    if len(pay) != len(frame):
        msg = f"Expected {len(frame)} salary values, got {len(pay)}"
        raise ValueError(msg)
    frame["Salary"] = pay
    high_salary = frame[frame["Salary"] > 55_000]
    without_salary = frame.drop(columns=["Salary"])
    return high_salary, without_salary


def average_age_by_city(df: pd.DataFrame | None = None) -> pd.Series:
    """GroupBy aggregation from the article."""
    frame = create_employee_dataframe() if df is None else df
    return frame.groupby("City")["Age"].mean()


def demo_frame_with_missing() -> pd.DataFrame:
    """Employee frame with one missing city value for missing-data demos."""
    frame = create_employee_dataframe().copy()
    frame.loc[frame.index[0], "City"] = pd.NA
    return frame


def handle_missing_values(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Check and drop missing values without modifying the input frame."""
    return {
        "null_mask": df.isna(),
        "without_nulls": df.dropna(how="any"),
    }


def apply_transformations(df: pd.DataFrame | None = None) -> pd.DataFrame:
    """Row-wise apply, datetime parsing, and descriptive summaries."""
    frame = create_employee_dataframe() if df is None else df.copy()
    frame["AgeGroup"] = frame.apply(
        lambda row: "senior" if row["Age"] >= 30 else "junior",
        axis=1,
    )
    frame["HireDate"] = pd.to_datetime(
        ["2020-01-15", "2018-06-01", "2019-03-20", "2017-11-30"]
    )
    return frame


def describe_and_value_counts(
    df: pd.DataFrame | None = None,
    *,
    transform: bool = False,
) -> dict[str, object]:
    """Descriptive statistics and categorical counts."""
    frame = create_employee_dataframe() if df is None else df.copy()
    if transform:
        frame = apply_transformations(frame)
    return {
        "describe": frame.describe(include="all"),
        "city_counts": frame["City"].value_counts(),
    }
