select query_name, 
       round(avg(rating / position), 2) as quality,
       round(((
        select count(*) from Queries
        where rating < 3 and query_name = q.query_name
       ) / count(*)) * 100, 2) as poor_query_percentage

from Queries as q
group by query_name

-- SELECT 
--     query_name,
--     ROUND(AVG(rating * 1.0 / position), 2) AS quality,
--     ROUND(AVG(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100, 2) AS poor_query_percentage
-- FROM Queries
-- GROUP BY query_name;