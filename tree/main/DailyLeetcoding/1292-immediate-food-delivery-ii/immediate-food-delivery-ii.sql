# Write your MySQL query statement below

select round((sum(

    case when order_date = 
    (select order_date from Delivery
    where customer_id = d.customer_id
    order by order_date limit 1)
     then 1 else 0 end

) / (
    select count(distinct customer_id) from Delivery
) * 100), 2) as immediate_percentage from Delivery as d
where order_date = customer_pref_delivery_date
