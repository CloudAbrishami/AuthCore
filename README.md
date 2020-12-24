# AuthCore
## authentication microservice 

simple implementation django project by docker and docker-compose
now you can test run django by kubernetes

### local run :

```bash
docker build -t authcordevelop -f Dockerfile.developer .
docker-compose up
```

#### after your work

```bash
press ctrl+c
docker-compose down
```

### for run in kubernetes

i suggest you to use microk8s https://microk8s.io/

```bash
bash utility/createImageForMicrok8s.sh
microk8s kubectl create namespace abrishami-cloud
microk8s kubectl apply $(ls Kuber/*.yaml | awk ' { print " -f " $1 } ')
```

now you can monitor your service by

```bash
microk8s dashboard-proxy
```