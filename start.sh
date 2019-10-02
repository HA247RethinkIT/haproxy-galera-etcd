#!/bin/bash
/usr/local/bin/haproxy-etcd --client-url $ETCD_NODE  --haproxy-binary /usr/sbin/haproxy --haproxy-pid /var/run/haproxy.pid --haproxy-config /etc/haproxy/haproxy.cfg --template /app/templates/haproxy.tpl
