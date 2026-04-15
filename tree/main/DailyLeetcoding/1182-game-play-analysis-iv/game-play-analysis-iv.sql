# Write your MySQL query statement below
select 
  round(COUNT(a2.player_id) / COUNT(DISTINCT a1.player_id), 2) as fraction
  from Activity as a1
left join Activity as a2
on a1.player_id = a2.player_id and a1.event_date = a2.event_date - INTERVAL 1 DAY
WHERE a1.event_date = (
  SELECT MIN(event_date)
  FROM Activity
  WHERE player_id = a1.player_id
)
