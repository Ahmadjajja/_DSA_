# Write your MySQL query statement below

select w2.id from Weather as w1
join Weather as w2
on datediff(w2.recordDate, w1.recordDate) = 1
where w2.temperature > w1.temperature


