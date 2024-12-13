# Week 11 Notes - DBMS

*Prof. Partha Pratham Das, IIT KGP*

*Notes by Adarsh (23f2003570)*  

## [L11.1, Module 51: Backup & Recovery/1: Backup/1 (28:53)](https://youtu.be/7oNFney4vhc)

### Backup and Recovery

A Backup of a database is a representative copy of data containing all necessary contents of a database such as data files and control files

- Unexpected database failures, especially those due to factors beyond our control, are unavoidable. Hence, it is important to keep a backup of the entire database
    - There are two major types of backup:
      - Physical Backup: A copy of physical database files such as data, control files, log files, and archived redo logs.
      - Logical Backup: A copy of logical data that is extracted from a database consisting of tables, procedures, views, functions, etc.

Recovery is the process of restoring the database to its latest known consistent state after a system failure occurs.
  - A Database Log records all transactions in a sequence. Recovery using logs is quite popular in databases
  - A typical log file contains information about transactions to execute, transaction states, and modified values

### Why is backup necessary? PPD

- Disaster Recovery
  - Data loss can occur due to various reasons like hardware failures, malware attacks, environmental & physical factors or a simple human error
- Client Side Changes
    - Clients may want to modify the existing application to serve their business’s dynamic needs
    - Developers might need to restore a previous version of the database in order to such address such requirements
- Auditing
    - From an auditing perspective, you need to know what your data or schema looked like at some point in the past
    - For instance, if your organization happens to get involved in a lawsuit, it may want to have a look at an earlier snapshot of the database.
- Downtime
    - Without backup, system failures lead to data loss, which in turn results in application downtime
    - This leads to bad business reputation

### Types of Backup Data
- Business Data includes personal information of clients, employees, contractors etc. along with details about places, things, events and rules related to the business.
- System Data includes specific environment/configuration of the system used for specialised development purposes, log files, software dependency data, disk images.
- Media files like photographs, videos, sounds, graphics etc. need backing up. Media files are typically much larger in size.


### Types of Backup Strategies

#### Full Backup
- Full Backup backs up everything. This is a complete copy, which stores all the objects of the database: tables, procedures, functions, views, indexes etc. Full backup can restore all components of the database system as it was at the time of crash.

- A full backup must be done at least once before any of the other type of backup
- The frequency of a full backup depends on the type of application. For instance, a full backup is done on a daily basis for applications in which one or more of the following is/are true:
  - Either 24/7 availability is not a requirement, or system availability is not affected as a consequence of backups.
  - A complete backup takes a minimum amount of media, i.e. the backup data is not too large.
-  Backup/system administrators may not be available on a daily basis, and therefore a primary goal is to reduce to a bare minimum the amount of media required to complete a restore.

##### Advantages
- Recovery from a full backup involves a consolidated read from a single backup
- Generally, there will not be any dependency between two consecutive backups.
- Effectively, the loss of a single day’s backup does not affect the ability to recover other backups
- It is relatively easy to setup, configure and maintain

##### Disadvantages
- The backup takes largest amount of time among all types of backups
- This results in longest system downtime during the backup process
- It uses largest amount of storage media per backup

#### Incremental Backup
- Incremental backup targets only those files or items that have changed since the last backup. This often results in smaller backups and needs shorter duration to complete the backup process.
- For instance, a 2 TB database may only have a 5% change during the day. With incremental database backups, the amount backed up is typically only a little more than the actual amount of changed data in the database.
- For most organizations, a full backup is done once a week, and incremental backups are done for the rest of the time. This might mean a backup schedule as shown below

| Friday | Saturday    | Sunday      | Monday      | Tuesday     | Wednesday   | Thursday    |
| ------ | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| Full   | Incremental | Incremental | Incremental | Incremental | Incremental | Incremental |

- This ensures a minimum backup window during peak activity times, with a longer backup window during non-peak activity times.

##### Advantages
- Less storage is used per backup
- The downtime due to backup is minimized
- It provides considerable cost reductions over full backups

##### Disadvantages
- It requires more effort and time during recovery
- A complete system recovery needs a full backup to start with
- It cannot be done without the full backups and all incremental backups in between
- If any of the intermediate incremental backups are lost, then the recovery cannot be 100%



