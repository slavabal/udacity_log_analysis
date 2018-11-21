
select authors.id,	authors.name, count(*) as rating from log join articles on log.path like '%'||articles.slug 
join authors on authors.id = articles.author
group by authors.id, authors.name order by rating desc limit 3;


select authors.id,	authors.name, count(*) as rating from log join articles on log.path like '%'||articles.slug join authors on authors.id = articles.author group by authors.id, authors.name order by rating desc limit 3;