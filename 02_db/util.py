import os
import polars as pl


ENV_VAR = "DATA"


def load_data():
    """Load data from file specified by DATA environment variable."""
    path = os.getenv(ENV_VAR)
    assert path, f"Environment variable {ENV_VAR} not set"
    return pl.read_csv(path)
