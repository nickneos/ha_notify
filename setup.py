from setuptools import find_packages, setup

__lib_name__ = 'ha_notify'
__author__ = 'Nick Neos'
__author_email__ = 'nicholas.neos@gmail.com'
__version__ = '0.1'
__url__ = ''
__license__ = 'MIT'
__description__ = ''
__long_description__ = """"""

setup(
    name=__lib_name__,
    version=__version__,
    description=__description__,
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    license=__license__,
    long_description=__long_description__,

    packages=find_packages()
)
