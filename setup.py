# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
    name='python_brfied',
    packages=['python_brfied', 'python_brfied.shortcuts', ],
    version='0.8.3',
    download_url='https://github.com/kelsoncm/python_brfied/releases/tag/0.8.3',
    description='Python library specific brazilian validations',
    author='Kelson da Costa Medeiros',
    author_email='kelsoncm@gmail.com',
    url='https://github.com/kelsoncm/python_brfied',
    keywords=['python', 'BR', 'Brazil', 'Brasil', 'model', 'form', 'locale', ],
    install_requires=['pyfwf==0.1.3', 'requests-ftp==0.3.1', 'requests==2.19.1'],
    classifiers=[]
)
