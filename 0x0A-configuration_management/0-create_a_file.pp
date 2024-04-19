# create a file in /tmp

$file='/tmp'

exec {'apt-get update':
command => '/usr/bin/apt-get update'
}

# make sure that the directory exists with set owner and permission
file { $file:
ensure => 'directory',
owner  => 'www-data',
group  => 'www-data',
mode   => '0744'
}

# create file school in directory /tmp
file { "${file}/school":
ensure  => 'present',
content => 'I love puppet',
require => File[$file]
}
