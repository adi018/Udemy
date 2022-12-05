#!/bin/bash

##################################### Exercise 1 ################################
#MESSAGE="Random number is:$RANDOM"
#echo "$MESSAGE"
#logger -p user.info "$MESSAGE"
##################################### Exercise 1 ################################

##################################### Exercise 2 ###############################
function logging(){
	MESSAGE=$@
	SET_MESSAGE="Random number is ${MESSAGE}"
	echo "${SET_MESSAGE}"
	logger -i -p user.info "$SET_MESSAGE"
}

logging $RANDOM
logging $RANDOM
logging $RANDOM
##################################### Exercise 2 ##############################
