#!/bin/bash
set -e
cmd="$@"

# This file can contain settings up of environment variables etc.

if [ -z "$POSTGRES_USER" ]; then
    base_postgres_image_default_user='postgres'
    export POSTGRES_USER="$base_postgres_image_default_user"
fi
export DATABASE_URL="postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB"

# PostgreSQL can be slow to start up - make a function to check if it is up
# and running

until psql $DATABASE_URL -c '\l'; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done

>&2 echo "PostgreSQL is ready - continuing..."

exec $cmd
