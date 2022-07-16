./listen.sh<myPipe
docker run --rm -v $(pwd):/usr/src/app evdev3/auto driver.py>myPipe