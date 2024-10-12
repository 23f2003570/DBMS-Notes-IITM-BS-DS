# Week 4 Notes - DBMS

*Prof. Partha Pratham Das, IIT KGP*

*Notes by Adarsh (23f2003570)*  

## [L4.1: Module 16 Formal Relational Query Languages/1 (28:05)](https://youtu.be/VfQcP-2VdLc)

### Formal Relational Query Language

Relational Algebra, Tuple Relational Calculus, and Domain Relational Calculus are forms that provides a theoretical framework for querying relational databases.

#### 1. Relational Algebra

Relational Algebra is a procedural query language that uses a set of operations to manipulate and retrieve data from relational databases. The key operations include:

- **Selection (σ)**: Filters rows based on a condition.
- **Projection (π)**: Selects specific columns from a table.
- **Union (∪)**: Combines results from two tables with the same attributes.
- **Difference (−)**: Retrieves rows from one table that are not in another.
- **Cartesian Product (×)**: Combines every row of one table with every row of another.
- **Join (⨝)**: Combines rows from two tables based on a related column.

##### Example

Given two tables, `employees` and `departments`:

**employees**:
| id | name   | dept_id | salary |
|----|--------|---------|--------|
| 1  | Alice  | 1       | 50000  |
| 2  | Bob    | 2       | 60000  |
| 3  | Charlie| 1       | 55000  |

**departments**:
| dept_id | dept_name  |
|---------|------------|
| 1       | HR         |
| 2       | Engineering |

**Query**: Get names of employees in the HR department.

**Relational Algebra**:

1. Selection: \( \sigma_{dept\_id=1}(employees) \)
2. Projection: \( \pi_{name}(\sigma_{dept\_id=1}(employees)) \)

#### 2. Tuple Relational Calculus

Tuple Relational Calculus is a non-procedural query language that allows you to specify what you want to retrieve without describing how to get it. It uses variables that represent tuples.

##### Example

To retrieve names of employees with a salary greater than 55000:

**Query**: Get names of employees with salary > 55000.

**Tuple Relational Calculus**:

```
{ e.name | e ∈ employees AND e.salary > 55000 }
```

#### 3. Domain Relational Calculus

Domain Relational Calculus is similar to Tuple Relational Calculus, but it uses variables that represent the values of attributes rather than entire tuples. 

##### Example

To retrieve names of employees with a salary greater than 55000:

**Query**: Get names of employees with salary > 55000.

**Domain Relational Calculus**:

```
{ n | ∃d, s (employees(d, n, d, s) AND s > 55000) }
```

Here, `d` represents `dept_id`, `n` represents `name`, and `s` represents `salary`.

- **Relational Algebra**: A procedural way to specify queries using operations.
- **Tuple Relational Calculus**: A non-procedural way that uses tuple variables. This uses predicate calculus
- **Domain Relational Calculus**: Similar to tuple calculus but focuses on attribute values. It is both non-procedural and uses predicate calculus

### Relational Algebra

![Relational Algebra](./imgs/15-relational_algebra.png)

These operators take 1 or 2 relations as input and produces a new relation as a result

|Symbol|Name|
|-|-|
|$\lor$|OR disjunction|
|$\land$|AND conjunction|
|$\displaystyle \large \neg$|NOT, Negation|
|$=, \not =, >, <, \leq, \geq$|Operators|
|$\sigma$|SELECT|
|$\Pi$|PROJECT|
|$\cup$|UNION|
|$\cap$|INTERSECTION|
|$-$|DIFFERENCE|

### Relational Algebra Notation

#### SELECT
$\sigma_{dept\_name =Physics}(instructor)$
  - `SELECT * FROM instructor WHERE dept_name='Physics'`

#### SELECT WITH WHERE
$\sigma_{A=B} \land {D > 5}(r)$
  - `SELECT * FROM r WHERE A = B AND D > 5`
#### PROJECT
$\prod_{a,b,c,d}(relation)$
  - `SELECT a,b,c,d FROM relation`

#### Operations

$\prod_{course\_id}(\sigma_{semester='fall' \land year = 2009}(section)) {[\cup/-/\cap]} \prod_{course\_id}(\sigma_{semester='spring' \land year = 2010}(section))$

