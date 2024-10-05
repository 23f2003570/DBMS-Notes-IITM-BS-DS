# Datasets

## FKIS

### referees
```sql
                                           Table "public.referees"
   Column   |         Type          | Collation | Nullable | Default | Storage  | Stats target | Description 
------------+-----------------------+-----------+----------+---------+----------+--------------+-------------
 referee_id | character varying(10) |           | not null |         | extended |              | 
 name       | character varying(80) |           | not null |         | extended |              | 
 dob        | date                  |           | not null |         | plain    |              | 
Indexes:
    "referees_pk" PRIMARY KEY, btree (referee_id)
Referenced by:
    TABLE "match_referees" CONSTRAINT "match_referees_fk2" FOREIGN KEY (referee) REFERENCES referees(referee_id)
    TABLE "match_referees" CONSTRAINT "match_referees_fk3" FOREIGN KEY (assistant_referee_1) REFERENCES referees(referee_id)
    TABLE "match_referees" CONSTRAINT "match_referees_fk4" FOREIGN KEY (assistant_referee_2) REFERENCES referees(referee_id)
    TABLE "match_referees" CONSTRAINT "match_referees_fk5" FOREIGN KEY (fourth_referee) REFERENCES referees(referee_id)
```

### matches
```sql
                                              Table "public.matches"
      Column      |         Type          | Collation | Nullable | Default | Storage  | Stats target | Description 
------------------+-----------------------+-----------+----------+---------+----------+--------------+-------------
 match_num        | character varying(10) |           | not null |         | extended |              | 
 match_date       | date                  |           | not null |         | plain    |              | 
 host_team_id     | character varying(10) |           | not null |         | extended |              | 
 guest_team_id    | character varying(10) |           | not null |         | extended |              | 
 host_team_score  | integer               |           | not null |         | plain    |              | 
 guest_team_score | integer               |           | not null |         | plain    |              | 
Indexes:
    "matches_pk" PRIMARY KEY, btree (match_num)
Foreign-key constraints:
    "matches_fk0" FOREIGN KEY (host_team_id) REFERENCES teams(team_id)
    "matches_fk1" FOREIGN KEY (guest_team_id) REFERENCES teams(team_id)
Referenced by:
    TABLE "match_referees" CONSTRAINT "match_referees_fk0" FOREIGN KEY (match_num) REFERENCES matches(match_num)

```

### teams

```sql
                                                Table "public.teams"
      Column       |         Type          | Collation | Nullable | Default | Storage  | Stats target | Description 
-------------------+-----------------------+-----------+----------+---------+----------+--------------+-------------
 team_id           | character varying(10) |           | not null |         | extended |              | 
 name              | character varying(80) |           | not null |         | extended |              | 
 city              | character varying(80) |           | not null |         | extended |              | 
 playground        | character varying(80) |           | not null |         | extended |              | 
 jersey_home_color | character varying(80) |           |          |         | extended |              | 
 jersey_away_color | character varying(80) |           |          |         | extended |              | 
Indexes:
    "teams_pk" PRIMARY KEY, btree (team_id)
Referenced by:
    TABLE "managers" CONSTRAINT "managers_fk3" FOREIGN KEY (team_id) REFERENCES teams(team_id)
    TABLE "matches" CONSTRAINT "matches_fk0" FOREIGN KEY (host_team_id) REFERENCES teams(team_id)
    TABLE "matches" CONSTRAINT "matches_fk1" FOREIGN KEY (guest_team_id) REFERENCES teams(team_id)
    TABLE "players" CONSTRAINT "players_fk0" FOREIGN KEY (team_id) REFERENCES teams(team_id)
```

### players
```sql
                                           Table "public.players"
  Column   |         Type          | Collation | Nullable | Default | Storage  | Stats target | Description 
-----------+-----------------------+-----------+----------+---------+----------+--------------+-------------
 player_id | character varying(10) |           | not null |         | extended |              | 
 name      | character varying(80) |           | not null |         | extended |              | 
 dob       | date                  |           | not null |         | plain    |              | 
 jersey_no | integer               |           | not null |         | plain    |              | 
 team_id   | character varying(10) |           | not null |         | extended |              | 
Indexes:
    "players_pk" PRIMARY KEY, btree (player_id)
Foreign-key constraints:
    "players_fk0" FOREIGN KEY (team_id) REFERENCES teams(team_id)

```

### match_referees
```sql
                                            Table "public.match_referees"
       Column        |         Type          | Collation | Nullable | Default | Storage  | Stats target | Description 
---------------------+-----------------------+-----------+----------+---------+----------+--------------+-------------
 match_num           | character varying(10) |           | not null |         | extended |              | 
 referee             | character varying(15) |           |          |         | extended |              | 
 assistant_referee_1 | character varying(15) |           |          |         | extended |              | 
 assistant_referee_2 | character varying(15) |           |          |         | extended |              | 
 fourth_referee      | character varying(15) |           |          |         | extended |              | 
Indexes:
    "match_referees_pkey" PRIMARY KEY, btree (match_num)
Foreign-key constraints:
    "match_referees_fk0" FOREIGN KEY (match_num) REFERENCES matches(match_num)
    "match_referees_fk2" FOREIGN KEY (referee) REFERENCES referees(referee_id)
    "match_referees_fk3" FOREIGN KEY (assistant_referee_1) REFERENCES referees(referee_id)
    "match_referees_fk4" FOREIGN KEY (assistant_referee_2) REFERENCES referees(referee_id)
    "match_referees_fk5" FOREIGN KEY (fourth_referee) REFERENCES referees(referee_id)
```
### managers

