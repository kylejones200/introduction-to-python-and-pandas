import pandas as pd
import pytest
from src.dataframe_ops import (
    add_salary_and_filter,
    apply_transformations,
    demo_frame_with_missing,
    describe_and_value_counts,
    handle_missing_values,
)
from src.pandas_structures import create_employee_dataframe


def test_add_salary_length_mismatch_raises():
    df = create_employee_dataframe().head(2)
    with pytest.raises(ValueError, match="Expected 2 salary values"):
        add_salary_and_filter(df, salaries=[1, 2, 3])


def test_demo_frame_with_missing_has_null_city():
    frame = demo_frame_with_missing()
    assert frame["City"].isna().any()


def test_handle_missing_values_does_not_mutate_input(employees):
    result = handle_missing_values(employees)
    assert employees["City"].notna().all()
    assert result["without_nulls"].shape[0] == len(employees)


def test_handle_missing_values_drops_null_rows():
    frame = demo_frame_with_missing()
    cleaned = handle_missing_values(frame)["without_nulls"]
    assert len(cleaned) == len(frame) - 1


def test_apply_transformations_adds_columns(employees):
    result = apply_transformations(employees)
    assert "AgeGroup" in result.columns
    assert "HireDate" in result.columns
    assert pd.api.types.is_datetime64_any_dtype(result["HireDate"])


def test_describe_without_transform_uses_original_columns(employees):
    summary = describe_and_value_counts(employees, transform=False)
    assert "AgeGroup" not in summary["describe"].columns


def test_describe_with_transform_includes_derived_columns(employees):
    summary = describe_and_value_counts(employees, transform=True)
    assert "AgeGroup" in summary["describe"].columns
