# Pipeline Analítico – Projeção da População (IBGE)

Fiz esse projeto pra resolver o desafio de criar um **pipeline analítico** usando os dados de projeção da população (tabela **6579**) do **IBGE**.  
Usei o **Databricks** pra rodar tudo com **PySpark**, separando os dados no esquema de **medalhão (Bronze, Silver e Gold)**.

---

## 1. Como eu dividi as camadas

A ideia foi organizar o fluxo pra não virar bagunça e seguir o que foi pedido no teste:

| Camada | O que eu fiz nela |
|------|-------------------|
| **Bronze** | Peguei o JSON direto da API e salvei bruto, com um `load_timestamp` pra saber quando o dado entrou. |
| **Silver** | Limpei a primeira linha de cabeçalho da API, arrumei os tipos (converti pra número) e dei nomes melhores pras colunas. |
| **Gold** | Onde o bicho pega: criei as agregações (ex: média de população por estado) pra deixar tudo pronto pro BI. |

---

## 2. Decisões que tomei (o *porquê* de cada coisa)

- **Modularização**  
  Separei cada camada em um notebook diferente. Pra rodar tudo, criei um script `Main` que chama um por um usando `dbutils.notebook.run`.  
  Se um der erro, ele avisa qual foi e para ali mesmo.

- **Delta Lake**  
  Usei formato **Delta** em tudo. Além de ser o padrão do Databricks, ajuda muito na performance e garante que os dados não fiquem corrompidos.

- **Nomes de Colunas**  
  Como o Delta é chato com caracteres especiais, usei `.alias()` nas agregações da Gold pra não ter erro com parênteses ou espaços.

- **Segurança no Erro**  
  Coloquei `try/except` no script principal. Se a API cair ou o Spark travar, o código não “morre” sem explicar o que aconteceu.

---

## 3. Como rodar essa belezinha

1. Joga a pasta `/DesafioCNI/` com os notebooks (**Bronze**, **Silver**, **Gold** e **Main**) dentro do seu workspace no Databricks.
2. Liga o cluster e abre o notebook **Main**.
3. Só dar o **Run All**.

Ele vai orquestrar as camadas e, no final, ainda mostra o `SHOW TABLES` pra provar que as tabelas foram criadas.

---

## 4. Evidência de que funcionou

No final do log do `Main`, você vai ver o resultado do:

```sql
spark.sql("SHOW TABLES")
