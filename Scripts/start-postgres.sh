#!/bin/bash


# Make sure you include /opt/postgres in Docker -> Preferences... -> Resources -> File Sharing
# create network using 'docker network create internal-network'
# make a uid:gid of 999:999 - check this Dockerfile https://hub.docker.com/layers/library/postgres/10.18/images/sha256-e37849ff3307519e542e6ad13ae3aa2ab8131e448df126f0f86d2c38980c31da?context=explore

# POSTGRES_IMAGE=postgres:10.18
POSTGRES_IMAGE=8ae3e9e1bbb0

echo "Starting PostgreSQL from ${POSTGRES_IMAGE} ...."

#     --entrypoint bash \
# --user postgres:postgres \


docker run --detach \
    --env-file .env \
    --publish 5432:5432 \
    --volume /opt/postgres:/var/lib/postgresql/data \
    --restart unless-stopped \
    --network internal-network \
    $POSTGRES_IMAGE

if [ $? -eq 0 ]; then
	echo "you can now connect using psql --username dbuser --password --dbname dbuser --host localhost --port 5432"
fi
