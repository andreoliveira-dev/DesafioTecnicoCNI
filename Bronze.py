# Databricks notebook source
import requests
from pyspark.sql.functions import current_timestamp, lit

def ingest_to_bronze():

    url = "https://apisidra.ibge.gov.br/values/t/6579/n3/all/p/all/v/all"
    
    response = requests.get(url)
    if response.status_code == 200:

        df_raw = spark.createDataFrame(response.json())
        

        df_bronze = df_raw.withColumn("input_file_name", lit("api_sidra_6579")) \
                          .withColumn("load_timestamp", current_timestamp())
        
    
        df_bronze.write.format("delta").mode("overwrite").saveAsTable("bronze_ibge_populacao")
        print("Bronze concluída.")