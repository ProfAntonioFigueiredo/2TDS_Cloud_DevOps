Install Docker
Enable all the required repositories. To do this you are going to need the yum-utils package.

dnf install -y dnf-utils zip unzip
dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo

Install Docker.

dnf remove -y runc
dnf install -y docker-ce --nobest

Finish Docker Setup
Enable and start the Docker service.

# systemctl enable docker.service
# systemctl start docker.service
You can get information about docker using the following commands.

# systemctl status docker.service
# docker info
# docker version

Docker Commands as Non-Root User
Docker commands run as the "root" user. You have three choices when if comes to running docker commands.

Run the docker commands from the root user.
Allow another user to perform "sudo" on the docker command, so all commands are run using "sudo docker ...".
Create a group called docker and assign that to the user you want to run docker commands from. The documentation says, "Warning: The docker group grants privileges equivalent to the root user", so we should avoid this.
In this case we want to run the docker commands from a user called "docker_user", so we add an entry in the "/etc/sudoers" file and use an alias in the user's ".bash_profile" file so we don't have to keep typing the "sudo" command.

# useradd docker_user
# echo "docker_user  ALL=(ALL)  NOPASSWD: /usr/bin/docker" >> /etc/sudoers
# echo "alias docker=\"sudo /usr/bin/docker\"" >> /home/docker_user/.bash_profile
# su - docker_user
$ docker ps