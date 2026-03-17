# Write your MySQL query statement below
select Product.product_name, Sales.year, Sales.price
From Sales
Left Join Product
On Product.product_id = Sales.product_id


