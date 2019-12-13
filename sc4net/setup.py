# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
    name='sc4net',
    packages=['sc4net', ],
    version='0.1.0',
    download_url='https://github.com/kelsoncm/pyatalhos/releases/tag/sc4net-v0.1.0',
    description='Shortcuts for user with requests and requests_ftp',
    author='Kelson da Costa Medeiros',
    author_email='kelsoncm@gmail.com',
    url='https://github.com/kelsoncm/sc4',
    keywords=['shortcuts', 'requests', 'requests_ftp', ],
    install_requires=['requests-ftp==0.3.1', 'requests==2.21.0'],
    classifiers=[]
)
