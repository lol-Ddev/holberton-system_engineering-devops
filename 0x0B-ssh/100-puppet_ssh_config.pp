# using Puppet to make changes to our configuration file
include ssh::server

class { 'ssh::server':
    options => {
          'PasswordAuthentication' => 'no',
          'IdentityFile'           => '~/.ssh/holberton'
            }
          }
