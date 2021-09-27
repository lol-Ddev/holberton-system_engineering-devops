# Install Nginx web server (w/ Puppet)
exec { "apt-update":
    command => "/usr/bin/apt-get -y update"
    command => "/usr/bin/apt-get -y upgrade"
}