#### Differential Backup
- Differential backup backs up all the changes that have occurred since the most recent full backup regardless of what backups have occurred in between
- This “rolls up” multiple changes into a single backup job which sets the basis for the next incremental backup
- As a differential backup does not back up everything, this backup process usually runs quicker than a full backup
- The longer the age of a differential backup, the larger the size of its backup window Database

- To evaluate how differential backups might work within an environment, consider the sample backup schedule shown in the figure below.
    - The incremental backup on Saturday backs up all files that have changed since the full backup on Friday. Likewise all changes since Saturday and Sunday is backed up on Sunday and Monday’s incremental backup respectively.
    - On Tuesday, a differential backup is performed. This backs up all files that have changed since the full backup on Friday. A recovery on Wednesday should only require data from the full and differential backups, skipping the Saturday/Sunday/Monday incremental backups.

| Friday | Saturday    | Sunday      | Monday      | Tuesday     | Wednesday   | Thursday    |
| ------ | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| Full   | Incremental | Incremental | Incremental | Differential | Incremental | Incremental |

*Recovery on any given day only needs the data from the full backup and the most recent differential backup*


##### Advantages
  - Recoveries require fewer backup sets.
  - Provide better recovery options when full backups are run rarely (for example, only monthly)


##### Disadvantages
- Although the number of backup sets required for recovery is less but in differential backups the amount of storage media required may exceed the storage media required for incremental backups
- If done after quite a long time, differential backups can even reach the size of a full backup


### Hot Backup

- Until now we have learnt about backup strategies which can not happen simultaneously with a running application
- In systems where high availability is a requirement Hot backup is preferable wherever possible
- Hot backup refers to keeping a database up and running while the backup is performed concurrently
  - Such a system usually has a module or plug-in that allows the database to be backed up while staying available to end users
- Databases which stores transactions of asset management companies, hedge funds, high frequency trading companies etc. try to implement Hot backups as these data are highly dynamic and the operations run 24x7
- Real time systems like sensor and actuator data in embedded devices, satellite transmissions etc. also use Hot backup

#### Advantages
◦ The database is always available to the end user.
◦ Point-in-time recovery is easier to achieve in Hot backup systems.
◦ Most efficient while dealing with dynamic and modularized data.

#### Disadvantages
◦ May not be feasible when the data set is huge and monolithic.
◦ Fault tolerance is less. Occurrence of any error on the fly can terminate the whole backup process.
◦ Maintenance and setup cost is high.

### Transactional Logging is a Hot Backup method!

- In regular database systems, hot backup is mainly used for Transaction Log Backup.
- Cold backup strategies like Differential, Incremental are preferred for Data backup. The reason is evident from the disadvantages of Hot backup.
- Transactional Logging is used in circumstances where a possibly inconsistent backup is taken, but another file generated and backed up (after the database file has been fully backed up) can be used to restore consistency.
- The information regarding data backup versions while recovery at a given point can be inferred from the Transactional Log backup set.
- Thus they play a vital role in database recovery.

----

## [L11.2, M52: Backup & Recovery/2: Recovery/1 (38:01)](https://youtu.be/2BkGxLntkBc)

### Database System Recovery

- All database reads/writes are within a transaction
- Transactions have the "ACID" properties
  - Atomicity - all or nothing
  - Consistency - preserves database integrity
  - Isolation - execute as if they were run alone
  - Durability - results are not lost by a failure
- Concurrency Control guarantees I, contributes to C
- Application program guarantees C
- Recovery subsystem guarantees A & D, Contributes to C

### Failure Classification
- Transaction failure:
    - Logical errors: transaction cannot complete due to some internal error condition
    - System errors: the database system must terminate an active transaction due to an error condition (for example, deadlock)
- System crash: a power failure or other hardware or software failure causes the system to crash
  - Fail-stop assumption: non-volatile storage contents are assumed to not be corrupted as result of a system crash
    - Database systems have numerous integrity checks to prevent corruption of disk data
- Disk failure: a head crash or similar disk failure destroys all or part of disk storage
  - Destruction is assumed to be detectable
    - Disk drives use checksums to detect failures
### Recovery Algorithms
- Consider transaction $T_i$ that transfers $50 from account A to account B
    - Two updates: subtract 50 from A and add 50 to B
