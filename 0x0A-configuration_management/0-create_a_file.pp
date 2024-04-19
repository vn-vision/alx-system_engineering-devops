# create a file in /tmp

$file='/tmp'

# make sure that the directory exists with set owner and permission
file { $file:
ensure => 'directory',
}

# create file school in directory /tmp
file { "${file}/school":
ensure  => 'present',
content => 'I love Puppet',
owner   => 'www-data',
group   => 'www-data',
mode    => '0744'
require => File[$file]
}
