USE project_py;


CREATE TABLE students (

    id INT PRIMARY KEY AUTO_INCREMENT,

    name VARCHAR(100),

    department VARCHAR(100)
);

CREATE TABLE grades (

    id INT PRIMARY KEY AUTO_INCREMENT,

    student_id INT,

    course VARCHAR(100),

    grade FLOAT,

    FOREIGN KEY (student_id) REFERENCES students(id)
);


CREATE TABLE ml_students (

    id INT PRIMARY KEY AUTO_INCREMENT,

    study_hours FLOAT,

    absences INT,

    final_grade FLOAT
);