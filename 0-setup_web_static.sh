#!/usr/bin/env bash
# Prepare web servers for static web-page

package_name='nginx'

status="$(dpkg-query -W --showformat='${db:Status-Status}' "$package_name" 2>&1)"
if [ ! "$status" = 'installed' ]; then
	apt-get update
	apt-get install -y nginx
fi

mkdir -p /data /data/web_static/ /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/

echo "Wala" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -Rh ubuntu:ubuntu /data


sed -i '33i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

nginx -s reload
