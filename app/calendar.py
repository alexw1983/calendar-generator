import pandas as pd
from datetime import date


def generate_calendar(start_date: date, end_date: date) -> pd.DataFrame:
    """
    Gets a calendar divided into 30 minute periods.
    - Runs from 00:00 to 2330
    - Is *not* inclusive. So goes up to but not including the last day
    """
    date_ranges = pd.date_range(
        start=start_date,
        end=end_date,
        freq="30min",
        tz="UTC",
        inclusive="left",
    )

    mapped_data = [
        {
            "Date": time_stamp.date(),
            "Time": time_stamp.time(),
            "Period": idx + 1,
        }
        for idx, time_stamp in enumerate(date_ranges)
    ]

    return pd.DataFrame(mapped_data)
