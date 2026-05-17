"""Shared pytest fixtures."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import pytest
from src.pandas_structures import create_employee_dataframe


@pytest.fixture
def employees():
    return create_employee_dataframe()