```sql
SELECT course_id FROM section
WHERE semester='fall' AND year=2009
UNION
SELECT course_id FROM section
WHERE semester='spring' AND year=2010
```

#### NOTE ABOUT SET OPERATIONS
For $R \cup S$to be possible
1. r, s should have same `Arity` aka same number of attributes/fields in the table


$R \cap S$is the same as $r - (r - s)$

![Set Operarions](./imgs/16-set-ops.png)

### Division Operator

In relational databases, the division operation is a specific operation used to find tuples in one relation that are associated with all tuples in another relation. This operation is particularly useful when dealing with queries that involve "all" conditions.

#### Division of Two Relations

In relational databases, the division operation finds tuples in one relation that are associated with all tuples in another relation.

#### Mathematical Definition

Given two relations:

- $R(A, B)$: Relation $R$has attributes $A$and $B$.
- $S(B)$: Relation $S$has attribute $B$.

The result of the division operation $R \div S$will yield a new relation containing all values of $A$from $R$such that for every tuple in $S$, there exists a corresponding tuple in $R$with that $A$and the matching $B$values.

#### Mathematical Representation

The result of the division $R \div S$can be expressed as:

$$
R \div S = \{ t \in \pi_A(R) \mid \forall s \in S, \exists r \in R (r.A = t.A \land r.B = s.B) \}
$$

Where:
- $\pi_A(R)$is the projection of relation $R$on attribute $A$.
- $t$is a tuple from the resulting relation.
- $s$is a tuple from relation $S$.
- $r$is a tuple from relation $R$.

#### Example

##### Given Relations

**Relation $R$**:

| A    | B    |
|------|------|
| 1    | x    |
| 1    | y    |
| 2    | x    |
| 2    | y    |
| 3    | x    |

**Relation $S$**:

| B    |
|------|
| x    |
| y    |

##### Performing the Division $R \div S$

1. **Identify tuples in $R$** for each tuple in $S$:
   - For $S.B = x$: Look for $A$such that $R.A = t.A$and $R.B = x$.
   - For $S.B = y$: Look for $A$such that $R.A = t.A$and $R.B = y$.

2. **Check each $A$**:
   - For $A = 1$: Exists in $R$for both $B = x$and $B = y$.
   - For $A = 2$: Exists in $R$for both $B = x$and $B = y$.
   - For $A = 3$: Exists in $R$only for $B = x$, not for $B = y$.

The result of the division $R \div S$will be:

| A    |
|------|
| 1    |
| 2    |

#### SQL Implementation in PostgreSQL

While SQL does not have a built-in division operator, you can simulate division using a combination of `GROUP BY` and `HAVING` clauses. Here’s how you can implement the division of two relations in PostgreSQL:

##### SQL Example

```sql
WITH R AS (
    SELECT 1 AS A, 'x' AS B UNION ALL
    SELECT 1, 'y' UNION ALL
    SELECT 2, 'x' UNION ALL
    SELECT 2, 'y' UNION ALL
    SELECT 3, 'x'
),
S AS (
    SELECT 'x' AS B UNION ALL
    SELECT 'y'
)

SELECT A
FROM R
GROUP BY A
HAVING COUNT(DISTINCT B) = (SELECT COUNT(*) FROM S);
```

#### Explanation of SQL Query

- The `WITH` clause defines two temporary relations, $R$and $S$.
- The main query groups results by $A$and counts distinct $B$values.
- The `HAVING` clause checks that the count of distinct $B$values for each $A$matches the total count of tuples in $S$.


### One more Relation Division Example

We have two relations:

1. **Students enrolled in courses** (Relation $R$): This relation contains students and the courses they are enrolled in.
2. **Required courses** (Relation $S$): This relation contains the courses that a specific program requires.

#### Given Relations

##### Relation $R(StudentID, CourseID)$

| StudentID | CourseID |
|-----------|----------|
| 101       | CS101    |
| 101       | CS102    |
| 101       | CS103    |
| 102       | CS101    |
| 102       | CS103    |
| 103       | CS102    |
| 103       | CS103    |
| 104       | CS101    |

##### Relation $S(CourseID)$

| CourseID |
|----------|
| CS101    |
| CS102    |

