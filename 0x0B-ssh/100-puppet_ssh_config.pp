# using Puppet to make changes to our configuration file
include stdlib

file_line {'private_key':
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/holberton',
  replace => 'true'
  }

file_line {'authenticate_false':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
  replace => 'true'
  }
