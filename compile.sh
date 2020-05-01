#! /bin/bash

g++ $1
if [[ $? == 0 ]];
then
    echo 'Input'
    ./a.out
else
	echo 'compilation error'
fi
