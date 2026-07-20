create DATABASE Employe;
use Employe;
CREATE TABLE Employes (
    EmployeeID INT,
    Name VARCHAR(100),
    Department VARCHAR(50),
    Salary INT
);

INSERT INTO Employes VALUES
(1,'Rahul','IT',65000),
(2,'Priya','HR',45000),
(3,'Aman','IT',70000);
CREATE VIEW HighSalaryEmployees AS
SELECT * FROM Employes
WHERE Salary > 60000;
SELECT * FROM HighSalaryEmployees;