# Install Docker Engine on Ubuntu

This lab is based on [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)) from official Docker document.

## Prerequisites

### OS requirements

To install Docker Engine, you need the 64-bit version of one of these Ubuntu versions:
- Ubuntu Lunar 23.04
- Ubuntu Kinetic 22.10
- Ubuntu Jammy 22.04 (LTS)
- Ubuntu Focal 20.04 (LTS)

Docker Engine is compatible with x86_64 (or amd64), armhf, arm64, and s390x architctures.

### Uninstall old versions

Before you can install Docker Engine, you must first make sure that any conflicting packages are uninstalled.

Distro maintainers provide an unofficial distributions of Docker packages in APT (Advanced Package Tool, is a free-software user interface that works with core libraries to handle the installation and removal of software on Debian, and Debian-based Linux distributions).

Run the following command to uninstall all conflicting packages

```
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

## Install Docker Engine using the apt repository

Before you install Docker Engine for the first time on a new host machine, you need to set up the Docker repository. Afterwards, you can install and update Docker from the repository.

### Set up the repository

1. Update the `apt` package index and install packages to allow `apt` to use a repository over HTTPS:

```
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
```

2. Add Docker’s official GPG key:

```
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

3. Use the following command to set up the repository:

```
echo \
"deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
"$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### Install Docker Engine

1. Update the `apt` package index:

```
sudo apt-get update
```

2. Install the latest version of Docker Engine, containerd, and Docker Compose.

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

3. Verify that the Docker Engine installation is successful by running the `hello-world` image.

```
sudo docker run hello-world
```

The output will be similar as the following:

```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
719385e32844: Pull complete 
Digest: sha256:a13ec89cdf897b3e551bd9f89d499db6ff3a7f44c5b9eb8bca40da20eb4ea1fa
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

This command downloads a test image and runs it in a container. When the container runs, it prints a confirmation message and exits.

Congratulations! You have now successfully installed and started Docker Engine.

## Linux post-installation steps for Docker Engine
These optional post-installation procedures shows you how to configure your Linux host machine to work better with Docker.

Once Docker has been installed and verified with `hello-world` image, you would consider to further utilize this tool for your application packaging. However, if you try to use its extensive command argument such as `docker image ls` to retrieve all the docker images, you would encounter error message like below:

```
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/images/json": dial unix /var/run/docker.sock: connect: permission denied
```

