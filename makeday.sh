#!/bin/bash
# create dayXX folder and files

# print helpFunction if arg is empty
helpFunction()
{
   echo ""
   echo "please provide a directory name"
   echo ""
   echo "usage: bash ./makeDay.sh dayXX"
   exit 1
}

if [ -z "$1" ]
then
   helpFunction
fi

DIR=$1

# make directory
mkdir $DIR
# copy from day00
cp day00/input.txt $DIR/
cp day00/*.py $DIR/
# create part2 duplicate
cp day00/part1.py $DIR/part2.py
