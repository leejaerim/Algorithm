# Write your MySQL query statement below
select name as Employee 
from Employee a
where 
    a.salary > (select salary from employee b where b.id =  a.managerId)