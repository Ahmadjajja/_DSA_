# Write your MySQL query statement below
SELECT DISTINCT product_id,
    COALESCE(
        (SELECT new_price
         FROM Products
         WHERE change_date <= '2019-08-16'
           AND product_id = p1.product_id
         ORDER BY change_date DESC
         LIMIT 1),
        10
    ) AS price
FROM Products AS p1;