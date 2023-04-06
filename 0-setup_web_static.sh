#!/usr/bin/env bash
# Prepare web servers for static web-page

# if [ ! "$(dpkg-query -W --showformat='${db:Status-Status}' nginllx 2>&1)" = 'installed' ]; then
#     apt-get update
#     apt-get install -y nginx
# fi

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/shared /data/web_static/releases/test

echo "Wala" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current

chown -hR ubuntu:ubuntu /data


sed -i '33i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

service nginx restart
