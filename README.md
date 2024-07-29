[ ![Docker](https://img.shields.io/badge/Docker%20Image-309DEE?style=for-the-badge&logo=docker&logoColor=white) ](https://hub.docker.com/r/jack20191124/graphgpt)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/QubitPi/graphgpt-docker/ci-cd.yml?branch=master&logo=github&style=for-the-badge)](https://github.com/QubitPi/graphgpt-docker/actions/workflows/ci-cd.yml)
![Last Commit](https://img.shields.io/github/last-commit/QubitPi/graphgpt-docker/master?logo=github&style=for-the-badge)
[![Apache License Badge]][Apache License, Version 2.0]

GraphGPT Docker Image
=====================

This image can be used for quick provisioning of [GraphGPT](https://huggingface.co/spaces/QubitPi/graphgpt) in the case
of

1. No VPN access to HuggingFace
2. Local Dev/Testing

Getting Image
-------------

### Docker Hub

We can pull the image from [my docker hub](https://hub.docker.com/r/jack20191124/graphgpt/):

```console
docker pull jack20191124/graphgpt
```

### GitHub

We could also build the image from [GitHub repository](https://github.com/QubitPi/graphgpt-docker):

```console
git clone https://github.com/QubitPi/graphgpt-docker.git
cd jupiter
docker build -t jack20191124/graphgpt .
```

Standing Up a Container
-----------------------

When image is on our machine (either by pulling or building), we can spin up a GraphGPT instance by

```console
docker run -d --name=graphgpt -it -p 7860:7860 jack20191124/graphgpt
```

* **name=graphgpt**: the container is named "graphgpt". We can change it accordingly.
* **-p 7860:7860**: the port-forwarding from host's 7860 to the GraphGPT app running in container at 7860
* **-d**: keeps container running in background after start

GraphGPT Inferencing
--------------------

After container starts up successfully, please visit http://localhost:7860/docs, which is a Swagger API that guides us
to send our first inferencing request

License
-------

The use and distribution terms for [graphgpt-docker] are covered by the [Apache License, Version 2.0].

<div align="center">
    <a href="https://opensource.org/licenses">
        <img align="center" width="50%" alt="License Illustration" src="https://github.com/QubitPi/QubitPi/blob/master/img/apache-2.png?raw=true">
    </a>
</div>

[Apache License Badge]: https://img.shields.io/badge/Apache%202.0-F25910.svg?style=for-the-badge&logo=Apache&logoColor=white
[Apache License, Version 2.0]: http://www.apache.org/licenses/LICENSE-2.0.html