- Transaction $T_i$ requires updates to A and B to be output to the database
    - A failure may occur after one of these modications have been made but before both of them are made
    - Modifying the database without ensuring that the transaction will commit may leave the database in an inconsistent state
    - Not modifying the database may result in lost updates if failure occurs just after transaction commits
- Recovery algorithms have two parts
    a) Actions taken during normal transaction processing to ensure enough information exists to recover from failures
    b) Actions taken after a failure to recover the database contents to a state that ensures atomicity, consistency and durability Database


### Storage Structure
- Volatile Storage:
  - does not survive system crashes
    - examples: main memory, cache memory
- Nonvolatile Storage:
  - survives system crashes
  - examples: disk, tape, flash memory, non-volatile (battery backed up) RAM
  - but may still fail, losing data
- Stable Storage:
    - a mythical form of storage that survives all failures
    - approximated by maintaining multiple copies on distinct non-volatile media
### Stable Storage Implementation
- Maintain multiple copies of each block on separate disks
    - copies can be at remote sites to protect against disasters such as fire or flooding
- Failure during data transfer can still result in inconsistent copies. Block transfer can result in
  - Successful completion
  - Partial failure: destination block has incorrect information
  - Total failure: destination block was never updated
- Protecting storage media from failure during data transfer (one solution):
  - Execute output operation as follows (assuming two copies of each block):
    - Write the information onto the 1st physical block.
    - When the 1st write is successful, write the same information onto the 2nd physical block
    - The output is completed only after the second write successfully completes
### Stable Storage Implementation (2)
Protecting storage media from failure during data transfer (cont.):
- Copies of a block may differ due to failure during output operation
- To recover from failure:
  - First find inconsistent blocks:
    - Expensive solution : Compare the two copies of every disk block
    - Better solution:
      - Record in-progress disk writes on non-volatile storage (Non-volatile RAM or special area of disk)
      - Use this information during recovery to find blocks that may be inconsistent, and only compare copies of these
      - This method is Used in hardware RAID systems
  - If either copy of an inconsistent block is detected to have an error (bad checksum), overwrite it by the other copy
  - If both have no error, but are different, overwrite the second block by the first block

### Data Access
-  Physical Blocks are those blocks residing on the disk
-  System Buffer Blocks are the blocks residing temporarily in main memory
-  Block movements between disk and main memory are initiated through the following two operations:
     - input(B) transfers the physical block B to main memory
     - output(B) transfers the buffer block B to the disk, and replaces the appropriate physical block there
-  We assume, for simplicity, that each data item fits in, and is stored inside, a single block
-  Each transaction $T_i$ has its **private work-area** in which local copies of all data items accessed and updated by it are kept
     - $T_i$'s local copy of a data item X is denoted by $x_i$
     - $B_X$ denotes block containing X
-  Transferring data items between system buffer blocks and its private work-area done by:
     - read(X) assigns the value of data item X to the local variable xi
     - write(X) assigns the value of local variable xi to data item X in the buffer block
-  Transactions
     - Must perform read(X) before accessing X for the first time (subsequent reads can be from local copy)
     - The write(X) can be executed at any time before the transaction commits
-  Note that output($B_X$) need not immediately follow write(X). System can perform the output operation when it deems fit
- Transaction Buffer writes to **System Buffer** which writes to disk buffer

### Recovery and Atomicity
-  To ensure atomicity despite failures, we first output information describing the
modifications to stable storage without modifying the database itself
-  We study Log-based Recovery Mechanisms
      - We first present key concepts
      - And then present the actual recovery algorithm
-  Less used alternative: **Shadow Paging**
-  In this Module we assume serial execution of transactions
-  In the next Module, we consider the case of concurrent transaction execution

### Log-Based Recovery
-  A log is kept on stable storage
      - The log is a sequence of log records, which maintains information about update activities on the database
- When transaction $T_i$ starts, it registers itself by writing a record `<$T_i$ start>` to the log
- Before $T_i$ executes `write(X)`, a log record `<$T_i$ ;X;V1;V2>` is written, where V1 is the value of X before the write (old value), and V2 is the value to be written to X (new value)
- When $T_i$ finishes its last statement, the log record `<$T_i$ commit>` is written

