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

- pgAdmin4.exe
- Servers > PostgreSQL 14 > Databases > postgres > Query Tool (Alt + Shift + Q)
- ![image](https://github.com/user-attachments/assets/3377c4da-3f1c-46d0-bb1a-f4240f4b7143)
- Janela em branco para escrever o código...
- Open File (Ctrl + O) - Carregar a Base (Northwind.sql)...
- Selecionar TODA A BASE (Ctrl + A)...
- Executar Script (F5)...
- ![image](https://github.com/user-attachments/assets/198c3dc2-e856-4b12-8760-2b8ac17543c9)
- Schemas > Public > Tables Refresh
- ![image](https://github.com/user-attachments/assets/788d0326-2706-44e2-a958-06a2c3db4656)
- ```sql
  SELECT * FROM categories
  ```
- Menu: Databases > Postgres > ERD For Databases
- ![image](https://github.com/user-attachments/assets/35dd6021-8530-4c5d-a3f6-423af87145f8)
- ![image](https://github.com/user-attachments/assets/39072ecf-9f67-4137-b39f-107684bcae26)
  - Como as tabelas se relacionam (consumidor, produtos, funcionário, fornecedores etc.)
  - Base que vamos utilizar para montar os exemplos...





___

## Aula 2 - Queries Simples

- Query = Pergunta, Dúvida, Questionamento. (T.I.) = Consulta/Busca informação específica no BD.
- Consultas simples no banco de dados (DB).
- Boas práticas e consultas simples para negócios.
- Pergunta em frente ao Northwind:
  - Quais as categorias de produtos que eu tenho nesse BD?
  - Usar "bons nomes" para as tabelas facilita o trabalho.
  - Algumas "tables" são intuitivas, mas usar nomes e rótulos ajudam ao não-técnico a entender a Informação oriunda do Dado.

- **SELECT**
  - Abrir o SQL -> PgAdmin.exe -> Query Tool (Alt+Shift+Q) -> Tables
  - Usamos o SELECT quando queremos consultar alguma coisa...
  - Usamos o * quando queremos consultar "tudo" sobre algo...
  - Do quê? Da tabela "categories"...
  - ```sql
    SELECT * FROM categories
    ```
    ![image](https://github.com/user-attachments/assets/5b87aca1-40cd-4822-ac05-98cb3ed232fb)

  - A "query" é o comando que se dá pro BD retornar a "query" com as informações.
  - Se a tabela tiver centenas/milhares/milhões de linhas, vale a pena lembrar do CUSTO por causa da Nuvem.
  - ![image](https://github.com/user-attachments/assets/081eb2c7-e630-4d57-843c-c9cbd2b0958d)
  - Boa prática: comando de LIMIT.
  - ```sql
    SELECT * FROM orders
    LIMIT 10
    ```
  - ![image](https://github.com/user-attachments/assets/07cf8fec-ffea-4dba-85b2-525a4b72ddb6)
    
  - Deve-se aprender a "ler" as tabelas, valendo sempre dar uma olhada nas tabelas, por exemplo:
  - ```sql
    SELECT * FROM products
    ```
  - ![image](https://github.com/user-attachments/assets/605c4862-250d-4f17-8bb9-e0d056ddbb01)
  - ID, Nome, ID no Fornecedor, Categoria, Quantidade, Preço Unitário, etc.
  - Alguns identificadores podem ser excessivos, então podemos trabalhar com colunas específicas:
 
  - ```sql
    SELECT product_name, unit_price, units_in_stock
    FROM products
    ```
  - ![image](https://github.com/user-attachments/assets/c55b7880-2667-470f-a5ba-49a2bd998b87)

  - 📈💰📊💼🌐 Pergunta de Negócios: Quantos $ eu poderia dispôr SE vendêssemos todo o estoque?
  - ```sql
    SELECT 
    	product_name, 
	    unit_price, 
	    units_in_stock,
	    unit_price * units_in_stock
    FROM products
    ```
  - ![image](https://github.com/user-attachments/assets/505b33be-f7c9-43bf-bc43-9d1262417980)

  - Importante, ao trabalhar com várias informações, IDENTAR o conteúdo. Também importante criar "alias" (codinomes)
  - ```sql
    SELECT 
    	product_name, 
	    unit_price, 
	    units_in_stock,
	    unit_price * units_in_stock AS total_revenue
    FROM products
    LIMIT 10
    ```
  - ![image](https://github.com/user-attachments/assets/ec2bac39-595a-4623-b2e0-e2e114ea206b)
 
  - 
  


