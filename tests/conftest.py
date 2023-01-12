from datetime import date
import pytest
from tests.test_data import test_data
import pandas as pd


@pytest.fixture
def sample_data_for_24_hour_range():
    first_day = list(filter(lambda x: x["Date"] == date(2023, 1, 1), test_data))
    return get_sample_data(first_day)


@pytest.fixture
def sample_data_for_72_hour_range():
    return get_sample_data(test_data)


def get_sample_data(sample_data: list) -> pd.DataFrame:
    raw_data = [
        {"Date": sample["Date"], "Time": sample["Time"], "Period": idx + 1}
        for idx, sample in enumerate(sample_data)
    ]
    return pd.DataFrame(list(raw_data))
