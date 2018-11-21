 
 
 
 select * from (select ok_response.date as date, ok_response.count as count_ok, bad_response.count as count_bad, 100 * bad_response.count::decimal / (ok_response.count + bad_response.count)  as pct_bad from (select time::date as date, count(*) as count from log where status = '200 OK' group by time::date) as ok_response JOIN (select time::date as date, count(*) as count from log where status != '200 OK' group by time::date) as bad_response ON ok_response.date = bad_response.date) as log_stats  where pct_bad>1.0 order by date;