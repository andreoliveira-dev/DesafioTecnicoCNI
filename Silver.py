# Databricks notebook source
from pyspark.sql.functions import col

def transform_to_silver():
    df = spark.read.table("bronze_ibge_populacao")

    df_filtered = df.filter(col("V") != "Valor")
    

    df_silver = df_filtered.select(
        col("D1N").alias("estado"),
        col("D2N").alias("ano"),
        col("V").cast("double").alias("populacao_projetada"),
        col("load_timestamp")
    )
    
    df_silver.write.format("delta").mode("overwrite").saveAsTable("silver_ibge_populacao")
    print("Silver concluída.")