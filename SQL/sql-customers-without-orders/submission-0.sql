-- Write your query below
-- select customers.name where customers.id not in (orders.customer_id)

select name from customers where id not in (select customer_id from orders)