

FROM node

# Set the working directory of the container (aka a "home")
WORKDIR /app

# Copy the node package file 
# to the main directory in the container 
# to list the dependencies of the project
COPY package*.json ./

# install the dependencies in the project
RUN npm install
LABEL org.opencontainers.image.source https://github.com/efwoods/docker
# copy the all the files from the local machine directory to the docker container
COPY . .

# expose port of the container located in the index.js file
EXPOSE 4000

# start the application in the container
CMD ["npm", "start"]