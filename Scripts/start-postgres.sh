#!/bin/bash
POSTGRES_IMAGE=postgres:10.18
echo "Starting PostgreSQL from ${POSTGRES_IMAGE} ...."
docker run -it \
    --env-file .env \
    --publish 5432:5432 \
    --volume /opt/postgres:/pg-data \
    --network internal-network \
    $POSTGRES_IMAGE

echo "you can now connect using psql --username dbuser --password --dbname dbuser --host localhost --port 5432"