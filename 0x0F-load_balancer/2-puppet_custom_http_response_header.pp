# Setup New Ubuntu server with nginx
# and add a custom HTTP header
Exec { ‘update system’:
 Command => ‘/usr/bin/apt-get update’,
}
Package { ‘nginx’:
Ensure => ‘installed’,
Require => Exec[‘update system’]
}
File {‘/var/www/html/index.html’:
Content => ‘Hello World!’
}
Exec {‘redirect_me’:
Command => ‘sed -I “24i\ rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;” 
/etc/nginx/sites-available/default’,
Provider => ‘shell’
}
Exec {‘HTTP header’:
Command => ‘sed -I “25i\ add_header X-Served-By \$hostname;” /etc/nginx/sitesavailable/default’,
Provider => ‘shell’
}
Service {‘nginx’:
Ensure => running,
Require => Package[‘nginx’]
}
