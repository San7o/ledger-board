# Kubernetes

I'm using `kind` to simulate a Kubernetes cluster, built with docker compose. I can load docker images in the cluster.
To interact with the clafter, I will use `kubectl`.

## Create the cluster
You can create a cluster with:
```bash
kind create cluster --config kubernetes-config.yaml
```

This is the official example config
```yaml
# this config file contains all config fields with comments
# NOTE: this is not a particularly useful config file
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
# patch the generated kubeadm config with some extra settings
kubeadmConfigPatches:
- |
  apiVersion: kubelet.config.k8s.io/v1beta1
  kind: KubeletConfiguration
  evictionHard:
    nodefs.available: "0%"
# patch it further using a JSON 6902 patch
kubeadmConfigPatchesJSON6902:
- group: kubeadm.k8s.io
  version: v1beta3
  kind: ClusterConfiguration
  patch: |
    - op: add
      path: /apiServer/certSANs/-
      value: my-hostname
# 1 control plane node and 3 workers
nodes:
# the control plane node config
- role: control-plane
# the three workers
- role: worker
- role: worker
- role: worker
```

Export logs:
```bash
kind export logs ./somedir
```

Convert from docker compose to kunernetes:
```bash
kompose convert
```
