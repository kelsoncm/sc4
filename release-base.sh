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

OPTION=$1
VERSION=$2

create_setup_cfg_file() {
  printf "\n\nCREATE setup.cfg file\n"
  sed "s/lib_version/$1/g" $ROOT_DIR/$PROJECT_NAME/setup.template > $ROOT_DIR/$PROJECT_NAME/setup.py 
}

build_docker() {
  printf "\n\nBUILD local version $FULL_IMAGE_NAME:latest\n"
  docker build -t $FULL_IMAGE_NAME:latest --force-rm .
}

lint_project() {
  printf "\n\nLINT project $PROJECT_NAME-v$VERSION\n"
  docker run --rm -it  -v `pwd`/$PROJECT_NAME:/src $FULL_IMAGE_NAME:latest sh -c 'flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics && flake8 . --count  --max-complexity=10 --max-line-length=127 --statistics'
}

test_project() {
  printf "\n\nTEST project $PROJECT_NAME-v$VERSION\n"
  docker run --rm -it  -v `pwd`/$PROJECT_NAME:/src $FULL_IMAGE_NAME:latest sh -c 'coverage run -m unittest tests/test_* && echo $? && coverage report -m' 
}

build_project() {
  printf "\n\nBUILD project $PROJECT_NAME-v$VERSION\n"
  docker run --rm -it  -v `pwd`/$PROJECT_NAME:/src $FULL_IMAGE_NAME:latest sh -c 'python setup.py sdist' 
}


push_to_github() {
  if [[ "$OPTION" == "-g" || "$OPTION" == "-a" ]]
  then
    printf "\n\n\GITHUB: Pushing\n"
    git add $PROJECT_NAME/setup.py \
    && git commit -m "Release $PROJECT_NAME-v$VERSION"
    #  \
    # && git tag $PROJECT_NAME-v$VERSION \
    # && git push --tags origin master
  fi
}

send_to_pypi() {
  if [[ "$OPTION" == "-p" || "$OPTION" == "-a" ]]
  then
    printf "\n\n\PYPI: Uploading\n"
    docker run --rm -it -v `pwd`/$PROJECT_NAME:/src $FULL_IMAGE_NAME:latest twine upload dist/$PROJECT_NAME-$VERSION.tar.gz
  fi
}

create_setup_cfg_file $VERSION \
&& build_docker \
&& lint_project \
&& test_project \
&& build_project \
&& push_to_github \
&& send_to_pypi

echo $?
echo ""
echo "Done."
