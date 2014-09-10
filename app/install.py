import os

from setuptools import setup
from setuptools.command.install import install


class SlinkyInstall(install):

    def run(self):
        try:
            os.remove('/usr/local/bin/slinky')
            os.unlink('/usr/local/bin/slinky')
        except:
            pass
        os.symlink(os.getcwd() + '/bin/slinky.py', '/usr/local/bin/slinky')
        os.chmod('/usr/local/bin/slinky', 755)
        install.run(self)