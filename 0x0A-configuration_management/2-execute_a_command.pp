# create a manifest that kills a process named killmenow.
exec { 'killme now':
  command  => 'pkill -f killmenow',
  provider => shell,
  }
