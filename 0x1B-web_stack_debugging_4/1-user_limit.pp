# To enable the user to login and open files error-free
# To increase the file limit(Hard)
exec { 'increase-hard-file-limit-for-holberton-user':
command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
path    => '/usr/local/bin/:/bin/'
}

# To increase soft file limit(Soft)
exec { 'increase-soft-file-limit-for-holberton-user':
command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
path    => '/usr/local/bin/:/bin/'
}
