
# Answers

## Question 1 (Q1/2023/T3)

### Understand WITH Syntax
```SQL
WITH A AS (SELECT roll_number, marks FROM student_marks WHERE assignment_id='Q1')
SELECT A.roll_number
FROM A

/*
roll_number 
-------------
 21f12
 21f11
(2 rows)
*/
```

### Answer

The sorted entities are

#### A
|roll_number|marks (Q1)|
|-|-|
|21f11|59|
|21f12|65|
|21f13|-|

#### B
|roll_number|marks (Q2)|
|-|-|
|21f11|-|
|21f12|72|
|21f13|90|

#### C
|roll_number|marks (Finals)|
|-|-|
|21f11|95|
|21f12|79|
|21f13|81|

Since the Professor wants all the roll numbers, the Left JOIN will have to start from C

**LEFT JOIN YIELDS**
```
 roll_number | marks | roll_number | marks | roll_number | marks 
-------------+-------+-------------+-------+-------------+-------
 21f11       |    95 | 21f11       |    59 |             |      
 21f12       |    79 | 21f12       |    65 | 21f12       |    72
 21f13       |    81 |             |       | 21f13       |    90
(3 rows)
```

**RIGHT JOIN YIELDS**
```
 roll_number | marks | roll_number | marks | roll_number | marks 
-------------+-------+-------------+-------+-------------+-------
 21f12       |    79 | 21f12       |    65 | 21f12       |    72
             |       |             |       | 21f13       |    90
(2 rows)
```


```sql
-- OPTION A - Incorrect
WITH A AS (SELECT roll_number, marks FROM student_marks WHERE assignment_id='Q1'),
B AS (SELECT roll_number, marks FROM student_marks WHERE assignment_id='Q2'),
C AS (SELECT roll_number, marks FROM student_marks WHERE assignment_id='Finals')
SELECT A.roll_number, A.marks AS Q1, B.marks AS Q2, C.marks as Finals FROM C
LEFT JOIN A ON A.roll_number = C.roll_number
LEFT JOIN B ON B.roll_number = C.roll_number
ORDER BY roll_number

 roll_number | marks | roll_number | marks | roll_number | marks 
-------------+-------+-------------+-------+-------------+-------
 21f11       |    95 | 21f11       |    59 |             |      
 21f12       |    79 | 21f12       |    65 | 21f12       |    72
 21f13       |    81 |             |       | 21f13       |    90
(3 rows)

 roll_number | q1 | q2 | finals 
-------------+----+----+--------
 21f11       | 59 |    |     95
 21f12       | 65 | 72 |     79
             |    | 90 |     81
(3 rows)

```

```sql
-- OPTION B CORRECT ANSWER

WITH A AS (SELECT roll_number, marks FROM student_marks WHERE assignment_id='Q1'),
B AS (SELECT roll_number, marks FROM student_marks WHERE assignment_id='Q2'),
C AS (SELECT roll_number, marks FROM student_marks WHERE assignment_id='Finals')
SELECT C.roll_number, A.marks AS Q1, B.marks AS Q2, C.marks as Finals FROM C
LEFT JOIN A ON A.roll_number = C.roll_number
LEFT JOIN B ON B.roll_number = C.roll_number
ORDER BY roll_number


roll_number | q1 | q2 | finals 
-------------+----+----+--------
 21f11       | 59 |    |     95
 21f12       | 65 | 72 |     79
 21f13       |    | 90 |     81
(3 rows)
```

```sql
---Option C Incorrect
WITH A AS (SELECT roll_number, marks FROM student_marks WHERE assignment_id='Q1'),
B AS (SELECT roll_number, marks FROM student_marks WHERE assignment_id='Q2'),
C AS (SELECT roll_number, marks FROM student_marks WHERE assignment_id='Finals')
SELECT B.roll_number, A.marks AS Q1, B.marks AS Q2, C.marks as Finals FROM C
LEFT JOIN A ON A.roll_number = C.roll_number
LEFT JOIN B ON B.roll_number = C.roll_number
ORDER BY roll_number

 roll_number | marks | roll_number | marks | roll_number | marks 
-------------+-------+-------------+-------+-------------+-------
 21f12       |    79 | 21f12       |    65 | 21f12       |    72
 21f13       |    81 |             |       | 21f13       |    90
 21f11       |    95 | 21f11       |    59 |             |      
(3 rows)


 roll_number | q1 | q2 | finals 
-------------+----+----+--------
 21f12       | 65 | 72 |     79
 21f13       |    | 90 |     81
             | 59 |    |     95
(3 rows)

```

