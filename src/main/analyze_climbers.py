# Imports
import pandas as pd
pd.set_option('display.width', 200)


# Constants
file_name_climbers = '../../data/climbers.csv'


# Functions
def read_data(file_name):
    return pd.read_csv(file_name, index_col='id')


def analyze_height(df):
    df.dropna(inplace=True)
    print(df.describe())


# Application code
df = read_data(file_name_climbers)
analyze_height(df['height'])
