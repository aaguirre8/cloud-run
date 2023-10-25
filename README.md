# GCP
Learn how to deploy a python server in GCP.


## Get started
1. Create and source conda env
```bash
$ conda env create -f environment.yml
$ conda activate cloudrun
```

2. Use the Makefile to upgrade pip and to install the dependencies from the requirements.txt file
```bash
$ make install
```

## Requirements
1. Docker installed.
2. GCP account.
2.1 Services:
2.1.1 Cloud Run
2.1.2 Cloud Storage


## Run Locally
1. Build docker image:
```
docker build -t gcp-image .
```
2. Run docker container:
```
docker run -e PORT=80 -p 4000:80 gcp-image
```