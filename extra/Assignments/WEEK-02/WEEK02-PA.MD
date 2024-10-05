# Practice Assignment Week 02

## PA-Q1

Write a SQL statement to find the name of the manager of the team: 'All Stars'.[Database: FLIS]

```sql
SELECT m.name FROM managers AS M
INNER JOIN
teams as t ON t.team_id = m.team_id AND t.name = 'All Stars'
```

## PA-02

Write an SQL statement to find the names of all teams.[Database: FLIS]

```sql
SELECT DISTINCT name FROM teams
```

## PA-03

Write an SQL statement to find the titles of books authored by an author having first name as 'Joh Paul' and last name as 'Mueller'.[Database: LIS]

```sql
SELECT b.title FROM book_catalogue as b
INNER JOIN book_authors AS a
ON b.ISBN_no = a.ISBN_no
AND a.author_fname ILIKE 'Joh Paul'
AND a.author_lname ILIKE 'Mueller'
```

## PA-04

Write a SQL statement to find the titles of books published by 'McGraw Hill Education'.[Database: LIS] 

```sql
SELECT title FROM book_catalogue
WHERE publisher ILIKE 'McGraw Hill Education'
```


## PA-04

Write a SQL statement to display the first name and the last name of students (student_fname, student_lname) pursuing 'PG' courses.[Database: LIS] 

```sql
SELECT student_fname, student_lname FROM students WHERE degree = 'MCA'
```