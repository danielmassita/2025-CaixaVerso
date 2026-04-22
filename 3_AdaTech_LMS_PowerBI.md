# CAIXAVERSO - 09 | Analista Dados - I | #1650
`[https://caixaverso.ada.tech/](https://lms.ada.tech/student/classroom-drive/by-class-id/505eda29-987d-41ea-b2d9-c1b7c8d4e917)`

![Copilot_20250609_002008](https://github.com/user-attachments/assets/b9854d88-8df6-4c5c-bbfd-72d978a06dd5)

- Professor: [Leonardo Simões](https://www.linkedin.com/in/leonardo-simoes/)
  - SR Data Scientist

### Dashboard - https://datastudio.google.com/s/jg5Y91GQlXY

## Estrutura da Apresentação

- Introdução
  - Tema do Projeto - Saúde Mental de Estudantes;
  - Dataset escolhido - Kaggle Student Lifestyle, Mental Health & Burnout Insight;
  - Objetivo da análise - Verificar quais variáveis mais impactam a saúde mental de estudantes (universitários); Criticar a estrutura e não o indivíduo.

- Entendimento dos Dados
  - Descrição do Dataset - Dataset público, com 1 milhão de entradas, e distribuição normal de ocorrências, sem tabelas indexadas;
  - Principais Variáveis - Idade (int), Gênero (str), Ano Letivo (int), Estudo Diário em Horas (decimal), Performance Notas (0-100), Nível de Stress + Ansiedade + Depressão (decimal), Horas Sono, Atividade Física, Suporte Social, Tempo Tela, Stress Financeiro, Índice Saúde Mental, Risco de Burnout (Categoria - string), Risco de Desistência;
  
- Tratamento e Modelagem
  - O que foi feito nos dados? - Adequação de Tipos (integer, string, decimal); ajuste de valores nulos (null -> 0 ou média), uso de métricas DAX para estatística descritiva (média e desvio-padrão, min. máx.).
 
- Dashboard
  - Apresentação dos Gráficos - KPIs de Risco (Burnout Risk (low, medium, high)), Histograma Saúde Mental (curva de Gauss), Dispersão e Correlação (variáveis)
  - Explicação das Visualizações - Ajustes no Gênero (filtros/categorias) e Ano Letivo (categoria) mudam as barras de estresse (desclocamento de curvas); 

- Insights (parte mais importante)
  - Principais descobertas - O pouco sono é o principal fator de risco, junto com aspectos de apoio social (falta de suporte), e exposição ao estresse financeiro. As correlações são superiores a 85%.
  - Interpretação dos Dados - Curiosidade: Alta performance também é um indicador de estresse e risco, internalizando a sobrecarga do indivíduo, muito embora haja variáveis de influência da disposição social (rede de apoio) e financeira (conforto financeiro). 

- Conclusão
  - Resumo Geral - O risco de burnout é variado, porém as principais tendências são a correlação de falta de sono, pouco suporte social, alta pressão financeira - e não como um fator meramente técnico (horas de estudo vs. notas obtidas). 
  - Possíveis decisões baseadas nos dados - Usar um modelo preditivo para alunos de 3º, e 4º anos que "mapeiam" as tendências de aumento de risco de burnout (delta da velocidade da função), vinculando os gatilhos estatísticos que poderiam gerar ocorrências de uma mudança de categoria de risco (de Médio para Alto). Essas categorias "em risco de mudança", para evitar a Desistência (dropout), deveriam ser correlacionadas, e categorizadas, devendo passar por um programa de "resiliência acadêmica". Em paralelo, orientação e Educação estrutural para dismantelar as violências estruturais ao invés de culpabilizar o individual.

 
___


## Critérios de Avaliação

- Comunicação (25%)
  -   Clareza na Explicação
  -   Organização da Fala

- Domínio do Projeto (20%)
  - Demonstra entendimento dos dados e do trabalho realizado

- Qualidade do Dashboard (15%)
  - Visual Limpo e Organizado
  - Gráficos Adequados

- Insights (25%)
  - Qualidade da Análise
  - Capacidade de Interpretação

- Organização da Apresentação (15%)
  - Estrutura Lógica
  - Respeito ao Tempo


___

<img width="1074" height="777" alt="image" src="https://github.com/user-attachments/assets/d367dcfc-197d-4b4f-a4fe-1e46ecffc8f2" />


## Desenvolvimento do Projeto

- Tratamento de Dados
    - Limpeza de Dados - Ajustes de Tipos e Filtros Manuais para Categorias (Gênero (M/F/Outros), Ano Letivo (1-4), Risco de Burnout (Low, Medium, High)).
    - Tratamento de Valores Nulos - Verificação de integridade (blank), preenchimento de lacunas com média (para não desconfigurar a curva normal).
    - Remoção de Duplicidades - Desnecessário já que o ID é Único e os dados não possuem index em outras tabelas.
    - Transformações no Power Query - Colunas condicionais manuais (categorias).
  
- Modelagem
  - Organização das Tabelas - Flat Table
  - Criação de Relacionamentos (se aplicável) - Não usado na tabela simples.
 
- Métricas
  - Criação de Medidas (DAX) - Cálculo de Média, Desvio-Padrão, Soma, Min., Máx., Correlação
  - Exemplos: Total Alunos, % Gênero, % Ano Letivo, % Risco (1,5% - 22% - 76%, Média/Desvio do Sono, Correlação Sono vs. Burnout

- Dashboard
  - Criação de Visualizaçẽes claras e organizadas
  - Uso de gráficos adequados - Histograma (normal), Dispersão, Pizza, Gauge
  - Uso de filtros e interatividade - Filtros de Gênero, Ano Letivo, Risco de Burnout
 

___

### Bibliografia Extra

- http://bit.ly/MasEraSoPedir - https://www.geledes.org.br/quadrinho-explica-por-que-as-mulheres-se-sentem-tao-cansadas/
- https://drauziovarella.uol.com.br/mulher/carga-mental-feminina-por-que-as-mulheres-estao-exaustas/
- https://thinkolga.com/report/economia-trabalho/
- https://www.instagram.com/despatologiza/
- <img width="878" height="776" alt="image" src="https://github.com/user-attachments/assets/e89771a5-fd3d-462e-a275-fe07dd0a480b" />
