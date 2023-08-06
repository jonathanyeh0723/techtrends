# Docker Compose Sample - Prometheus & Grafana

## Introduction

- What

- Why

- How

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
