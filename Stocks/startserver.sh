#!/bin/bash

/etc/init.d/postgresql start

sudo -H -u postgres bash -c "psql --command \"CREATE USER stocksdb WITH SUPERUSER PASSWORD 'stocksdb'\" ";
sudo -H -u postgres bash -c "createdb -O stocksdb 'stocksdb'";

export PGPASSWORD=stocksdb
psql -h localhost -d stocksdb -U stocksdb -f /Stocks/sql/load_stocks_into_db.sql

python3 /Stocks/stocks_scraper.py 
# TODO: set up a working directory??
export FLASK_RUN_PORT=8000
export FLASK_APP=/Stocks/stocks_api
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
flask run
