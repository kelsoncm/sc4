#!/usr/bin/env python
import argparse
import os


parser = argparse.ArgumentParser(description='release project')
parser.add_argument('version')
args = parser.parse_args()

with open('setup.py', 'w') as f:
    f.write("""# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
    name='django_brfied',
    packages=['django_brfied', 'python_brfied', ],
    package_dir={'django_brfied': 'django_brfied'},
    package_data={'django_brfied': ['static/js/*'],},
    version='%s',
    download_url='https://github.com/kelsoncm/django_brfied/releases/tag/%s',
    description='Django Application specific brazilian fields types',
    author='Kelson da Costa Medeiros',
    author_email='kelsoncm@gmail.com',
    url='https://github.com/kelsoncm/django_brfied',
    keywords=['django', 'BR', 'Brazil', 'Brasil', 'model', 'form', 'locale', ],
    classifiers=[]
)
""" % (args.version, args.version,))

os.system("git add setup.py")
os.system("git commit -m 'Release %s'" % args.version)
os.system("git tag %s" % args.version)
os.system("git push --tags origin master")
os.system("python setup.py sdist upload -r pypi")
