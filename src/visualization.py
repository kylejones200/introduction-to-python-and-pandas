"""Pandas and Matplotlib plotting helpers."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def plot_age_histogram(
    df: pd.DataFrame,
    *,
    bins: int = 20,
    output_path: Path | None = None,
    show: bool = False,
) -> Path | None:
    """Age distribution histogram from the article."""
    fig, ax = plt.subplots(figsize=(8, 5))
    df["Age"].hist(bins=bins, ax=ax, color="#4A90A4", edgecolor="white")
    ax.set_xlabel("Age")
    ax.set_ylabel("Frequency")
    ax.set_title("Age Distribution")

    saved: Path | None = None
    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=100, bbox_inches="tight")
        saved = output_path

    if show:
        plt.show()
    else:
        plt.close(fig)

    return saved
