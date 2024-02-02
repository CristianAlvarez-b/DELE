

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    major TEXT,
    FOREIGN KEY (major) REFERENCES courses(course_code)
);

CREATE TABLE professors (
    professor_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE administrators (
    admin_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE courses (
    course_code TEXT PRIMARY KEY,
    course_name TEXT NOT NULL,
    professor_id INTEGER,
    FOREIGN KEY (professor_id) REFERENCES professors(professor_id)
    );

/*INNER JOIN
Devuelve sólo las filas que tienen valores coincidentes en ambas tablas.
*/
SELECT students.name AS student_name, students.email, students.age, courses.course_name
FROM students
INNER JOIN courses ON students.major = courses.course_code;

/* LEFT JOIN
Devuelve todas las filas de la tabla de la izquierda y las filas coincidentes de la tabla de la derecha.
*/
SELECT students.student_id, students.name, COALESCE(courses.course_name, 'No asignado') AS course_name
FROM students
LEFT JOIN courses ON students.major = courses.course_code;


/*RIGHT JOIN
Devuelve todas las filas de la tabla derecha y las filas coincidentes de la tabla izquierda.
*/

SELECT students.student_id, students.name AS student_name, courses.course_name, professors.name AS professor_name
FROM courses
LEFT JOIN students ON students.major = courses.course_code
RIGHT JOIN professors ON courses.professor_id = professors.professor_id;


/*FULL OUTER JOIN
Devuelve todas las filas cuando hay una coincidencia en la tabla izquierda o derecha.
*/
SELECT COALESCE(students.student_id, 'No asignado') AS student_id, 
       COALESCE(students.name, 'No asignado') AS student_name, 
       COALESCE(courses.course_name, 'No asignado') AS course_name, 
       COALESCE(professors.name, 'No asignado') AS professor_name,
       administrators.name AS admin_name
FROM students
FULL OUTER JOIN courses ON students.major = courses.course_code
FULL OUTER JOIN professors ON courses.professor_id = professors.professor_id
FULL OUTER JOIN administrators ON students.student_id = administrators.admin_id;



/* "where” clauses
 */
 SELECT student_id, name, age, major
FROM students
WHERE age > 21;


SELECT course_code, course_name, professor_id
FROM courses
WHERE professor_id = 2;

/*inserts*/
INSERT INTO students (name, email, age, major) VALUES
('Diego Rojas', 'diego.rojas@mail.com', 21, 'Math'),
('Enrique Gonzalez', 'enrique.gonzalez@mail.com', 21, 'Enge'),
('Sergio Otero', 'sergio.otero@example.com', 21, 'Enge'),
('Laura Torres', 'laura.torres@mail.com', 22, 'Adco'),
('Miguel Rodriguez', 'miguel.rodriguez@mail.com', 20, 'Phys'),
('Ana Lopez', 'ana.lopez@mail.com', 23, 'Math'),
('Luisa Gomez', 'luisa.gomez@mail.com', 20, 'Hist'),
    ('Carlos Mendoza', 'carlos.mendoza@mail.com', 22, 'BioAd'),
    ('Isabel Ramirez', 'isabel.ramirez@mail.com', 21, 'EconM'),
    ('Raul Fernandez', 'raul.fernandez@mail.com', 23, 'CompSci'),
    ('Maria Santos', 'maria.santos@mail.com', 22, 'EngLit'),
    ('Javier Torres', 'javier.torres@mail.com', 20, 'Art1'),
    ('Elena Rodriguez', 'elena.rodriguez@mail.com', 24, 'MusicT'),
    ('Pedro Martinez', 'pedro.martinez@mail.com', 21, 'MathB'),
    ('Sofia Herrera', 'sofia.herrera@mail.com', 20, 'ChemB'),
    ('Alejandro Garcia', 'alejandro.garcia@mail.com', 23, 'Math');

INSERT INTO professors (professor_id, name) VALUES 
    (1, 'Professor A'),
    (2, 'Professor B'),
    (3, 'Professor C'),
    (4, 'Professor D');
    
INSERT INTO courses (course_code, course_name, professor_id) VALUES 
    ('Enge', 'Engineering', 1),
    ('Math', 'Mathematics', 2),
    ('Adco', 'Advanced Computer Science', 3),
    ('Phys', 'Intro to Physics', 4),
    ('MathB', 'Basic Mathematics', 2),
    ('ChemB', 'Chemistry Basics', 3),
    ('Hist', 'World History', 4),
    ('BioAd', 'Biology Advanced', 1),
    ('EconM', 'Microeconomics', 2),
    ('CompSci', 'Data Structures', 3),
    ('EngLit', 'English Literature', 4),
    ('Art1', 'Introduction to Art', 1),
    ('MusicT', 'Music Theory', 2);
    
INSERT INTO administrators (admin_id, name) VALUES 
    (1, 'Admin 1'),
    (2, 'Admin 2'),
    (3, 'Admin 3'),
    (4, 'Admin 4'),    
    (5, 'Admin 5');
    
   

