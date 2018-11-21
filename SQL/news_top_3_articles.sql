select 
	articles.id, 
	articles.title, 
	count(*) as rating 
from log 
	join articles 
		on log.path like '%'||articles.slug 
group by articles.id, articles.title 
order by rating 
desc limit 3;


select articles.id,	articles.title, count(*) as rating from log join articles on log.path like '%'||articles.slug group by articles.id, articles.title order by rating desc limit 3;
