listen checkit_cluster1
  bind *:3306
  mode tcp
  % for instance in instances['checkit_cluster1']:
    server ${instance['hostname']} ${instance['ipaddr']}:3306 check maxconn 100
  % endfor
