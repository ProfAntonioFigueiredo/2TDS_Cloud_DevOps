# From base image node
FROM node

# Create app directory
RUN mkdir -p /mslear/code/0-starter/
WORKDIR /mslear/code/0-starter/

# Copying all the files from your file system to container file system
COPY package.json . /mslear/code/0-starter/
COPY snowpack.config.js /mslear/code/0-starter/

#RUN cd mslearn-react/code/0-starter

# Install all dependencies
CMD ["npm","install"]
CMD ["npm","install","--save-de snowpack"]
CMD ["npm","install","react"]
CMD ["npm","install","dom"]

# Copy other files too
COPY ./ .

# Expose the port
#EXPOSE 8080

# Command to run app when intantiate an image
CMD ["npm","start"]

#docker build -t mslearn-react .

#docker container run -d -p 8080:8080 --name react_snowpack react_snowpack