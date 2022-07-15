# node-docker
Simple node and express docker 

## building an image
- `docker build -t eveng1neer/simple-backend .`
  - '-t' to name your image
  - 'build' to build the image
- `docker images`
  - list images
- `docker run -p 4000:4000 eveng1neer/simple-backend`
  - create a container from the image and map the port of the host machine to the port of the container (host-machine-port:exposed-container-port)
- `docker ps`
  - list the running containers
- `docker stop [container ID]`
  - stops the container using the container ID
- `docker push`
  - push the name of the image to docker hub
- `docker pull`
  - pull a docker image from the docker hub
