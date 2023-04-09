# Configures a web server for deployment.


file { ['/data', '/data/web_static', '/data/web_static/shared', '/data/web_static/releases', '/data/web_static/releases/test']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "Holberton School Puppet\n",
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}
