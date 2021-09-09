mv apache_logs.txt sample.txt
mv sample.txt apache_logs.txt
top -p $(ps -ef | grep python | grep -v grep | awk '{print $2}')