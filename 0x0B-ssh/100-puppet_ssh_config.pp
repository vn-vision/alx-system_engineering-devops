# puppet script to make changes to our config file
/**
* Line: ' PasswordAuthentication no' :configures SSH to disable password
* path: '/etc/ssh/ssh_config' :global SSH client configuration file).
* Line: ' IdentityFile ~/.ssh/school' : declare location of SSH priv key to use
*/

file_line { 'Turn off passwd auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}
