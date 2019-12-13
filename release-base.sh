#!/usr/bin/env bash
FULL_IMAGE_NAME="kelsoncm/sc4"

if [ $# -eq 0 ]; then
  echo ''
  echo 'NAME '
  echo '       release'
  echo 'SYNOPSIS'
  echo '       ./release.sh [-l|-g|-p|-a] <version>'
  echo 'DESCRIPTION'
  echo '       Create a new release $PROJECT_NAME image.'
  echo 'OPTIONS'
  echo '       -l         Build only locally'
  echo '       -g         Push to Github'
  echo '       -p         Registry on PyPi'
  echo '       -a         Push and registry on Github'
  echo '       <version>  Release version number'
  echo 'EXAMPLES'
  echo '       o   Build a image to local usage only:'
  echo '                  ./release.sh -l 1.0'
  echo '       o   Build and push to GitHub:'
  echo '                  ./release.sh -g 1.0'
  echo '       o   Build and registry on PyPi:'
  echo '                  ./release.sh -p 1.0'
  echo '       o   Build, push to Guthub and registry on PyPi:'
  echo '                  ./release.sh -a 1.0'
  echo "LAST TAG: $(git tag | grep $PROJECT_NAME | tail -1 )"
  exit
fi


create_setup_cfg_file() {
  sed "s/lib_version/$1/g" $ROOT_DIR/$PROJECT_NAME/setup.template > $ROOT_DIR/$PROJECT_NAME/setup.py 
}

build_docker() {
  echo "Build local version $FULL_IMAGE_NAME:latest"
  echo ""
  time docker build -t $FULL_IMAGE_NAME:latest --force-rm .
}

lint_project() {
  time docker run --rm -it  -v `pwd`/$PROJECT_NAME:/src $FULL_IMAGE_NAME:latest sh -c 'flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics && flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics'
}

test_project() {
  time docker run --rm -it  -v `pwd`/$PROJECT_NAME:/src $FULL_IMAGE_NAME:latest sh -c 'coverage run -m unittest tests/test_* && coverage report -m && python setup.py sdist' 
}

build_project() {
  time docker run --rm -it  -v `pwd`/$PROJECT_NAME:/src $FULL_IMAGE_NAME:latest sh -c 'python setup.py sdist' 
}

create_setup_cfg_file $2
build_docker
lint_project
test_project
build_project

if [[ "$1" == "-g" || "$1" == "-a" ]]
then
  echo ""
  echo "GitHub: Pushing"
  echo ""
  git add setup.py
  git commit -m "Release $PROJECT_NAME-v$2"
  git tag $PROJECT_NAME-v$2
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
