# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
    name='django_brfied',
    packages=['django_brfied', 'python_brfied', ],
    package_dir={'django_brfied': 'django_brfied'},
    package_data={'django_brfied': ['django_brfied/static/js/*', 'django_brfied/*', 'django_brfied/migrations/*', 'django_brfied/management/commands/*'],},
    version='0.4.5',
    download_url='https://github.com/kelsoncm/django_brfied/releases/tag/0.4.5',
    description='Django Application specific brazilian fields types',
    author='Kelson da Costa Medeiros',
    author_email='kelsoncm@gmail.com',
    url='https://github.com/kelsoncm/django_brfied',
    keywords=['django', 'BR', 'Brazil', 'Brasil', 'model', 'form', 'locale', ],
    classifiers=[]
)
