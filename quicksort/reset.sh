
function createlogs {
  while true; do
    # This breaks it pretty quickly due to recursion depth. Too many keys 🤣
    #echo '83.149.9.216 - - [17/May/2015:10:05:03 +0000] "GET '$(uuidgen)' HTTP/1.1" 200 203023 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"' \
    #    >> apache_logs.txt
    sleep 0.00001
  done
}



#createlogs &
cp sample.txt apache_logs.txt
#top -p $(ps -ef | grep python | grep -v grep | awk '{print $2}')

