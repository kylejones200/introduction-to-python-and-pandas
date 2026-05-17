# Introduction to Python and Pandas

Runnable examples from the Medium article [Introduction to Python and Pandas](https://medium.com/@kyle-t-jones/introduction-to-python-and-pandas-4ea7346aaf3e). The original export is in `article.md`.

## Setup

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12+.

```bash
uv sync
```

## Run

Run every section from the article:

```bash
uv run python main.py
```

Run a single section:

```bash
uv run python main.py --section basics
uv run python main.py --section pandas
uv run python main.py --section io
uv run python main.py --section viz
uv run python main.py --section advanced
```

## Project layout

```
.
├── article.md              # Original Medium export
├── config.yaml             # Paths and output settings
├── main.py                 # CLI entry point
├── pyproject.toml          # Dependencies (uv)
├── src/
│   ├── python_basics.py    # Python types and control flow
│   ├── pandas_structures.py
│   ├── dataframe_ops.py
│   ├── data_io.py
│   ├── visualization.py
│   └── advanced.py
├── data/                   # Sample CSV/Excel (created on first run)
├── tests/
└── output/                 # Generated CSV, pickle, and plots
```

## Tests

```bash
uv run pytest
```

## Notes

- Sample `data/MER_T02_01.csv` and `data/EnergyData.xlsx` are created automatically if missing, so the repo works without external downloads.
- The article’s `apply` example used age strings as years; this project uses a clearer `AgeGroup` label and a proper `HireDate` column for datetime parsing.
