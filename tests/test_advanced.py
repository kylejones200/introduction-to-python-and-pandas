from src.advanced import deep_copy_dataframe, inner_join_example
from src.pandas_structures import create_employee_dataframe


def test_inner_join_has_shared_index_only():
    joined = inner_join_example()
    assert len(joined) == 2
    assert "B" in joined.columns


def test_deep_copy_is_independent():
    source = create_employee_dataframe()
    copied = deep_copy_dataframe(source)
    copied.loc[0, "Age"] = 99
    assert source.loc[0, "Age"] != 99
