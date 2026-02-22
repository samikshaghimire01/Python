
USE gbd_task;

CREATE TABLE Department (
    Id INT PRIMARY KEY,
    Name VARCHAR(50)
);

CREATE TABLE Employee (
    Id INT PRIMARY KEY,
    Name VARCHAR(50),
    DepartmentId INT,
    Salary INT,
    Active TINYINT,
    FOREIGN KEY (DepartmentId) REFERENCES Department(Id)
);
INSERT INTO Department (Id, Name) VALUES
(1, 'IT'),
(2, 'Admin'),
(3, 'HR'),
(4, 'Accounts'),
(5, 'Health');

INSERT INTO Employee (Id, Name, DepartmentId, Salary, Active) VALUES
(1, 'John', 1, 2000, 1),
(2, 'Sean', 1, 4000, 1),
(3, 'Eric', 2, 2000, 1),
(4, 'Nancy', 2, 2000, 1),
(5, 'Lee', 3, 3000, 1),
(6, 'Steven', 4, 2000, 1),
(7, 'Matt', 1, 5000, 1),
(8, 'Sarah', 1, 2000, 0);

SELECT *FROM Employee
ORDER BY Salary ASC;

SELECT DISTINCT Salary
FROM Employee;

SELECT COUNT(*) AS TotalActiveEmployees
FROM Employee
WHERE Active = 1;

UPDATE Employee
SET DepartmentId = 3
WHERE Name = 'Nancy';

SELECT *FROM Employee
ORDER BY Salary DESC
LIMIT 2;

SELECT e.Name AS EmployeeName, d.Name AS DepartmentName
FROM Employee e
JOIN Department d ON e.DepartmentId = d.Id;

SELECT d.Name AS DepartmentName, COUNT(e.Id) AS EmployeeCount
FROM Department d
LEFT JOIN Employee e ON e.DepartmentId = d.Id
GROUP BY d.Id, d.Name
ORDER BY EmployeeCount DESC
LIMIT 1;

SELECT d.Name AS DepartmentName
FROM Department d
LEFT JOIN Employee e ON e.DepartmentId = d.Id
WHERE e.Id IS NULL;

SELECT Name, Salary
FROM Employee
WHERE Salary IN (
    SELECT Salary
    FROM Employee
    GROUP BY Salary
    HAVING COUNT(*) > 1
)
ORDER BY Salary;

SELECT name, Avg(Salary)
FROM Employee
group by name
ORDER By AVG(salary);








