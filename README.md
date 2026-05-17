# Introduction to Python and Pandas

Runnable examples from the Medium article [Introduction to Python and Pandas](https://medium.com/@kyle-t-jones/introduction-to-python-and-pandas-4ea7346aaf3e). The original export is in `article.md`.

## Quick start

```bash
uv sync --extra dev
uv run pandas-intro --section basics
```

```python
from src.pandas_structures import create_employee_dataframe
from src.dataframe_ops import select_and_query

df = create_employee_dataframe()
print(select_and_query(df)["age_over_30"])
```

## Setup

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12+.

```bash
uv sync --extra dev
```

## Run

All article sections:

```bash
uv run pandas-intro
# or: uv run python main.py
```

Single section:

```bash
uv run pandas-intro --section basics
uv run pandas-intro --section pandas
uv run pandas-intro --section io
uv run pandas-intro --section viz
uv run pandas-intro --section advanced
```

## Article → code map

| Article section | Module | Key functions |
|-----------------|--------|---------------|
| Imports / versions | `src/pandas_structures.py` | `library_versions()` |
| Python basics | `src/python_basics.py` | `hello_world()`, `demonstrate_types()`, `adult_label()` |
| Pandas Series / DataFrames | `src/pandas_structures.py` | `create_series_from_list()`, `create_employee_dataframe()` |
| Select, filter, groupby | `src/dataframe_ops.py` | `select_and_query()`, `add_salary_and_filter()`, `average_age_by_city()` |
| File I/O | `src/data_io.py` | `read_csv_sample()`, `read_excel_sample()`, `write_csv()` |
| Missing data | `src/dataframe_ops.py` | `demo_frame_with_missing()`, `handle_missing_values()` |
| Apply / describe | `src/dataframe_ops.py` | `apply_transformations()`, `describe_and_value_counts()` |
| Plotting | `src/visualization.py` | `plot_age_histogram()` |
| Joins / copy / pickle | `src/advanced.py`, `src/data_io.py` | `inner_join_example()`, `deep_copy_dataframe()`, `write_pickle()` |

## Project layout

```
.
├── article.md
├── config.yaml
├── main.py
├── pyproject.toml
├── data/                   # Committed sample CSV and Excel
├── scripts/
│   └── generate_sample_data.py
├── src/
├── tests/
└── output/                 # Generated at runtime (gitignored)
```

## Quality checks

```bash
uv run ruff check src tests main.py
uv run pytest
```

CI runs ruff and pytest on every push to `main`.

Regenerate sample data if needed:

```bash
uv run python scripts/generate_sample_data.py
```

## Notes

- Sample files in `data/` ship with the repo so tests work on a fresh clone.
- The article’s `apply` → year example is replaced with `AgeGroup` and `HireDate` for clearer datetime practice.
