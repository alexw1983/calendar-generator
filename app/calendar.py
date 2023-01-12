import pandas as pd
from datetime import date


def generate_calendar(start_date: date, end_date: date) -> pd.DataFrame:
    """
    TODO add comments.
    """
    dr = pd.date_range(
        start=start_date,
        end=end_date,
        freq="30min",
        tz="UTC",
        inclusive="left",
    )

    raw_data = [
        {
            "Date": time_stamp.date(),
            "Time": time_stamp.time(),
            "Period": idx + 1,
        }
        for idx, time_stamp in enumerate(dr)
    ]

    return pd.DataFrame(raw_data)
