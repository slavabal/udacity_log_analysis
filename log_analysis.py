#!/usr/bin/env python3

import psycopg2

# Definitions - BEGIN
# DB name to run analysis
DBNAME = 'news'

# % requests errors threshold to report
PCT_BAD = 1.0

# SQL_QUERY: On which days did more than 1% of requests lead to errors?
sql_log_stats = """
    select
        date, pct_bad
    from (
        select
            ok_response.date as date,
            ok_response.count as count_ok,
            bad_response.count as count_bad,
            100 * bad_response.count::decimal /
                (ok_response.count + bad_response.count)  as pct_bad
        from (
            select
                time::date as date, count(*) as count
            from log
            where status = '200 OK'
            group by time::date
            ) as ok_response
        join (
            select
                time::date as date, count(*) as count
            from log
            where status != '200 OK'
            group by time::date
            ) as bad_response
        on ok_response.date = bad_response.date
        ) as log_stats
    where pct_bad>%s order by date;"""

# SQL_QUERY: What are the most popular three articles of all time?
sql_top_articles = """
    select
        articles.title,
        count(*) as rating
    from log
        join articles
            on log.path like '%'||articles.slug
    group by articles.id, articles.title
    order by rating
    desc limit 3;"""

# SQL_QUERY: Who are the most popular article authors of all time?
sql_top_authors = """
    select
        authors.name,
        count(*) as rating
    from log
    join articles
    on log.path like '%'||articles.slug
    join authors
    on authors.id = articles.author
    group by authors.id, authors.name
    order by rating desc limit 3;"""
# Definitions - END

# Interaction with the database - BEGIN
conn = psycopg2.connect(dbname=DBNAME)
cur = conn.cursor()

cur.execute(sql_top_articles)
result_top_articles = cur.fetchall()

cur.execute(sql_top_authors)
result_top_authors = cur.fetchall()

cur.execute(sql_log_stats, (PCT_BAD,))
result_bad_day = cur.fetchall()

conn.close()
# Interaction with the database - END

# Display Results - BEGIN
print ("="*60)
print (" Most popular three articles of all time")
for i in result_top_articles:
    print(' * "{}" - {} viewes'.format(*i))

print ("\n"+"="*60)
print (" Most popular article authors of all time")
for i in result_top_authors:
    print(" * {} - {} viewes".format(*i))

print ("\n"+"="*60)
print (" Days when more than %d%% of requests lead to errors\n" % PCT_BAD)
for i in result_bad_day:
    print(" * {:%B %d,%Y} - {:1.2}% errors".format(*i))
print ("\n"+"="*60)
# Display Results - END

# Happy End
