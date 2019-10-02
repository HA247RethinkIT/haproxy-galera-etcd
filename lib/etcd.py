import sys
from apiclient import APIClient


class Etcd(APIClient):
    """
        Get services from etcd
        Expects them at /keys/pxc-cluster/, for each service, the value expected is (HOST|IP):PORT
        e.g. for a galera cluster with the name cluster1:
        $ curl http://{IP:PORT}/v2/keys/pxc-cluster/cluster1/
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
    """

    def __init__(self, base_url):
        self.BASE_URL = base_url + '/v2'
        super(Etcd, self).__init__()

    def fetch_services(self, key='pxc-cluster'):
        services = []
        try:
            req = self.call('/keys/' + key, sorted='true')
            nodes = req['node']['nodes']
            for node in nodes:
                service = {
                    'path': '/keys' + node['key'],
                    'name': node['key'].split('/')[2]
                }
                services.append(service)
        except:
            print 'Unexpected error in fetch_services():', sys.exc_info()[0]
        return services

    def fetch_instances_of(self, service):
        instances = []
        try:
            print(service)
            req = self.call(service['path'], sorted='true')
            nodes = req['node']['nodes']
            counter = 0
            for node in nodes:
                hostname = self.call('/keys' + node['key'] + '/hostname', sorted='true')
                ipaddr = self.call('/keys' + node['key'] + '/ipaddr', sorted='true')
                instance = {
                    'hostname': hostname['node']['value'],
                    'ipaddr': ipaddr['node']['value']
                }
                instances.append(instance)
                counter += 1
        except:
            print 'Unexpected error in fetch_instances_of():', sys.exc_info()[0]
        
        return instances
