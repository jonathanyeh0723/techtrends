## Introduction 
- Containers are a form of operating system virtualization. However, containers do not contain operating system images. This makes them more lightweight and portable, with significantly less overhead.

-  A container includes all the necessary executables, binary codes, libraries, and configuration files. Therefore, it can be run anything from a small microservice or software process to a larger application.

- In large-scale application deployments, multiple containers may be deployed as one or more container clusters. Such clusters might be managed by a container orchestrator such as Docker Swarm, Kubernetes.

In a nutshell, using containers could be more streamlined to build, test, and deploy the applications on multiple environments, from a developer’s local laptop to an on-premises data center and even the cloud.

## Build

Hierarchy
```
.
├── docker_commands
├── Dockerfile
├── references
└── third-party-programs-docker-dev.txt

0 directories, 4 files
```

To build the image, run
```
docker build . --build-arg package_url=https://storage.openvinotoolkit.org/repositories/openvino/packages/2023.0/linux/l_openvino_toolkit_ubuntu20_2023.0.0.10926.b4452d56304_x86_64.tgz -t ov-2023.0.0-dev:latest
```

Reference logs:
```
[+] Building 93.1s (19/50)                                                                                                                            
[+] Building 1782.6s (51/51) FINISHED                                                                                                                 
 => [internal] load build definition from Dockerfile                                                                                             0.0s
 => => transferring dockerfile: 14.52kB                                                                                                          0.0s
 => [internal] load .dockerignore                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                  0.0s
 => [internal] load metadata for docker.io/library/ubuntu:22.04                                                                                  2.5s
 => [auth] library/ubuntu:pull token for registry-1.docker.io                                                                                    0.0s
 => [internal] load build context                                                                                                                0.0s
 => => transferring context: 162.34kB                                                                                                            0.0s
 => [ov_base  1/32] FROM docker.io/library/ubuntu:22.04@sha256:0bced47fffa3361afa981854fcabcd4577cd43cebbb808cea2b1f33a3dd7f508                  1.2s
 => => resolve docker.io/library/ubuntu:22.04@sha256:0bced47fffa3361afa981854fcabcd4577cd43cebbb808cea2b1f33a3dd7f508                            0.0s
 => => sha256:0bced47fffa3361afa981854fcabcd4577cd43cebbb808cea2b1f33a3dd7f508 1.13kB / 1.13kB                                                   0.0s
 => => sha256:b060fffe8e1561c9c3e6dea6db487b900100fc26830b9ea2ec966c151ab4c020 424B / 424B                                                       0.0s  => => sha256:5a81c4b8502e4979e75bd8f91343b95b0d695ab67f241dbed0d1530a35bde1eb 2.30kB / 2.30kB                                                   0.0s
 => => sha256:3153aa388d026c26a2235e1ed0163e350e451f41a8a313e1804d7e1afb857ab4 29.53MB / 29.53MB                                                 0.6s
 => => extracting sha256:3153aa388d026c26a2235e1ed0163e350e451f41a8a313e1804d7e1afb857ab4                                                        0.5s
 => CACHED https://storage.openvinotoolkit.org/repositories/openvino/packages/2023.0/linux/l_openvino_toolkit_ubuntu20_2023.0.0.10926.b4452d563  1.2s
 => [ov_base  2/32] RUN sed -ri -e 's@^UMASK[[:space:]]+[[:digit:]]+@UMASK 000@g' /etc/login.defs &&  grep -E "^UMASK" /etc/login.defs && usera  0.3s
 => [base 2/8] RUN apt-get update &&     apt-get install -y --no-install-recommends curl tzdata ca-certificates &&     rm -rf /var/lib/apt/lis  19.6s
 => [ov_base  3/32] RUN mkdir /opt/intel                                                                                                         0.3s 
 => [base 3/8] WORKDIR /tmp/openvino_installer                                                                                                   0.0s 
 => [base 4/8] ADD https://storage.openvinotoolkit.org/repositories/openvino/packages/2023.0/linux/l_openvino_toolkit_ubuntu20_2023.0.0.10926.b  0.3s 
 => [base 5/8] RUN useradd -ms /bin/bash -G users openvino                                                                                       0.2s 
 => [base 6/8] RUN tar -xzf "/tmp/openvino_installer"/*.tgz &&     OV_BUILD="$(find . -maxdepth 1 -type d -name "*openvino*" | grep -oP '(?<=_)  1.2s 
 => [base 7/8] RUN rm -rf /opt/intel/openvino/.distribution && mkdir /opt/intel/openvino/.distribution &&     touch /opt/intel/openvino/.distri  0.3s 
 => [opencv 1/7] RUN apt-get update;     apt-get install -y --no-install-recommends         git         python3-dev         python3-pip        162.8s 
 => [ov_base  4/32] COPY --from=base /opt/intel/ /opt/intel/                                                                                     0.2s 
 => [ov_base  5/32] WORKDIR /thirdparty                                                                                                          0.0s 
 => [ov_base  6/32] RUN apt-get update &&     dpkg --get-selections | grep -v deinstall | awk '{print $1}' > base_packages.txt  &&     apt-get  12.2s 
 => [ov_base  7/32] RUN apt-get update && apt-get reinstall -y ca-certificates && rm -rf /var/lib/apt/lists/* && update-ca-certificates         13.2s
 => [ov_base  8/32] RUN apt-get update &&     apt-get install -y --no-install-recommends ${LGPL_DEPS} &&     ${INTEL_OPENVINO_DIR}/install_dep  53.8s
 => [ov_base  9/32] RUN curl -L -O  https://github.com/oneapi-src/oneTBB/releases/download/v2021.9.0/oneapi-tbb-2021.9.0-lin.tgz &&     tar -xz  2.1s
 => [ov_base 10/32] WORKDIR /opt/intel/openvino/licensing                                                                                        0.0s
 => [ov_base 11/32] RUN if [ "no" = "no" ]; then         echo "This image doesn't contain source for 3d party components under LGPL/GPL license  0.2s
 => [ov_base 12/32] RUN python3.10 -m pip install --upgrade pip                                                                                  1.9s
 => [ov_base 13/32] WORKDIR /opt/intel/openvino                                                                                                  0.0s 
 => [ov_base 14/32] RUN apt-get update && apt-get install -y --no-install-recommends cmake make git && rm -rf /var/lib/apt/lists/* &&     if   285.4s 
 => [opencv 2/7] RUN python3 -m pip install --no-cache-dir numpy==1.23.1                                                                         8.1s 
 => [opencv 3/7] WORKDIR /opt/repo                                                                                                               0.0s 
 => [opencv 4/7] RUN git clone https://github.com/opencv/opencv.git --depth 1 -b 4.7.0                                                          34.6s 
 => [opencv 5/7] WORKDIR /opt/repo/opencv/build                                                                                                  0.1s 
 => [opencv 6/7] RUN . "/opt/intel/openvino"/setupvars.sh;     cmake -G Ninja     -D BUILD_INFO_SKIP_EXTRA_MODULES=ON     -D BUILD_EXAMPLES=O  758.8s 
 => [ov_base 15/32] WORKDIR /opt/intel/openvino/licensing                                                                                        0.0s 
 => [ov_base 16/32] COPY third-party-programs-docker-dev.txt /opt/intel/openvino/licensing                                                       0.0s 
 => [opencv 7/7] WORKDIR /opt/repo/opencv/build/install                                                                                          0.1s
 => [ov_base 17/32] COPY --from=opencv /opt/repo/opencv/build/install /opt/intel/openvino/extras/opencv                                          0.1s
 => [ov_base 18/32] RUN  echo "export OpenCV_DIR=/opt/intel/openvino/extras/opencv/cmake" | tee -a "/opt/intel/openvino/extras/opencv/setupvars  0.2s
 => [ov_base 19/32] RUN apt-get update && apt-get install -y --no-install-recommends opencl-headers ocl-icd-opencl-dev && rm -rf /var/lib/apt/  12.0s
 => [ov_base 20/32] RUN apt-get update &&     apt-get install libopencv-dev -y                                                                 145.9s
 => [ov_base 21/32] WORKDIR /opt/intel/openvino/samples/cpp                                                                                      0.0s
 => [ov_base 22/32] RUN ./build_samples.sh -b build &&     cp -R build/intel64/Release samples_bin &&     rm -Rf build                          18.3s
 => [ov_base 23/32] RUN git clone https://github.com/openvinotoolkit/open_model_zoo &&     sed -i '/opencv-python/d' open_model_zoo/demos/comm  82.8s
 => [ov_base 24/32] RUN apt-get update &&     apt-get install -y --no-install-recommends ocl-icd-libopencl1 &&     apt-get clean ;     rm -rf /  2.9s
 => [ov_base 25/32] RUN mkdir /tmp/gpu_deps && cd /tmp/gpu_deps &&     curl -L -O https://github.com/intel/compute-runtime/releases/download/2  13.0s
 => [ov_base 26/32] RUN apt-get update &&     apt-get autoremove -y gfortran &&     rm -rf /var/lib/apt/lists/*                                  9.3s
 => [ov_base 27/32] WORKDIR /opt/intel/openvino                                                                                                  0.0s
 => [ov_base 28/32] RUN apt-get update &&     apt-get install curl vim git -y                                                                   14.7s
 => [ov_base 29/32] RUN python3.10 -m pip install matplotlib                                                                                     4.8s
 => [ov_base 30/32] RUN python3.10 -m pip install pyqt5                                                                                         71.1s
 => [ov_base 31/32] RUN git clone --recurse-submodules https://github.com/openvinotoolkit/open_model_zoo.git                                   405.1s
 => exporting to image                                                                                                                          12.2s
 => => exporting layers                                                                                                                         12.2s
 => => writing image sha256:ddd270df67541a178b8e93899e8a512e5f50e69a01c7ac3898dad7949a8c6668                                                     0.0s
 => => naming to docker.io/library/ov-2023.0.0-dev:latest             
```

