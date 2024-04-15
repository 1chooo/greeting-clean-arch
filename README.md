# Python with Redis through Docker

## Developing Requirements

Python version `python3.11` or later with [`poetry`](https://python-poetry.org/) to manage the dependencies.

> [!IMPORTANT]
> If you have not installed `poetry`, please install it by following the [official guide](https://python-poetry.org/docs/#installation)


### Build `venv` for **MacOS**
```shell
$ python3.11 -m venv venv
$ source venv/bin/activate
$ poetry install
$ rm -rf venv     # remove the venv
```

### Build `venv` for **Windows**
```shell
$ pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
$ poetry install
$ rmdir /s venv     # remove the venv
```

### Run web app

Edit the `.env` file with your own token.

```shell
$ cp .env.example .env
```

<!-- ```shell
# LINE
CHANNEL_ACCESS_TOKEN='YOUR_CHANNEL_ACCESS_TOKEN'
CHANNEL_SECRET='YOUR_CHANNEL_SECRET'

# FASTAPI
HOST='YOUR_DOMAIN_NAME'
PORT=8080

# AWS
AWS_CLIENT_ACCESS_KEY_ID="YOUR_AWS_CLIENT_ACCESS_KEY_ID"
AWS_CLIENT_SECRET_ACCESS_KEY="YOUR_AWS_CLIENT_SECRET_ACCESS_KEY"
AWS_CLIENT_SESSION_TOKEN = "YOUR_AWS_CLIENT_SESSION_TOKEN"
AWS_CLIENT_BUCKET_ARN = "YOUR_AWS_CLIENT_BUCKET_ARN"
AWS_CLIENT_REGION_NAME = "YOUR_AWS_CLIENT_REGION_NAME"
``` -->

```shell
./scripts/run.sh
```

## Deployment

with `docker` and `docker-compose` installed, you can build and run the docker image.

### Build the docker image

```shell
$ docker build -t todam-backend:<TAG_NAME> .

$ docker run -p 8080:8080 todam-backend:<TAG_NAME>
```

### Run the docker container
```shell
# build the docker image and run the container
$ docker-compose up -d
# follow the logs
$ docker-compose logs -f
# stop the container but keep the container
$ docker-compose stop
# stop the container and discard the container
$ docker-compose down
```


```bash
$ docker run --name my-redis -p 6379:6379 -d redis
```

```bash
$ docker exec -it my-redis sh
# 
```

```bash
redis-cli
127.0.0.1:6379> keys *
(empty array)
```

```bash
127.0.0.1:6379> SET key1 value1
OK
127.0.0.1:6379>
127.0.0.1:6379> keys *
1) "key1"
127.0.0.1:6379>
127.0.0.1:6379> mget key1
1) "value1"
127.0.0.1:6379>
```