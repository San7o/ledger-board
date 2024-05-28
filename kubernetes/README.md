# kubernetes

This directory contains all the files that kubernetes need to deploy a functioning cluster for production. There are 3 main "categories" of files:
- `Service`: endpoint to communicate with the cluster, you can use services to interact with the cluster
- `Deployment`: an application deployment. It's defined by It's desired state, kubernetes will try to math the desired state.
- `Network`: information about how the deployments are connected

The deployments are all in the same Pod, which can be thought of as a grounp of containers or network.

a kubernetes cluster is made of **Control Pane Nodes** and **Worker Nodes**:
- `Control Pane Nodes`: administrate the cluster (the other worker nodes). There are usually multiple control pane nodes
- `Worker Node`: the machine where you application workloads run

**Create the cluster**
```bash
kind create cluster --name ledger-board-cluster --config ../kubernetes-config.yaml
```

**Deploy**
```bash
sudo kubectl apply -f kubernetes/
```

## useful commands
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
