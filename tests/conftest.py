"""Shared pytest fixtures."""

from __future__ import annotations

import matplotlib
import pytest
from src.pandas_structures import create_employee_dataframe

matplotlib.use("Agg")



@pytest.fixture
def employees():
    return create_employee_dataframe()
