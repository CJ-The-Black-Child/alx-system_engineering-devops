# This increases the ammount of traffic on Nginx server
# increment the Limit of the default file
exec { 'fix--got-nginx':
  command => 'sed -i "/15/4096" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# To restart Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