#### Performing the Division $R \div S$

We want to find students who are enrolled in **all** required courses.

1. **Identify tuples in $R$** for each tuple in $S$:
   - For $S.CourseID = CS101$: Look for students who are enrolled in $CS101$.
   - For $S.CourseID = CS102$: Look for students who are enrolled in $CS102$.

2. **Check each StudentID**:
   - For **Student 101**: Enrolled in $CS101$and $CS102$(matches all).
   - For **Student 102**: Enrolled in $CS101$but not in $CS102$(does not match).
   - For **Student 103**: Enrolled in $CS102$but not in $CS101$(does not match).
   - For **Student 104**: Enrolled in $CS101$but not in $CS102$(does not match).

#### Result of the Division $R \div S$

Based on the checks above, the resulting relation will be:

| StudentID |
|-----------|
| 101       |


The division $R \div S$shows that **only Student 101** is enrolled in all the required courses (both $CS101$and $CS102$).

### Another Relation Division problem

We have two relations:

1. **Employees assigned to projects** (Relation $R$): This relation contains employees and the projects they are working on.
2. **Required projects** (Relation $S$): This relation lists the projects that need to be completed for a certain initiative.

#### Given Relations

##### Relation $R(EmployeeID, ProjectID)$

| EmployeeID | ProjectID |
|------------|-----------|
| 201        | P1        |
| 201        | P2        |
| 202        | P1        |
| 202        | P3        |
| 203        | P2        |
| 204        | P1        |
| 204        | P2        |
| 204        | P3        |

##### Relation $S(ProjectID)$

| ProjectID |
|-----------|
| P1        |
| P2        |

#### Performing the Division $R \div S$

We want to find employees who are assigned to **all** required projects.

1. **Identify tuples in $R$** for each tuple in $S$:
   - For $S.ProjectID = P1$: Look for employees who are assigned to $P1$.
   - For $S.ProjectID = P2$: Look for employees who are assigned to $P2$.

2. **Check each EmployeeID**:
   - For **Employee 201**: Assigned to $P1$and $P2$(matches all).
   - For **Employee 202**: Assigned to $P1$but not to $P2$(does not match).
   - For **Employee 203**: Assigned to $P2$but not to $P1$(does not match).
   - For **Employee 204**: Assigned to $P1$, $P2$, and $P3$(matches all).

### Result of the Division $R \div S$

Based on the checks above, the resulting relation will be:

| EmployeeID |
|------------|
| 201        |
| 204        |

The division $R \div S$or $R | S$shows that **Employees 201 and 204** are assigned to all the required projects ($P1$and $P2$).

In this figure $R - S$is the **lecturer** field. $S$is the Module-Subject link.

![Relation Division](imgs/17-relation-division.png)

Relation Division Means **$R|S$or $R \div S$is associated with all instances of $S$**

One more Relation Division Example

![Relation Division](imgs/18-rel-div.png)

One more Relation Division example with 2 or more columns

![Relation Division](imgs/19-rel-div.png)

### Mathematical Expression of Relation Division
![Rel Div Formula](imgs/20-rel-div-formula.png)


### Theta Join

$\Join_{\theta} (r, s) = \sigma_{\theta}(r \times s)$

A **theta join** is a type of join operation in relational databases that combines rows from two or more tables based on a specified condition. Unlike natural joins or inner joins that use equality conditions, theta joins can use any condition, including inequalities, greater than, less than, etc.

#### Syntax

In SQL, a theta join can be implemented using the `JOIN` clause along with an `ON` clause that specifies the condition for the join.

#### Example Scenario

Let's consider two tables: **Employees** and **Departments**.

##### Table Structures

1. **Employees**

| EmployeeID | Name   | Salary | DeptID |
|------------|--------|--------|--------|
| 1          | Alice  | 60000  | 1      |
| 2          | Bob    | 70000  | 2      |
| 3          | Charlie| 80000  | 1      |
| 4          | David  | 90000  | 3      |

2. **Departments**

| DeptID | DeptName       | MinSalary |
|--------|----------------|-----------|
| 1      | HR             | 50000     |
| 2      | Engineering    | 60000     |
| 3      | Sales          | 75000     |

