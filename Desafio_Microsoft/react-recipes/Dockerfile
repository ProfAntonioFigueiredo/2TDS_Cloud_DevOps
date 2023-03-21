# From base image node
FROM node

# Create app directory
RUN mkdir -p react-recipes && cd react-recipes
WORKDIR react-recipes
RUN mkdir src
RUN mkdir public
RUN touch package.json
echo "{}" > package.json

# Copying all the files from your file system to container file system
COPY package.json . /react-recipes/src
COPY snowpack.config.js /react-recipes/src

# Install all dependencies
CMD ["npm","install"]
CMD ["npm","install","--save-de snowpack"]
CMD ["npm","install","react"]
CMD ["npm","install","dom"]

# Copy other files too
COPY ./ .

# Expose the port
EXPOSE 8080

# Command to run app when intantiate an image
CMD ["npm","start"]

#docker build -t mslearn-react .

#docker container run -d -p 8080:8080 --name react_snowpack react_snowpack