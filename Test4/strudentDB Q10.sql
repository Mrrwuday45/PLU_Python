CREATE DATABASE StudentDB;

USE StudentDB;

CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    CourseID INT
);
CREATE TABLE Course (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(50)
);

INSERT INTO Student (StudentID, Name, CourseID)
VALUES
(1, 'Rahul', 101),
(2, 'Neha', 102),
(3, 'Aman', 101);

INSERT INTO Course (CourseID, CourseName)
VALUES
(101, 'Python'),
(102, 'Java');

SELECT * FROM Student;

SELECT * FROM Course;
SELECT 
    Student.Name,
    Course.CourseName
FROM Student
INNER JOIN Course
ON Student.CourseID = Course.CourseID;
SELECT 
    Student.Name,
    Course.CourseName
FROM Student
INNER JOIN Course
ON Student.CourseID = Course.CourseID
WHERE Course.CourseName = 'Python';
CREATE VIEW PythonStudents AS
SELECT 
    Student.Name,
    Course.CourseName
FROM Student
INNER JOIN Course
ON Student.CourseID = Course.CourseID
WHERE Course.CourseName = 'Python';