#### Example of a Theta Join

Let’s say we want to find employees whose salary is greater than the minimum salary for their respective department. We can perform a theta join on the **Employees** and **Departments** tables using the condition that compares the employee's salary to the department's minimum salary.

##### SQL Query

```sql
SELECT 
    e.EmployeeID,
    e.Name,
    e.Salary,
    d.DeptName
FROM 
    Employees e
JOIN 
    Departments d ON e.DeptID = d.DeptID AND e.Salary > d.MinSalary;
```

#### Explanation of the Query

- **FROM Employees e**: Selects from the `Employees` table and gives it an alias `e`.
- **JOIN Departments d**: Joins with the `Departments` table, giving it the alias `d`.
- **ON e.DeptID = d.DeptID**: Specifies the first condition for the join, matching employees with their respective departments.
- **AND e.Salary > d.MinSalary**: Specifies the second condition for the join, ensuring that we only include employees whose salary is greater than the minimum salary for their department.

#### Result of the Query

Based on the data in the tables, the result will be:

| EmployeeID | Name   | Salary | DeptName    |
|------------|--------|--------|-------------|
| 2          | Bob    | 70000  | Engineering  |
| 3          | Charlie| 80000  | HR          |
| 4          | David  | 90000  | Sales       |

The theta join allows us to combine information from the `Employees` and `Departments` tables based on the condition of employee salaries being greater than their department's minimum salary. Theta joins are flexible and can accommodate various conditions, making them powerful tools in SQL queries.

When $\theta$does the following
1. Enforces equality b/w R & S then its a equality join
2. If it enforces column binding between R & S then its a natural join


## [L4.2: Formal Relational Query Languages/2 (30:40)](https://youtu.be/WjlbMfEqom8)

### Predicate Calculus or Predicate Logic
Predicate calculus, also known as first-order logic, is a formal system used in relational databases for expressing queries and constraints. Here are key points regarding its application in relational databases:

1. **Foundational Logic**: Predicate calculus extends propositional logic by incorporating quantifiers and predicates, allowing for more expressive statements about database entities.

2. **Predicates**: Predicates represent properties or relations among objects. For example, in a database of students, a predicate could be "is enrolled in" relating students to courses. This is also called Predicate Logic and is an extension of Propositional Logic or Boolean Algebra

3. **Quantifiers**: Two main types:
   - **Universal Quantifier (∀)**: Indicates that a statement holds for all elements in a domain. E.g., "For every student, there exists a course they are enrolled in."
   - **Existential Quantifier (∃)**: Indicates that there is at least one element for which the statement is true. E.g., "There exists a student who is enrolled in a mathematics course."

4. **Logical Connectives**: Similar to propositional logic, predicate calculus uses logical connectives like AND (∧), OR (∨), NOT (¬), and IMPLIES (→) to build complex expressions.

5. **Domain of Discourse**: The set of objects under consideration (e.g., all students, all courses) is referred to as the domain of discourse. Predicates and quantifiers operate over this domain.

6. **Formal Semantics**: Predicate calculus provides a formal framework for interpreting database queries. Each predicate can be associated with a relational table, and the truth of a statement can be evaluated based on the data in those tables.

7. **Query Language**: SQL can be viewed as a practical application of predicate calculus. Queries can be expressed using SELECT, WHERE, and JOIN clauses that embody logical predicates and quantifiers.

8. **Constraints and Rules**: Database integrity constraints (e.g., uniqueness, referential integrity) can be expressed using predicate calculus, ensuring that certain conditions hold for the data.

9. **Expressiveness**: Predicate calculus enhances the ability to express complex queries, enabling operations like filtering, aggregation, and subqueries based on logical conditions.

10. **Evaluation**: The evaluation of predicates in queries can lead to optimization techniques, helping databases retrieve data efficiently by minimizing unnecessary computation.

### Boolean Algebra

