# PostgreSQL Notes
## Links
1. [Postgres 10 Manual](https://www.postgresql.org/docs/10/index.html)  
2. [Docker Hub/Postgres](https://hub.docker.com/_/postgres/tags?page_size=&ordering=&name=10.18)
3. [Course version of PostgreSQL Docker Image](https://hub.docker.com/layers/library/postgres/10.18/images/sha256-e37849ff3307519e542e6ad13ae3aa2ab8131e448df126f0f86d2c38980c31da?context=explore)
4. [PostgreSQL 10 Environment Variables](https://www.postgresql.org/docs/10/libpq-envars.html)

## General Notes
1. Every PostgreSQL statement ends with a semicolon
2. Comments start with `--`
3. SQL does not care about casing...You case for code readability!
4. Convention
   1. UPPERCASE all SQL keywords - anything baked in Postgres
   2. lowercase-snakecase everything related to your relations and entities 
   3. Don't use pluralized names in tables. User - not Users, SQL Tables are not LINQ collections
   4. double quotes for reserved keywords in entities. Try this in the [Tasks](#tasks) below
   5. Single quotes for string values
### "Relational" Meaning
"relational" in relational databases is closely tied to relational algebra, which is a formal system used to manipulate and query data within the relational model. Here’s a brief overview:

1. **Foundational Concepts**: Relational algebra provides a set of operations (like selection, projection, union, intersection, and join) that can be performed on tables (relations). These operations form the basis for querying data.

2. **Operations**: Each operation in relational algebra transforms one or more relations into a new relation. For example:
   - **Selection**: Filters rows based on a condition.
   - **Projection**: Selects specific columns from a table.
   - **Join**: Combines rows from two or more tables based on a related column.

3. **Set Theory**: Relational algebra is rooted in set theory, which allows for operations on relations (tables) as if they were sets. This helps in understanding how to combine and manipulate data logically.

4. **Theoretical Foundation**: While SQL is the practical language used for interacting with relational databases, relational algebra provides the theoretical framework that underpins these operations, ensuring they are sound and efficient.

## Setting up postgres - Docker way

Select the version from [Docker Hub](https://hub.docker.com/_/postgres/tags?page_size=&ordering=&name=10.18)  

```sh
docker pull postgres:10.18

docker run -it postgres:10.18 bash
```

## Postgres Data Types
### Numeric Types
- **`integer`**: 4-byte integer, range: -2,147,483,648 to 2,147,483,647.
- **`bigint`**: 8-byte integer, range: -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807.
- **`smallint`**: 2-byte integer, range: -32,768 to 32,767.
- **`decimal(n, s)`**: Exact numeric with user-defined precision `n` and scale `s`.
- **`numeric(n, s)`**: Synonym for decimal, same precision and scale.
- **`real`**: 4-byte floating-point number.
- **`double precision`**: 8-byte floating-point number.
### Character Types
- **`character varying(n)`**: Variable-length string with maximum length `n`.
- **`character(n)`**: Fixed-length string, padded with spaces if shorter than `n`.
- **`text`**: Variable-length string with no specific maximum length.
### Boolean Type
- **`boolean`**: Stores true, false, or null values.
### Date/Time Types
- **`timestamp`**: Date and time without time zone.
- **`timestamp with time zone`**: Date and time with time zone info.
- **`date`**: Stores only the date.
- **`time`**: Time without time zone.
- **`time with time zone`**: Time with time zone info.
### Geometric Types
- **`point`**: Represents a point in 2D space.
- **`line`**: Represents an infinite line in 2D space.
- **`lseg`**: Represents a line segment in 2D space.
- **`box`**: Represents a rectangular box in 2D space.
- **`path`**: Represents a geometric path.
- **`polygon`**: Represents a polygon in 2D space.
- **`circle`**: Represents a circle.
### Network Address Types
- **`cidr`**: Stores IPv4 or IPv6 network addresses.
- **`inet`**: Stores individual IPv4 or IPv6 addresses.
- **`macaddr`**: Stores MAC addresses.
### JSON Types
- **`json`**: Stores JSON data as text.
- **`jsonb`**: Binary format for JSON data, optimized for querying.
### Array Types
- **`type[]`**: Array of any data type, allowing multiple values in one column.
### UUID Type
- **`uuid`**: 128-bit Universally Unique Identifier.
### XML Type
- **`xml`**: Stores XML data for hierarchical data storage.
### Composite Types
- **`composite`**: User-defined type consisting of multiple fields, representing a row.
### Range Types
- **`int4range`**: Range of integers.
- **`numrange`**: Range of numeric values.
- **`tsrange`**: Range of timestamps.
- **`daterange`**: Range of dates.
### Hstore Type
- **`hstore`**: Key-value pairs for semi-structured data.
### SERIAL Type
1. Pseudo Data Type
1. **Auto-Incrementing** integer, as good as primary key, concurrent
      - **`SERIAL`**: Equivalent to `integer`. It creates a sequence generator that increments the integer value for each new row.
      - **`BIGSERIAL`**: Equivalent to `bigint`. It allows for a much larger range of values.
      - **`SMALLSERIAL`**: Equivalent to `smallint`. It is used when you need a smaller range of integers.

2. **Sequence Creation**: When you declare a column as `SERIAL`, PostgreSQL automatically creates a sequence object for that column. The sequence is responsible for generating the next value. For example, if you define a column as `id SERIAL`, PostgreSQL creates a sequence named `id_seq` (by default).

3. **Default Value**: The `SERIAL` column is given a default value of the next value from the associated sequence. This means you don’t have to explicitly set a value for this column when inserting data.

**Example Usage**

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);
```
- The `id` column is defined as `SERIAL`, which makes it an auto-incrementing primary key.
- Whenever you insert a new user into the `users` table, PostgreSQL automatically generates a unique `id` value.
- **DO NOT SPECIFY VALUE OF A SERIAL**. Let the DB control that! When unspecified, Database will insert as `id = id + 1`


## PostgreSQL Commands
1. \timing [on|off]       toggle timing of commands (currently off)

## Tasks

1. Create a table called `users`