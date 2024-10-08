# Week 3 Practice Assignments

## Q01

### Write a SQL statement to find the names of teams that have played more than 3 matches.[Database: FLIS]

```sql
SELECT name from teams WHERE team_id IN
(
    SELECT tid FROM
    (SELECT tid, count(tid) AS tid_count FROM
        (
        SELECT host_team_id AS tid FROM matches
        UNION ALL
        SELECT guest_team_id AS tid FROM matches
        ) AS teams
        GROUP BY (tid)) AS filtered_teams
    WHERE tid_count > 3
)
```
NOTE: This was tough. You will have to count both host and guest teams
## Q02

### Write an SQL statement to find the first name, last name of the faculty of the department having department code as 'ME' and who have issued at least one book, such that there are no duplicate firstname-lastname pairs.[Database: LIS]


```SQL
/* REWRITE */
SELECT faculty_fname, faculty_lname, id AS fid FROM faculty
WHERE department_code = 'ME' AND
count(SELECT * FROM book_issue AS s WHERE member_no IN (SELECT member_no FROM members WHERE id = id)) > -10

```

```sql
/* Using Joins */
SELECT faculty_fname, faculty_lname FROM faculty
INNER JOIN
members ON faculty.id = members.id
INNER JOIN
book_issue ON members.member_no = book_issue.member_no
WHERE faculty.department_code = 'ME'
```
## Q03

### Write an SQL statement to find the number of book-titles issued on 11th August 2021.[Database: LIS]

```sql

/* Using Joins */

SELECT count(title) FROM book_catalogue
INNER JOIN
book_copies ON book_copies.ISBN_no = book_catalogue.ISBN_no
INNER JOIN
book_issue ON book_issue.accession_no = book_copies.accession_no
WHERE book_issue.doi = '2021-08-11'
```

```sql
/* Using Sub Queries */

SELECT count(title) FROM book_catalogue
WHERE book_catalogue.ISBN_no 
IN 
(SELECT ISBN_no FROM book_copies 
    WHERE book_copies.ISBN_no = book_catalogue.ISBN_no
        AND book_copies.accession_no IN
            (SELECT accession_no FROM book_issue 
                WHERE book_copies.accession_no = accession_no
                    AND doi = '2021-08-11'))
```
## Q04

### Write a SQL statement to find the names of faculty (faculty_fname, faculty_lname) who did not issue any book.[Database: LIS]

**Tough and WONDERFUL Question!** Actually could not solve it without some additional thinking and rereading the question 4 times !

```sql
SELECT faculty_fname, faculty_lname FROM faculty
LEFT JOIN members ON members.id = faculty.id
LEFT JOIN book_issue ON members.member_no = book_issue.member_no
WHERE book_issue.doi IS NULL
```
## Q05

### Write a SQL statement to find the unique book titles which are issued to 'PG' students but not to 'UG' students .[Database: LIS] lisdb

Heres the UGLY code.

```sql
SELECT DISTINCT title FROM book_catalogue
INNER JOIN book_copies ON book_copies.ISBN_no = book_catalogue.ISBN_no
INNER JOIN book_issue ON book_issue.accession_no = book_copies.accession_no
INNER JOIN members ON members.member_no = book_issue.member_no
WHERE members.member_type = 'PG'
EXCEPT
SELECT DISTINCT title FROM book_catalogue
INNER JOIN book_copies ON book_copies.ISBN_no = book_catalogue.ISBN_no
INNER JOIN book_issue ON book_issue.accession_no = book_copies.accession_no
INNER JOIN members ON members.member_no = book_issue.member_no
WHERE members.member_type = 'UG'
```