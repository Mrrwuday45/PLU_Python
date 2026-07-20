create DATABASE Employees;
use Employees;

CREATE TABLE Employee (
    EmployeeID INT,
    Name VARCHAR(100),
    DepartmentID INT
);

INSERT INTO Employee VALUES
(1,'Rahul',101),
(2,'Priya',102),
(3,'Aman',101);

CREATE TABLE Department (
    DepartmentID INT,
    DepartmentName VARCHAR(50)
);

INSERT INTO Department VALUES
(101,'IT'),
(102,'HR');

SELECT Employee.Name,
       Department.DepartmentName
FROM Employee
INNER JOIN Department
ON Employee.DepartmentID = Department.DepartmentID;