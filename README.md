# TechTreds Web Application in CI/CD Pipeline

[![Project_Version](https://img.shields.io/badge/version-2023.1-blue)](PROJECT)
[![Method](https://img.shields.io/badge/method-CI%2FCD-red)](CICD)
[![Build](https://img.shields.io/badge/build-passing-success)](BUILD)
[![Test](https://img.shields.io/badge/test-passing-success)](TEST)
[![Package](https://img.shields.io/badge/docker%20package-passing-success)](PACKAGE)
[![K8s](https://img.shields.io/badge/kubernetes%20deploy-passing-success)](K8s)
[![Delivery](https://img.shields.io/badge/delivery-passing-success)](DELIVERY)
[![Apache License Version 2.0](https://img.shields.io/badge/license-Apache%202.0-blueviolet)](LICENSE)

**TechTrends** is an online website used as a news sharing platform, that enables consumers to access the latest news within the cloud-native ecosystem.

In addition to accessing the available articles, readers are able to create new media articles and share them with the wider community.

This is **NOT** only a Flask web app. It is an end-to-end [CI/CD](https://www.redhat.com/en/topics/devops/what-is-ci-cd) (Build, Test, Package, Delivery) showcase.
-	Using [Python](https://www.python.org/) as backend programming to construct a frontend architecture.
-	Leveraging [Docker](https://www.docker.com/) to package the application.
-	Automating the CI (Continuous Integration) process with [GitHub Actions](https://github.com/features/actions).
-	Deploying the app by conducting [Kubernetes](https://kubernetes.io/) declarative manifests.
-	Templating with [Helm](https://helm.sh/) for convenient distinguishing the different development phase (staging, production).
-	Automating the Continuous Delivery release with [ArgoCD](https://argo-cd.readthedocs.io/en/stable/). 

:moyai::moyai::moyai:TechTrends web application demo 
![demo](./resources/app_demo.gif)


## Run 

To run this application there are 2 steps required:

1. Initialize the database by using the `python init_db.py` command. This will create or overwrite the `database.db` file that is used by the web application.
2.  Run the TechTrends application by using the `python app.py` command. The application is running on port `3111` and you can access it by querying the `http://127.0.0.1:3111/` endpoint.
