from pathlib import Path

from src.visualization import plot_age_histogram


def test_plot_age_histogram_writes_file(employees, tmp_path: Path):
    output = tmp_path / "age_distribution.png"
    saved = plot_age_histogram(employees, output_path=output)
    assert saved == output
    assert output.is_file()
    assert output.stat().st_size > 0
