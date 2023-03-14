# From base image node
FROM node:16

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copying all the files from your file system to container file system
COPY package.json .

# Install all dependencies
RUN npm install

# Copy other files too
COPY ./ .

# Expose the port
EXPOSE 9000

# Command to run app when intantiate an image
CMD ["npm","start"]

#docker build -t nodehelloworld .

#docker container run -d -p 9000:9000 --name MyfirstApphello nodehelloworld