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

## [Linux post-installation steps for Docker Engine](https://docs.docker.com/engine/install/linux-postinstall/)

### Manage Docker as a non-root user
The docker daemon binds to a Unix socket, not a TCP port. By default it’s the `root` user that owns the Unix docket, and other users can only access it using `sudo`. The Docker daemon always runs as the `root` user.

If you don’t want to preface the `docker` command with `sudo`, create a Unix group called `docker` and add users to it. When the Docker daemon starts, it creates a Unix docker accessible by members of the `docker` group. On some Linux distributions, the system automatically creates this group when installing Docker Engine using a package manager, such as Ubuntu. In that case, there is no need for you to manually create the group.

<font color=#FF0000>Warning: The `docker` group grants root-level privileges to the user. For details on how this impacts security in your system, see [Docker Daemon Attack Surface]([https://docs.docker.com/engine/security/#docker-daemon-attack-surface](https://docs.docker.com/engine/security/#docker-daemon-attack-surface)).</font>

#### To create the `docker` group and add your user
1. Create the `docker` group.

```
sudo groupadd docker
```

**Note:** If you are using Ubuntu, the `docker`group would be created once the docker has been installed successfully. So, the `groupadd docker` command will get the output `groupadd: group 'docker' already exists`.

2. Add your user to the `docker` group.
```
sudo usermod -aG docker $USER
```

3. Log out and log back in so that your group membership is re-evaluated. If you are running Linux in a virtual machine, it may be necessary to restart the virtual machine for changes to take effect. You can also run the following command to activate the changes to groups:

```
newgrp docker
```

4. Verify that you can run `docker` commands without `sudo`.
```
docker run hello-world
```

### Configure Docker to start on boot with system
Many modern Linux distributions use `systemd` to manage which services start when the system boots. On Debian and [Ubuntu]([https://ubuntu.com/](https://ubuntu.com/)), the Docker service starts on boot by default. To automatically start Docker and containerd on boot for other Linux distributions using system, run the following commands:

```
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

To check the current docker daemon status, run the following commands:

```
sudo systemctl status docker.service 
```

You should be able to see the docker daemon information as following:
```
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2023-07-11 20:05:33 CST; 4min 3s ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 701 (dockerd)
      Tasks: 9
     Memory: 99.7M
     CGroup: /system.slice/docker.service
             └─701 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
```

Now we can re-run the `docker image ls` for confirmation.
```
docker image ls

REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
hello-world   latest    9c7a54a9a43c   2 months ago   13.3kB
```
