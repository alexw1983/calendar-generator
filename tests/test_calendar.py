from datetime import date
from app.calendar import generate_calendar
import pandas as pd


first_of_january = date(2023, 1, 1)
second_of_january = date(2023, 1, 2)
fourth_of_january = date(2023, 1, 4)


def test_generate_calendar_for_a_24_hour_range_should_match_predicted_data(
    sample_data_for_24_hour_range,
):
    # Act
    actual = generate_calendar(first_of_january, second_of_january)

    # Assert
    pd.testing.assert_frame_equal(actual, sample_data_for_24_hour_range)


def test_generate_calendar_for_a_72_hour_range_should_match_predicted_data(
    sample_data_for_72_hour_range,
):
    # Act
    actual = generate_calendar(first_of_january, fourth_of_january)

    # Assert
    pd.testing.assert_frame_equal(actual, sample_data_for_72_hour_range)
