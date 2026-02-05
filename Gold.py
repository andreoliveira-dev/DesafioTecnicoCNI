# Databricks notebook source
from pyspark.sql import functions as F

def create_gold_summary():
    df_silver = spark.read.table("silver_ibge_populacao")
    

    df_gold = df_silver.groupBy("estado").agg(
        F.avg("populacao_projetada").alias("media_populacao"),
        F.max("ano").alias("ano_referencia_recente")
    )
    
    df_gold.write.format("delta").mode("overwrite").saveAsTable("gold_populacao_estado")
    print("Gold concluída.")