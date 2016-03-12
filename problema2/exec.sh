#!/bin/bash
$HADOOP_HOME/bin/hadoop com.sun.tools.javac.Main $1/$2.java
jar cf wc.jar $1/$2*.class
rm -r $output
echo "$HADOOP_HOME/bin/hadoop jar $1/wc.jar $1/$2 $input $output"
$HADOOP_HOME/bin/hadoop jar $1/wc.jar $2 $input $output
