"""Read and write CSV and Excel files; ensure bundled sample data exists."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src import DATA_DIR


def ensure_sample_data(data_dir: Path | None = None) -> Path:
    """Create article sample files when they are not already on disk."""
    root = data_dir or DATA_DIR
    root.mkdir(parents=True, exist_ok=True)

    csv_path = root / "MER_T02_01.csv"
    if not csv_path.exists():
        pd.DataFrame(
            {
                "Month": pd.date_range("2000-01", periods=24, freq="ME"),
                "Value": [
                    100,
                    102,
                    98,
                    105,
                    110,
                    108,
                    112,
                    115,
                    111,
                    109,
                    114,
                    118,
                    120,
                    119,
                    121,
                    123,
                    125,
                    124,
                    126,
                    128,
                    130,
                    129,
                    131,
                    133,
                ],
            }
        ).to_csv(csv_path, index=False)

    excel_path = root / "EnergyData.xlsx"
    if not excel_path.exists():
        before = pd.DataFrame(
            {
                "Year": range(1990, 2000),
                "Consumption": [90 + i for i in range(10)],
            }
        )
        after = pd.DataFrame(
            {
                "Year": range(2000, 2010),
                "Consumption": [100 + i * 2 for i in range(10)],
            }
        )
        with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
            before.to_excel(writer, sheet_name="before2000", index=False)
            after.to_excel(writer, sheet_name="after2000", index=False)

    return root


def read_csv_sample(csv_path: Path) -> pd.DataFrame:
    """Read the monthly energy CSV referenced in the article."""
    return pd.read_csv(csv_path)


def read_excel_sample(excel_path: Path, sheet_name: str = "after2000") -> pd.DataFrame:
    """Read the Excel sheet referenced in the article."""
    return pd.read_excel(excel_path, sheet_name=sheet_name)


def write_csv(df: pd.DataFrame, path: Path) -> Path:
    """Write a DataFrame to CSV."""
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path


def write_pickle(df: pd.DataFrame, path: Path) -> pd.DataFrame:
    """Pickle and reload a DataFrame."""
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_pickle(path)
    return pd.read_pickle(path)
