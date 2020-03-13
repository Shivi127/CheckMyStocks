#!/bin/bash

/etc/init.d/postgresql start

sudo -H -u postgres bash -c "psql --command \"CREATE USER stocksdb WITH SUPERUSER PASSWORD 'stocksdb'\" ";
sudo -H -u postgres bash -c "createdb -O stocksdb 'stocksdb'";

export PGPASSWORD=stocksdb
psql -h localhost -d stocksdb -U stocksdb -f /Stocks/sql/load_stocks_into_db.sql

python3 /Stocks/stocks_scraper.py 
echo "I have finished running"