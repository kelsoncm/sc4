#!/usr/bin/env bash

PROJECT_NAME="pyatalhos"
FULL_IMAGE_NAME="kelsoncm/$PROJECT_NAME"

if [ $# -eq 0 ]
  then
    echo "
NAME
       release
SYNOPSIS
       ./release.sh [-l|-g|-p|-a] <version>
DESCRIPTION
       Create a new release $PROJECT_NAME image.
OPTIONS
       -l         Build only locally
       -g         Push to GitLab
       -p         Registry on GitLab
       -a         Push and registry on GitLab
       <version>  Release version number
EXAMPLES
       o   Build a image to local usage only:
                  ./release.sh -b 1.0
       o   Build and push to GitHub:
                  ./release.sh -g 1.0
       o   Build and registry on GitHub:
                  ./release.sh -p 1.0
       o   Build, push and registry on GitHub:
                  ./release.sh -a 1.0
LAST TAG: $(git tag| tail -1)"
    exit
fi


create_setup_cfg_file() {
    echo """# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
    name='pyatalhos',
    packages=['pyatalhos', ],
    version='$1',
    download_url='https://github.com/kelsoncm/pyatalhos/releases/tag/$1',
    description='Python library specific brazilian validations',
    author='Kelson da Costa Medeiros',
    author_email='kelsoncm@gmail.com',
    url='https://github.com/kelsoncm/pyatalhos',
    keywords=['python', 'BR', 'Brazil', 'Brasil', 'model', 'form', 'locale', ],
    install_requires=['pyfwf==0.1.3', 'requests-ftp==0.3.1', 'requests==2.21.0'],
    classifiers=[]
)
""" > setup.py

    echo "Build local version $FULL_IMAGE_NAME:$1"
    echo ""
    docker build -t $FULL_IMAGE_NAME:latest --force-rm .
    docker run --rm -it -v `pwd`:/src $FULL_IMAGE_NAME:latest sh -c 'coverage run -m unittest tests/test_* && coverage report -m && python setup.py sdist'
}

create_setup_cfg_file $2

if [[ "$1" == "-g" || "$1" == "-a" ]]
then
  echo ""
  echo "GitHub: Pushing"
  echo ""
  git add setup.py
  git commit -m "Release $2"
  git tag $2
  git push --tags origin master
fi

if [[ "$1" == "-p" || "$1" == "-a" ]]
then
  echo ""
  echo "PyPI Hub: Uploading"
  echo ""
  docker login
  docker run --rm -it -v `pwd`:/src $FULL_IMAGE_NAME:latest twine upload dist/$PROJECT_NAME-$2.tar.gz
fi

echo ""
echo "Done."
