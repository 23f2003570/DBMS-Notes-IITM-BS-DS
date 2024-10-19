# SQL Problems

## Question 1 (Q1/2023/T3)

```SQL
CREATE TABLE student_marks(
    roll_number     VARCHAR(5) NOT NULL,
    course_id       VARCHAR(6) NOT NULL,
    assignment_id   VARCHAR(20) NOT NULL,
    marks           INT NOT NULL
)
INSERT INTO student_marks VALUES ('21f12', 'CS2001', 'Q1', 65);
INSERT INTO student_marks VALUES ('21f12', 'CS2001', 'Q2', 72);
INSERT INTO student_marks VALUES ('21f12', 'CS2001', 'Finals', 79);

INSERT INTO student_marks VALUES ('21f13', 'CS2001', 'Finals', 81);
INSERT INTO student_marks VALUES ('21f13', 'CS2001', 'Q2', 90);

INSERT INTO student_marks VALUES ('21f11', 'CS2001', 'Finals', 95);
INSERT INTO student_marks VALUES ('21f11', 'CS2001', 'Q1', 59);
```

What is the SQL QUERY to:
1. Show distinct roll numbers
2. Their corresponding marks in Q1, Q2, Finals?



