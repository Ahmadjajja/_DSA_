-- # Write your MySQL query statement below
-- select employee_id, department_id from Employee
-- where primary_flag = 'Y'
-- union
-- select employee_id, department_id from Employee
-- group by employee_id
-- having count(*) = 1

-- left join

select distinct e1.employee_id, e1.department_id
from Employee e1
left join Employee e2 
  on e1.employee_id = e2.employee_id 
  and e1.department_id != e2.department_id
where e1.primary_flag = 'Y' or e2.employee_id is null
