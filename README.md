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
    * Kubernetes manifest file for a deployment with 2 replicas of the random-key container with a LB service exposing the container on port 80.
        ```
        $ kubectl apply -f random-key.yaml
        ```
### Extra Curricular Componets
* test_infra/[__main__.py
    * Pulumi EKS cluster deployment
* .github/workflows/*.yaml
    * Deploy Pulumi EKS stack or push new docker image to docker hub