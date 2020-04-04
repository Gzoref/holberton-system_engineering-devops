#!/usr/bin/env bash
#Add a custom HTTP header with Puppet

exec { 'Install':
       command  =>  'sudo apt-get update && sudo apt-get -y install nginx && echo "Holberton School for the win!" | sudo tee /var/www/html/index.nginx-debian.html && sudo sed -i "/^\sserver_name.*/a \                     rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default && sudo sed -i \'/^\slocation.*/i \        add_header X-Served-By $hostname;'                   etc/nginx/sites-available/default && sudo service nginx start',
       provider => shell,
}