1. `<$T_i$ start>`
2. `<$T_i$ ;X;V1;V2>` is (`write(X)`)
3. `<$T_i$ commit>`

### Database Modification Schemes
-  The **immediate-modification** scheme allows updates of an uncommitted transaction to be made to the buffer, or the disk itself, before the transaction commits
    - Update log record must be written before a database item is written
        - We assume that the log record is output directly to stable storage
    - Output of updated blocks to disk storage can take place at any time before or after transaction commit
    - Order in which blocks are output can be different from the order in which they are written
-  The **deferred-modification** scheme performs updates to buffer/disk only at the time of transaction commit
      - Simplifies some aspects of recovery
      - But has overhead of storing local copy
-  We cover here only the immediate-modification scheme


### Transaction Commit
  - A transaction is said to have committed when its commit log record is **output** to stable storage
    - The commit might not have happened from system buffer to disk!
    - All previous log records of the transaction must have been **output** already
  - Writes performed by a transaction may still be in the buffer when the transaction commits, and may be **output** later
- **NOTE:** In this course 
        - **Written** means written to the **System Buffer**
        - **Output** means written to disk!
        - Variables are stored in Variable specific **System Blocks** a.k.a System Buffer

### Immediate Database Modification
$B_x$ is the `System Buffer Block` number for variable $x$

Remember, It's up to Database to decide when to write a `System Buffer Block` into `Physical Block`!!!! You just place you variable in the `Output` Channel

`Logical Write` means you wrote to the `System Buffer Block` but its not in the Disk


| Log                   | Write (System Buffer) | Output (Disk)                                     |
| --------------------- | --------------------- | ------------------------------------------------- |
| <$T_0$ **start**>     |                       |                                                   |
| <$T_0$ A, 1000, 950>  |                       |                                                   |
| <$T_0$ B, 2000, 2050> |                       |                                                   |
|                       | A = 950               |                                                   |
|                       | B = 2050              |                                                   |
| <$T_0$ **commit**>    |                       |                                                   |
| <$T_1$ **start**>     |                       |                                                   |
| <$T_1$ C, 700, 600>   |                       |                                                   |
|                       | C=600                 |                                                   |
|                       |                       | $B_B$, $B_C$ ($B_C$ outputs before $T_1$ commits) |
| <$T_1$ **commit**>    |                       |                                                   |
|                       |                       | $B_A$ ($B_A$ outputs after $T_0$ commits)         |
|                       |                       |                                                   |

### Undo and Redo Operations
-  Undo of a log record **<$T_i$ X V1 V2>** writes the old value V1 to X
-  Redo of a log record **<$T_i$ X V1 V2>** writes the new value V2 to X
-  Undo and Redo of Transactions
    - undo ($T_i$) restores the value of all data items updated by $T_i$ to their old values, going backwards from the last log record for $T_i$
      - Each time a data item X is restored to its old value V a special log record (called redo-only) **<$T_i$ X V>** is written out
      - When undo of a transaction is complete, a log record **<$T_i$ abort>** is written out (to indicate that the undo was completed)
    - redo($T_i$) sets the value of all data items updated by $T_i$ to the new values, going forward from the first log record for $T_i$
      - No logging is done in this case

-  The undo and redo operations are used in several different circumstances:
    - The undo is used for transaction rollback during normal operation
        - in case a transaction cannot complete its execution due to some logical error
    - The undo and redo operations are used during recovery from failure
-  We need to deal with the case where during recovery from failure another failure occurs prior to the system having fully recovered

### Undo and Redo on Normal Transaction Rollback
-  Let $T_i$ be the transaction to be rolled back
-  Scan log backwards from the end, and for each log record of $T_i$ of the form **<$T_i$ $X_j$ V1 V2>**
    - Perform the undo by writing V1 to Xj ,
    - Write a log record <$T_i$ $X_j$ $V_1$>
        - such log records are called **Compensation Log Records**
-  Once the record <$T_i$ **start**> is found stop the scan and write the log record <$T_i$ **abort**>

