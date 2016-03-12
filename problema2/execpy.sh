$HADOOP_HOME/bin/hadoop jar contrib/streaming/hadoop-*streaming*.jar \
-file $code/mapper_wc.py    -mapper $code/mapper_wc.py \
-file $code/reducer.py   -reducer $code/reducer.py \
-input $input/* -output $output
