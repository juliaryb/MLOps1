## PostgreSQL + TimescaleDB + pgvectorscale
terminal output:

```
julia@julia-zenbook:~/Documents/MLOps/MLOps1/lab04/lab$ psql -d "postgres://postgres:password@localhost:5555/postgres"
psql (16.10 (Ubuntu 16.10-0ubuntu0.24.04.1))
Type "help" for help.

postgres=# \dx
                                                    List of installed extensions
        Name         | Version |   Schema   |                                      Description                                      
---------------------+---------+------------+---------------------------------------------------------------------------------------
 plpgsql             | 1.0     | pg_catalog | PL/pgSQL procedural language
 timescaledb         | 2.23.0  | public     | Enables scalable inserts and complex queries for time-series data (Community Edition)
 timescaledb_toolkit | 1.22.0  | public     | Library of analytical hyperfunctions, time-series pipelining, and other SQL utilities
(3 rows)

postgres=# CREATE EXTENSION IF NOT EXISTS vectorscale CASCADE;
NOTICE:  installing required extension "vector"
CREATE EXTENSION
postgres=# \dx
                                                    List of installed extensions
        Name         | Version |   Schema   |                                      Description                                      
---------------------+---------+------------+---------------------------------------------------------------------------------------
 plpgsql             | 1.0     | pg_catalog | PL/pgSQL procedural language
 timescaledb         | 2.23.0  | public     | Enables scalable inserts and complex queries for time-series data (Community Edition)
 timescaledb_toolkit | 1.22.0  | public     | Library of analytical hyperfunctions, time-series pipelining, and other SQL utilities
 vector              | 0.8.1   | public     | vector data type and ivfflat and hnsw access methods
 vectorscale         | 0.8.0   | public     | diskann access method for vector search
(5 rows)

postgres=# 

```

