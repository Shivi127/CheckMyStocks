# 1) Write a program that scrapes the stocks from google 
# 2) Stores/Updates to the db
# 3) From which I can make paginantion and a front end for it
# 4) I would like to maybe write a cron job or maybe use airflow for this
# 5) Later I will try to incoperate a Queue Later on??


# How do I get started?

#  Lets start with scraping 
import psycopg2
from psycopg2 import sql

class Stocks:
    # The stocks are stored in Postgres? 
    # Lets do this on Docker for the time being as I dont want to buy a service.

    def __init__ (self, connection=None):
        # Connecting to the db using psycopg
        # Refactor this once we have an API to do this.
        self.connection = connection

        if not self.connection:
            try:
                self.connection = psycopg2.connect("dbname='stocksdb' user='stocksdb' host='localhost' password='stocksdb'")
            except:
                print("Could not establish connection to the database.")
    
    def stock_exists(self, stock_name):
        pass

    def add_new_stock(self, name, price, quantity):
        print(f"Adding {quantity} of {name} to the db at price {price}")
        query = " INSERT INTO stocks_db VALUES (%s,%s,%s) ON CONFLICT DO NOTHING; "
        with self.connection.cursor() as cur:
            cur.execute(query, (name, price, quantity))

    def remove_stock(self, stock_name, quantity=0):
        # TODO: 1) Reduce Quantity 2) Delete FROM DB or give arropriate error
        print(f"Removing {stock_name} from DB")
        # query = "SELECT quantity FROM stocks_db WHERE stock_name=%s;"
        # with self.connection.cursor() as cur:
        #     cur.execute(query, [stock_name])
        #     row = cur.fetchone()
        #     return row[0]

    def get_all_stocks(self):
        # TODO: Add checks for miising
        print("Getting Stock Names from DB")
        query = " SELECT DISTINCT stock_name FROM stocks_db;"
        with self.connection.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            return [ele[0] for ele in rows]
    
    def get_count_of_stock(self, stock_name):
        # TODO: Add checks for miising
        print(f"Getting Stock Count for {stock_name} from DB")
        query = "SELECT quantity FROM stocks_db WHERE stock_name=%s;"
        with self.connection.cursor() as cur:
            cur.execute(query, [stock_name])
            row = cur.fetchone()
            return row[0]
