import time
import os
import sys
from etcd import Etcd
from haproxy import Haproxy


def main():
    """Generate a haproxy config file based on etcd then gracefully reload haproxy"""

    # This is designed to work with containers, we expect to receive params via the environment
    template = os.environ.get('TEMPLATE', '/app/templates/haproxy.tpl')
    client_url = os.environ.get('CLIENT_URL', None)
    haproxy_binary = os.environ.get('HAPROXY_BINARY', '/usr/sbin/haproxy')
    haproxy_pid = os.environ.get('HAPROXY_PID', '/var/run/haproxy.pid')
    haproxy_service = None
    haproxy_config = os.environ.get('HAPROXY_CONFIG', '/etc/haproxy/haproxy.cfg')
    interval_check = os.environ.get('INTERVAL_CHECK', 5)
    cluster_name = os.environ.get('CLUSTER_NAME', 'cluster1')

    # Cant continue if we don't have an etcd endpoint
    if not client_url:
        sys.exit('CLIENT_URL has not been defined')

    etcd = Etcd(client_url)

    haproxy = Haproxy(haproxy_service, haproxy_binary, haproxy_pid)
    if template:
        haproxy.set_template(template)
    if haproxy_config:
        haproxy.set_config_file(haproxy_config)

    while True:
        data = []
        services = etcd.fetch_services()
        for service in services:
            # Rename the service to match the template, if the cluster name in etcd matches our galera cluster.
            if service['name'] != cluster_name:
                continue
            service['name'] = 'galera'
            instances = etcd.fetch_instances_of(service)
            data.append({'service': service, 'instances': instances})

        # TODO - if we don't have any cluster data, should we die?
        haproxy.reload(data)
        time.sleep(interval_check)


if __name__ == "__main__":
    main()
