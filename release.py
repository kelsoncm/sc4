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
    name='python_brfied',
    packages=['python_brfied', ],
    package_dir={'python_brfied': 'python_brfied'},
    version='%s',
    download_url='https://github.com/kelsoncm/python_brfied/releases/tag/%s',
    description='Python library specific brazilian validations',
    author='Kelson da Costa Medeiros',
    author_email='kelsoncm@gmail.com',
    url='https://github.com/kelsoncm/python_brfied',
    keywords=['python', 'BR', 'Brazil', 'Brasil', 'model', 'form', 'locale', ],
    classifiers=[]
)
""" % (args.version, args.version,))

os.system("git add setup.py")
os.system("git commit -m 'Release %s'" % args.version)
os.system("git tag %s" % args.version)
os.system("git push --tags origin master")
os.system("python setup.py sdist")
os.system("twine upload dist/python_brfied-%s.tar.gz" % args.version)
# os.system("python setup.py sdist upload -r pypi")

