# Databricks notebook source

from pyspark.dbutils import DBUtils
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
dbutils = DBUtils(spark)

print(dbutils.fs.ls("dbfs:/FileStore/packages"))

# COMMAND ----------

print("2")