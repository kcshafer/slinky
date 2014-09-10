from setuptools import setup, find_packages
import glob

from app.install import SlinkyInstall

setup(
    name = "slinky",
    version = "0.0.0",
    description = "Salesforce Development Tools",
    author = "KC Shafer",
    cmdclass={
        'install': SlinkyInstall,
    },
    author_email = "kclshafer@gmail.com",
    url = "https://github.com/kcshafer/slinky/",
    keywords = ["salesforce"],
    install_requires = [
        "pyrannosaurus",
        "lxml",
        'argparse',
        ],
    #package_dir={},
    #include_package_data=True,
    #packages=,
    package_data={
    },
    long_description = """\
    Salesforce Development Tools
    ----------------------------
    """
)