CREATE TABLE students (
    SID INT PRIMARY KEY,
    Name VARCHAR(50),
    Birth_date DATE,
    Department VARCHAR(50)
);

INSERT INTO students (SID, Name, Birth_date, Department)
VALUES (2022999999, 'Jeon', '2009-09-09', 'CSE'),
       (2022999998, 'Hong', '2008-08-08', 'CSE');