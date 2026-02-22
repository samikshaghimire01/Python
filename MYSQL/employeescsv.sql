CREATE DATABASE company_db;
USE company_db;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    hire_date DATE
);
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/employees.csv'
INTO TABLE employees
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT department, COUNT(*) AS total_employees 
FROM employees 
GROUP BY department;

SELECT department, AVG(salary) as average_salary
From employees
group by department;

Select MAX(salary) as maximum_salary
from employees;

select department, sum(salary) as total_salary_expense
from employees
group by department;

Select department, Count(*) as emp_count
from employees
group by department
having emp_count > 2;

SELECT name, department, salary,
RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS salary_rank
FROM employees;

select name, department, salary,
avg(salary) over(partition by department) as dept_avg_sal
from employees;

select name, hire_date,
row_number() over(order by hire_date) as hire_sequence
from employees;

select name, department, salary, 
salary - avg(salary) over(partition by department) as diff_from_avg
from employees;

select * From(
select name, department, salary,
rank() over(partition by department order by salary desc) as rnk 
 From employees
 ) as highest_paid
 where rnk = 1;