```sql
-- OPTION D - Incorrect
WITH A AS (SELECT roll_number, marks FROM student_marks WHERE assignment_id='Q1'),
B AS (SELECT roll_number, marks FROM student_marks WHERE assignment_id='Q2'),
C AS (SELECT roll_number, marks FROM student_marks WHERE assignment_id='Finals')
SELECT A.roll_number, A.marks AS Q1, B.marks AS Q2, C.marks as Finals FROM C
FULL JOIN A ON A.roll_number = C.roll_number
FULL JOIN B ON B.roll_number = C.roll_number
ORDER BY roll_number

 roll_number | marks | roll_number | marks | roll_number | marks 
-------------+-------+-------------+-------+-------------+-------
 21f11       |    95 | 21f11       |    59 |             |      
 21f12       |    79 | 21f12       |    65 | 21f12       |    72
 21f13       |    81 |             |       | 21f13       |    90
(3 rows)

 roll_number | q1 | q2 | finals 
-------------+----+----+--------
 21f11       | 59 |    |     95
 21f12       | 65 | 72 |     79
             |    | 90 |     81
(3 rows)
```

-----



## Question 2 (Q1/2023/T3)

Using University DB, Find ID and student names of all students who take all courses offered by biology department


**Question Decomposition**
1. Find me ALL STUDENTS
2. WHO TAKE ALL COURSES OFFERED BY BIOLOGY DEPARTMENT
3. optional: they may take other courses.


**Plan**
1. SET A - ALL COURSES FROM BIOLOGY DEPARTMENT
2. SET B - ALL COURSES A STUDENT TAKES
3. $A - B$ set difference
   1. This will be $\{\}$ if he takes all courses offered by biology department
   2. This will be a set if he takes SOME or NO courses from Biology department

### Options from the Exam Question

```sql
-- Option A - INCORRECT
SELECT DISTINCT S.id, S.name
FROM student AS S
WHERE NOT EXISTS (
    (SELECT course_id FROM course WHERE dept_name='Biology'
     UNION
     SELECT T.course_id 
     FROM takes AS T
     WHERE S.id = T.ID)
)

/*
id | name 
----+------
(0 rows)
*/

/*
    A = The subquery of NOT EXISTS says
        ALL COURSES OFFERED BY BIOLOGY DEPT (SELECT course_id FROM course WHERE dept_name='Biology')
        +
        ALL COURSES THE STUDENT TAKES (SELECT T.course_id 
                FROM takes AS T
                WHERE S.id = T.ID)
    IF A IS EMPTY THEN SELECT THE STUDENT

    This can only happen if there are NO Biology courses AND No courses the student has selected.
/*
```

```sql
-- Option B - INCORRECT

SELECT DISTINCT S.id, S.name
FROM student AS S
WHERE EXISTS (
    (SELECT course_id FROM course WHERE dept_name='Biology')
     EXCEPT
     SELECT T.course_id 
     FROM takes AS T
     WHERE S.id = T.ID);
-- (2000 rows), basically there was at least 1 relation in the EXISTS clause

/*
The query is saying
    1. A = (ALL BIO COURSES - ALL STUDENT COURSES)
    2. IF A is NOT EMPTY then select the student

This means the student selected SOME or NO BIOLOGY courses
*/
```

```sql
-- Option C - Correct one!
SELECT DISTINCT S.id, S.name
FROM student AS S
WHERE NOT EXISTS (
    (SELECT course_id FROM course WHERE dept_name='Biology')
     EXCEPT
     SELECT T.course_id 
     FROM takes AS T
     WHERE S.id = T.ID);

/*
    A = ALL BIOLOGY COURSES
    B = COURSES The kid took
    A-B = ALL BIOLOGY COURSES the kid DID not take

    if A-B is EMPTY then kid took all biology courses
    if A-B is same cardinality as all bio-courses offered then the kid took no bio courses
    IF A-B has elements then kid took some bio courses
*/

/*
 id | name 
----+------
(0 rows)
*/
```


```sql
-- Option C

SELECT DISTINCT S.id, S.name
FROM student AS S
WHERE NOT EXISTS (
    (SELECT course_id FROM course WHERE dept_name='Biology')
     INTERSECT
     SELECT T.course_id 
     FROM takes AS T
     WHERE S.id = T.ID);
-- (1207 rows)

/*
This means show kids who took bio courses
*/
```

```SQL
SELECT s.id, s.name
FROM student AS S

```