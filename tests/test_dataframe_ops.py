from src.dataframe_ops import (
    add_salary_and_filter,
    average_age_by_city,
    select_and_query,
)


def test_select_and_query_filters_ages():
    result = select_and_query()
    assert len(result["age_over_30"]) == 2


def test_add_salary_and_filter(employees):
    high_salary, cleaned = add_salary_and_filter(employees)
    assert len(high_salary) == 2
    assert "Salary" not in cleaned.columns


def test_average_age_by_city():
    means = average_age_by_city()
    assert means.loc["Paris"] == 34
