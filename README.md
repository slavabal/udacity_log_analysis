# Log Analysis Project
Udacily Full Stack Web Developer Nanodegree Program project #1 by [Slava Balashov](mailto:slavabal@gmail.com ).


## Decription
This project analyses logs database for the news website and reports the data to answer the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Prerequisites
- `psycopg2` module 
- `news` database with _no_ additional views

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