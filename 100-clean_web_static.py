#!/usr/bin/python3
"""
    => Generates a .tgz archive from the contents of the web_static folder.
    => Distributes an archive to your web servers
    => Full deployment
    => Keep it clean!
"""
from fabric.api import *
from os import path, walk
from datetime import datetime


env.hosts = ['52.207.157.20', '54.175.3.48']


def do_pack():
    """
        Generates a .tgz archive from the contents of the web_static folder
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        if path.exists("./versions") is False:
            local('mkdir versions')
            # print('yes')

        archive_name = "versions/web_static_{}.tgz".format(date)
        print(archive_name)
        local("tar -czvf {} web_static".format(archive_name))
        return archive_name
    except Exception:
        return None


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


def deploy():
    """
    Full deployment
    """
    new_archive = do_pack()
    if new_archive is not None:
        return do_deploy(new_archive)
    return False


def do_clean(number=0):
    """
    Keep it clean!
    """
    try:
        number = int(number)
    except Exception:
        return False
    nb_of_arch = local('ls -ltr versions | wc -l', capture=True).stdout
    nb_of_arch = int(nb_of_arch) - 1
    if nb_of_arch <= 0 or nb_of_arch == 1:
        return True
    if number == 0 or number == 1:
        arch_to_rm = nb_of_arch - 1
    else:
        arch_to_rm = arch_to_rm - number
        if arch_to_rm <= 0:
            return True
    archives = local("ls -ltr versions | tail -n " + str(nb_of_arch) + "\
            | head -n \
            " + str(arch_to_rm) + "\
            | awk '{print $9}'", capture=True)
    archives_list = archives.rsplit('\n')
    if len(archives_list) >= 1:
        for arch in archives_list:
            if (arch != ''):
                local("rm versions/" + arch)
                run('rm -rf /data/web_static/releases/\
                    ' + arch.split('.')[0])
