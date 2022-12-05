#!/bin/bash

################################### Exericse 1 ######################################
#DATE=$(date +%F)
#for FILE in *.jpg
#do 
#	mv $FILE ${DATE}-${FILE}
#	echo "$FILE renamed to ${DATE}-${FILE}"
#done 
################################### Exericse 1 ######################################


################################### Exericse 2 ######################################
DATE=$(date +%F)

echo "Please enter the file extension:"
read EXTENSION

echo "Please enter the prefix:(Press ENTER for $DATE)"
read PREFIX

SIZE=${#PREFIX}
for NAME in *.$EXTENSION
do
	if [ "$SIZE" -eq "0" ]
	then
		echo "Renaming $NAME to ${DATE}-${NAME}"
		mv $NAME ${DATE}-${NAME}
	else
		echo "Renaming $NAME to ${PREFIX}${NAME}"
		mv $NAME ${PREFIX}${NAME}
	fi
done
################################### Exericse 2 ######################################

################################### Exericse 3 ######################################

################################### Exericse 3 ######################################

################################### Exericse 4 ######################################

################################### Exericse 4 ######################################