### Undo and Redo on Recovering from Failure
- When recovering after failure:
    - Transaction $T_i$ needs to be undone if the log
        - contains the record <$T_i$ **start**>,
        - but does not contain either the record <$T_i$ **commit**> or <$T_i$ **abort**>
    - Transaction $T_i$ needs to be redone if the log
        - contains the records <$T_i$ **start**>
        - and contains the record <$T_i$ **commit**> or <$T_i$ **abort**>
    - It may seem strange to redo transaction $T_i$ if the record <$T_i$ **abort**> record is in the log
        - To see why this works, note that if <$T_i$ **abort**> is in the log, so are the redo-only records written by the undo operation. Thus, the end result will be to undo $T_i$ 's modifications in this case. This slight redundancy simplifies the recovery algorithm and enables faster overall recovery time
        - such a redo redoes all the original actions including the steps that restored old value Known as **Repeating History**

### Checkpoints
  - Redoing/undoing all transactions recorded in the log can be very slow
      - Processing the entire log is time-consuming if the system has run for a long time
      - We might unnecessarily redo transactions which have already output their updates to the database
  - Streamline recovery procedure by periodically performing **checkpointing**
  - All updates are stopped while doing **checkpointing**
      1. Output all log records currently residing in main memory onto stable storage
      2. Output all modified buffer blocks to the disk
      3. Write a log record <**checkpoint** L> onto stable storage where L is a list of all transactions active at the time of checkpoint
- During recovery we need to consider only the most recent transaction $T_i$ that started before the checkpoint, and transactions that started after $T_i$
    - Scan backwards from end of log to find the most recent <**checkpoint** L> record
    - Only transactions that are in L or started after the checkpoint need to be redone or undone
    - Transactions that committed or aborted before the checkpoint already have all their updates output to stable storage
- Some earlier part of the log may be needed for undo operations
    - Continue scanning backwards till a record <$T_i$ **start**> is found for every transaction $T_i$ in L
    - Parts of log prior to earliest <$T_i$ **start**> record above are not needed for recovery, and can be erased whenever desired


- Any transactions that committed before the last checkpoint should be ignored
    - $T_1$ can be ignored (updates already output to disk due to checkpoint)
- Any transactions that committed since the last checkpoint need to be redone
    - $T_2$ and $T_3$ redone
- Any transaction that was running at the time of failure needs to be undone and restarted
    - $T_4$ undone

----

## [L11.3, Module 53: Backup & Recovery/3: Recovery/2 (33:43)](https://youtu.be/41cWyckqqRc)


## [L11.5: Backup & Recovery/5: Backup/2: RAID (32:57)](https://youtu.be/YYl4onLINRY)

### RAID: Redundant Array of Independent Disks (or Inexpensive)  

- Disk organization techniques that manage a large numbers of disks, providing a view of a single disk of
    - high capacity and high speed by using multiple disks in parallel,
    - high reliability by storing data redundantly, so that data can be recovered even if a disk fails
- The chance that some disk out of a set of n disks will fail is much higher than the chance that a specific single disk will fail
    - For example, a system with 100 disks, each with MTTF (Mean Time To Failure) of 100,000 hours will have a system MTTF of 1000 hours (do the math)
    - Techniques for using redundancy to avoid data loss are critical with large numbers of disks
- Originally a cost effective alternative to large, expensive disks
    - "I" in RAID originally stood for inexpensive
    - Today RAIDs are used for their higher reliability and bandwidth
        - The "I" is interpreted as independent

### RAID Mirroring

- Redundancy means: Store extra information that can be used to rebuild information lost in a disk failure
    - **Mean time to data loss** depends on mean time to failure, and mean time to repair
      - For example, in a single disk MTTF of 100,000 hours, **Mean Time To Repair** of 10 hours gives **Mean Time To Data Loss** of $500 \times 10^6$ hours (or 57,000 years) for a mirrored pair of disks (ignoring dependent failure modes)
  
        $$
          MTTDL = \dfrac{MTTF_{disk_1} \times MTTF_{disk_2}}{2 \times MTTR}
        $$
        $$
          MTTDL = \dfrac{10^5 \times 10^5}{2 \times 10} \ hours \\
          = 5 \times 10^8 \ hours \\
          = 57077.625 \ years \\
          This \ is \ how \ Prof. \ PPD \ calculated \ this
        $$
