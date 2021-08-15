# using Puppet to make changes to our configuration file

class { 'ssh::server':
    path    => '/etc/ssh/ssh_config',
    options => {
          'PasswordAuthentication' => 'no',
          'IdentityFile'           => '~/.ssh/holberton'
            }
          }
