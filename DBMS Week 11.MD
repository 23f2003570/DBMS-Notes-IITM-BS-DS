# Week 11 Notes - DBMS

*Prof. Partha Pratham Das, IIT KGP*

*Notes by Adarsh (23f2003570)*  

## [L11.1, Module 51: Backup & Recovery/1: Backup/1 (28:53)]

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

### Transactional Logging as Hot Backup

- In regular database systems, hot backup is mainly used for Transaction Log Backup.
- Cold backup strategies like Differential, Incremental are preferred for Data backup. The reason is evident from the disadvantages of Hot backup.
- Transactional Logging is used in circumstances where a possibly inconsistent backup is taken, but another file generated and backed up (after the database file has been fully backed up) can be used to restore consistency.
- The information regarding data backup versions while recovery at a given point can be inferred from the Transactional Log backup set.
- Thus they play a vital role in database recovery.
