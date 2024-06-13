# Ensure the correct ulimit setting in /etc/default/nginx/
# this script increases the amount of traffic an Nginx server can handle
# Increase the ULIMIT of the default file

# Modify the ULIMIT value in /etc/default/nginx if it's not set to "-n 4096"
exec { 'fix-for-nginx':
  command => 'sed -i "s/^ULIMIT=.*/ULIMIT=\\"-n 4096\\"/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  unless  => 'grep -q "^ULIMIT=\\"-n 4096\\"$" /etc/default/nginx',
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and reload it if necessary
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Exec['fix-for-nginx'],
}

