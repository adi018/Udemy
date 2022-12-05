#!/bin/bash

######################################## Exercise 1 #######################################
#FILENAME="/etc/passwd"

#NUM_LINE=0

#while read LINE
#do
#	echo "${NUM_LINE} : ${LINE}"
#	((NUM_LINE++))
#done < ${FILENAME}

######################################## Exercise 1 #######################################

######################################## Exercise 2 #######################################
FILENAME="/etc/passwd"
NUM_LINE=0

echo "How many lines to display?"
read INPUT

while read LINE
do
	echo "${NUM_LINE} : ${LINE}"
	((NUM_LINE++))
	if [ "$NUM_LINE" -eq "${INPUT}" ]
	then 
		break
	fi
done < ${FILENAME}


######################################## Exercise 2 #######################################

######################################## Exercise 3 #######################################

######################################## Exercise 3 #######################################

