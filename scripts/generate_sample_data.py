#!/usr/bin/env python3
"""Regenerate committed sample files under data/."""

from pathlib import Path

from src.data_io import ensure_sample_data

if __name__ == "__main__":
    data_dir = ensure_sample_data(Path(__file__).resolve().parents[1] / "data")
    print(f"Sample data ready in {data_dir}")
