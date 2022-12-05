#!/bin/bash

#################################### Exercise 1 ##############################
#function file_count(){
#	local NUM_OF_FILES=$( ls $1 -l | wc -l )
#	echo "Number of files in path $1 : ${NUM_OF_FILES}"
#}

#file_count
#################################### Exercise 1 ##############################

#################################### Exercise 2 ##############################

function file_count(){
	local DIRECTORY=$1
	NUM_FILES=$(ls $DIRECTORY -l | wc -l)
	echo "$DIRECTORY has files: $NUM_FILES"
}

file_count /etc
file_count /var
file_count /usr/bin

#################################### Exercise 2 ###############################

