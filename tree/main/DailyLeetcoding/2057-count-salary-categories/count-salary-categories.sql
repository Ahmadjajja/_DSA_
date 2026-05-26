# Write your MySQL query statement below
select 'Low Salary' as category, sum(case when income < 20000 then 1 else 0 end) as accounts_count
from Accounts

union 

select 'Average Salary' as category, sum(case when income between 20000 and 50000 then 1 else 0 end) as accounts_count
from Accounts

union 

select 'High Salary' as category, sum(case when income > 50000 then 1 else 0 end) as accounts_count
from Accounts

-- learned 3 things inside that:
-- union when everything is similar in one row except one (maybe)
-- labeling each row
-- case when 
