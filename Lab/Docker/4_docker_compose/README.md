# Docker Compose Sample - Prometheus & Grafana

## Introduction

- **What:** According to [Docker Compose from Official Docker Docs](https://docs.docker.com/compose/), it is a took that was developed to help define and share multi-container applications. With Docker Compose, we can create a YAML file to define the services and with a single command can spin everything up or tear it all down.

*The big advantage is that you can define your application stack in a file, keep it at the root of your project repo (it is now version controlled), and easily enable someone else to contribute to your project.*

- **How:** If you installed Docker Desktop for Windows, Mac, or Linux you already have Docker Compose! Or if you prefer to proceed with standalone installations, you can check out [install the Compose plugin](https://docs.docker.com/compose/install/linux/).

For example, if you’re a Linux user in Ubuntu or Debian distribution, and would like to install using the repository, you will need to first set up the repository. Once it’s done, you can update the package index and install the latest version of Docker Compose.

```
$ sudo apt-get update
$ sudo apt-get install docker-compose-plugin
```

After installation, you should be able to run the following and see version information.
```
$ docker compose version
```

Example output
```
Docker Compose version v2.19.1
```

- **Why:** With Docker Compose, you can replace multiple Docker build and Docker run commands with just one configuration file. You can easily have all the containerized services and applications up or down with a simple, set of orchestration commands, and build all necessary images as well if required.

The `docker-compose` mainly solve the problem of annoying repetition of long commands. You don’t really need to use it, but that case you will have to execute every single commands manually otherwise.

On the other hand, although some commands could be replaced by `docker-compose`, but it is not all! For instance, you would still need to use `docker push` to push the image to a public registry like `Docker Hub`. So, we should flexibly use these commands together.

In addition, by using `Docker Compose` a default network would be created for all the composed containers. Each container for a service joins the default network and is both reachable by other containers on that network, and discoverable by them at a hostname identical to the container name.

For more information, refer to https://docs.docker.com/compose/install/.

**Project Hierarchy**
```
.
├── compose.yml
├── grafana
│   └── grafana.yml
├── prometheus
│   └── prometheus.yml
└── README.md

2 directories, 4 files
```

## Deploy with docker compose
Running the following command to have the docker compose up:
```
✔ Network 4_docker_compose_default  Created                                                                                                          0.1s 
 ✔ Container prometheus              Started                                                                                                          1.0s 
 ✔ Container grafana                 Started                                                                                                          0.9s 
```

Checking the pulled images:
```
REPOSITORY        TAG       IMAGE ID       CREATED        SIZE
grafana/grafana   latest    d09b57894d6e   11 days ago    329MB
prom/prometheus   latest    3b907f5313b7   12 days ago    245MB
```

Using `docker ps` to confirm that two containers are running and the correspondent port mapping as below:
```
CONTAINER ID   IMAGE             COMMAND                  CREATED         STATUS         PORTS                                       NAMES
502c12861643   prom/prometheus   "/bin/prometheus --c…"   4 minutes ago   Up 4 minutes   0.0.0.0:9090->9090/tcp, :::9090->9090/tcp   prometheus
1e62fc5b29ee   grafana/grafana   "/run.sh"                4 minutes ago   Up 4 minutes   0.0.0.0:3000->3000/tcp, :::3000->3000/tcp   grafana
```

Now you can navigate to `http://localhost:3000` in your web browser and use the login credentials specified in the compose file to access Grafana. In this case:
```
username:   devops_admin	
password:   prometheus_grafana	
```
It is already configured with prometheus as the default datasource. Check out `compose.yml` for more information in detail.

![grafana_login](./resources/grafana_login.png)
