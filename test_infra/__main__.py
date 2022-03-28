"""An AWS Python Pulumi program"""
import pulumi
import pulumi_eks as eks
import pulumi_kubernetes as k8s
from pulumi_kubernetes.yaml import ConfigGroup


# Create an EKS cluster with the default configuration.
cluster = eks.Cluster("my-cluster",
    role_mappings=[
        eks.RoleMappingArgs(
            groups=["system:masters"],
            role_arn="arn:aws:iam::008511285722:role/Admin",
            username="pulumi:admin-usr",
        ),
    ]
)

# Export the cluster's kubeconfig.
pulumi.export('kubeconfig', cluster.kubeconfig)