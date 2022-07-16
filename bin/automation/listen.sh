# while read line; do echo "What has been passed through the pipe is ${line}"; done
while : ; read line; do eval ${line}; done
