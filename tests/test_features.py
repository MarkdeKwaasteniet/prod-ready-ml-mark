import pytest
import pandas as pd
from pandas.testing import assert_series_equal

from animal_shelter import features

@pytest.fixture()
def list_of_animals():
    return pd.Series(["dog", "cat", "dog", "cat", "dog"])

def test_check_has_name():
    s = pd.Series(["Ivo", "Henk", "unknown"])
    result = features.check_has_name(s)
    expected = pd.Series([True, True, False])
    assert_series_equal(result, expected)

def test_check_is_dog(list_of_animals):
    s = list_of_animals
    result = features.check_is_dog(s)
    expected = pd.Series([True, False, True, False, True])
    assert_series_equal(result, expected)

def test_sex():
    s = pd.Series(["Female", "Male"])
    result = features.get_sex(s)
    expected = pd.Series(["female", "male"])
    assert_series_equal(result, expected)

def test_for_exceptions():
    with pytest.raises(RuntimeError) as exception:
        features.check_is_dog(pd.Series(["Parrot"]))