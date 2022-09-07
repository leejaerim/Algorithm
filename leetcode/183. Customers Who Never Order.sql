# Write your MySQL query statement below
select name as Customers from Customers where not id in (select customerId from Orders)