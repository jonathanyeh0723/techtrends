# Docker For Application Packaging

## Why Container and Container Orchestration?

Once a team has developed an application, the next phase is to move on to the release process. This includes techniques for:
 - service packaging 
 - containerization
 - distribution

The end result of a product release is represented by a service that is deployed in a production environment and can be accessed by consumers.

## Transitions from VMs to Containers

### VMs
In the past years, VMs (Virtual Machines) were the main mechanism to host an application. VMs encapsulate the code, configuration files, and dependencies necessary to execute the application.

![fig_1](./figures/multiple_apps_hosted_on_vms.png)

In essence, a VM is composed of an operating system (OS) with a set of pre-installed libraries and packages. During execution, an application utilizes an OS filesystem, resources, and packages.

A set of VMs is managed through hypervisor. A hypervisor provides the virtualization of the infrastructure which is composed of physical servers. As a result, a hypervisor is capable of creating, configuring, and managing multiple VMs on the available servers. For example, we are able to running applications A, B, and C on 3 separate VMs.

The utilization of VMs introduced standardization in infrastructure provisioning, in association with efficient use of available infrastructure. Instead of running an application per server, a hypervisor enables multiple VMs to run at the same time to host multiple applications. However, there is one downside to this mechanism: it is not efficient enough. For example, applications A, B, and C uses the same Operating System. Replicating an OS consumes a lot of resources, and the more applications we run the more space we allocate to the replication of the operating systems alone.