1. **Basic Operations**: 
   - **AND ( ∧ )**: Returns true if both operands are true.
     - **Example**: $A \land B$ is true if both $A$ and $B$ are true.
     - **Truth Table**:
       | A | B | $A \land B$|
       |---|---|-------|
       | 0 | 0 |   0   |
       | 0 | 1 |   0   |
       | 1 | 0 |   0   |
       | 1 | 1 |   1   |

   - **OR ( ∨ )**: Returns true if at least one operand is true.
     - **Example**: $A \lor B$ is true if either $A$ or $B$ is true.
     - **Truth Table**:
       | A | B | $A \lor B$|
       |---|---|-------|
       | 0 | 0 |   0   |
       | 0 | 1 |   1   |
       | 1 | 0 |   1   |
       | 1 | 1 |   1   |

   - **NOT ( ¬ )**: Inverts the value of the operand.
     - **Example**: $\neg A$ is true if $A$is false.
     - **Truth Table**:
       | A | $\neg A$|
       |---|----|
       | 0 |  1 |
       | 1 |  0 |

2. **Identity Laws**:
   - $A \land 1 = A$
   - $A \lor 0 = A$

3. **Domination Laws**:
   - $A \land 0 = 0$
   - $A \lor 1 = 1$

4. **Idempotent Laws**:
   - $A \land A = A$
   - $A \lor A = A$

5. **Complement Laws**:
   - $A \land \neg A = 0$
   - $A \lor \neg A = 1$

6. **Distributive Laws**:
   - $A \land (B \lor C) = (A \land B) \lor (A \land C)$
   - $A \lor (B \land C) = (A \lor B) \land (A \lor C)$

7. **Absorption Laws**:
   - $A \lor (A \land B) = A$
   - $A \land (A \lor B) = A$

8. **De Morgan's Theorems**:
   - $\neg(A \land B) = \neg A \lor \neg B$
   - $\neg(A \lor B) = \neg A \land \neg B$

9. **Applications**: Boolean algebra is widely used in:
   - **Digital Logic Design**: Designing circuits using gates like AND, OR, and NOT.
   - **Computer Algorithms**: Simplifying logic expressions in programming.
   - **Search Engines**: Formulating search queries based on logical expressions.

10. **Example Expression**:
    - Simplifying the expression $A \land (B \lor \neg A)$:
      - Using Distributive Law: $A \land B \lor A \land \neg A$
      - By Complement Law: $A \land B \lor 0$
      - Result: $A \land B$

### Predicates

A **predicate** is a statement that contains one or more variables and becomes a proposition when the variables are assigned specific values. It expresses a property or a relation among objects.

#### Mathematical Notation:
A predicate can be denoted as:
$P(x)$
where:
- \(P\) is the predicate symbol (often representing a property or relation).
- \(x\) is a variable that can take values from a specified domain.

#### Parts of a Predicate

1. **Predicate Symbol**:
   - Represents the property or relation.
   - Example: In the predicate $P(x)$, \(P\) might represent "is even".
   - Predicate is a function which tells the truth value of statement P(X) at X.
   - P(x1, x2, x3,....,xn) is called a n-th place predicate
     - or a n-ary predicate
   - P(X) is a predicate
   - P(5) is a proposition!
     - $P(X) \equiv X > 3$ is a Predicate
       - $P(5)$ is a proposition that returns TRUE
       - $P(2)$ is a proposition that returns FALSE

2. **Variables**:
   - The symbols that can take on values from a domain.
   - Example: In $P(x)$, \(x\) is a variable.

3. **Domain of Discourse**:
   - The set of all possible values that the variables can take.
   - Example: If the domain is the set of integers, \(x\) can be any integer.

4. **Terms**:
   - These are the specific values or expressions that can replace the variables in the predicate.
   - Example: If \(x=2\), then $P(2)$ might evaluate to true if \(P\) is "is even".

5. **Quantifiers**:
   - Quantifiers allow us to express the extent to which a predicate holds over a domain:
     - **Universal Quantifier** ($\forall$): Indicates that the predicate is true for all elements in the domain.
       - Notation: $\forall x\,P(x)$ means "for all \(x\), \(P(x)\) is true."
     - **Existential Quantifier** ($\exists$): Indicates that there exists at least one element in the domain for which the predicate is true.
       - Notation: $\exists x\,P(x)$ means "there exists an \(x\) such that \(P(x)\) is true."

#### Example

Let’s consider a specific example with a predicate:

1. **Predicate**: 
   $P(x): x \text{ is an even number}$

