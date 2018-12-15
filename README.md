# Log Analysis Project
## Purpose
Udacily Full Stack Web Developer Nanodegree Program project #1 by [Slava Balashov](mailto:slavabal@gmail.com ).

## Description
This project sets up a PostgreSQL database for a `news` website.

The provided Python script `log_analysis.py` uses the `psycopg2` library to query the database
and produce a report that answers the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Prerequisites
### The database
- `news` database is required for running the project.
- The `log` table has a database row for each time a reader access a web page.
- The `log` table includes a column status that indicates the HTTP status code
that the news site sent to the user's browser (`'200 OK'` or `'404 NOT FOUND'` etc. See [Wiki](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) for the list of codes).
- The `articles` table contains rows for each of the article's title, content and a reference to article's author
- The `authors` table contains rows for authors and their biographies
- no additional views are required for the `news` database

#### Database Installation
- Download database from Udacity using this [link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
- import `news` database
```python
    $ psql -d news -f newsdata.sql
```
### Imported modules
- `psycopg2` module 

## Running the Project
```python
$ python log_analysis.py
$ python3 log_analysis.py
```
## Sample Output
```
============================================================
 Most popular three articles of all time
 * "Candidate is jerk, alleges rival" — 338647 viewes
 * "Bears love berries, alleges bear" — 253801 viewes
 * "Bad things gone, say good people" — 170098 viewes

============================================================
 Most popular article authors of all time
 * Ursula La Multa — 507594 viewes
 * Rudolf von Treppenwitz — 423457 viewes
 * Anonymous Contributor — 170098 viewes

============================================================
 Days when more than 1% of requests lead to errors

 * July 17,2016 — 2.3% errors

============================================================

```