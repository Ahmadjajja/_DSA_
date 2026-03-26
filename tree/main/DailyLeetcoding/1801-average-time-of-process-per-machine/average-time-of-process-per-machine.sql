# Write your MySQL query statement below



-- select a1.machine_id, round(avg(a1.timestamp - a2.timestamp), 3) as processing_time  from Activity as a1
-- join Activity as a2
-- on a1.machine_id = a2.machine_id and a1.process_id = a2.process_id
-- where a1.activity_type = 'end' and a2.activity_type = "start"
-- group by a1.machine_id

SELECT 
    a1.machine_id,
    ROUND(AVG(
        a1.timestamp - (
            SELECT a2.timestamp
            FROM Activity AS a2
            WHERE a2.machine_id = a1.machine_id
              AND a2.process_id = a1.process_id
              AND a2.activity_type = 'start'
        )
    ), 3) AS processing_time
FROM Activity AS a1
WHERE a1.activity_type = 'end'
GROUP BY a1.machine_id;