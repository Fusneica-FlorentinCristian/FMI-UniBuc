--11
describe employees;

select last_name, department_id
FROM employees
where employee_id=104;

--12
select last_name, salary
FROM employees
where salary not between 1500 and 2850;

select last_name, salary
FROM employees
where salary not between 4800 and 9000
order by salary;

--13
SELECT last_name,job_id, hire_date
FROM employees
WHERE hire_date BETWEEN '20-FEB-1987' and '1-may-1989'
ORDER BY 3;

--14
select last_name, department_id
FROM employees
where department_id in (10, 30, 50)
order by last_name;

--15
select last_name as Angajat, department_id, 
       salary as "Salariu lunar"
FROM employees
where department_id in (10, 30, 50) and salary >1500
order by last_name;

--16 
select sysdate
from dual;

select to_char(sysdate, 'dd/mm/yyyy hh24:mi:ss') as "data si ora"
from dual;

select to_char(sysdate,'d/ddd/dy/day/mon/month/yy/year sssss') as "Alte elemente"
from dual;

--17
select last_name,hire_date
FROM employees
WHERE hire_date like('%87%');

--18
select last_name,first_name, hire_date
from employees
where extract(day from hire_date)=extract(day from sysdate);

--19 florin
select job_id
from employees
where manager_id is null;

--Florin 20
select last_name, salary, commission_pct
from employees
where commission_pct is not null
order by salary desc, commission_pct desc;

--22
select last_name
from employees
where last_name like('__a%');

--23
SELECT first_name 
FROM employees 
WHERE lower(first_name) LIKE ('%l%l%') AND (department_id=30 OR manager_id=102);

--24
select last_name, job_id, salary
from employees
where (upper(job_id) like '%CLERK%' or upper(job_id) like '%REP%') and salary not in(1000, 2000, 3000);

--25
select department_name
from departments
where manager_id is null;

