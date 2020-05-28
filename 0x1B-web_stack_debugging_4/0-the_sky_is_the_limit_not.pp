#Change ULIMIT value from 15 to 2000
exec {'/etc/default/nginx':
command  => "sudo sed -i 's/15/2000/g' /etc/defaultnginx'; sudo service nginx restart",
provider => 'shell'
}