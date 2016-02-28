# -*- coding: utf-8 -*-
from distutils.core import setup
this_version = '0.1.5'
setup(
    name='django_brfied',
    packages=['django_brfied',
              'python_brfied', ],
    package_data={
        'django_brfied.static.js': ['*'],
    },
    version=this_version,
    download_url='https://github.com/kelsoncm/django_brfied/releases/tag/%s' % this_version,
    description='Django Application specific brazilian fields types',
    author='Kelson da Costa Medeiros',
    author_email='kelsoncm@gmail.com',
    url='https://github.com/kelsoncm/django_brfied', 
    keywords=['django', 'BR', 'Brazil', 'Brasil', 'model', 'form', 'locale', ],
    classifiers=[]
)
