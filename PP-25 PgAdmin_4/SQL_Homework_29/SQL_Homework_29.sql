-- CREATE TABLE departments (
--     id INT PRIMARY KEY,
--     name VARCHAR(30),
--     location VARCHAR(30)
-- );

-- CREATE TABLE employees (
--     id INT PRIMARY KEY,
--     name VARCHAR(30),
--     salary DECIMAL(6, 2),
--     department_id INT,
--     FOREIGN KEY (department_id) REFERENCES departments(id)
-- );


-- INSERT INTO departments (id, name, location) VALUES
-- (1, 'IT', 'Wizard Tower'),
-- (2, 'Marketing', 'Atlantis Underwater HQ'),
-- (3, 'HR', 'Ninja Mountain'),
-- (4, 'Finance', 'Secret Volcano Lair');


-- INSERT INTO employees (id, name, salary, department_id) VALUES
-- (1, 'Anna', 5500, 1),
-- (2, 'Ben', 6000, 2),
-- (3, 'Charlie', 4500, 3),
-- (4, 'Diana', 7000, 1),
-- (5, 'Eli', 6200, 2),
-- (6, 'Fiona', 5000, 4),
-- (7, 'George', 4800, 3),
-- (8, 'Helen', 5200, 4);

-- SELECT * FROM employees
-- ORDER BY id ASC 
-- SELECT * FROM departments
-- ORDER BY id ASC

-- 1)
-- SELECT name, salary
-- FROM employees
-- WHERE salary > (SELECT AVG(salary) FROM employees);

-- 2)
-- SELECT 
--     e.name, 
--     e.salary, 
--     (SELECT d.name FROM departments d WHERE d.id = e.department_id) AS department_name
-- FROM employees e;

-- 3)
-- SELECT name, salary
-- FROM employees
-- WHERE department_id IN (
--     SELECT id FROM departments WHERE location = 'Wizard Tower'
-- );

-- 4)
-- SELECT *
-- FROM departments d
-- WHERE EXISTS (
--     SELECT 1 FROM employees e WHERE e.department_id = d.id
-- );

-- 5)
-- SELECT name, salary
-- FROM employees
-- WHERE salary > ANY (
--     SELECT salary FROM employees WHERE department_id = (
--         SELECT id FROM departments WHERE name = 'Marketing'
--     )
-- );

-- 6)
-- INSERT INTO employees (id, name, salary, department_id)
-- VALUES (9, 'Captain Bananas', 7500, 2); -- ეს მეექვსეში ასეთი თანამშრომელი არ მყავდა და დავამატე

-- SELECT name, salary FROM employees
-- WHERE salary > ALL (
--     SELECT salary FROM employees WHERE department_id = (
--         SELECT id FROM departments WHERE name = 'IT'
--     )
);

-- 7)
-- SELECT * FROM employees
-- WHERE department_id IN (
--     SELECT id FROM departments WHERE location = 'Wizard Tower'
-- )
-- UNION
-- SELECT * FROM employees
-- WHERE department_id IN (
--     SELECT id FROM departments WHERE location = 'Atlantis Underwater HQ'
-- );

-- 8)
-- SELECT * FROM employees
-- WHERE department_id IN (
--     SELECT id FROM departments WHERE location = 'Wizard Tower'
-- )
-- UNION ALL
-- SELECT * FROM employees
-- WHERE department_id IN (
--     SELECT id FROM departments WHERE location = 'Atlantis Underwater HQ'
-- );







 

