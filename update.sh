#!/bin/sh

WORK_DIR=/opt/
cd $1
git reset --hard HEAD
git pull
supervisorctl restart $1
