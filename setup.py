# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
    name='pyshortcuts',
    packages=['pyshortcuts', 'pyshortcuts.shortcuts', ],
    version='0.1.0',
    download_url='https://github.com/kelsoncm/pyshortcuts/releases/tag/0.1.0',
    description='Python library specific brazilian validations',
    author='Kelson da Costa Medeiros',
    author_email='kelsoncm@gmail.com',
    url='https://github.com/kelsoncm/pyshortcuts',
    keywords=['python', 'BR', 'Brazil', 'Brasil', 'model', 'form', 'locale', ],
    install_requires=['pyfwf==0.1.3', 'requests-ftp==0.3.1', 'requests==2.21.0'],
    classifiers=[]
)