- Mirroring (or shadowing)
  - Duplicate every disk. Logical disk consists of two physical disks.
  - Every write is carried out on both disks
      - Reads can take place from either disk
  - If one disk in a pair fails, data still available in the other
      - Data loss would occur only if a disk fails, and its mirror disk also fails before the system is repaired
          - Probability of combined event is very small
          - Except for dependent failure modes such as fire or building collapse or electrical power surges

In a mirrored RAID setup, data loss occurs only if both disks fail before the failed disk is replaced. Given that the Mean Time to Repair is relatively short (10 hours), the system can typically replace a failed disk before the second one fails. This results in a very long Mean Time to Data Loss in such configurations.

### Striping
  - **Bit-level Striping**: Split the bits of each byte across multiple disks
      - In an array of eight disks, write bit i of each byte to disk i
      - Each access can read data at eight times the rate of a single disk
      - But seek/access time worse than for a single disk
          - Bit level striping is not used much any more
  - **Byte-level Striping**: Each file is split up into parts one byte in size. Using n = 4 disk array as an example
      - the 1st byte would be written to the 1st drive
      - the 2nd byte to the 2nd drive and so on, until
      - the 5th byte is then written to the 1st drive again and the whole process starts over
      - the i th byte is then written to the $(((i - 1) \% n) + 1)$th drive
  - **Block-level Striping**:
    - With n disks, block i of a file goes to disk $(i \% n) + 1$
    - Requests for different blocks can run in parallel if the blocks reside on different disks
    - A request for a long sequence of blocks can utilize all disks in parallel

### Parity
  **Bit-Interleaved Parity**:

- A single parity bit is enough for error correction, not just detection, since we know which disk has failed
      - When writing data, corresponding parity bits must also be computed and written to a parity bit disk
      - To recover data in a damaged disk, compute XOR of bits from other disks (including parity bit disk)
  

**Block-Interleaved Parity**:

- Uses block-level striping, and keeps a parity block on a separate disk for corresponding blocks from n other disks
- When writing data block, corresponding block of parity bits must also be computed and written to parity disk
- To  find value of a damaged block, compute XOR of bits from corresponding blocks (including parity block) from other disks

### Parity Checks


**Odd-Even Parity** refers to a method used to detect errors in data transmission or storage. It involves adding a parity bit to a sequence of data bits to ensure that the total number of 1's (or 0's) in the data, including the parity bit, is either odd or even.


#### 1. Odd Parity:
In **odd parity**, the number of 1's in the data, including the parity bit, is always an **odd number**.

- If the number of 1's in the data bits is already odd, the parity bit is set to **0** to maintain the odd count.
- If the number of 1's in the data bits is even, the parity bit is set to **1** to make the total number of 1's odd.

**Example of Odd Parity:**
Suppose the data is `1011001` (7 bits).
- Count the number of 1's: There are 4 ones (even).
- To make it odd, set the parity bit to **1**.

So, the transmitted data with odd parity would be:  
`1011001 1` (The parity bit is added to make the total number of 1's equal to 5, which is odd).

#### 2. Even Parity:
In **even parity**, the number of 1's in the data, including the parity bit, is always an **even number**.

- If the number of 1's in the data bits is already even, the parity bit is set to **0** to keep the count even.
- If the number of 1's in the data bits is odd, the parity bit is set to **1** to make the total number of 1's even.

**Example of Even Parity:**
Suppose the data is `1011001` (7 bits).
- Count the number of 1's: There are 4 ones (even).
- The parity bit should be set to **0** since the count is already even.

So, the transmitted data with even parity would be:  
`1011001 0` (The parity bit is added to maintain an even number of 1's, which remains 4).

#### Parity Checking:
At the receiving end, the parity bit is checked to ensure that the total number of 1's in the received data matches the expected odd or even parity. If there’s an error (i.e., a bit is flipped during transmission), the parity check will fail, and the system can detect that an error has occurred.

##### Example of Error Detection:

- If the data `1011001` with odd parity (and a parity bit of `1`) is transmitted but the bit sequence is corrupted, e.g., changed to `1011101`, the parity bit would no longer make the total count of 1's odd.
  - In this case, the receiver will detect the mismatch and realize that an error occurred.

- **Odd Parity:** The total number of 1's (data + parity) is odd.
- **Even Parity:** The total number of 1's (data + parity) is even.
- The parity bit is added as a simple error-detection mechanism to help ensure data integrity during transmission or storage.