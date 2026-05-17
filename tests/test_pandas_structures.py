from src.pandas_structures import (
    create_employee_dataframe,
    create_employee_dataframe_from_records,
    create_series_from_dict,
    create_series_from_list,
    library_versions,
)


def test_series_from_list_length():
    assert len(create_series_from_list()) == 4


def test_series_from_dict_index():
    series = create_series_from_dict()
    assert list(series.index) == ["a", "b", "c"]


def test_employee_dataframe_shape():
    df = create_employee_dataframe()
    assert df.shape == (4, 3)
    assert set(df.columns) == {"Name", "Age", "City"}


def test_records_dataframe():
    df = create_employee_dataframe_from_records()
    assert len(df) == 2
    assert df.loc[0, "City"] == "Tokyo"


def test_library_versions_keys():
    versions = library_versions()
    assert "pandas" in versions
    assert "numpy" in versions
