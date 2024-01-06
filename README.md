# wanda

## build on python 3.8

### Scylla Commands

    1. docker run --name some-scylla -p 127.0.0.1:9042:9042 -d scylladb/scylla --smp 1 --listen-address 0.0.0.0 --broadcast-rpc-address 127.0.0.1
    2. docker exec -it some-scylla nodetool status
    3. docker exec -it some-scylla cqlsh 
    4. CREATE KEYSPACE vision WITH replication = {'class': 'NetworkTopologyStrategy', 'replication_factor' : 1};