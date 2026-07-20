CREATE DATABASE STUDENTS;
USE STUDENTS;

CREATE TABLE StudentS (
    StudentID INT,
    Name VARCHAR(100),
    CourseID INT
);

INSERT INTO StudentS VALUES
(1,'Rahul',201),
(2,'Neha',202),
(3,'Aman',NULL);

CREATE TABLE Course (
    CourseID INT,
    CourseName VARCHAR(100)
);

INSERT INTO Course VALUES
(201,'Python'),
(202,'SQL');

SELECT StudentS.Name,
       Course.CourseName
FROM StudentS
LEFT JOIN Course
ON StudentS.CourseID = Course.CourseID;