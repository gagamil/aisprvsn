# Tech challenge AISupervision

## Input

### Data

Number of csv files with some structured data.

### Desription

The task is to create an API for browsing financial stock data. The api should contain the
following functionality:

● List stocks
● Get a stock
● Get price history for a stock between two dates
● Get price at a point for a stock on a day
● Optional: Endpoint for general querying using basic statistical/mathematical functions

This should be implemented using the technology we work with: Django, Django Ninja,
TimescaleDB and PostgreSQL. Only the data in the CSV files attached should be used.

## Workflow

1. Look into the csv files and get the initial idea of the task size and complexity.
2. Create the raw Django project and add the basic libraries necessary for data import and processing (runtime).
3. Import the data and ensure it is in the DB via the admin.
4. Add UnitTests for the first 4 api endpoints and implement these.

## Concerns & Improvements

1. Import data using the current strucure or preprocess files (add col with ticker).
2. Add model for the company to dynamically import values for any Company
3. Import data to dedicated Import table which will launch cleaning logic (conflicting data) in background mode. Afterwards this will populate the Stock data which is considered as valid and ready to be used by the main logic (statistical app?).