2. **Domain**: 
   The domain could be the set of integers: $\mathbb{Z}$.

3. **Quantified Statements**:
   - **Universal Statement**: 
     $\forall \ x \in \mathbb{Z}, P(x) \text{ is false for odd integers.}$
   - **Existential Statement**: 
     $\exists \ x \in \mathbb{Z}\,(P(x)) \text{ is true for } x=2.$

### Quantifiers in Predicate Logic

In predicate logic, quantifiers are used to express statements about the properties of objects in a domain. There are two primary types of quantifiers:

1. **Universal Quantifier** (denoted as $\forall$)
2. **Existential Quantifier** (denoted as $\exists$)

#### 1. Universal Quantifier ($\forall$)

The universal quantifier expresses that a property holds for all elements in a given domain. The notation is:

$$
\forall x \, P(x)
$$

This reads as "for all $x$, $P(x)$ is true," meaning that the statement $P(x)$ is true for every possible value of $x$.

##### Example

**Statement**: "All humans are mortal."

- **Predicate**: Let $P(x)$ represent "x is mortal."
- **Domain**: All humans.

The logical expression would be:

$$
\forall x \, (Human(x) \rightarrow P(x))
$$

This means: For every $x$, if $x$ is a human, then $x$ is mortal.

#### 2. Existential Quantifier ($\exists$)

The existential quantifier expresses that there exists at least one element in the domain for which the property holds. The notation is:

$$
\exists x \, P(x)
$$

This reads as "there exists an $x$ such that $P(x)$ is true," meaning at least one value of $x$ makes the statement $P(x)$ true.

##### Example

**Statement**: "Some humans are doctors."

- **Predicate**: Let $P(x)$ represent "x is a doctor."
- **Domain**: All humans.

The logical expression would be:

$$
\exists x \, (Human(x) \land P(x))
$$

This means: There exists an $x$ such that $x$ is a human and $x$ is a doctor.

#### Combining Quantifiers

Quantifiers can also be combined to express more complex statements. The order of quantifiers is significant and can change the meaning of the statement.

##### Example

**Statement**: "Every student has at least one book."

- **Predicate**: Let $P(x, y)$ represent "x has y."
- **Domain**: Students and books.

The logical expression would be:

$$
\forall x \, (Student(x) \rightarrow \exists y \, (Book(y) \land P(x, y)))
$$

This means: For every student $x$, there exists a book $y$ such that $x$ has $y$.

#### Problem
1. Find the first names of students whose age > 21
   1. $\{t.FName | Student(t) \land t.Age > 21\}$

### Tuple Relation Calculus (TRC)

Tuple Relational Calculus (TRC) is a non-procedural query language that allows users to specify the desired information without describing how to obtain it. In TRC, queries are expressed using tuples and the language is based on predicate logic.

#### Syntax

A TRC expression generally has the form:

$$
\{ t | P(t) \}
$$

Where:
- \( t \) is a tuple variable.
- \( P(t) \) is a predicate that describes the conditions that the tuples must satisfy.

#### Example Database Schema

Let's assume we have the following relations:

1. **Students**(StudentID, Name, Major)

| StudentID | Name    | Major     |
|-----------|---------|-----------|
| 1         | Alice   | CS        |
| 2         | Bob     | EE        |
| 3         | Charlie | CS        |
| 4         | David   | ME        |

2. **Courses**(CourseID, Title, Credits)

| CourseID | Title          | Credits |
|----------|----------------|---------|
| 101      | Database       | 3       |
| 102      | Operating Sys  | 4       |
| 103      | Algorithms     | 3       |

3. **Enrollments**(StudentID, CourseID)

| StudentID | CourseID |
|-----------|----------|
| 1         | 101      |
| 1         | 102      |
| 2         | 101      |
| 3         | 103      |
| 4         | 102      |

#### Examples of Tuple Relational Calculus Queries

##### 1. Retrieve the Names of All Students

To retrieve the names of all students, you can express the query as:

$$
\{ s.Name | \text{Students}(s) \}
$$

This means: "Select the Name of tuple \( s \) from the Students relation."

##### 2. Find Students Major in Computer Science

To find all students majoring in Computer Science (CS):

