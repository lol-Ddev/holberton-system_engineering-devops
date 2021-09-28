# Using strace, find out why Apache is returning a 500 error.
# Once you find the issue, fix it and then automate it using Puppet

exec { 'Fix phpp':
  command  => 'sudo sed -i "s/phpp/php/" /var/www/html/wp-settings.php;
                        sudo service apache2 restart',
  provider => shell,
}
