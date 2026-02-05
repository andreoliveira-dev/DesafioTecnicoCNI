# Databricks notebook source
# DBTITLE 1,Cell 1
def main():
    print("Executando o notebook principal...")
    print("Executando o notebook Bronze...")
    try:
        dbutils.notebook.run("/DesafioCNI/Bronze", 0)
    except Exception as e:
        print(f"Erro ao executar o notebook Bronze: {e}")
        raise e
    print("Executando o notebook Silver...")
    try:
        dbutils.notebook.run("/DesafioCNI/Silver", 0)
    except Exception as e:
        print(f"Erro ao executar o notebook Silver: {e}")
        raise e
    print("Executando o notebook Gold...")
    try:
        dbutils.notebook.run("/DesafioCNI/Gold", 0)
    except Exception as e:
        print(f"Erro ao executar o notebook Gold: {e}")
        raise e
    print("Execução concluída com sucesso!")
    print("EvidÊncia das tabelas: ", spark.sql("SHOW TABLES").collect())

if __name__ == "__main__":
    main()