$$
\{ s | \text{Students}(s) \land s.Major = 'CS' \}
$$

This means: "Select tuple \( s \) from Students where the Major of \( s \) is 'CS'."

##### 3. Retrieve the Student IDs of Students Enrolled in a Specific Course

To find students enrolled in the course with CourseID = 101:

$$
\{ e.StudentID | \text{Enrollments}(e) \land e.CourseID = 101 \}
$$

This means: "Select the StudentID from the Enrollments relation where CourseID is 101."

##### 4. Find Students Enrolled in More Than One Course

To find students who are enrolled in more than one course, you can express it as:

$$
\{ e_1.StudentID | \text{Enrollments}(e_1) \land \exists e_2 (\text{Enrollments}(e_2) \land e_1.StudentID = e_2.StudentID \land e_1.CourseID \neq e_2.CourseID) \}
$$

This means: "Select StudentID \( e_1 \) from Enrollments where there exists another enrollment \( e_2 \) for the same student in a different course."

##### 5. Retrieve All Courses Taken by a Specific Student

To get all courses taken by the student with StudentID = 1:

$$
\{ c | \exists e (\text{Enrollments}(e) \land e.StudentID = 1 \land \text{Courses}(c) \land c.CourseID = e.CourseID) \}
$$

This means: "Select course \( c \) such that there exists an enrollment \( e \) for StudentID 1, and \( c \) matches the CourseID of that enrollment."

Tuple Relational Calculus provides a way to express queries based on the properties of tuples in a database.

#### TRC Example 1
![Tuple Relational Calculus](imgs/21-TRC-tuple-relational-calculus.png)

### TRC Example 2
![Tuple Relational Calculus](imgs/22-TRC-tuple-relational-calculus.png)

### TRC Example 3
![Tuple Relational Calculus](imgs/23-TRC-tuple-relational-calculus.png)

### Safety Of Expressions in TRC

In Tuple Relational Calculus (TRC), the **safety** of an expression is an important concept that ensures that the query will produce a finite result. A TRC expression is considered **safe** if it guarantees that the variables used in the query will be bounded by the domain of the relations, preventing the query from producing an infinite result.

#### Criteria for Safety

A TRC expression is safe if:
1. All free variables in the expression must be bounded by the range of some relation in the database.
2. The expression must not produce tuples that rely on infinite domains or arbitrary set constructions.

#### Examples of Safe and Unsafe Expressions

##### Example Database Schema

Let's use a simplified version of our previous database:

1. **Students**(StudentID, Name, Major)

| StudentID | Name    | Major     |
|-----------|---------|-----------|
| 1         | Alice   | CS        |
| 2         | Bob     | EE        |
| 3         | Charlie | CS        |

2. **Enrollments**(StudentID, CourseID)

| StudentID | CourseID |
|-----------|----------|
| 1         | 101      |
| 1         | 102      |
| 2         | 101      |
| 3         | 103      |

#### Safe Expressions

1. **Retrieve Student Names**

$$
\{ s.Name | \text{Students}(s) \}
$$

**Explanation**: This expression is safe because the variable \( s \) is bounded by the Students relation, ensuring a finite set of results.

2. **Find Students with Major in Computer Science**

$$
\{ s | \text{Students}(s) \land s.Major = 'CS' \}
$$

**Explanation**: This is safe as well, because \( s \) is again bounded by the Students relation.

3. **Find Enrolled Students for a Specific Course**

$$
\{ e.StudentID | \text{Enrollments}(e) \land e.CourseID = 101 \}
$$

**Explanation**: This expression is safe since \( e \) is bounded by the Enrollments relation.

#### Unsafe Expressions

1. **Retrieve All Possible Combinations of Students and Courses**

$$
\{ (s, c) | \text{Students}(s) \land \text{Courses}(c) \} \cup \{ (s, c) | s \text{ is any tuple} \} 
$$

**Explanation**: This expression is unsafe because it tries to create tuples from all possible combinations of students and courses, which can lead to infinite results due to the second part of the expression that includes "any tuple." This creates an unbounded variable.

2. **Using a Non-Bounded Variable**

$$
\{ s | s \text{ is a tuple} \} 
$$

