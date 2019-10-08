defaults
  timeout connect 10000ms
  timeout client 120000ms
  timeout server 120000ms

listen galera
  bind *:3306
  mode tcp
  % for instance in instances['galera']:
    server ${instance['hostname']} ${instance['ipaddr']}:3306 check maxconn 100
  % endfor
