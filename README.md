# Tech challenge AISupervision

## Input

### Data

Number of csv files with some structured data.

## Challenge Desription

The task is to create an API for browsing financial stock data. The api should contain the
following functionality:

- List stocks
- Get a stock
- Get price history for a stock between two dates
- Get price at a point for a stock on a day
- Optional: Endpoint for general querying using basic statistical/mathematical functions

This should be implemented using the technology we work with: Django, Django Ninja,
TimescaleDB and PostgreSQL. Only the data in the CSV files attached should be used.

## Workflow

1. Look into the csv files and get the initial idea of the task size and complexity.
2. Create the raw Django project and add the basic libraries necessary for data import and processing (runtime).
3. Import the data and ensure it is in the DB via the admin.
4. Add UnitTests for the first api endpoints and implement these.
5. Meet the requirements - use Postgres and TDB, dockerize (TODO)

## Considerations

Import data via the admin (import export lib).
preformat - add symbol col to associate the data with a company (symbol).

The app logic is relatively simple. Basically only data fetching as is (unless I misunderstood the requirements).
Thus no real design is needed. The request/response cycle is short and no additional layers are required for the business logic.

### Sync/Async tasks

However separated data import from the clean data itself using build in signals.
Currently runs synchonously.
If the app evolves and it will be clear that the runtime env of the both app parts have different footprint the monolithic app can be either decoupled or some logic could be wrapped in uwsgi spoolers thus processed in async mode.

## Requirements - endpoints

### List stocks

/api/stocks

#### Filter by date range

Use qs date_from and date_till.
If both params equal then filtering within the same day.

#### Filterby ticker (symbol)

Use qs ticker

### Get a stock

/api/stocks/<id>

### Get price history for a stock between two dates

### Get price at a point for a stock on a day

Satisfied via filters in the list endpoint. If not, pls add more description (need feedback).

## Concerns & Improvements

1. Import data using the current strucure or preprocess files (add col with ticker).
2. Use cookiecutter to bootstrap a production ready project config.
3. Implements some stats functionality (ORM aggregates or https://github.com/pennersr/django-trackstats)
4. Add ActionStreams for logging peurpose if needed
5. Tune as per performance reqiuerments and profiling.
