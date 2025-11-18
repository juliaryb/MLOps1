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