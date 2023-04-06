#!/usr/bin/python3
"""
    Generates a .tgz archive from the contents of the web_static folder
"""

from fabric.api import *
import os
from os import path
from datetime import datetime

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
