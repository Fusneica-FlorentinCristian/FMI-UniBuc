-- Lab 2

----Exercitii
--2
DESC employees;
DESC departments;
DESC jobs;
DESC job_history;
DESC locations;
DESC countries;
DESC regions;


--3
SELECT * FROM employees;
SELECT * FROM departments;
SELECT * FROM jobs;
SELECT * FROM job_history;
SELECT * FROM locations;
SELECT * FROM countries;
SELECT * FROM regions;


--4
SELECT employee_id, first_name, job_id, hire_date FROM employees;

--5
SELECT job_id FROM employees;
SELECT DISTINCT job_id FROM employees;
SELECT UNIQUE job_id FROM employees;


--6
SELECT employee_id ||', '|| first_name||', '||last_name||', '||email||', '||phone_number||', '||hire_date||', '||job_id
||', '||salary||', '||commission_pct||', '||manager_id||', '||department_id "Informatii complete"
FROM employees;

--7
SELECT first_name, salary
FROM employees
WHERE salary>=2850;

--8
SELECT first_name, department_id FROM employees
WHERE employee_id = 104;

--9
SELECT first_name, salary
FROM employees
WHERE NOT (salary <= 2850 AND salary >= 1500);

SELECT first_name, salary
FROM employees
WHERE salary NOT BETWEEN 1500 AND 2850;

--9.1
SELECT first_name, last_name, salary
FROM employees
WHERE salary BETWEEN 3000 AND 7000;

--9.2
SELECT first_name, last_name, salary
FROM employees
WHERE salary >= 3000 AND SALARY <= 7000;

--10
SELECT first_name, job_id, hire_date
 FROM employees
 WHERE hire_date BETWEEN '20-FEB-1987' AND '1-MAY-1989'
 ORDER BY hire_date;

--11
SELECT first_name, department_id
 FROM employees
 WHERE department_id IN (10, 30)
 ORDER BY first_name;
 
 --12
 SELECT first_name ANGAJAT, salary Salariu_lunar
 FROM employees
 WHERE department_id IN (10, 30) AND salary > 1500
 ORDER BY first_name;

--13
SELECT TO_CHAR(SYSDATE, 'YY') FROM dual;

--14
SELECT first_name, hire_date
FROM employees
WHERE TO_NUMBER(TO_CHAR(hire_date,'YYYY')) = 1987;

SELECT first_name, hire_date
FROM employees
WHERE TO_CHAR(hire_date,'YYYY') = '1987'; --merge si fara  ' '

SELECT first_name, hire_date
FROM employees
WHERE hire_date LIKE ('%87%');

--15
SELECT first_name, job_id
FROM employees
WHERE manager_id IS NULL;

--16
SELECT first_name, salary, commission_pct
FROM employees
WHERE commission_pct IS NOT NULL
ORDER BY salary DESC, commission_pct DESC;

--17
SELECT first_name, salary, commission_pct
FROM employees
--WHERE commission_pct IS NOT NULL
ORDER BY salary DESC, commission_pct DESC;

--18
SELECT first_name
FROM employees
WHERE LAST_NAME LIKE('__a%');

--19
SELECT first_name, department_id, manager_id
FROM employees
WHERE lower(first_name)LIKE('%l%l%') AND (department_id = 30 OR manager_id = 102);

--20
SELECT first_name, job_id, salary
FROM employees
WHERE (lower(job_id) LIKE '%clerk%' OR lower(job_id) LIKE '%rep%') AND salary NOT IN (1000,2000,3000);

select last_name, job_id, salary
from employees
where (upper(job_id) like '%CLERK%' or upper(job_id) like '%REP%') and salary not in(1000, 2000, 3000);


SELECT * FROM employees;