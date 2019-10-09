# haproxy-etcd for a Percona Galera Cluster in Docker

Simple tool forked from (https://github.com/aksalj/haproxy-etcd) to generate a haproxy config file for a single galera
cluster based on availability info. from `etcd` and gracefully reload haproxy. The code comes with a Dockerfile
and a Docker Image available on the Docker Hub

## To use in docker stack or docker compose
```yaml
  haproxy:
    image: ha247/haproxy-galera-etcd
    environment:
      CLIENT_URL: http://etcd1:2379
      CLUSTER_NAME: cluster1
```

This is designed to be used for the default format for percona galera clusters as shown on their Docker Hub:
https://hub.docker.com/r/percona/percona-xtradb-cluster/

e.g. for a cluster named `cluster`, a `GET` from `/keys/pxc-cluster/cluster1` could return the following instances/nodes:

```json
        {
          "action": "get",
          "node": {
            "key": "/pxc-cluster/cluster1",
            "dir": true,
            "nodes": [
              {
                "key": "/pxc-cluster/cluster1/10.0.4.32",
                "dir": true,
                "expiration": "2019-10-01T09:02:52.805000625Z",
                "ttl": 26,
                "modifiedIndex": 8781875,
                "createdIndex": 8781875
              },
              {
                "key": "/pxc-cluster/cluster1/10.0.4.44",
                "dir": true,
                "expiration": "2019-10-01T09:02:52.954038826Z",
                "ttl": 26,
                "modifiedIndex": 8781907,
                "createdIndex": 8781907
              },
              {
                "key": "/pxc-cluster/cluster1/10.0.57.47",
                "dir": true,
                "expiration": "2019-10-01T09:02:55.784384213Z",
                "ttl": 29,
                "modifiedIndex": 9029896,
                "createdIndex": 9029896
              }
            ],
            "modifiedIndex": 102238,
            "createdIndex": 102238
          }
        }
```

### Bugs & Issues

To report bugs (or any other issues), use the [issues page](https://github.com/HA247RethinkIT/haproxy-etcd/issues).
