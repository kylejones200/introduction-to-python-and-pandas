#!/usr/bin/env python3
"""Run the Introduction to Python and Pandas tutorial examples."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

import pandas as pd
import yaml
from src import DATA_DIR, ROOT
from src.advanced import deep_copy_dataframe, inner_join_example
from src.data_io import (
    ensure_sample_data,
    read_csv_sample,
    read_excel_sample,
    write_csv,
    write_pickle,
)
from src.dataframe_ops import (
    add_salary_and_filter,
    apply_transformations,
    average_age_by_city,
    demo_frame_with_missing,
    describe_and_value_counts,
    handle_missing_values,
    select_and_query,
)
from src.pandas_structures import (
    create_employee_dataframe,
    create_employee_dataframe_from_records,
    create_series_from_dict,
    create_series_from_list,
    library_versions,
)
from src.python_basics import (
    adult_label,
    count_with_while,
    demonstrate_types,
    hello_world,
    list_fruits,
)
from src.visualization import plot_age_histogram

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def load_config(config_path: Path | None = None) -> dict:
    path = config_path or ROOT / "config.yaml"
    with path.open() as handle:
        return yaml.safe_load(handle)


def run_python_basics() -> None:
    logger.info("Hello: %s", hello_world())
    logger.info("Types: %s", demonstrate_types())
    logger.info("Adult check: %s", adult_label(18))
    logger.info("Fruits: %s", list_fruits(["apple", "banana", "cherry"]))
    logger.info("While loop: %s", count_with_while(3))


def run_pandas_structures() -> pd.DataFrame:
    logger.info("Library versions: %s", library_versions())
    logger.info("Series from list:\n%s", create_series_from_list())
    logger.info("Series from dict:\n%s", create_series_from_dict())

    employees = create_employee_dataframe()
    logger.info("Employee DataFrame:\n%s", employees)
    logger.info(
        "DataFrame from records:\n%s",
        create_employee_dataframe_from_records(),
    )
    return employees


def run_dataframe_operations(employees: pd.DataFrame) -> pd.DataFrame:
    selections = select_and_query(employees)
    logger.info("Ages:\n%s", selections["ages"])
    logger.info("Row by label:\n%s", selections["row_by_label"])
    logger.info("Age > 30:\n%s", selections["age_over_30"])

    high_salary, without_salary = add_salary_and_filter(employees)
    logger.info("High salary:\n%s", high_salary)
    logger.info("After dropping salary:\n%s", without_salary)

    logger.info("Average age by city:\n%s", average_age_by_city(without_salary))
    logger.info(
        "Missing values:\n%s",
        handle_missing_values(demo_frame_with_missing()),
    )

    transformed = apply_transformations(without_salary)
    logger.info("Transformed frame:\n%s", transformed)
    logger.info(
        "Summary stats: %s",
        describe_and_value_counts(without_salary, transform=True),
    )
    return without_salary


def run_file_io(config: dict, employees: pd.DataFrame) -> None:
    data_dir = ensure_sample_data(DATA_DIR)
    csv_path = data_dir / Path(config["data"]["csv_path"]).name
    excel_path = data_dir / Path(config["data"]["excel_path"]).name

    logger.info("CSV sample:\n%s", read_csv_sample(csv_path).head())
    logger.info(
        "Excel sample:\n%s",
        read_excel_sample(excel_path, config["data"]["excel_sheet"]).head(),
    )

    output_dir = ROOT / config["output"]["dir"]
    write_csv(employees, output_dir / config["output"]["csv_name"])
    reloaded = write_pickle(employees, output_dir / config["output"]["pickle_name"])
    logger.info("Pickle round-trip shape: %s", reloaded.shape)


def run_visualization(
    employees: pd.DataFrame, config: dict, output_dir: Path
) -> None:
    figures_dir = output_dir / config["output"]["figures_dir"]
    plot_age_histogram(
        employees,
        output_path=figures_dir / "age_distribution.png"
        if config["run"]["save_figures"]
        else None,
        show=config["run"]["show_plots"],
    )


def run_advanced(employees: pd.DataFrame) -> None:
    logger.info("Inner join:\n%s", inner_join_example())
    copy = deep_copy_dataframe(employees)
    copy.loc[copy.index[0], "Age"] = 99
    logger.info(
        "Deep copy isolates mutations (original age=%s, copy age=%s)",
        employees.loc[0, "Age"],
        copy.loc[0, "Age"],
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Introduction to Python and Pandas tutorial"
    )
    parser.add_argument("--config", type=Path, default=None, help="Path to config.yaml")
    parser.add_argument(
        "--section",
        choices=["all", "basics", "pandas", "io", "viz", "advanced"],
        default="all",
        help="Which article section to run",
    )
    parser.add_argument("--output-dir", type=Path, default=None, help="Output directory")
    args = parser.parse_args()

    config = load_config(args.config)
    output_dir = args.output_dir or ROOT / config["output"]["dir"]
    output_dir.mkdir(parents=True, exist_ok=True)

    employees = create_employee_dataframe()

    if args.section in ("all", "basics"):
        run_python_basics()

    if args.section in ("all", "pandas"):
        employees = run_pandas_structures()
        employees = run_dataframe_operations(employees)

    if args.section in ("all", "io"):
        run_file_io(config, employees)

    if args.section in ("all", "viz"):
        run_visualization(employees, config, output_dir)

    if args.section in ("all", "advanced"):
        run_advanced(employees)

    logger.info("Done. Outputs in %s", output_dir)


if __name__ == "__main__":
    main()
