SELECT d.Name AS DepartmentName, SUM(e.Salary) AS TotalSalary
FROM Department d
JOIN Employee e ON e.DepartmentId = d.Id
GROUP BY d.Id, d.Name;

SELECT d.Name AS DepartmentName, AVG(e.Salary) AS AvgSalary
FROM Department d
JOIN Employee e ON e.DepartmentId = d.Id
GROUP BY d.Id, d.Name;

SELECT e2.Name AS EmployeeName, d.Name AS DepartmentName
FROM Employee e1
JOIN Employee e2 ON e1.DepartmentId = e2.DepartmentId
JOIN Department d ON e2.DepartmentId = d.Id
WHERE e1.Name = 'John' AND e2.Name <> 'John';

SELECT e.Name AS EmployeeName, d.Name AS DepartmentName
FROM Employee e
JOIN Department d ON e.DepartmentId = d.Id
WHERE d.Name <> 'IT';

SELECT d.Name AS DepartmentName, SUM(e.Salary) AS TotalSalary
FROM Department d
JOIN Employee e ON e.DepartmentId = d.Id
GROUP BY d.Id, d.Name
ORDER BY TotalSalary DESC
LIMIT 1;

SELECT e.Name, e.Salary
FROM Employee e
JOIN Department d ON e.DepartmentId = d.Id
WHERE d.Name = 'HR' AND e.Salary = (
    SELECT MAX(e2.Salary)
    FROM Employee e2
    JOIN Department d2 ON e2.DepartmentId = d2.Id
    WHERE d2.Name = 'HR'
);

SELECT e.Name AS EmployeeName, 
       COALESCE(d.Name, 'No Department') AS DepartmentName
FROM Employee e
LEFT JOIN Department d ON e.DepartmentId = d.Id;

SELECT DISTINCT d.Name AS DepartmentName
FROM Department d
JOIN Employee e ON e.DepartmentId = d.Id
WHERE e.Salary > (SELECT AVG(Salary) FROM Employee);

SELECT d.Name AS DepartmentName, e.Salary, COUNT(*) AS EmployeeCount
FROM Employee e
JOIN Department d ON e.DepartmentId = d.Id
GROUP BY d.Id, e.Salary
HAVING COUNT(*) > 1;





