from typing import Hashable
from fastapi import FastAPI
from app.calendar import generate_calendar
from datetime import date

api = FastAPI()


@api.get("/calendar")
async def get_calendar(start_date: date, end_date: date):
    """
    Returns a calendar split in to 30 minute periods for the two days not inclusive.
    Takes 2 query sting arguments:
    - start_date i.e. 2023-01-01
    - end_date i.e. 2023-01-02
    """
    calendar = generate_calendar(start_date, end_date)
    res = calendar.to_dict(orient="records")
    return res
