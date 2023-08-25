# This kills the process id as killmenow

exec { 'pkill':
command  => 'pkill killmenow',
provider => 'shell',
}
