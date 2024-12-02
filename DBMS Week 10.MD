## [L10.2 (Module 47): Transactions/2: Serializability (30:28)](https://youtu.be/MNXTL69Ud9A)


### Serializable

We assume that every transaction will enter from a consistent state of the DB and will terminate leaving the DB in a consistent state

- A serial execution of a set of transactions will also leave the database in a consistent state
- `Serial Schedule` is a list of transactions grouped on a resource. Ex: All operations on Table A one after another, then all operations on table B one after another.
  - Every `Concurrent Schedule` is not Serializable, but there are some that can be Serializable.
- `Transactions` is a list of Instructions

- A `Concurrent Schedule` is serializable only if its `equivalent` to a serial schedule
  - All concurrent schedules are not serializable
- Two schedules are `equivalent` if they keep the database in the same state after execution

- A schedule consists of transactions.

- 2 schedules A & B might be equivalent even though they are not a serial schedule
- A schedule consisting of 2 transactions T1 and T2 is called `serializable` if it keeps the DB in the same consistent state as a `Serial Schedule` would do.


### Conflicting Instructions

Two instructions $I_i$ and $I_j$ are accessing resource `O`

|Operation $I_i$|Operation $I_j$|Conflict?|
|-|-|-|
|Read|Read|No|
|Read|Write|Yes|
|Write|Read|Yes|
|Write|Write|Yes|

if $I_i$ and $I_j$ are consecutive in a schedule and they don't conflict then their results would be same if they were interchanged


### Conflict Serializable

**Conflict Serializable** ensures the correctness of transactions in a multi-transaction environment, where multiple transactions might be executed concurrently. It is a stricter form of **serializability**, which is the highest isolation level for database transactions.

#### What is Conflict Serializability?

Conflict serializability refers to a situation where the schedule (or order of execution) of a set of transactions can be rearranged (by swapping non-conflicting operations) into a serial schedule without affecting the final result.

In simpler terms, a schedule of transactions is **conflict-serializable** if it can be transformed into a serial schedule (a schedule where transactions are executed one after the other, without any interleaving) by swapping operations that do not conflict with each other.

#### Conflict Between Operations

Two operations are said to **conflict** if:
- They belong to different transactions.
- They access the same data item.
- At least one of the operations is a **write**.

For example:
- A **read** operation on a data item by one transaction and a **write** operation on the same data item by another transaction do not conflict.
- Two **write** operations on the same data item by different transactions conflict.
- A **write** operation on a data item by one transaction and a **read** operation on the same data item by another transaction conflict.

#### Conflict Serializable vs. Serializable

- **Serializable**: A schedule is serializable if its result is equivalent to the result of some serial execution of the transactions. In a serial schedule, transactions are executed one by one, without overlapping.
- **Conflict Serializable**: A schedule is conflict-serializable if it can be transformed into a serial schedule by swapping non-conflicting operations. This is a more specific version of serializability, where only conflicting operations are considered when determining whether the schedule can be transformed into a serial schedule.
- Are all `Serializable Schedules` Conflict Serializable? **NO!**
- Are there `Serializable Schedules` that are not `Conflict Serializable`? **YES**
- If some schedule is `Conflict Serializable` then it's necessarily `Serializable`
  - The reverse does not hold true

Consider 3 Transactions T1 T2 T3 with the following schedule (R = read, W = write, 1,2,3 are transaction numbers)
1. $W_1(A)$, $W_2(A)$, $W_2(B)$, $W_1(B)$,$W_3(B)$
2. Cannot swap $W_1(A)$, $W_2(A)$ as working on same object A
3. Cannot swap $W_2(A)$, $W_2(B)$ as part of transaction 2. Cannot change order of instruction within a transaction
4. Cannot Swap $W_2(B)$, $W_1(B)$ - Same B
5. Cannot Swap $W_1(B)$,$W_3(B)$ - Same B
6. No swap is possible!
7. So this schedule is not `Conflict Equivalent` to anything
8. This is not a `Serial Schedule`.
   1. $W_1(A)$, $W_1(B)$, $W_2(A)$, $W_2(B)$, $W_3(B)$ is in **Serial Order**


#### Conflict Graph (Precedence Graph)

To determine whether a schedule is conflict-serializable, we can use a **conflict graph** (or **precedence graph**):
- Each transaction is represented as a **node in the graph**.
- An **edge** is drawn from one transaction to another if one transaction's **operation conflicts** with the other.
- If the graph has a **cycle**, the schedule is **not conflict-serializable** because a cycle indicates a dependency between transactions that cannot be resolved without changing the order of operations.
- If the graph is **acyclic**, the schedule is conflict-serializable because the transactions can be rearranged to avoid conflicts.

#### Example of Conflict Serializable Schedule

Consider two transactions, T1 and T2:

1. T1: **Read(A)**
2. T2: **Write(A)**
3. T1: **Write(A)**
4. T2: **Read(A)**

In this case, T1 and T2 have conflicting operations:
- The **Write(A)** by T2 and the **Read(A)** by T1 conflict because T2 is writing to A, and T1 is reading it.
- The **Write(A)** by T1 and the **Read(A)** by T2 also conflict.

