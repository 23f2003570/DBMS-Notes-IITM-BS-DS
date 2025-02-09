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




### Nice question from end term

```sql
CREATE TABLE Products (
    Product_SID CHAR(10) PRIMARY KEY,
    Product_Name CHAR(60) UNIQUE,
    Category CHAR(30) NOT NULL,
    Price NUMERIC(8,2) CHECK (Price >= 0),
    Stock INT CHECK (STOCK >= 0)
)
INSERT INTO Products VALUES ('P101', 'Laptop', 'Electronics', 1200.00, 50)
INSERT INTO Products VALUES ('P102', 'Smartphone', 'Electronics', 800.00, 100)
INSERT INTO Products VALUES ('P103', 'Desk Chair', 'Furniture', 150.00, 20)
INSERT INTO Products VALUES ('P104', 'Lamp', 'Furniture', -20, 40);
INSERT INTO Products VALUES ('P106', 'Desk', 'Furniture', 200, NULL);
INSERT INTO Products VALUES ('P105', 'Laptop', 'Electronics', 1100.0, 30);

```