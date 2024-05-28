# kubernetes

This directory contains all the files that kubernetes need to deploy a functioning cluster for production. There are 3 main "categories" of files:
- `Service`: endpoint to communicate with the cluster, you can use services to interact with the cluster
- `Deployment`: an application deployment. It's defined by It's desired state, kubernetes will try to math the desired state.
- `Network`: information about how the deployments are connected

The deployments are all in the same Pod, which can be thought of as a grounp of containers or network.

a kubernetes cluster is made of **Control Pane Nodes** and **Worker Nodes**:
- `Control Pane Nodes`: administrate the cluster (the other worker nodes). There are usually multiple control pane nodes
- `Worker Node`: the machine where you application workloads run

## Create the cluster

First, you need to create a test cluster. I use `kind` which creates a local deploy of kubernetes with docker. I'ts the fastest and lightest way to create a test cluster on ypur machine. To create a cluster with kind, run teh gollowing command:
```bash
kind create cluster --name ledger-board-cluster --config kubernetes-config.yaml
```

## Using docker images in the cluster

To use local docker images (not pulled from some reposiroty) we first need to create the images (with "docker build" or "docker compose up") and load. Run the following command to lead the 3 images:
```bash
sudo kind load docker-image ledger-board-nginx --name ledger-board-cluster
sudo kind load docker-image ledger-board-backend --name ledger-board-cluster
sudo kind load docker-image ledger-board-backend --name ledger-board-cluster
```

## Apply a configuration
To deploy in the cluster we can use the following command:
```bash
sudo kubectl apply -f kubernetes/
```

This configuration creates a pod with the 3 docker images. A pod puts all the images on the same network accessible via localhost. To check that the images are running in the nodes, run:
```bash
sudo kubectl get pods
```
It should say they are all "Running"

To remove something (either a pod, service, ...) you can use:
```bash
sudo kubectl delete <service | pod | ... > <name>
```

## some useful commands

List all nodes in the cluster along with their status
```basj
kubectl get nodes
```

Get all the information about a node (many info):
```bash
kubectl describe node ledger-board-cluster-worker
```

Get all pods:
```bash
sudo kubectl get pods --all-namespaces
```

Descrive a pod:
```bash
kubectl describe pod <pod-name>
```

Get pod logs
```bash
kubectl logs <pod-name>
```

Execute command in Pod:
```bash
kubectl exec -it <pod-name> -- /bin/bash
```

The previous commands also apply to deployments and services
```bash
kubectl get deployments
kubectl describe deployment <deployment-name>
```

Scale a deployment: change the number of replicas
```bash
kubectl scale deployment <deployment-name> --replicas=<number>
```

Delete a cluster:
```bash
sudo kind get clusters
sudo kind delete cluster --name ledger-board-cluster
```

Many many more...