```sql
                                        Table "public.managers"
 Column  |         Type          | Collation | Nullable | Default | Storage  | Stats target | Description 
---------+-----------------------+-----------+----------+---------+----------+--------------+-------------
 mgr_id  | character varying(10) |           | not null |         | extended |              | 
 name    | character varying(80) |           | not null |         | extended |              | 
 dob     | date                  |           | not null |         | plain    |              | 
 team_id | character varying(10) |           |          |         | extended |              | 
 since   | date                  |           |          |         | plain    |              | 
Indexes:
    "managers_pk" PRIMARY KEY, btree (mgr_id)
Foreign-key constraints:
    "managers_fk3" FOREIGN KEY (team_id) REFERENCES teams(team_id)
```


### Data

```
referees:

 referee_id |       name        |    dob     
------------+-------------------+------------
 R0001      | Tony Joseph Louis | 1975-12-20
 R0002      | Samar Pal         | 1972-08-02
 R0003      | Kennedy Sapam     | 1970-12-06

 
 players:
                                        
 player_id | name  |    dob     | jersey_no | team_id 
-----------+-------+------------+-----------+---------
 P1001     | Rudra | 2003-05-01 |        99 | T0001
 P1002     | Advik | 2004-06-01 |        89 | T0001
 P1003     | Adi   | 2003-05-07 |        79 | T0001

matches:

 match_num | match_date | host_team_id | guest_team_id | host_team_score | guest_team_score 
-----------+------------+--------------+---------------+-----------------+------------------
 M0001     | 2020-05-06 | T0001        | T0006         |               5 |                4
 M0002     | 2020-05-07 | T0002        | T0005         |               0 |                1
 M0003     | 2020-05-09 | T0003        | T0004         |               2 |                3


match_referees

 match_num | referee | assistant_referee_1 | assistant_referee_2 | fourth_referee 
-----------+---------+---------------------+---------------------+----------------
 M0001     | R0001   | R0002               | R0003               | R0004
 M0002     | R0005   | R0006               | R0007               | R0001
 M0003     | R0002   | R0003               | R0004               | R0005


managers
mgr_id |  name   |    dob     | team_id |   since    
--------+---------+------------+---------+------------
 M0001  | Jacob   | 1990-08-23 | T0001   | 2020-06-22
 M0002  | Scott   | 1985-05-02 | T0002   | 2021-03-22
 M0003  | Brandon | 1995-02-15 | T0003   | 2019-04-02

 teams

 team_id |  name   |  city  |    playground    | jersey_home_color | jersey_away_color 
---------+---------+--------+------------------+-------------------+-------------------
 T0001   | Amigos  | London | Emirates Stadium | Red               | Blue
 T0002   | Thunder | leeds  | Villa Park       | White             | Red
 T0003   | Rainbow | Moscow | City Park        | Black             | White

 ```


### Commentary
#### Order By
```
SELECT * FROM referees ORDER BY name, dob;
```

1. This should project all fields in the `referees` table after sorting `name` in ascending order
2. It then orders the `dob` column without disturbing the order of `name`

```
flis=# SELECT * FROM referees ORDER BY name, dob;
 referee_id |          name          |    dob     
------------+------------------------+------------
 R0005      | Antony Abraham         | 1980-04-30
 R0004      | Asit Kumar Sarkar      | 1960-05-12
 R0003      | Kennedy Sapam          | 1970-12-06
 R0002      | Samar Pal              | 1972-08-02
 R0006      | Sumanta Dutta          | 1974-02-28
 R0001      | Tony Joseph Louis      | 1975-12-20
 R0007      | Vairamuthu Parasuraman | 1979-01-25
(7 rows)

flis=# INSERT INTO referees VALUES ('R0008', 'Tony Joseph Louis', '1974-01-02');
INSERT 0 1


flis=# SELECT * FROM referees ORDER BY name, dob;
 referee_id |          name          |    dob     
------------+------------------------+------------
 R0005      | Antony Abraham         | 1980-04-30
 R0004      | Asit Kumar Sarkar      | 1960-05-12
 R0003      | Kennedy Sapam          | 1970-12-06
 R0002      | Samar Pal              | 1972-08-02
 R0006      | Sumanta Dutta          | 1974-02-28
 R0008      | Tony Joseph Louis      | 1974-01-02
 R0001      | Tony Joseph Louis      | 1975-12-20
 R0007      | Vairamuthu Parasuraman | 1979-01-25
(8 rows)

```


#### Cross Product

**referees:** has 8 rows, 3 columns  
**players** has 71 rows, 5 columns  

so `SELECT * from referees, players` should have
1. 5 + 3 ie 8 columns
2. 71 * 8 ie 568 rows
   1. Which is correct
3. the fields in the output will be ordered fields of referees joined with ordered fields of players.
