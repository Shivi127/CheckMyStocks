#!/bin/bash

/etc/init.d/postgresql start

sudo -H -u postgres bash -c "psql --command \"CREATE USER stocksdb WITH SUPERUSER PASSWORD 'stocksdb'\" ";
sudo -H -u postgres bash -c "createdb -O stocksdb 'stocksdb'";

echo "I ran"

# export PGPASSWORD=stocksdb
# psql -h localhost -d stocksdb -U stocksdb -f /Stocks/{}.sql