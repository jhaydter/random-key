## Repository Contents

### Key files
* test_app/random-key.py
    * Python flask service that takes integer path, generates bytes == integer, and returns response with bytes encoded in base64.
        ```
        $./random-key.py $port
        $ curl http://localhost:$port/key/20
        5jTXcpV2pebZ1RLq5PvzG5gxS8c=
        ```
* test_app/Dockerfile
    * Packages random-key.py into Docker container
        ```
        $ docker build -t random-key .
        $ docker run -d random-key $port
        ```
* test_app/random-key.yaml
    * Kubernetes manifest file for deployment with 2 replicas of the random-key container and an LB service exposing the deployment on port 80.
        ```
        $ kubectl apply -f random-key.yaml
        ```
### Extra Curricular Componets
* test_infra/__main__.py
    * Pulumi EKS cluster IaC
* .github/workflows/*.yaml
    * On push of specific paths deploys Pulumi EKS stack using OIDC
    * On push of specific paths builds and pushes new docker image to docker hub