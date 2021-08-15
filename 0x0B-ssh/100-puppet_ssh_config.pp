# using Puppet to make changes to our configuration file

class { 'ssh::server':
    options => {
          'PasswordAuthentication' => 'no',
          'IdentityFile'           => '~/.ssh/holberton'
            }
          }
