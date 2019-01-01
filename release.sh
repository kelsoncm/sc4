#!/usr/bin/env bash

if [ $# -eq 0 ]
  then
    echo "NAME
       release

SYNOPSIS
       ./release.sh [-d|-p|-g] <version>

DESCRIPTION
       Create a new release to ege_django_auth_jwt python package.

OPTIONS
       -d         Deploy to Github and PyPI
       -p         Deploy to PyPI
       -g         Deploy to Github
       <version>  Release version number

EXAMPLES
       o   Build to local usage only:
                  ./release.sh 1.1
       o   Build and deploy to both Github and PyPI:
                  ./release.sh -d 1.1
       o   Build and deploy to PyPI only:
                  ./release.sh -p 1.1
       o   Build and deploy to Github only:
                  ./release.sh -g 1.1
"
fi


create_setup_cfg_file() {
    echo """# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
    name='python_brfied',
    packages=['python_brfied', 'python_brfied.shortcuts', ],
    version='%s',
    download_url='https://github.com/kelsoncm/python_brfied/releases/tag/%s',
    description='Python library specific brazilian validations',
    author='Kelson da Costa Medeiros',
    author_email='kelsoncm@gmail.com',
    url='https://github.com/kelsoncm/python_brfied',
    keywords=['python', 'BR', 'Brazil', 'Brasil', 'model', 'form', 'locale', ],
    install_requires=['pyfwf==0.1.3', 'requests-ftp==0.3.1', 'requests==2.21.0'],
    classifiers=[]
)
""" > setup.py
    docker build -t kelsoncm/python_brfied --force-rm .
    docker run --rm -it -v `pwd`:/src kelsoncm/python_brfied python setup.py sdist
}

if [[ $# -eq 1 ]]
  then
    echo "Build to local usage only. Version: $1"
    echo ""
    create_setup_cfg_file $1
fi

if [[ $# -eq 2 ]] && [[ "$1" == "-d" || "$1" == "-g" || "$1" == "-p" ]]
  then
    echo "Build to local. Version: $2"
    echo ""
    create_setup_cfg_file $2

    if [[ "$1" == "-d" || "$1" == "-g" ]]
      then
        echo ""
        echo "GitHub: Pushing"
        echo ""
        git add setup.py
        git commit -m "Release $2"
        git tag $2
        git push --tags origin master
    fi

    if [[ "$1" == "-d" || "$1" == "-p" ]]
      then
        echo ""
        echo "PyPI Hub: Uploading"
        echo ""
        docker run --rm -it -v `pwd`:/src kelsoncm/python_brfied twine upload dist/python_brfied-$2.tar.gz
    fi
fi

echo ""
echo "Done."
