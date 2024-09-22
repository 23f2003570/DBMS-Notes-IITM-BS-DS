# Week 3 Notes - DBMS

*Prof. Partha Pratham Das, IIT KGP*

*Notes by Adarsh (23f2003570)*  


## [SQL Samples (28:26)](https://www.youtube.com/watch?v=j6v3lL5xbao&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=10&t=2s)

### Retrieve names of buildings that has classrooms with maximum capacity UTMOST 100

```sql
SELECT DISTINCT building_name
FROM classroom
WHERE capacity < 100
```

### Cartesian Product example

```sql
SELECT name, budget
FROM student, department
WHERE student.dept_name = department.dept_name
        AND budget < 5000
```
This generates ALL combination of student department pairs and applies the 2 filters

### Rename Feature (AS operator)

```sql
SELECT S.name AS student_name, budget AS dept_budget
FROM student AS S, department AS D
WHERE S.dept_name = D.dept_name
        AND budget < 5000
```

### String operations

1. Starts with 3 alphabets
```sql
SELECT title
FROM course
WHERE course.id LIKE `___%`
```

### Order By

```sql
SELECT name, dept_name, total_cred
FROM student
ORDER BY dept_name ASC, total_cred DESC;
```

First sort by dept_name and within those results sort by total_cred

### Intersect and IN operator

```sql
SELECT name
FROM instructor
WHERE dept_name IN ('ComSci', 'Maths')
INTERSECT
SELECT name
FROM instructor
WHERE salary < 50000
```

- You can use AND clause to make this neater
- Selects all instructors from comp-sci and maths who have salary < 50K

### Aggregate Functions

```sql
SELECT building, AVG(capacity)
FROM classroom
GROUP BY building
HAVING AVG(capacity) > 25
```

1. MAX
2. AVG
3. MIN
4. COUNT
5. SUM


## [Intermediate SQL /1 (33:05)](https://www.youtube.com/watch?v=Pk1j1UE3JLI&list=PLZ2ps__7DhBYc4jkUk_yQAjYEVFzVzhdU&index=11)

### Nested sub queries

1. Every output of a query is an relation
2. Every input of a query is one or more relations
3. An attribute in a query can be replaced with a query that generates a single value 

```sql
SELECT a1, a2, a3...
FROM r1, r2,...
WHERE P 
```

1. a1, a2... can be replaced by sub-query that generates single value
2. r1 can be replaced by any valid subquery
3. P can be replaced by B `<op>` sub-query
   1. op is like in, not in
   2. B is the attribute/field name
```sql
SELECT DISTINCT course_id
FROM section
WHERE semester='Fall' AND year=2009
    AND course_id IN (SELECT course_id FROM section where
                        semester='Spring' AND year=2010);
```

Nested subqueries in SQL involve placing one query inside another query. They are used to perform operations that depend on the results of another query. 

**Example 1: Basic Usage**

Find employees who earn more than the average salary in their department:
```sql
SELECT EmployeeID, Name
FROM Employees e
WHERE Salary > (SELECT AVG(Salary)
                FROM Employees
                WHERE Department = e.Department);
```
Here, the inner subquery calculates the average salary for each department, and the outer query retrieves employees who earn more than that average.

**Example 2: Multiple Levels**

Find employees who work in the same department as employees with the highest salary:
```sql
SELECT Name
FROM Employees
WHERE Department = (SELECT Department
                    FROM Employees
                    WHERE Salary = (SELECT MAX(Salary)
                                    FROM Employees));
```
The innermost subquery finds the highest salary, the middle subquery finds the department with that highest salary, and the outer query retrieves employees in that department.

### Some Operator

```sql
SELECT name
FROM instructor
WHERE salary > SOME (SELECT salary FROM instructor
                        WHERE dept_name = 'biology');
```

The `SOME` operator is used in a subquery to compare a value to any value returned by the subquery. It is functionally equivalent to `ANY`. The `SOME` operator allows you to check if a condition is true for at least one of the values returned by the subquery.

For example:
```sql
SELECT * 
FROM Employees 
WHERE Salary > SOME (SELECT Salary 
                      FROM Employees 
                      WHERE Department = 'Sales');
```
This query selects employees whose salary is greater than at least one salary from the Sales department.

### ALL Operator

ALL operators will match ALL results of a subquery

### EXIST

1. exists means atleast one match exists
2. not exists

### UNIQUE

Sir talks about unique construct.
    1. returns TRUE is there are no dupes
    2. FALSE otherwise

