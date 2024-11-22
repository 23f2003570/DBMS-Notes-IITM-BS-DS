# Week 9 Notes - DBMS

*Prof. Partha Pratham Das, IIT KGP*

*Notes by Adarsh (23f2003570)*  

## [L9.1: Indexing and Hashing/1: Indexing/1 (32:02)](https://youtu.be/fY-EC1dknnQ)

### Indexes

Database indexes are essential structures that enhance the speed and efficiency of data retrieval operations. At a high level, an index is a data structure that allows the database management system (DBMS) to quickly look up and access rows in a table without scanning every single row. This can drastically reduce query times, especially when dealing with large datasets.

#### 1. **What Is an Index?**
An index in a database is similar to the index in a book. Instead of going through every page to find a specific word, you can look it up in the index, which points directly to the page number. Similarly, a database index points to the physical location of data in the database table, enabling quick retrieval.

#### 2. **Index Types**
There are various types of indexes, each with its own internal structure and use cases. Some common ones include:

##### **B-Tree Index (Balanced Tree Index)**
- **Structure**: A **B-tree** index is a balanced tree structure where each node contains a sorted key and a reference (pointer) to the corresponding data row.
- **How it works**: The index is divided into a tree of nodes, and each node holds a sorted list of keys. The B-tree ensures that the tree remains balanced (i.e., every path from the root to the leaves has the same length), guaranteeing efficient searching, insertion, and deletion.
- **Use case**: This is the most common type of index for queries involving equality (`=`) or range queries (`<`, `<=`, `>`, `>=`). It's typically used in OLTP (Online Transaction Processing) systems.

##### **Hash Index**
- **Structure**: A **hash index** uses a hash function to map the key to a specific location (bucket) in the table.
- **How it works**: When a query is issued with a key, the database applies the hash function to map the key to the corresponding bucket where the data is stored. Hash indexes are fast for exact match queries (e.g., `WHERE column = value`) but are not suitable for range queries.
- **Use case**: Used in situations where exact matching is the primary operation, such as lookups in key-value stores.

##### **Bitmap Index**
- **Structure**: A **bitmap index** uses bitmaps (bit arrays) to represent the presence or absence of a particular value in the indexed column.
- **How it works**: For a column with a limited number of distinct values (e.g., gender with values "male" and "female"), a bitmap index will create a bitmap where each bit corresponds to a row, and the bit is set to `1` if the row contains the value, and `0` otherwise.
- **Use case**: Bitmap indexes are efficient for columns with low cardinality (few distinct values) and are often used in data warehousing scenarios.

##### **Full-text Index**
- **Structure**: A **full-text index** is specialized for searching text-based data. It stores information about words in text columns and their positions in the documents.
- **How it works**: Full-text indexes often use a combination of algorithms like inverted indexes, where each word in the text is mapped to a list of rows that contain that word.
- **Use case**: Used in search engines, content management systems, or applications that need to support text searching (e.g., "find all rows containing the word 'apple'").

#### 3. **Index Storage**
Indexes are typically stored separately from the actual data rows (the table itself), and they consist of:
- **Keys**: The indexed column(s) or expression(s) that the index is built on.
- **Pointers**: References (often memory addresses or row IDs) to the actual data rows or table entries.

#### 4. **How Indexes Speed Up Queries**
When a query is issued to the database, the DBMS decides whether to use an index based on several factors, such as the type of query and the available indexes. Here's how indexes help:
- **Direct Lookup**: If an index exists on a column being queried, the DBMS can use the index to directly find the location of the required rows.
- **Reduced Search Space**: Instead of scanning all rows, an index narrows down the search space, often requiring just a small number of disk accesses, even for large tables.
- **Efficient Sorting**: If the index stores data in a sorted order (as in a B-tree index), sorting operations can be optimized by using the index directly rather than having to sort the data from scratch.

#### 5. **Cost of Indexes**
While indexes speed up reads, they come with overhead:
- **Storage**: Indexes require additional disk space. The more indexes you have, the more storage space is consumed.
- **Write Performance**: Every time a row is inserted, updated, or deleted, the database must update all associated indexes. This can slow down write-heavy workloads.
- **Index Maintenance**: Some indexes may require periodic rebuilding or optimization to maintain their efficiency, especially when there is heavy write activity.

#### 6. **Clustered vs Non-clustered Indexes**
- **Clustered Index**: A table can have only one clustered index, which means the data rows themselves are stored in the order of the index. In a clustered index, the index structure contains pointers to the data rows themselves.
- **Non-clustered Index**: A table can have multiple non-clustered indexes. These indexes are separate from the table and contain pointers to the actual rows in the table.

#### 7. **Index Operations**
- **Creation**: Indexes are usually created using the `CREATE INDEX` statement in SQL, and they can be created on one or more columns.
- **Update**: When a row in the indexed column is modified, the corresponding index needs to be updated to reflect the change.
- **Drop**: Unused or redundant indexes can be dropped to save space and improve write performance.

#### 8. **Choosing the Right Index**
The effectiveness of an index depends on the query patterns. Factors to consider:
- **Columns Used in Queries**: Index columns should be those that are frequently queried, especially in `WHERE`, `ORDER BY`, `JOIN`, and `GROUP BY` clauses.
- **Cardinality**: Indexing columns with high cardinality (many distinct values) is usually more beneficial than low-cardinality columns.
- **Query Frequency**: Frequently accessed columns or tables should be indexed for performance benefits.
