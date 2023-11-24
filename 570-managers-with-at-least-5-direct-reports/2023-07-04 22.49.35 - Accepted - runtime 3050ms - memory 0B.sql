# Write your MySQL query statement below
select e.name from employee as e where (select count(f.managerId ) from employee as  f where f.managerId=e.id )>=5;