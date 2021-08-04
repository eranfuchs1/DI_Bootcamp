```
select first_name as First_Name, last_name as Last_Name from employees;
select distinct department_id from employees;
select * from employees order by first_name desc;
select first_name, last_name, salary, salary * 0.15 as PF from employees;
select employee_id, first_name, last_name, salary from employees order by salary asc;
select sum(salary) from employees;
select min(salary) as minimum, max(salary) as maximum from employees;
select avg(salary) from employees;
select count(employee_id) from employees;
select upper(first_name) from employees;
select substring(first_name, 0, 4) from employees;
select first_name||' '||last_name as full_name from employees;
select first_name, last_name, char_length(first_name||' '||last_name) as full_name_length from employees;
select first_name like '%[0-9]%' as contains_numbers from employees;
select * from employees limit 10;
select * from employees where first_name like '%c%' and first_name like '%e%';
select first_name, last_name, salary from employees where salary >= 10000 and salary <= 15000;
select first_name, last_name, hire_date from employees where extract(year from hire_date) = '1997';
select employees.first_name, employees.last_name, jobs.job_title from employees inner join jobs on employees.job_id = jobs.job_id where jobs.job_title != 'Programmer' and jobs.job_title != 'Shipping Clerk' and employees.salary not in (4500, 10000, 15000);
select last_name from employees where char_length(last_name) = 6;
select last_name from employees where last_name like '__e%';
select distinct jobs.job_title from employees inner join jobs on jobs.job_id = employees.job_id;
select * from employees where last_name in ('Jones', 'Blake', 'Scott', 'King', 'Ford');
```
