import pandas as pd
import sqlite3
import openpyxl
from random import randint
# Q1

with sqlite3.connect("data\chinook.db") as connection:
    df_customers = pd.read_sql(
        "SELECT * FROM customers",
        con=connection
    )
print(df_customers.head(10))


# Q2

df_iris = pd.read_json("data/iris.json")
print(df_iris.shape)
print(df_iris.columns)


# Q3

df_excel = pd.read_excel("data/titanic.xlsx")
print(df_excel.head())


# Q4

df_parquet = pd.read_parquet("data/flights")
print(df_parquet.info)


# Q5

df_movie = pd.read_csv("data/movie.csv")
print(df_movie.sample(10))

