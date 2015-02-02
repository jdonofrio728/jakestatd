#!/bin/bash

# Author: Jacob D'Onofrio
# Date: May 2014

if [ -z ${JAVA_HOME} ]; then
	echo "JAVA_HOME is not defined!"
	exit 1
fi

export CLASSPATH="./lib/*:${JAVA_HOME}/lib/tools.jar"
nohup ${JAVA_HOME}/bin/java -Dfile.encoding="UTF-8" -Djava.security.policy="tools.policy" org.python.util.jython jakestatd.py $* 2>&1 1>my.log &
echo $! > jakestatd.pid