```sql
SELECT T.course_id
FROM course as T
WHERE UNIQUE (SELECT R.course_id
                FROM section as R
                WHERE T.course_id = R.course_id
                AND R.year = 2009);
```

### WITH Clause

The `WITH` clause, also known as a Common Table Expression (CTE), allows you to define a temporary result set that can be referenced within a `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement. CTEs improve query readability and can simplify complex queries by breaking them into manageable parts.

**Syntax:**

```sql
WITH CTE_Name AS (
    -- CTE query
    SELECT column1, column2
    FROM table_name
    WHERE condition
)
-- Main query using the CTE
SELECT column1
FROM CTE_Name
WHERE another_condition;
```

**Example:**

Find employees with salaries above the average salary of their department:

```sql
WITH AvgSalary AS (
    SELECT Department, AVG(Salary) AS AverageSalary
    FROM Employees
    GROUP BY Department
)
SELECT e.EmployeeID, e.Name, e.Salary
FROM Employees e
JOIN AvgSalary a
ON e.Department = a.Department
WHERE e.Salary > a.AverageSalary;
```

In this example, the `WITH` clause defines a CTE named `AvgSalary` to calculate the average salary per department. The main query then joins the `Employees` table with this CTE to find employees earning more than the average salary in their respective departments.

1. WITH defines a temporary relation available only in the query


### Scalar Subquery

A scalar subquery is a subquery that returns a single value (one row and one column). It can be used in contexts where a single value is expected, such as in comparisons or assignments.

**Syntax:**

```sql
SELECT column1
FROM table_name
WHERE column2 = (SELECT scalar_value
                  FROM another_table
                  WHERE condition);
```

**Examples:**

1. **Find Employees Earning More Than the Highest Salary in a Department:**

   Suppose you want to find employees who earn more than the highest salary in a particular department. The scalar subquery retrieves the highest salary for that department.

   ```sql
   SELECT EmployeeID, Name
   FROM Employees
   WHERE Salary > (SELECT MAX(Salary)
                   FROM Employees
                   WHERE Department = 'Sales');
   ```

   Here, the scalar subquery `(SELECT MAX(Salary) FROM Employees WHERE Department = 'Sales')` returns a single value, the maximum salary in the 'Sales' department. This value is then used to filter employees with higher salaries.

2. **Find Products More Expensive Than the Average Price:**

   To find products that cost more than the average price across all products:

   ```sql
   SELECT ProductName
   FROM Products
   WHERE Price > (SELECT AVG(Price)
                  FROM Products);
   ```

   In this case, the scalar subquery `(SELECT AVG(Price) FROM Products)` returns the average price of all products. The main query uses this single value to filter products priced above this average.

Scalar subqueries are often used in `WHERE` clauses, but they can also appear in `SELECT` clauses, `HAVING` clauses, and `SET` clauses where a single value is needed.

Gives a runtime error if subquery returns more than 1 result


### Modification of Databases

##### DELETE

```SQL
DELETE FROM instructors

DELETE FROM instructors
    WHERE dept_name = 'Finance'

