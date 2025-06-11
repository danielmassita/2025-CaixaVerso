# CAIXAVERSO
`https://caixaverso.ada.tech/`

![Copilot_20250609_002008](https://github.com/user-attachments/assets/b9854d88-8df6-4c5c-bbfd-72d978a06dd5)


## Trilha de Estudo
## Analista de Dados | Nível I
`https://caixaverso.ada.tech/trilhas/7a60221d-4b64-405a-9beb-558e1ba2aba5`


# Introdução a SQL e Power BI 
`https://caixaverso.ada.tech/cursos/ac3bcc2a-bccf-466a-854c-244b64a0f5fa?backTitle=Trilha&backUrl=%2Ftrilhas%2F7a60221d-4b64-405a-9beb-558e1ba2aba5%3F`

___

## Aula 1 - Introdução ao SQL e Ambiente de Trabalho

- Professor: [Tiago Marto](https://www.linkedin.com/in/tiagomarto/)
  - Desenvolvedor Full Stack
  - Data Scientist
- Software: [PostgresSQL](https://www.enterprisedb.com/postgresql-tutorial-resources-training-1?uuid=140fdf8e-34e6-4b1b-ac32-532e5ac826c4&campaignId=Product_Trial_PostgreSQL_14) v.14.18 (stable)
- Banco de Dados: Exemplo [Northwind](https://operational-production.s3.sa-east-1.amazonaws.com/Materiais+extras+-+cursos+digitais/Introdu%C3%A7%C3%A3o+a+SQL+e+Power+BI/northwind+(1).sql)

- Postgres SQL -> Generate ERD
- ![image](https://github.com/user-attachments/assets/a6da2490-7e45-44d3-b879-184b040f2fca)

___

## Aula 2 - Queries Simples

- Consultas simples no banco de dados (DB).
- Boas práticas e consultas simples para negócios.
- Pergunta em frente ao Northwind:
  - Quais as categorias de produtos que eu tenho nesse BD?
  - Usar "bons nomes" para as tabelas facilita o trabalho.

- **SELECT**
  - Usamos o SELECT quando queremos consultar alguma coisa...
  - Usamos o * quando queremos consultar "tudo" sobre algo...
  - Do quê? Da tabela "categories"...
  - ```sql
    SELECT * FROM categories
    ```
  - A "query" é o comando que se dá pro BD retornar a "query" com as informações... 
