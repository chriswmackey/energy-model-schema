#!/bin/sh
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker build . -t $TRAVIS_REPO_SLUG:$1 
docker push $TRAVIS_REPO_SLUG:$1 
docker push $TRAVIS_REPO_SLUG