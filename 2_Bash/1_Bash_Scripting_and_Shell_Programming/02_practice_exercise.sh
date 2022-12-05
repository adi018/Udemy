#!/bin/bash

######################### Exercise 1 ########################################

#echo "This script will exit with a 0 exit status."

######################### Exercise 1 #######################################

######################### Exercise 2 #######################################
#FILE=$1

#if [ -f $FILE ]
#then 
#	echo "Regular File!"
#	exit 0
#elif [ -d $FILE ]
#then 
#	echo "Directory!"
#	exit 1
#else
#	echo "Other found!"
#	exit 2
#fi

######################### Exercise 2 #######################################

######################### Exercise 3 #######################################
sudo cat /etc/shadow

if [ "$?" -eq "0" ]
then 
	echo "Command succeeded"
	exit 0
else
	echo "Command failed"
	exit 1
fi
######################### Exercise 3 #######################################