DELETE FROM instructors
    WHERE dept_name IN (SELECT dept_name FROM department
                            WHERE building_name = 'Watson`)
```

**Delete Changes the state of the Table**

    ```sql
    DELETE FROM instructors
        WHERE salary < (SELECT AVG(salary) FROM instructors)
    ```

    1. if delete happens, the average salary changes

##### INSERT

1. Always use named attributes/fields.. the order might change
2. Values in order of named attributes

**Copy from one table to another**
```sql
INSERT INTO table1
    SELECT * FROM table2
```

**Basic Syntax:**

1. **Insert Data into All Columns:**

   ```sql
   INSERT INTO table_name (column1, column2, column3)
   VALUES (value1, value2, value3);
   ```

2. **Insert Data into Specific Columns:**

   ```sql
   INSERT INTO table_name (column1, column2)
   VALUES (value1, value2);
   ```

**Examples:**

1. **Insert Data into All Columns:**

   Suppose you have a `Users` table with columns `UserID`, `UserName`, and `Email`.

   ```sql
   INSERT INTO Users (UserID, UserName, Email)
   VALUES (1, 'Alice', 'alice@example.com');
   ```

   This query inserts a new row into the `Users` table with `UserID` 1, `UserName` 'Alice', and `Email` 'alice@example.com'.

2. **Insert Data into Specific Columns:**

   If you only want to insert values into `UserName` and `Email`, assuming `UserID` is an auto-incrementing primary key:

   ```sql
   INSERT INTO Users (UserName, Email)
   VALUES ('Bob', 'bob@example.com');
   ```

   This query inserts a new row with `UserName` 'Bob' and `Email` 'bob@example.com', letting the database automatically assign a `UserID`.

3. **Insert Multiple Rows:**

   You can also insert multiple rows in a single query:

   ```sql
   INSERT INTO Users (UserName, Email)
   VALUES ('Charlie', 'charlie@example.com'),
          ('Diana', 'diana@example.com');
   ```

   This query inserts two new rows into the `Users` table.

4. **Insert Data from Another Table:**

   You can insert data into a table based on a `SELECT` statement from another table:

   ```sql
   INSERT INTO ArchiveUsers (UserID, UserName, Email)
   SELECT UserID, UserName, Email
   FROM Users
   WHERE RegistrationDate < '2023-01-01';
   ```

   This query copies rows from the `Users` table into the `ArchiveUsers` table where the `RegistrationDate` is before January 1, 2023.

#### UPDATE

**Conditional Updates with case**

```sql
UPDATE instructor
    SET salary = CASE
        WHEN salary <= 1000
        THEN salary * 1.05
        ELSE salary * 1.03
        END
```
**Basic Syntax:**

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- **`table_name`**: The name of the table you want to update.
- **`SET`**: Specifies the columns to be updated and their new values.
- **`WHERE`**: Defines which rows should be updated. If omitted, all rows in the table will be updated.

**Examples:**

1. **Update a Single Record:**

   Suppose you have a `Users` table and you want to update the email address of a user with a specific `UserID`.

   ```sql
   UPDATE Users
   SET Email = 'newemail@example.com'
   WHERE UserID = 1;
   ```

   This query changes the `Email` of the user with `UserID` 1 to 'newemail@example.com'.

2. **Update Multiple Columns:**

   To update multiple columns for a specific user:

   ```sql
   UPDATE Users
   SET UserName = 'Alice Smith', Email = 'alice.smith@example.com'
   WHERE UserID = 1;
   ```

   This updates both the `UserName` and `Email` of the user with `UserID` 1.

3. **Update Multiple Records:**

   To increase the salary for all employees in a particular department:

   ```sql
   UPDATE Employees
   SET Salary = Salary * 1.10
   WHERE Department = 'Sales';
   ```

   This query gives a 10% raise to all employees in the 'Sales' department.

4. **Update Using a Subquery:**

   Suppose you want to update a table based on values from another table. For instance, update the `Salary` in the `Employees` table to match the average salary from a `Salaries` table:

   ```sql
   UPDATE Employees
   SET Salary = (SELECT AVG(Salary)
                 FROM Salaries
                 WHERE Department = Employees.Department)
   WHERE Department IN (SELECT Department
                        FROM Salaries);
   ```

   This query updates each employee's salary to the average salary for their department.

5. **Update All Records (Use with Caution):**

   To set a default value for a column in all records:

   ```sql
   UPDATE Users
   SET Status = 'Active';
   ```

   This query sets the `Status` column to 'Active' for all rows in the `Users` table.

**Important Notes:**

- Always use the `WHERE` clause to specify which rows to update. Without it, the update will apply to all rows in the table.
- Be cautious when performing updates, especially when updating multiple rows, to avoid unintended data changes.


### SQL CASE STATEMENT
The `CASE` statement in SQL provides a way to perform conditional logic within a query. It allows you to return different values based on specified conditions, similar to if-else logic in programming.

**Basic Syntax:**

```sql
CASE 
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ...
    ELSE default_result
END
```

- **`WHEN condition`**: Defines a condition to be evaluated.
- **`THEN result`**: Specifies the result to return if the corresponding `WHEN` condition is true.
- **`ELSE default_result`** (optional): Provides a default result if none of the `WHEN` conditions are met.
- **`END`**: Marks the end of the `CASE` statement.

**Examples:**

1. **Simple Case Expression:**

   Categorize employees based on their salary:

   ```sql
   SELECT EmployeeID, Salary,
          CASE
              WHEN Salary < 30000 THEN 'Low'
              WHEN Salary BETWEEN 30000 AND 60000 THEN 'Medium'
              ELSE 'High'
          END AS SalaryCategory
   FROM Employees;
   ```

   This query classifies salaries into 'Low', 'Medium', or 'High' categories and includes this classification as a new column `SalaryCategory` in the result set.

2. **Case in a `SELECT` Statement:**

   Display different messages based on order status:

   ```sql
   SELECT OrderID, Status,
          CASE Status
              WHEN 'P' THEN 'Pending'
              WHEN 'S' THEN 'Shipped'
              WHEN 'D' THEN 'Delivered'
              ELSE 'Unknown'
          END AS StatusDescription
   FROM Orders;
   ```

   This query translates order status codes into descriptive text.

3. **Case in an `ORDER BY` Clause:**

   Sort employees by a custom ranking based on job title:

   ```sql
   SELECT EmployeeID, JobTitle
   FROM Employees
   ORDER BY CASE JobTitle
                WHEN 'Manager' THEN 1
                WHEN 'Team Lead' THEN 2
                WHEN 'Staff' THEN 3
                ELSE 4
            END;
   ```

   This query sorts employees by job title, giving priority to 'Manager', then 'Team Lead', and so on.

4. **Case in a `WHERE` Clause:**

   Apply different filters based on a condition:

   ```sql
   SELECT ProductName, Price
   FROM Products
   WHERE CASE
             WHEN Category = 'Electronics' THEN Price > 100
             WHEN Category = 'Books' THEN Price < 50
             ELSE Price > 20
         END;
   ```

   This query applies different price filters based on the product category.

**Important Notes:**

- **`CASE` in SQL** can be used in `SELECT`, `ORDER BY`, `WHERE`, and `HAVING` clauses.
- **`CASE` is evaluated in order**: Once a condition is true, subsequent `WHEN` clauses are not evaluated.
- **`ELSE` clause is optional**: If omitted, `CASE` returns `NULL` when no conditions are met.

### Update with Scalar sub-queries

The `UPDATE` statement with a scalar subquery allows you to modify records in a table based on a single value returned by a subquery. A scalar subquery is a subquery that returns exactly one row and one column.

**Basic Syntax:**

```sql
UPDATE table_name
SET column_name = (SELECT scalar_value
                   FROM another_table
                   WHERE condition)
WHERE condition;
```

In this syntax:
- **`table_name`**: The table you want to update.
- **`column_name`**: The column to be updated.
- **`scalar_value`**: The value returned by the subquery.
- **`another_table`**: The table from which the subquery retrieves the scalar value.
- **`condition`**: The condition for filtering records to be updated.

**Examples:**

1. **Update Based on a Single Value from Another Table:**

   Suppose you have an `Employees` table and a `Departments` table. You want to update the `Salary` of employees to match the average salary of their department from the `Departments` table.

   ```sql
   UPDATE Employees
   SET Salary = (SELECT AVG(Salary)
                 FROM Employees e2
                 WHERE e2.Department = Employees.Department)
   WHERE Department IN (SELECT DISTINCT Department
                        FROM Employees);
   ```

   **Explanation:**
   - The scalar subquery `(SELECT AVG(Salary) FROM Employees e2 WHERE e2.Department = Employees.Department)` calculates the average salary for the department of each employee.
   - The `UPDATE` statement then sets each employee's salary to this average value where the department matches.

2. **Update with a Scalar Subquery in the Same Table:**

   Suppose you have a `Products` table with columns `ProductID`, `Price`, and `Category`. You want to set the `Price` of each product to the average price of products within its own category.

   ```sql
   UPDATE Products
   SET Price = (SELECT AVG(Price)
                FROM Products p2
                WHERE p2.Category = Products.Category)
   WHERE Category IN (SELECT DISTINCT Category
                      FROM Products);
   ```

   **Explanation:**
   - The scalar subquery `(SELECT AVG(Price) FROM Products p2 WHERE p2.Category = Products.Category)` computes the average price for each product's category.
   - The `UPDATE` query uses this average to set the `Price` for each product.

3. **Update Based on a Constant Value from a Subquery:**

   Suppose you want to update a `Discount` column in the `Orders` table with the highest discount value available from a `Discounts` table.

   ```sql
   UPDATE Orders
   SET Discount = (SELECT MAX(DiscountValue)
                   FROM Discounts)
   WHERE OrderDate < '2024-01-01';
   ```

   **Explanation:**
   - The scalar subquery `(SELECT MAX(DiscountValue) FROM Discounts)` retrieves the highest discount value.
   - The `UPDATE` statement applies this discount value to orders placed before January 1, 2024.

**Important Points:**
- The scalar subquery must return exactly one value; otherwise, the `UPDATE` statement will fail with an error.
- If the subquery returns more than one value or no value, you'll need to adjust the query to handle such cases, possibly by using aggregate functions or additional conditions.