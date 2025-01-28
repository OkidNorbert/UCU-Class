-- Create programs table
CREATE TABLE programs (
  PID CHAR(4) PRIMARY KEY, 
  PNAME VARCHAR(50) NOT NULL
);

-- Create students table
CREATE TABLE students (
  S_ID CHAR(4) PRIMARY KEY, 
  SNAME VARCHAR(50) NOT NULL, 
  Gender CHAR(1) CHECK (Gender IN ('M', 'F')), 
  PID CHAR(4), 
  FOREIGN KEY (PID) REFERENCES programs(PID)
);

-- Describe programs table
DESC programs;

-- Describe students table
DESC students;

-- Insert data into students table
INSERT INTO students (S_ID, SNAME, Gender, PID) 
VALUES  
  ('S001', 'SIMON', 'M', 'P003'), 
  ('S002', 'MARY', 'F', 'P001'), 
  ('S003', 'JOHN', 'M', 'P002');

-- Add DOB column to students table
ALTER TABLE students ADD DOB DATE;

-- Rename column S_ID to Student_ID in students table
ALTER TABLE students RENAME COLUMN S_ID TO Student_ID;

-- Select students with Gender 'M'
SELECT * FROM students WHERE Gender = 'M';
