# create file school in directory /tmp


file { '/tmp/school':
ensure  => 'present',
content => 'I love Puppet',
owner   => 'www-data',
group   => 'www-data',
mode    => '0744'
}
