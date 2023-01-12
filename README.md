# Calendar Generator

Code for the Renewable Exchange Tech Test which focuses around generating a calendar and exposing an API.

[The Task Description can be found here](https://zglinski.com/backend/)

I have over documented this a bit, but wanted to be clear on my thinking and what I have assumed :smile:.

The main task is in the `/main/calendar.py` file.

## Pre-Requisites

- [Python 3.9+](https://www.python.org/downloads/release/python-390/)
- [Poetry](https://python-poetry.org/docs)

## Assumptions

I made some assumptions. In the real world I would clarify these with stake-holders but I thought for this exercise it would be more appropriate to just be explicit on the assumptions I have made and deliver that.

I apologise if I have misinterpreted the task. All of the below are easily changeable if required.

- Only **dates** not **datetime** is required for the input to the API.
  - In the example request on the description it shows `/calendar?start_date=2020-01-01&end_date=2020-12-31`
  - This doesn't include the `T00:00:00Z` for the time.
- Dates are not inclusive. So 1st January to 3rd January includes 1st and 2nd but not the 3rd.
- Query strings are used for parameters rather than path variables.
- Frequency will always be 30 minutes and doesn't need to be a variable or collected from user input.
- Only dealing with full days
  - i.e. We want to know the periods on the days specified _not_ from, for example, 1000 to 1300.
- We start at 00:00 and the last period is 23:30 so there should be 48 periods in a day.
- UTC timezone.
  - This is just a habit I have gotten in to :)
- It would be better to use the existing tools rather than re-invent the wheel.
  - I assumed the exercise should reflect what I would do in the real world.
  - Normally I would try and find existing libraries and tools that do the job (i.e. Pandas) and not re-inventing the wheel.
  - I am happy to rework this to take out external libraries if that is the intention of the test.
  - Please let me know.

## Project Notes

- Using [mypy](https://mypy.readthedocs.io/en/stable/index.html) for type checking.
  - Normally I would run this on the build server but I am just running manually now `poetry run mypy tests app`.
  - Configuration can be found in the `mypy.ini` file in the root of the project.
- Using [black](https://black.readthedocs.io/en/stable/index.html) for formatting.
  - I have this configured as my formatter on save in VSCode.
- Using [Poetry](https://python-poetry.org/docs) for package management.
  - See [running locally](#running-locally).
  - I am happy to refactor this to use something else if required.
- Using [FastApi](https://fastapi.tiangolo.com/) for the API.
- Using [pytest](https://pytest.org/) for tests.

## Thought Process

I thought it would be a good idea to explain how I went about this and what I did.

- Read up on [Pandas](https://pandas.pydata.org/). I haven't used this much before so wanted to get more familiar.
- Found the [date_range function](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html) which looked like what we need.
- Wrote some tests for the calendar generation.
- Added the calendar file and implemented using the links above and a list comprehension to do the mapping.
  - Please note that my background has been mostly OO and javascript so I would be keen to hear any feedback to make this a bit more pythonic.
- Added some tests for the API.
  - Note that I focused these tests on API responses and the tests for the calendar on more specific logic.
  - This seemed more readable to me with less repetition.
  - I also considered just having all tests at the API level as more of a service test. I don't really mind either way and I am happy to take advice on this.
- Implemented API
- Added Readme.

## Future Work

If given more time I would:

- Clarify the above assumptions and adjust accordingly
- Host this somewhere.
  - Probably a lambda or in GCP with Cloud Functions behind an API gateway.
  - Using Terraform to set up infrastructure.
- Add a UI.
  - React or Vuejs
  - Host in a S3 bucket as a static site or GCP object storage.

## Running Locally

I like to use poetry for package management.

```bash
# OPTION 1: start the poetry shell (venv)
$ poetry shell

# First time you might need to install dependencies
> poetry install

# Then you can run the tests
> pytest

# or start the api server
> uvicorn app.main:api --reload

# OPTION 2: run poetry directly
$ poetry run <COMMAND>
```

To call the API:

```bash
# use curl (or HTTP tool of choice)
$ curl http://127.0.0.1:8000/calendar?start_date=2023-01-01&end_date=2023-01-02
```

Or alternatively use [the swagger interface](http://127.0.0.1:8000/docs)
