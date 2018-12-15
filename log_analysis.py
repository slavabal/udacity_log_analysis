#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import psycopg2

# DB name to run analysis
DBNAME = 'news'

# % requests errors threshold to report
PCT_BAD = 1.0

# SQL_QUERY: On which days did more than 1% of requests lead to errors?
sql_log_stats = """
    select
       to_char(date,'FMMonth DD, YYYY') as date,
       to_char(pct_bad,'9.99%%') as pct_bad
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
            on log.path = concat('/article/',articles.slug)
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
    on log.path = concat('/article/',articles.slug)
    join authors
    on authors.id = articles.author
    group by authors.id, authors.name
    order by rating desc limit 3;"""

# Titles for the answers
title_log_stats = "Most popular three articles of all time"
title_top_articles = "Most popular article authors of all time"
title_top_authors = "Days when more than %d%% of requests"\
                    " lead to errors" % PCT_BAD

# Formatting for the answers
format_log_stats = " * {} - {} errors"
format_top_articles = ' * "{}" - {} viewes'
format_top_authors = " * {} - {} viewes"

# Standard divider line
divider_line = "\n"+"="*60


# Show and format the answer
def display_answer(title, data_format, data):
    print (divider_line)
    print (title)
    for i in data:
        print (data_format.format(*i))


# Read data from the DB
def read_result(sql_query, params, cursor):
    cursor.execute(sql_query, params)
    return cursor.fetchall()


# Establish DB connection
def connect(database_name):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor

    except psycopg2.Error as err:
        print ("Unable to connect to database")
        sys.exit(1)


def run():
    # Open DB Connection
    conn, cur = connect(DBNAME)

    # Read data from the DB - BEGIN
    result_top_articles = read_result(sql_top_articles, (), cur)
    result_top_authors = read_result(sql_top_authors, (), cur)
    result_log_stats = read_result(sql_log_stats, (PCT_BAD,), cur)
    # Read data from the DB - END

    # Close DB Connection
    conn.close()

    # Display Results - BEGIN
    display_answer(title_top_articles, format_top_articles,
                   result_top_articles)
    display_answer(title_top_authors, format_top_authors, result_top_authors)
    display_answer(title_log_stats, format_log_stats, result_log_stats)
    print (divider_line)
    # Display Results - END


if __name__ == '__main__':
    run()

# Happy End
