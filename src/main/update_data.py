# Imports
import pandas as pd
import sqlalchemy


# Constants
file_name_connection_uri = '../hardclimbs_connection_uri.txt'
table_name_climbers = 'climbers'
file_name_climbers = '../../data/climbers.csv'


# Functions
def get_connection_uri(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def get_engine(connection_uri):
    return sqlalchemy.create_engine(connection_uri)


def update_climbers(engine, table_name, file_name):
    df = pd.read_sql_table(table_name, engine, index_col='id')
    df.to_csv(file_name)


# Application code
connection_uri = get_connection_uri(file_name_connection_uri)
engine = get_engine(connection_uri)
update_climbers(engine, table_name_climbers, file_name_climbers)
