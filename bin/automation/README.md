# Automation
## What is it?
This code base is used to call commands on a host machine from a docker container.

## Why is this useful?
This is useful because this allows aliases-like commands to be run without needing to install aliases. It also allows for often used commands to be easily implemented which increases productivity.

## How to build and use 
1. On the host run:
- `docker build -t evdev3/auto .`

- `./listen.sh<myPipe`

- `docker run --rm -v $(pwd):/usr/src/app evdev3/auto py.py>myPipe`

## How this works
"listen.sh" will accept input from the pip "myPipe" and evaluate the commands one at a time. The docker image will use "driver.py" to call the command contained in "command.sh" which will echo a command out to myPipe where it is evaluated by the host machine.

## What's next?
1. Allow the "listen" script to run on build with a build script. 
2. Allow more commands to be accepted or dynamically interpreted by the "driver"
3. Allow the "listen" script to restart after evaluating a command (zero downtime)