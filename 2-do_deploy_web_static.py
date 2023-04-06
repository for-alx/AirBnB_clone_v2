#!/usr/bin/python3
"""
    Distributes an archive to your web servers
"""
from fabric.api import put, run, env
from os import path


env.hosts = ['52.207.157.20', '54.175.3.48']


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if path.exists(archive_path) is False:
        return False
    try:
        archive_name = archive_path.split('/')[-1]
        file_name = archive_name.split('.')[0]
        des = "/data/web_static/releases/"

        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(des, file_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(archive_name, des, file_name))
        run('rm /tmp/{}'.format(archive_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(des, file_name))
        run('rm -rf {}{}/web_static'.format(des, file_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(des, file_name))
        return True
    except Exception:
        return False
