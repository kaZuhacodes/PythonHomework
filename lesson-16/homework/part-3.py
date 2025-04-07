import pandas as pd
import numpy as np
import sqlite3
import openpyxl


df_iris = pd.read_json("data/iris.json")
print("Mean: \n",df_iris.select_dtypes("number").mean())
print("Median: \n",df_iris.select_dtypes("number").median())
print("Standart deviation:\n",df_iris.select_dtypes("number").std())


df_excel = pd.read_excel("data/titanic.xlsx")
min_age =df_excel["Age"].min()
max_age = df_excel["Age"].max()
sum_age = df_excel["Age"].sum()
print(f"Min: {min_age}, max: {max_age}, sum: {sum_age}")


df_movie = pd.read_csv("data/movie.csv")

df_director_likes = df_movie.groupby("director_name")[["director_facebook_likes"]].sum()
print(f"Director: {df_director_likes.idxmax()}, Total likes: {df_director_likes.max()}")
df_director_likes.sort_values("director_facebook_likes", ascending=False, inplace=True)
print(f"Top 5:\n {df_director_likes.head(5)}")


df_parquet = pd.read_parquet("data/flights")
num_cols = df_parquet.select_dtypes("number").columns
df_parquet[num_cols] = df_parquet[num_cols].apply(lambda col: col.fillna(col.mean()))