USE BSCS;
CREATE TABLE department
(DeptNo INT NOT NULL PRIMARY KEY,
DName VARCHAR(50) NOT NULL,
Loc VARCHAR(50) NOT NULL);
CREATE TABLE employee
(EmpNo VARCHAR(50) NOT NULL PRIMARY KEY,
Ename VARCHAR(50) NOT NULL,
Job VARCHAR(50) NOT NULL,
Salary INT,
DeptNo INT NOT NULL,
FOREIGN KEY (DeptNo) REFERENCES department(DeptNo));
INSERT INTO department VALUES ('10', 'SALES', 'KAMPALA'), ('40', 'MARKETING', 'ENTEBBE'), ('30', 'ACCOUNTING', 'MUKONO');
INSERT INTO employee VALUES ('E001', 'NULL', 'Clerk', 40000, 30), ('E002', 'Agaba', 'Manager', 16000, 30), ('E003', 'Mary', 'SalesLady', 20000, 10), ('E004', 'Timo', 'Clerk', 40000, 30), ('E005', 'Simon', 'Manager', 60000, 40), ('E006', 'Mark', 'Manager', 45000, 10), ('E007', 'Solomon', 'Teacher', 30000, 30);

DESC department;
DESC employee;
CREATE VIEW view_d AS SELECT * FROM employee WHERE `DeptNo`=30;

CREATE view view_e AS SELECT job, count(*) AS numEmployees FROM employee GROUP BY job;

CREATE view view_f AS SELECT * FROM employee WHERE ename LIKE 't%';

CREATE view view_g AS SELECT DISTINCT job FROM employee ORDER BY job DESC;

CREATE view view_h AS SELECT job, sum(salary) AS  totalSalary FROM employee GROUP BY job;

CREATE view view_i AS SELECT job, sum(salary) AS totalSalary FROM employee GROUP BY job HAVING sum(salary)>30000;

CREATE view view_j AS SELECT job, sum(salary) AS totalSalary, avg(salary) AS averageSalary FROM employee GROUP BY job;

ALTER TABLE department ADD COLUMN Project VARCHAR(50);

ALTER TABLE department MODIFY COLUMN Dname VARCHAR(60);

show tables;

CREATE VIEW view_n AS SELECT DeptNo, Dname, Loc, Project, CASE
WHEN deptno = 10 THEN 'computing dept'
WHEN deptno = 30 THEN 'business dept'
WHEN deptno = 40 THEN 'marketing dept'
ELSE 'N/A'
END AS newdeptnames FROM department;

CREATE view view_o AS SELECT empno, ename, job, salary, deptno, CASE
WHEN deptno = 10 THEN salary*1.08
WHEN deptno = 30 THEN salary*1.12
WHEN deptno = 40 THEN salary*1.1
ELSE salary
END AS newsalary FROM employee;

START TRANSACTION;

UPDATE employee SET Salary= 80000, job='cleaner' WHERE EmpNo='e004';

DELETE FROM employee WHERE empno='e002';

SELECT * FROM employee;

ROLLBACK;

SELECT * FROM employee;
CREATE TABLE project
(projID INT PRIMARY KEY AUTO_INCREMENT,
projName VARCHAR(100) NOT NULL,
DeptNo INT,
FOREIGN KEY (DeptNo) REFERENCES department(DeptNo),
EmpNo VARCHAR(50),
FOREIGN KEY (EmpNo) REFERENCES employee(EmpNo));
INSERT INTO project VALUES (1, 'Sales Boost', 10, 'E003'), (2, 'Marketing Expansion', 40, 'E005'), (3, 'Accounting Automation', 30,'E007'), (4, 'Sales Strategy', 10,'E006');

/*ALTER TABLE project ADD COLUMN assignedDate DATE, ROLE;*/
SELECT e.EmpNO, e.Ename, e.Job, e.Salary, d.DName, d.Loc
FROM employee e
JOIN department d ON e.DeptNo = d.DeptNo;

SELECT p.projID, p.projName, d.DName, d.Loc
FROM project p
JOIN department d ON p.DeptNo = d.DeptNo;
SELECT e.EmpNo, e.Ename, e.Job, e.Salary, d.DName AS department, p.projName AS project
FROM employee e 
JOIN department d ON e.DeptNo = d.DeptNo
JOIN project p ON d.DeptNo = p.DeptNo;
SELECT p.projName, d.DName, e.Ename, e.Job
FROM project p 
JOIN department d ON p.DeptNo = d.DeptNo 
JOIN employee e ON e.DeptNo = d.DeptNo;
SELECT e.EmpNo, e.Ename, e.Job, e.Salary, d.DName, p.projName 
FROM employee e
JOIN department d ON e.DeptNo = d.DeptNo 
JOIN project p ON d.DeptNo = p.DeptNo WHERE e.Salary > 40000;
SELECT d.DName, p.projName, COUNT(e.EmpNo) AS totalEmployees 
FROM employee e 
JOIN department d on e.DeptNo = d.DeptNo 
JOIN project p ON d.DeptNo = p.DeptNo;
SELECT e.EmpNo, e.Ename, e.Job, d.DName, p.projName 
FROM employee e
JOIN department d ON e.DeptNo = d.DeptNo 
JOIN project p ON d.DeptNo = p.DeptNo WHERE e.Job = 'Manager';
UPDATE employee SET Salary = 45000 WHERE EmpNo = 'E003';
ALTER TABLE project ADD COLUMN role VARCHAR(50);
ALTER TABLE project ADD COLUMN assignedDate DATE;
