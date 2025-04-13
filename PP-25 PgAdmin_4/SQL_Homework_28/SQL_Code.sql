-- One-To-One Relationship

-- CREATE TABLE users (
-- 	user_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(50) NOT NULL,
-- 	username VARCHAR(20) NOT NULL,
-- 	email VARCHAR(20)
-- );

-- CREATE TABLE profiles (
-- 	profile_id SERIAL PRIMARY KEY,
-- 	user_id INT REFERENCES users(user_id) UNIQUE,
-- 	bio TEXT NOT NULL
-- )

-- INSERT INTO users (name, username) VALUES
-- 	('Arjevanidze Giorgi', 'Giorgi123'),
-- 	('Gaphrindashvili Levan', 'Levan123'),
-- 	('Meskhoradze Beka', 'Beka777')
	

-- INSERT INTO profiles (user_id, bio) VALUES
-- 	(1, 'sjkgdhnlbfk'),
-- 	(2, 'sdjkfbdknc'),
-- 	(3, 'sufhdslkn')

-- SELECT name, username, email, bio FROM users u
-- JOIN profiles p ON u.user_id = p.user_id

-- Many-To-Many Relationship

CREATE TABLE students (
	student_id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	email VARCHAR(30) NOT NULL
);

CREATE TABLE lecturers (
	lecturer_id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	email VARCHAR(20) NOT NULL
);

CREATE TABLE subjects (
	subject_id SERIAL PRIMARY KEY,
	title VARCHAR(20) UNIQUE,
	lecturer_id INT REFERENCES lecturers(lecturer_id) ON DELETE SET NULL
);


CREATE TABLE enrollments (
	enr_id SERIAL PRIMARY KEY,
	student_id INT REFERENCES students(student_id) ON DELETE CASCADE,
	subject_id INT REFERENCES subjects(subject_id) ON DELETE CASCADE,
	enrollment_date DATE DEFAULT CURRENT_DATE,
	UNIQUE(student_id, subject_id)
);


-- INSERT INTO students (name, email) VALUES
-- 	('Guguchia Davit', 'davit@gmail.com'),
-- 	('Tato qoqoshvili', 'tato@gmail.com'),
-- 	('Churkveidze Davit', 'churkv-davit@gmail.com'),
-- 	('Khatia Eliauri', 'eliauri@gmail.com');


-- INSERT INTO lecturers (name, email) VALUES
-- 	('Otar Tumanishvili', 'oto@gmail.com'),
-- 	('Nino Nakashidze', 'nino@gmail.com');


-- INSERT INTO subjects (title, lecturer_id) VALUES
-- 	('Python', 1),
-- 	('JS', 2),
-- 	('HTML', 2),
-- 	('Git', 1)

-- INSERT INTO enrollments(student_id, subject_id) VALUES
-- 	(2, 1),
-- 	(2, 3),
-- 	(1, 3),
-- 	(1, 2),
-- 	(4, 4),
-- 	(4, 1),
-- 	(4, 2),
-- 	(3, 1);

-- SELECT s.name, s.email, title, l.name FROM students s
-- JOIN enrollments e ON s.student_id = e.student_id
-- JOIN subjects su ON su.subject_id = e.subject_id
-- JOIN lecturers l ON l.lecturer_id = su.lecturer_id













