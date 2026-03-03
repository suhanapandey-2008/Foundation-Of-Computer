# Inserting a new student
INSERT INTO Student (StudentID, StudentName, Email)
VALUES (8, 'Riya', 'riya@email.com');
# Inserting a New Club
INSERT INTO Club (ClubID, ClubName, ClubRoom, ClubMentor)
VALUES (5, 'Art Club', 'R404', 'Ms. Meera');
# Displaying all students
SELECT * FROM Student;
# Displaying all clubs
SELECT * FROM Club;
# SQL JOIN Operation
SELECT 
    Student.StudentName,
    Club.ClubName,
    Membership.JoinDate
FROM Membership
JOIN Student 
    ON Membership.StudentID = Student.StudentID
JOIN Club 
    ON Membership.ClubID = Club.ClubID;
