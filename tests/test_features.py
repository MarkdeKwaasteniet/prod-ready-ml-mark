"""Tests for the feature engineering functions."""

import pandas as pd
import pytest
from pandas.testing import assert_series_equal

from animal_shelter import features


@pytest.fixture  # type: ignore
def list_of_animals() -> pd.Series:
    """Fixture with a list of animals."""
    return pd.Series(["dog", "cat", "dog", "cat", "dog"])


def test_check_has_name() -> None:
    """Test the check_has_name function."""
    s = pd.Series(["Ivo", "Henk", "unknown"])
    result = features.check_has_name(s)
    expected = pd.Series([True, True, False])
    assert_series_equal(result, expected)


def test_check_is_dog(list_of_animals: pd.Series) -> None:
    """Test the check_is_dog function."""
    result = features.check_is_dog(list_of_animals)
    expected = pd.Series([True, False, True, False, True])
    assert_series_equal(result, expected)


def test_sex() -> None:
    """Test the get_sex function."""
    s = pd.Series(["Female", "Male"])
    result = features.get_sex(s)
    expected = pd.Series(["female", "male"])
    assert_series_equal(result, expected)


def test_for_exceptions() -> None:
    """Test that exceptions are raised when expected."""
    with pytest.raises(RuntimeError):
        features.check_is_dog(pd.Series(["Parrot"]))
