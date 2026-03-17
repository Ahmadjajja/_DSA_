# Write your MySQL query statement below
Select EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI
ON Employees.id = EmployeeUNI.id



-- -- join
-- id, name,   unique_id
-- 1   Alice   null
-- 7.  Bob.    null
-- 11. Meir.   2
-- 90. Winston 3
-- 3.  Jonathon 1