Checking the image built by running `docker image ls`
```
REPOSITORY                TAG       IMAGE ID       CREATED          SIZE
ov-2023.0.0-dev           latest    ddd270df6754   15 minutes ago   6.01GB
```

For more information about building and running the image, refer to `https://github.com/openvinotoolkit/docker_ci`.


## Test

Default run the container with interactive mode:
```
docker run --interactive --tty ov-2023.0.0-dev:latest
```

Note currently only the `CPU` plugin is available, we can check by running `python3` with following command:
```
Python 3.10.6 (main, May 29 2023, 11:10:38) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from openvino.runtime import Core
>>> core = Core()
>>> core.available_devices
['CPU', 'GNA']
>>> 
```

To use `GPU` accelerator, we need to add the argument `--device /dev/dri:/dev/dri` like this:
```
docker run --interactive --tty --device /dev/dri:/dev/dri ov-2023.0.0-dev:latest
```

Inside the container, running `python3` again for plugins confirmation:
```
Python 3.10.6 (main, May 29 2023, 11:10:38) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from openvino.runtime import Core
>>> core = Core()
>>> devices = core.available_devices
>>> for device in devices:
...     full_device_name = core.get_property(device, "FULL_DEVICE_NAME")
...     print(device, full_device_name)
... 
CPU 11th Gen Intel(R) Core(TM) i7-1185G7 @ 3.00GHz
GNA GNA_SW
GPU Intel(R) Iris(R) Xe Graphics (iGPU)
>>> 
```

Now the `GPU` is ready for inference.

In real-world practical use cases, it's more convenient to add volume for easier data usage and webcam for live streaming. For example:<br>
- Bind the local `/home/<user>/Downloads` directory to `/mnt` the container directory: `--volume /home/cnai/Downloads:/mnt`
- Link the USB video camera: `--device /dev/video0:/dev/video0`

Putting all together:
```
docker run --interactive --tty --device /dev/dri:/dev/dri --volume /home/cnai/Downloads:/mnt --device /dev/video0:/dev/video0 ov-2023.0.0-dev:latest
```
