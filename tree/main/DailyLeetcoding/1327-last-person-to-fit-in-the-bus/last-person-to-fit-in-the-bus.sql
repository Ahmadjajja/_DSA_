# Write your MySQL query statement below
select a.person_name
from Queue a join queue b
on a.turn >= b.turn
group by a.turn
having sum(b.weight) <= 1000
order by a.turn desc
limit 1