However, if we reorder the operations by swapping the non-conflicting ones, like so:
- **Read(A)** by T1
- **Write(A)** by T2
- **Write(A)** by T1
- **Read(A)** by T2

This would result in a serializable schedule. Thus, this schedule is **conflict-serializable**.

#### Why is Conflict Serializable Important?

Conflict serializability is important because it ensures that a system can handle concurrent transactions in a way that the final state of the database will be the same as if the transactions were executed serially. This eliminates anomalies like **lost updates**, **temporary inconsistency**, and **uncommitted data** from concurrent transactions, which could otherwise lead to errors or incorrect results.

Conflict serializability is a way of ensuring transaction correctness in a multi-transaction environment by focusing on conflicts between operations and ensuring that schedules can be rearranged to follow a serial order.


### Topological Sort

**Topological sorting** is an algorithm used to order the vertices (nodes) of a **directed acyclic graph (DAG)** in a linear sequence, such that for every directed edge from vertex $u$ to vertex $v$, vertex $u$ appears before vertex $v$ in the ordering. In other words, it is a way to order tasks that have dependencies, ensuring that a task is completed before another task that depends on it.

#### Key Properties of Topological Sorting:
1. **Directed**: The graph must be directed, meaning the edges have a direction (from one vertex to another).
2. **Acyclic**: The graph must be acyclic, meaning there should be no cycles (i.e., no paths where a vertex is revisited after following the edges).
3. **Linear Order**: The result of the topological sort is a linear order of vertices, which satisfies all dependency constraints.

#### When is Topological Sorting used?
Topological sorting is commonly used in scenarios where tasks depend on each other. Some common applications include:
- Task scheduling (e.g., scheduling jobs in a project).
- Compilation order in programming languages.
- Dependency resolution in package management systems (e.g., installing software packages).

#### Example of Topological Sorting

Let’s consider an example where you have the following tasks and their dependencies:

- Task **A** must be done before **B**.
- Task **A** must be done before **C**.
- Task **B** must be done before **D**.
- Task **C** must be done before **D**.

We can represent these tasks and their dependencies as a directed graph:

```
A → B → D
 ↓
 C → D
```

This is a **Directed Acyclic Graph (DAG)** because it doesn’t contain any cycles (you can't go from any node back to itself following the edges).

#### Step-by-step Topological Sort:

1. **Identify vertices with no incoming edges**: These are tasks that have no dependencies, i.e., tasks that can be done first. In this case, **A** has no dependencies, so it is the first task.

2. **Remove the vertex and its outgoing edges**: After task **A** is completed, remove it from the graph along with the edges from **A** to **B** and **A** to **C**.

    New graph:
    ```
    B → D
    ↓
    C → D
    ```

3. **Repeat the process**: Now, the vertices **B** and **C** have no incoming edges. Either **B** or **C** can be chosen to execute next, but let's pick **B**.

4. **Remove the vertex and its outgoing edges**: After completing **B**, remove it from the graph along with the edge from **B** to **D**.

    New graph:
    ```
    C → D
    ```

5. **Continue the process**: Now, **C** is the next task with no incoming edges.

6. **Remove **C** and its outgoing edge**: After completing **C**, remove it from the graph along with the edge from **C** to **D**.

    New graph:
    ```
    D
    ```

7. **Complete the final task**: Finally, task **D** has no outgoing edges, so it is the last task to be executed.

#### Final Topological Order:
The topological order of the tasks is:
**A → B → C → D**

This means that the tasks should be executed in the following order to satisfy all dependencies:
1. **A** (no dependencies).
2. **B** (depends on **A**).
3. **C** (depends on **A**).
4. **D** (depends on both **B** and **C**).

#### Properties and Considerations:

1. **Uniqueness**: The topological order is not necessarily unique. If there are tasks that are independent of each other, they can appear in different orders. For example, in the case where **B** and **C** had no dependencies on each other, we could have either **A → B → C → D** or **A → C → B → D**.
   
2. **Cycle Detection**: If a graph has a cycle, topological sorting is not possible. For example, if task **A** depends on **B** and **B** depends on **A**, this forms a cycle, and there is no valid way to order the tasks.

#### Algorithms for Topological Sorting:
There are different algorithms to perform topological sorting:
1. **Kahn's Algorithm**: 
   - Identify vertices with no incoming edges and add them to a queue.
   - Repeatedly remove a vertex from the queue, add it to the result, and decrease the in-degree (number of incoming edges) of its neighbors.
   - If the in-degree of a neighbor becomes 0, add it to the queue.
   - time complexity of $O(V + E)$, where:
        - $V$ is the number of vertices (nodes) in the graph.
        - E is the number of edges in the graph.

1. **Depth-First Search (DFS) Approach**: 
   - Perform a DFS traversal on the graph.
   - Mark nodes as visited. When a node is fully explored (i.e., all its descendants are visited), add it to the topological order.

In both cases, if there is a cycle, the algorithm will detect it and signal that topological sorting is not possible.

### Testing for Conflict Serializability