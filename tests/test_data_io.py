from pathlib import Path

import pandas as pd

from src.data_io import ensure_sample_data, read_csv_sample, read_excel_sample, write_pickle
from src.pandas_structures import create_employee_dataframe


def test_ensure_sample_data_creates_files(tmp_path: Path):
    data_dir = ensure_sample_data(tmp_path)
    csv_path = data_dir / "MER_T02_01.csv"
    excel_path = data_dir / "EnergyData.xlsx"
    assert csv_path.is_file()
    assert excel_path.is_file()
    assert len(read_csv_sample(csv_path)) == 24
    assert "Consumption" in read_excel_sample(excel_path).columns


def test_write_pickle_round_trip(tmp_path: Path):
    df = create_employee_dataframe()
    reloaded = write_pickle(df, tmp_path / "test.pkl")
    pd.testing.assert_frame_equal(df, reloaded)