**Explanation**: This expression is unsafe because it introduces a free variable \( s \) without any bounding condition, potentially leading to an infinite number of tuples.

![Safety of TRC Expressions](imgs/24-trc-safety.png)

### Equivalence of Algebra and Relational Calculus

The equivalence of Relational Algebra, Tuple Relational Calculus (TRC), and Domain Relational Calculus (DRC) lies in their ability to express the same queries and retrieve the same results from a relational database. Here’s an overview of each, followed by their equivalences expressed in mathematical notation.

1. **Relational Algebra (RA)**:
   - A procedural query language that provides a set of operations (like selection, projection, union, difference, and joins) to manipulate relations.

2. **Tuple Relational Calculus (TRC)**:
   - A non-procedural query language that describes queries in terms of tuple variables and predicates.

3. **Domain Relational Calculus (DRC)**:
   - Another non-procedural query language, but it uses domain variables instead of tuple variables, allowing queries to be expressed in terms of individual attributes.

#### Equivalence

To show equivalence, we express that a query expressed in one of these languages can be represented in the other two.

##### 1. Equivalence of Relational Algebra and Tuple Relational Calculus

If we have a relational algebra expression $R_1$, we can find a TRC expression $R_2$ that returns the same result:

- **RA Expression**:
  $$
  R_1 = \sigma_{\text{condition}}(R) \quad \text{(Selection)}
  $$
- **TRC Expression**:
  $$
  R_2 = \{ t | R(t) \land \text{condition}(t) \}
  $$

This means: The selection operation in RA can be represented in TRC by selecting tuples from $R$ that satisfy the condition.

##### 2. Equivalence of Relational Algebra and Domain Relational Calculus

Similarly, a relational algebra expression $R_1$ can also be represented by a DRC expression $R_3$:

- **RA Expression**:
  $$
  R_1 = \sigma_{\text{condition}}(R) \quad \text{(Selection)}
  $$
- **DRC Expression**:
  $$
  R_3 = \{ (d_1, d_2, \ldots, d_n) | \text{condition}(d_1, d_2, \ldots, d_n) \land R(d_1, d_2, \ldots, d_n) \}
  $$

Here, $d_1, d_2, \ldots, d_n$ are domain variables corresponding to the attributes of $R$.

##### 3. Equivalence Between Tuple and Domain Relational Calculus

For any TRC expression $R_2$, there exists a corresponding DRC expression $R_4$:

- **TRC Expression**:
  $$
  R_2 = \{ t | R(t) \land \text{condition}(t) \}
  $$
- **DRC Expression**:
  $$
  R_4 = \{ (d_1, d_2, \ldots, d_n) | R(d_1, d_2, \ldots, d_n) \land \text{condition}(d_1, d_2, \ldots, d_n) \}
  $$

#### Summary of Equivalence

We can denote the equivalence as follows:

1. **Relational Algebra $\leftrightarrow$ Tuple Relational Calculus**:
   $$
   \forall R_1 \, \exists R_2: \text{RA}(R_1) \equiv \text{TRC}(R_2)
   $$

2. **Relational Algebra $\leftrightarrow$ Domain Relational Calculus**:
   $$
   \forall R_1 \, \exists R_3: \text{RA}(R_1) \equiv \text{DRC}(R_3)
   $$

3. **Tuple Relational Calculus $\leftrightarrow$ Domain Relational Calculus**:
   $$
   \forall R_2 \, \exists R_4: \text{TRC}(R_2) \equiv \text{DRC}(R_4)
   $$

#### EQ Combining Operation
![Equivalence Combining](imgs/25-equivalence-combining.png)

#### EQ SELECT Operation
![Equivalence Select](imgs/26-equivalence-select.png)

#### EQ PROJECT Operation
![Equivalence Project](imgs/27-equivalence-project.png)

#### EQ UNION Operation
![Equivalence-Union](imgs/28-equivalence-union.png)


#### EQ SET DIFF Operation
![Equivalence-Set Difference](imgs/29-equivalence-setdiff.png.png)


#### EQ INTERSECTION Operation
![Equivalence-Intersection](imgs/30-equivalence-intersection.png)

#### EQ NATURAL JOIN

![Equivalence Natural Join](imgs/31-equivalence-natural-join.png)