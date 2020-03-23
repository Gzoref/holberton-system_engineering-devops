#client SSH configuration file to connect to server without typing a password.
file_line { 'Declare identify file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentifyFile ~/.ssh/holberton',
}

file_line { 'Turn off passwd auth':
  ensure => 'present',
  path   => 'etc/ssh_config',
  line   => 'PasswordAuthentification no',
}