```
docker compose up -d
WARN[0000] /home/julia/Documents/MLOps/MLOps1/lab04/lab/vectorscale_db/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 2/2
 ✔ Network vectorscale_db_default  Created                                                                                                                                  0.1s 
 ✔ Container vectorscaledb         Started                                                                                                                                  0.7s 
julia@julia-zenbook:~/Documents/MLOps/MLOps1/lab04/lab/vectorscale_db$ psql -d "postgres://postgres:password@localhost:5555/postgres"
psql (16.10 (Ubuntu 16.10-0ubuntu0.24.04.1))
Type "help" for help.

postgres=# \dx
                                                    List of installed extensions
        Name         | Version |   Schema   |                                      Description                                      
---------------------+---------+------------+---------------------------------------------------------------------------------------
 plpgsql             | 1.0     | pg_catalog | PL/pgSQL procedural language
 timescaledb         | 2.23.0  | public     | Enables scalable inserts and complex queries for time-series data (Community Edition)
 timescaledb_toolkit | 1.22.0  | public     | Library of analytical hyperfunctions, time-series pipelining, and other SQL utilities
(3 rows)

postgres=# exit
julia@julia-zenbook:~/Documents/MLOps/MLOps1/lab04/lab/vectorscale_db$ docker logs vectorscaledb
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "C.UTF-8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /home/postgres/pgdata/data ... ok
creating subdirectories ... ok
selecting dynamic shared memory implementation ... posix
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting default time zone ... Etc/UTC
creating configuration files ... ok
running bootstrap script ... ok
performing post-bootstrap initialization ... ok
syncing data to disk ... ok


Success. You can now start the database server using:

initdb: warning: enabling "trust" authentication for local connections
initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
    pg_ctl -D /home/postgres/pgdata/data -l logfile start

waiting for server to start....2025-11-18 18:41:28.195 UTC [39] LOG:  starting PostgreSQL 16.10 (Ubuntu 16.10-1.pgdg22.04+1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, 64-bit
2025-11-18 18:41:28.199 UTC [39] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2025-11-18 18:41:28.210 UTC [42] LOG:  database system was shut down at 2025-11-18 18:41:26 UTC
2025-11-18 18:41:28.221 UTC [39] LOG:  database system is ready to accept connections
2025-11-18 18:41:28.223 UTC [45] LOG:  TimescaleDB background worker launcher connected to shared catalogs
 done
server started

/docker-entrypoint.sh: sourcing /docker-entrypoint-initdb.d/000_install_timescaledb.sh
CREATE EXTENSION
CREATE EXTENSION
2025-11-18 18:41:29.135 UTC [60] ERROR:  background worker "TimescaleDB Background Worker Scheduler for database 1" trying to connect to template database, exiting

/docker-entrypoint.sh: running /docker-entrypoint-initdb.d/001_timescaledb_tune.sh
Using postgresql.conf at this path:
/home/postgres/pgdata/data/postgresql.conf

Writing backup to:
/tmp/timescaledb_tune.backup202511181841

Recommendations based on 3.55 GB of available memory and 16 CPUs for PostgreSQL 16
shared_buffers = 930887kB
effective_cache_size = 2727MB
maintenance_work_mem = 465443kB
work_mem = 1163kB
timescaledb.max_background_workers = 16
max_worker_processes = 35
max_parallel_workers_per_gather = 8
max_parallel_workers = 16
wal_buffers = 16MB
min_wal_size = 512MB
default_statistics_target = 100
random_page_cost = 1.1
checkpoint_completion_target = 0.9
max_connections = 50
max_locks_per_transaction = 128
autovacuum_max_workers = 10
autovacuum_naptime = 10
default_toast_compression = lz4
jit = off
effective_io_concurrency = 256
timescaledb.last_tuned = '2025-11-18T18:41:29Z'
timescaledb.last_tuned_version = '0.18.1'
Saving changes to: /home/postgres/pgdata/data/postgresql.conf

/docker-entrypoint.sh: running /docker-entrypoint-initdb.d/010_install_timescaledb_toolkit.sh
CREATE EXTENSION
CREATE EXTENSION

/docker-entrypoint.sh: running /docker-entrypoint-initdb.d/create_similarity_search_service_db.sql
CREATE DATABASE
You are now connected to database "similarity_search_service_db" as user "postgres".
psql:/docker-entrypoint-initdb.d/create_similarity_search_service_db.sql:10: NOTICE:  installing required extension "vector"
CREATE EXTENSION


waiting for server to shut down....2025-11-18 18:41:29.968 UTC [39] LOG:  received fast shutdown request
2025-11-18 18:41:29.972 UTC [39] LOG:  aborting any active transactions
2025-11-18 18:41:29.973 UTC [55] FATAL:  terminating background worker "TimescaleDB Background Worker Scheduler" due to administrator command
2025-11-18 18:41:29.973 UTC [45] FATAL:  terminating background worker "TimescaleDB Background Worker Launcher" due to administrator command
2025-11-18 18:41:29.975 UTC [39] LOG:  background worker "TimescaleDB Background Worker Launcher" (PID 45) exited with exit code 1
2025-11-18 18:41:29.975 UTC [39] LOG:  background worker "TimescaleDB Background Worker Scheduler" (PID 55) exited with exit code 1
2025-11-18 18:41:29.978 UTC [39] LOG:  background worker "logical replication launcher" (PID 46) exited with exit code 1
2025-11-18 18:41:29.978 UTC [40] LOG:  shutting down
2025-11-18 18:41:29.982 UTC [40] LOG:  checkpoint starting: shutdown immediate
.2025-11-18 18:41:31.374 UTC [40] LOG:  checkpoint complete: wrote 2324 buffers (14.2%); 0 WAL file(s) added, 0 removed, 1 recycled; write=0.051 s, sync=1.330 s, total=1.396 s; sync files=787, longest=0.007 s, average=0.002 s; distance=15095 kB, estimate=15095 kB; lsn=0/23A5A58, redo lsn=0/23A5A58
2025-11-18 18:41:31.392 UTC [39] LOG:  database system is shut down
 done
server stopped

PostgreSQL init process complete; ready for start up.

2025-11-18 18:41:31.598 UTC [1] LOG:  starting PostgreSQL 16.10 (Ubuntu 16.10-1.pgdg22.04+1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, 64-bit
2025-11-18 18:41:31.599 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2025-11-18 18:41:31.599 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2025-11-18 18:41:31.610 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2025-11-18 18:41:31.623 UTC [89] LOG:  database system was shut down at 2025-11-18 18:41:31 UTC
2025-11-18 18:41:31.637 UTC [1] LOG:  database system is ready to accept connections
2025-11-18 18:41:31.638 UTC [92] LOG:  TimescaleDB background worker launcher connected to shared catalogs
2025-11-18 18:41:32.263 UTC [96] LOG:  the "timescaledb" extension is not up-to-date
2025-11-18 18:41:32.263 UTC [96] HINT:  The most up-to-date version is 2.23.1, the installed version is 2.23.0.
julia@julia-zenbook:~/Documents/MLOps/MLOps1/lab04/lab/vectorscale_db$ psql -d "postgres://postgres:password@localhost:5555/postgres"
psql (16.10 (Ubuntu 16.10-0ubuntu0.24.04.1))
Type "help" for help.

postgres=# \l
                                                             List of databases
             Name             |  Owner   | Encoding | Locale Provider | Collate |  Ctype  | ICU Locale | ICU Rules |   Access privileges   
------------------------------+----------+----------+-----------------+---------+---------+------------+-----------+-----------------------
 postgres                     | postgres | UTF8     | libc            | C.UTF-8 | C.UTF-8 |            |           | 
 similarity_search_service_db | postgres | UTF8     | libc            | C.UTF-8 | C.UTF-8 |            |           | 
 template0                    | postgres | UTF8     | libc            | C.UTF-8 | C.UTF-8 |            |           | =c/postgres          +
                              |          |          |                 |         |         |            |           | postgres=CTc/postgres
 template1                    | postgres | UTF8     | libc            | C.UTF-8 | C.UTF-8 |            |           | =c/postgres          +
                              |          |          |                 |         |         |            |           | postgres=CTc/postgres
(4 rows)

postgres=# \c similarity_search_service_db
\dx
You are now connected to database "similarity_search_service_db" as user "postgres".
                                                    List of installed extensions
        Name         | Version |   Schema   |                                      Description                                      
---------------------+---------+------------+---------------------------------------------------------------------------------------
 plpgsql             | 1.0     | pg_catalog | PL/pgSQL procedural language
 timescaledb         | 2.23.0  | public     | Enables scalable inserts and complex queries for time-series data (Community Edition)
 timescaledb_toolkit | 1.22.0  | public     | Library of analytical hyperfunctions, time-series pipelining, and other SQL utilities
 vector              | 0.8.1   | public     | vector data type and ivfflat and hnsw access methods
 vectorscale         | 0.8.0   | public     | diskann access method for vector search
(5 rows)

similarity_search_service_db=# 
```
