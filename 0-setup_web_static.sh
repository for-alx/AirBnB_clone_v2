#!/usr/bin/env bash
# Prepare web servers for static web-page

# package_name='nginx'

# status="$(dpkg-query -W --showformat='${db:Status-Status}' "$package_name" 2>&1)"
# if [ ! "$status" = 'installed' ]; then
# 	apt-get update
# 	apt-get install -y nginx
# fi
apt-get update && \
apt-get install -y nginx && \
mkdir -p -m=755 /data/web_static/{releases/test,shared} || exit 0
echo 'Testing 123' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
insert='\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;}'
sed -i "37i $insert" /etc/nginx/sites-available/default
service nginx restart
