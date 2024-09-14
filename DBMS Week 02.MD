# Week 2 Notes - DBMS

*Prof. Partha Pratham Das, IIT KGP*

*Notes by Adarsh (23f2003570)*  

## Module 1 (Duration 00:31:44)

### Attribute type
    1. Attributes are fields or columns of a table
    2. set of values allowed for each attribute is called Domain of the attribute
    3. Attribute values are supposed to be *atomic* that is non divisible.
    4. Attributes can be defined as nullable. - I guess for non value types
### Relation Schema and Instance
   
   Schema can be expressed mathematically as a relation.

   $A_1$, $A_2$ ,..., $A_n$ are attributes
   1. these attributes can be line name, employee-id, date_of_birth etc

   $R=(A_1, A_2, A_3,....,A_n)$ is a *relationship schema*.
   Example instructor = (ID, name, dept_name, salary)  
   instructor = $(String(5) \times String \times String \times Number)$

   $D_1$, $D_2$ ,..., $D_n$ are domains of attibutes $A_1$, $A_2$ ,..., $A_n$

   Then $R \subset D_1 \times D_2 \times D_3 \times ..... \times D_n$

   A relation is a set of n-tuples $(a_1, a_2, ..., a_n)$ where $a_i \in  D_i$

Current values (relation instance) of a relation are specified by a table

### Order of relations
1. Order of tuples/rows are not important
2. No 2 tuples or rows may be identical. They have to be distinct
3. Relation is a set and a set has no order

### Keys

Keys cannot be nullable !!!

**Super Key** is any combination of columns that ensures uniqueness for rows in the table.

**Surrogate Key** is an artificial or synthetic key used to uniquely identify rows in a table. It is created specifically for the purpose of serving as a unique identifier, rather than being derived from the data itself. Also called **Synthetic Key**

**Surrogate Key vs. Natural Key:**

1. **Natural Key:** A key that is derived from the data itself, such as a Social Security Number or email address, which inherently has meaning and is used to uniquely identify records.
2. **Surrogate Key:** A key created for the sole purpose of uniquely identifying records, with no inherent meaning or relationship to the actual data.

Good examples of surrogate key are like **JobID**, **Serial Number**. These have nothing to do with the line of business.

**Candidate Key** is a set of one or more columns (attributes) in a table that can uniquely identify each row in that table. 

**Conditions for Candidate Keys**

1. Uniqueness: The values of the candidate key must be unique for each row in the table. No two rows can have the same value for the candidate key.
2. Minimality: The candidate key must be minimal, meaning that if any column is removed from the key, it will no longer be able to uniquely identify each row. In other words, a candidate key is the smallest possible combination of columns that can uniquely identify a row.

A table can have multiple candidate keys, and each one is a potential choice for the primary key of the table. 


#### Foreign Keys

Foreign key is a column or a set of columns in one table that creates a link between data in two or more tables. It establishes a relationship between the current table (the child table) and another table (the parent table) by referencing the primary key of the parent table.

- Reference to Primary Key: The foreign key in the child table refers to the primary key of the parent table. This means that the values in the foreign key column(s) must match values in the primary key column(s) of the parent table or be null.
- Data Integrity: Foreign keys are used to enforce referential integrity, ensuring that the relationship between tables remains consistent. For example, if a row in the child table has a foreign key value, that value must correspond to an existing primary key value in the parent table, if the foreign key is not null.
- Relationship Types: Foreign keys help define the type of relationship between tables:
One-to-One: Each row in the child table relates to one and only one row in the parent table.
One-to-Many: Each row in the parent table can relate to multiple rows in the child table.
Many-to-Many: Typically, this is implemented using a junction table (or associative table) with two foreign keys, each pointing to the primary keys of the related tables.
- Cascading Actions: Foreign keys can also specify cascading actions for updates and deletions. For instance, if a row in the parent table is deleted or updated, the foreign key constraints can automatically handle these changes in the child table based on defined rules (e.g., CASCADE, SET NULL, RESTRICT, or NO ACTION).


### Relational Programming Languages

#### Procedural vs Relational Programming

Procedural programming is based on the concept of procedure calls. Procedures, also known as functions or routines, are a sequence of instructions that operate on data. The main idea is to structure the program as a set of procedures that manipulate data.


Relational programming is based on the principles of relational databases and logic. It involves working with data in the form of relations (tables) and using logical queries to manipulate and retrieve data.


## Procedural vs Declarative

Prof. Das says finding a square root using code is procedural

but finding a x such that $X^2 = Y$ is declarative

WIP Let's explore this later, This is the end of Module 6/Module 1/week 2