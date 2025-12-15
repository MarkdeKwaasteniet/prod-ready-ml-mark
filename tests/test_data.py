"""Tests for the data loading functions."""

from animal_shelter import data


def test_convert_camel_case() -> None:
    """Test the convert_camel_case function."""
    assert data.convert_camel_case("CamelCase") == "camel_case"
    assert data.convert_camel_case("CamelCASE") == "camel_case"
    assert data.convert_camel_case("camel-case") != "camel_case"
