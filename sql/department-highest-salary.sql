with cte as (select
    *,
    dense_rank() over (partition by departmentid order by salary desc) as salary_rnk
from
    employee)

select
    d.name as department,
    e.name as employee,
    e.salary
from
    department d
join
    cte e on e.departmentid = d.id
where
    e.salary_rnk = 1