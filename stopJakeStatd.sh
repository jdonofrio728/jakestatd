#!/bin/sh

# Author: Jacob D'Onofrio
# Date: May 2014

PID_FILE="jakestatd.pid"

if [ ! -f ${PID_FILE} ]; then
	echo "No pid file found!"
	exit 1
fi

pid=`cat ${PID_FILE}`
kill ${pid}
echo "JakeStatd Stopped"
rm ${PID_FILE}

