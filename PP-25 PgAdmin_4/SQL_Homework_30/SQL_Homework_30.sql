CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Grade INT
);

CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseName VARCHAR(100),
    Semester VARCHAR(20),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

INSERT INTO Students (StudentID, FirstName, LastName, Grade) VALUES
(1, 'Anna', 'Smith', 10),
(2, 'John', 'Doe', 11),
(3, 'Maria', 'Lopez', 10);

INSERT INTO Enrollments (EnrollmentID, StudentID, CourseName, Semester) VALUES
(101, 1, 'Math', 'Fall'),
(102, 1, 'English', 'Fall'),
(103, 2, 'Biology', 'Spring'),
(104, 3, 'History', 'Fall');

CREATE VIEW AllStudents AS
SELECT * FROM Students;
SELECT * FROM AllStudents;

CREATE VIEW TenthGradeStudents AS
SELECT * 
FROM Students
WHERE Grade = 10;
SELECT * FROM TenthGradeStudents;

CREATE VIEW StudentEnrollments AS
SELECT 
    s.StudentID,
    s.FirstName,
    s.LastName,
    s.Grade,
    e.EnrollmentID,
    e.CourseName,
    e.Semester
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID;

SELECT * FROM StudentEnrollments;

CREATE OR REPLACE VIEW TenthGradeStudents AS
SELECT * 
FROM Students
WHERE Grade = 11;

CREATE OR REPLACE VIEW StudentEnrollments AS
SELECT 
    s.StudentID,
    s.FirstName,
    s.LastName,
    CONCAT(s.FirstName, ' ', s.LastName) AS FullName, 
    e.EnrollmentID,
    e.CourseName,
    e.Semester
FROM Students s
JOIN Enrollments e ON s.StudentID = e.StudentID;

DROP VIEW IF EXISTS TenthGradeStudents;
DROP VIEW IF EXISTS StudentEnrollments;

CREATE OR REPLACE PROCEDURE DeleteStudentByID(IN sid INT)
LANGUAGE SQL
AS $$
    DELETE FROM Students WHERE StudentID = sid;
$$;

CALL DeleteStudentByID(2);

CREATE OR REPLACE PROCEDURE UpdateStudentGrade(IN sid INT, IN new_grade INT)
LANGUAGE SQL
AS $$
    UPDATE Students
    SET Grade = new_grade
    WHERE StudentID = sid;
$$;

CALL UpdateStudentGrade(1, 12);

ALTER TABLE Students
ADD COLUMN LastUpdated TIMESTAMP;

CREATE OR REPLACE FUNCTION update_last_modified()
RETURNS TRIGGER AS $$
BEGIN
    NEW.LastUpdated := NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_last_updated
BEFORE UPDATE ON Students
FOR EACH ROW
EXECUTE FUNCTION update_last_modified();
