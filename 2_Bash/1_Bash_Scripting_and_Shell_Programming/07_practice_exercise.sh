#!/bin/bash
INPUT=$1
cd /hms/installs/mongod/mongodb-linux-x86_64-2.6.0/bin
case $INPUT in
start)
       ./mongod -f ../../mongod.conf &
       echo "Mongodb server Start"
       ;;
stop)
      PID_ID=$(ps -ef | grep mongo | cut -d" " -f3 | sed '1!d')
      kill $PID_ID
if [ $? -eq '0']
      echo "Mongodb server Stop"
      ;;
*)
     echo "Error input"
     ;;
esac
