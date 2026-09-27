CAIXAVERSO - FC5 | Analista Dados - II | #1735
Logica de Programação em Python
___

# CAIXAVERSO - FC5 | Analista Dados - II | #1735

https://lms.ada.tech/student/topics/by-class-id/097ee233-0745-490b-b38c-1dc99dfd1305/by-module-id/4e6fa598-53f4-4856-a75d-b7e879ff1b7d

<img width="1024" height="682" alt="image" src="https://github.com/user-attachments/assets/25020c6a-0432-40a2-a039-655d14492299" />


- Professor: [Thiago Tavares Magalhães](https://www.linkedin.com/in/thiagotm/)
  - Senior Data Scientist at SuperSim | Teacher at Ada | Master's Degree in Computational Modeling from the National Laboratory for Scientific Computing

___

# Introdução à Lógica de Programação com Python

Olá! Seja bem-vindo ao curso de lógica de programação com linguagem Python! Vamos repassar algumas orientações iniciais para otimizar o seu uso deste material.

## 1. Onde programar em Python?

O Python é uma linguagem interpretada. Isso significa que é necessário termos um **interpretador Python** instalado em nosso computador para poder executar nossos programas.

Além disso, é importante termos um programa que permita a edição dos códigos. Tecnicamente, qualquer editor de textos puro serviria, incluindo o Bloco de Notas do Windows. Mas programadores normalmente preferem utilizar uma **IDE** (*Integrated Development Environment*), que oferecerá uma série de recursos para facilitar ainda mais o nosso trabalho, como utilizar código de cores e formatação para deixar o código mais legível, ferramentas para autocompletar o código, ferramentas para procurar erros (*debuggers* e *linters*), entre outros.

Vamos passar brevemente por algumas diferentes opções que poderiam ser adotadas. Mas antes de iniciar a instalação de qualquer uma delas, verifique se o seu professor planejou o curso considerando alguma ferramenta específica.

> [!NOTE]
> Caso queira entender melhor como funciona o processo de interpretação do Python, aqui está uma ótima referência!

### 1.1. IDLE

Ao baixar o interpretador Python no site oficial, ele irá trazer junto consigo um editor bastante simples, o **IDLE**.

Ele possui poucos recursos comparado com as próximas IDEs que mencionaremos, mas já é um bom quebra-galho caso você precise editar rapidamente um código.

> [!IMPORTANT]
> Caso seu professor tenha optado por trabalhar com a distribuição padrão do Python disponível no site oficial, procure baixar a versão mais recente disponível no site e lembre-se de marcar a opção **"Add Python to PATH"** durante a instalação. Isso evitará uma série de problemas na hora de instalar outros recursos e bibliotecas.

### 1.2. Thonny

O **Thonny** não é exatamente uma IDE profissional, utilizada no mercado. Seu foco é no aprendizado de Python. Ela oferece recursos especialmente úteis para quem ainda está aprendendo, como acompanhar o valor de variáveis e chamadas de função. Ela também é bastante leve. Ela pode ser obtida gratuitamente no site do projeto.

### 1.3. Visual Studio Code

O **Visual Studio Code** é uma IDE gratuita da Microsoft. Seu grande charme é a possibilidade de ter seus recursos expandidos através de extensões. Sendo assim, ele é, na prática, compatível com praticamente qualquer linguagem em uso atualmente, e é bastante fácil acrescentar novas ferramentas a ele. Ele também é bastante leve e fácil de ser configurado.

Você pode fazer o download no site oficial e configurá-lo para suportar Python.

### 1.4. PyCharm

O **PyCharm** é uma IDE profissional fornecida pela JetBrains, responsável por diversas IDEs, como o IntelliJ, bastante popular entre desenvolvedores Java e Kotlin. Suas ferramentas são populares de maneira geral entre desenvolvedores web e mobile. O PyCharm possui alguns recursos para facilitar a integração com outros sistemas (em particular com linguagem JavaScript e SQL), e para gerenciar a instalação de bibliotecas, evitando que uma atualização de biblioteca em um projeto possa acidentalmente "quebrar" outro projeto. Em contrapartida, ela é mais pesada, o que pode atrapalhar a experiência de quem estiver utilizando computadores mais lentos.

Sua versão **Community** pode ser baixada gratuitamente no site da JetBrains.

### 1.5. Anaconda e Jupyter Notebook

O **Anaconda** é um pacote completo para análise de dados que já vem com uma versão especial do Python (o IPython, ou *Interactive Python*) pré-instalada, bem como diversas bibliotecas prontas extremamente populares na comunidade científica. Essas bibliotecas incluem uma infinidade de funções prontas para conexão com internet, computação matemática, computação científica, aprendizado de máquina, visualização de dados, conexão com banco de dados, entre outras.

Uma das ferramentas inclusas no Anaconda é o **Jupyter Notebook**. O grande diferencial dele em relação a uma IDE convencional é o seu formato de "caderno", onde é possível intercalar trechos de códigos com anotações formatadas utilizando a linguagem Markdown.

Ele é extremamente popular na análise de dados, pois é possível ir escrevendo pequenos trechos de código e já visualizando o resultado na forma de gráficos, tabelas e anotações.

O Anaconda pode ser obtido gratuitamente em seu site oficial e já virá com o Jupyter instalado. Alternativamente, você pode seguir o tutorial no blog da Let's Code para instalar apenas o Jupyter e dar os seus primeiros passos.

> [!TIP]
> Tanto o Visual Studio Code quanto o PyCharm podem ser utilizados para abrir os notebooks. Inicie a instalação pelo Anaconda, e através do aplicativo **Anaconda Navigator**, busque a opção de abrir a IDE desejada e ele fará a mágica por você.

### 1.6. Google Colab

O Google possui o seu próprio notebook, compatível com Jupyter. Ele é **100% online** e integrado com Google Drive. Você precisa estar logado com a sua conta Google e o seu trabalho será salvo em seu Drive.

Ele pode ser acessado aqui.

### 1.7. Programando online

Caso algum dia você se encontre sem o Python instalado em sua máquina — por exemplo, o seu computador quebrou e você conseguiu outro emprestado em cima da hora da aula — não se preocupe. Não faltam opções para programar direto no navegador. Vejamos algumas opções:

- **Repl.it**: uma IDE online bastante simples, com visualização da saída do código logo ao lado do editor.
- **OnlineGDB**: uma IDE online com suporte a múltiplas linguagens de programação diferentes. Não se esqueça de selecionar `"Python3"` no menu antes de começar os seus trabalhos.
- **Jupyter**: O Jupyter oferece uma área em seu site para você experimentá-lo sem precisar instalar. Ele será executado direto no seu navegador e possui acesso às bibliotecas padrão de ciência de dados.
- **Google Colab**: Já mencionado anteriormente, vale reforçar que ele é online e não exige qualquer instalação na sua máquina.

---

## 2. Como estudar Python?

Gostamos de dizer que o nome da nossa escola não é *Let's Talk*, e sim *Let's Code*. Participar das aulas é bastante importante, mas mais importante do que escutar o professor falar é **programar**.

Sempre que você ver um código de exemplo nesse material, **execute o código na sua IDE**. Experimente com o código também: modifique, altere detalhes e veja o que acontece. E, claro, não deixe de fazer os exercícios propostos pelo professor. Eles foram planejados para sedimentar os novos conceitos recém-introduzidos e ajudar a consolidar e integrar os conceitos anteriores.

> [!TIP]
> Quando for executar os exemplos, evite utilizar o famoso "copia e cola". Ao invés disso, **digite o código** e aproveite para se familiarizar com a sintaxe da linguagem.

Quando o seu código não funcionar, não desista, nem simplesmente copie de alguém que funcionou. Busque entender a mensagem de erro (caso haja alguma) e tente ler e entender o que o código está fazendo em cada passo. Caso não consiga resolver, busque o professor, um monitor ou mesmo um colega de turma com quem você se sinta à vontade e mostre seu código para que eles possam ajudar você a entender o seu erro.

E quando você tiver uma ideia, não tenha medo de tentar implementá-la e ver o que acontece!

---

## 3. Material extra e referências

Caso você queira complementar seus estudos, há diversas opções baratas ou mesmo gratuitas. Citaremos alguns aqui que são bastante populares e serviram de base para o nosso material aqui.

### Livros

- **Pense em Python (2ª edição) — Allen B. Downey**: esse livro é bastante introdutório, e possui uma linguagem extremamente acessível. É ideal para quem está começando e usa vários exemplos em código. Ele é disponibilizado gratuitamente e pode ser lido online. A versão impressa pode ser comprada no site da Editora Novatec.
- **Think Python (2nd edition) — Allen B. Downey**: é a versão original do livro acima. Quem tem facilidade com a língua inglesa pode preferir ler o original. Assim como na tradução, é possível ler gratuitamente online ou adquirir a versão impressa no mesmo link.
- **Python Basics (4th edition) — RealPython.com**: disponível apenas em inglês, é um livro escrito pela equipe que mantém o site RealPython.com. Esse livro é bastante introdutório, mirando estudantes iniciantes. Mas ele percorre uma variedade muito maior de tópicos que o Think Python, e acaba oferecendo mais aplicações.
- **Python Tricks — Dan Bader**: disponível apenas em inglês, escrito por um dos editores do RealPython.com. Esse livro é um pouco mais avançado, e seria mais interessante para quem já chegou aqui sabendo Python ou então após a conclusão do módulo. Ele é um livro de aprofundamento, que irá ajudar quem já sabe o básico de Python a explorar mais a fundo os diferentes recursos que a linguagem oferece.
- **Python Fluente — Luciano Ramalho**: assim como o livro anterior, ele é recomendável para quem já está confortável com a linguagem e gostaria de se aprofundar. Foi escrito por um brasileiro e possui traduções para diversas línguas. É uma leitura obrigatória para programadores Python experientes.
- **Toda a coleção do Al Sweigart**: esse autor escreve diversos livros totalmente baseados em projetos e atividades. Eles são bem legais para complementar os estudos justamente pela oportunidade de ver tudo funcionando na prática. Seus livros são em inglês, mas estão todos disponíveis gratuitamente no próprio site do autor, e assim como em outros casos, também podem ser comprados em versões impressas.

### Sites

- **Documentação Oficial do Python**: disponível em português, é ponto de parada obrigatório para todos os programadores. Ela explica detalhadamente todos os recursos da linguagem e possui uma referência bastante completa de todas as bibliotecas incluídas na linguagem.
- **RealPython.com**: um site riquíssimo em cursos, artigos e tutoriais. Alguns são gratuitos, outros são pagos. Eles possuem um newsletter que envia dicas de Python regularmente por e-mail.
- **StackOverflow**: talvez você não tenha utilidade imediata para ele. Mas conforme você for programando e pesquisando erros, frequentemente cairá neste site. Ele é um site de perguntas e respostas sobre programação com filtros bastante eficientes para garantir a prevalência de perguntas relevantes e respostas corretas.

Ademais, há uma infinidade de blogs, tutoriais e vídeos, muitas vezes em sites com temáticas específicas (ex: análise de dados ou machine learning). Não deixe de pesquisar quando você tiver dúvidas específicas, você ficará surpreso com quanto material bom de Python existe gratuitamente por aí! :)

### Cursos digitais Ada

Além dos materiais acima, temos também diversos cursos digitais da Ada, que podem ser muito úteis em sua jornada de aprendizagem de lógica de programação e Python! Seguem as principais recomendações:

- **Funcionamento do computador**: https://cursos.letscode.com.br/curso-digital/65757051-1636-4c95-8cb3-fd14198d741b
- **Lógica Pura**: https://cursos.letscode.com.br/curso-digital/2120c9f0-02ba-45c1-a81d-3ed26232cc0c
- **Introdução a Python**: https://cursos.letscode.com.br/curso-digital/ad77ffa3-6dde-4efb-9e0d-3b14e60b097b
- **Como melhorar o seu aprendizado**: https://cursos.letscode.com.br/curso-digital/956710f8-d7cf-4bff-93d7-b9d544a82e77
- **História da Ciência da Computação**: https://cursos.letscode.com.br/curso-digital/4114870c-c8e7-4701-aa55-3b6277a8ae67

---

# Variáveis, entradas e saídas

## 4. Variáveis

Em nossos programas, frequentemente precisaremos armazenar dados temporariamente. Esses dados podem ser adquiridos de alguma maneira (digitados pelo teclado, lidos de um arquivo etc.) ou calculados pelo nosso programa com base em outros dados. Imagine, por exemplo, que você gostaria de calcular a média de um aluno a partir de suas notas. Precisaremos que o aluno digite suas notas, e o programa irá calcular um novo valor, a média. Armazenaremos nossos dados temporariamente em **variáveis**.

Variáveis são "pedacinhos de memória" onde guardamos dados. Sempre que referenciamos o nome, o pedacinho de memória é acessado e seu dado é recuperado.

Criamos variáveis dando um nome a elas e usando o **operador de atribuição** (o sinal de igualdade: `=`) para atribuir um valor inicial.

```python
x = 10
```

No exemplo acima, foi criada uma variável chamada `x` que guarda o valor `10`. Ou seja, reservamos um pedacinho de memória e guardamos o número 10 lá.

> [!TIP]
> Tente sempre utilizar **nomes intuitivos** para suas variáveis. O nome deveria ser uma boa descrição do dado que a variável guarda. Nomes como `x`, `y`, `z`, `a`, `b`, `c`, `a1`, `a2`, `a3` etc. podem se tornar bastante confusos quando nossos códigos são muito grandes. Quanto mais descritivos os nomes forem, melhor.

Os nomes de variáveis podem conter letras, números e o símbolo `_`, mas eles **não podem começar com número**.

> [!NOTE]
> Existe uma grande variedade de padrões diferentes que podemos adotar para nomear nossas variáveis. Em Python é recomendável utilizar o padrão conhecido como **snake case**, em que nomes de variáveis com múltiplas palavras adotam o símbolo `_` para separar as palavras. Exemplos: `nome_completo`, `nota_da_prova` etc.

## 5. Tipos de variáveis

Variáveis podem ter diferentes tipos. Alguns tipos são considerados **tipos primitivos**, ou seja, eles são tipos de dados mais básicos que podem ser utilizados para compor outros tipos mais complexos. Em Python esses tipos levam os seguintes nomes:

- `int`: números inteiros, ou seja, números sem parte decimal: `0`, `5`, `-1`, `1000`
- `float`: números reais, ou seja, números com parte decimal: `1.0`, `-2.7`, `3.14`
- `str`: cadeias de caracteres (*strings*), ou seja, dados textuais: `'Olá Mundo!'`, `"eu tenho 18 anos"`
- `bool`: valores lógicos (booleanos), ou seja, apenas um entre dois valores possíveis: `True` ou `False`

```python
nome = 'Zé'                          # uma variável do tipo string - note as aspas
email = "ze@letscode.com.br"         # outra string
idade = 22                           # uma variável inteira
salario = 5999.85                    # uma variável float - usamos ponto, não vírgula
receber_newsletter = True            # uma variável bool
```

O Python é uma linguagem **dinamicamente tipada**. Isso significa que não precisamos especificar o tipo de uma variável: a própria linguagem tenta determinar o tipo de acordo com o dado atribuído à variável.

## 6. Comentários

Note que nos exemplos acima, escrevemos textos no meio do código utilizando o símbolo `#`. Esses textos são **comentários**: quando utilizamos o símbolo `#`, o Python irá ignorar tudo o que vier em seguida (na mesma linha). Utilizamos comentários para explicar pedaços do nosso código para que nós mesmos ou outros colegas no futuro entendam o que fizemos e possam modificar ou corrigir o código com mais facilidade. Também podemos escrever comentários de múltiplas linhas utilizando aspas triplas — neste caso, as utilizamos para abrir e depois para fechar o bloco de comentários.

```python
'''
Este é um comentário de várias linhas.
Tudo que veio após o primeiro trio de aspas e antes do segundo
será ignorado pelo Python.
'''
```

Na verdade, esse tipo de comentário não é exatamente um comentário, mas uma *string* com múltiplas linhas. O Python enxerga que apenas "declaramos" uma *string* no meio do código, sem utilizá-la ou atribuí-la para qualquer variável, e por conta disso ela é ignorada, funcionando na prática como um comentário.

Na maioria das IDEs você possui teclas de atalho para facilmente transformar um bloco inteiro de código em comentário para temporariamente desabilitá-lo. Isso pode ser útil quando estamos testando soluções alternativas para um problema ou corrigindo erros. No Visual Studio Code, por exemplo, você pode utilizar `ctrl+/` para transformar uma seleção em comentário.

## 7. Saídas

Chamamos de **saídas** do nosso programa todos os dados que são gerados pelo programa e serão fornecidos para o usuário. A função de saída em tela no Python é o `print`. Colocamos entre parênteses o dado que queremos que apareça.

```python
print('olá mundo!')  # exibe a frase 'olá mundo' na tela
```

Os dados a serem exibidos não precisam ser valores constantes, como a frase fixa acima. Eles podem ser variáveis:

```python
idade = 20
print(idade)
```

Note que quando usamos aspas, o Python trata o valor como uma *string*, um texto literal. Quando não usamos aspas, o Python irá considerar que aquele é o nome de uma variável e irá acessá-la para buscar seu valor.

Podemos exibir múltiplos dados em um `print`. Para isso, basta separá-los por vírgula e eles irão aparecer na tela na mesma ordem que apareceram no código:

```python
nome = 'Mario'
linguagem = 'Python'
print('Oi, eu sou o', nome, 'e eu programo em', linguagem)
```

```console
Resultado na tela:
Oi, eu sou o Mario e eu programo em Python
```

Note que os dados aparecem em tela separados por um espaço automaticamente. Dois `print`s sucessivos também possuem uma quebra de linha entre eles. Você pode passar as opções `sep` e `end` dentro de seu `print` para especificar diferentes comportamentos. Exemplo:

```python
nome = 'Mario'
linguagem = 'Python'
print('Oi, eu sou o', nome, sep='@', end='***')
print('Eu programo em', linguagem, sep='@')
```

```console
Resultado na tela:
Oi, eu sou o@Mario***Eu programo em@Python
```

> [!TIP]
> Caso você ache confuso separar os dados por vírgulas, você pode alternativamente utilizar uma **f-string**. Não entraremos em detalhes agora, mas o funcionamento básico é simples: coloque um `f` antes de abrir aspas, e dentro do texto você pode colocar o nome das variáveis entre chaves. O `print` abaixo terá o mesmo resultado que o exemplo anterior:
>
> ```python
> print(f'Oi, eu sou o {nome} e eu programo em {linguagem}')
> ```

## 8. Entradas

Assim como temos dados de saída — dados gerados pelo código e fornecidos para o usuário — também temos dados de **entrada**: informações que o usuário possui e deve fornecer ao código. Para receber entradas pelo teclado, utilizaremos a função `input`. Devemos levar uma variável a receber o valor capturado pelo `input`.

```python
nome = input()
print('Olá', nome)
```

O programa acima captura o nome do usuário e em seguida mostra a mensagem "olá" seguida do nome do usuário. Note que o programa fica parado em uma tela em branco com um cursor piscando aguardando a digitação pelo usuário. Isso pode ser confuso para o usuário, que não sabe o que o programa está esperando. Por isso, dentro dos parênteses do `input` podemos colocar uma mensagem simples informando o que o programa gostaria que ele fizesse:

```python
nome = input('Qual é o seu nome?')
print('Olá', nome)
```

### 8.1. Determinando o tipo da entrada

Vamos imaginar um programa que informa quantos anos falta para que uma criança atinja a maioridade. Podemos ler a idade da criança pelo teclado (entrada), subtrair a idade do número 18 (processamento) e exibir o resultado da conta na tela (saída). Considere a solução abaixo:

```python
idade = input('Digite a sua idade: ')
resto = 18 - idade
print('Faltam', resto, 'anos.')
```

Se você copiar e executar o programa, ele dará erro na segunda linha. Isso ocorre porque o teclado é uma "máquina de escrever" um pouco mais moderna. Portanto, **tudo que entra pelo teclado é considerado pelo Python como texto** (ou seja, `str`). Porém, não podemos "fazer contas" com textos. Fazemos contas com números. Portanto, neste caso, precisamos falar para o Python interpretar a nossa entrada como um número. Um bom tipo de dado para "idade" seria um número inteiro. Fazemos isso colocando o nome do tipo desejado, e entre parênteses colocamos nosso `input`:

```python
idade = int(input('Digite a sua idade: '))
resto = 18 - idade
print('Faltam', resto, 'anos.')
```

Chamamos essa operação de **coerção de tipo**. Em materiais em inglês você verá essa operação com o nome *casting*. Tome cuidado: operações de coerção podem resultar em perdas de dados. Se você converter o número `float` `3.9` para `int`, ele não arredondará para `4`, e sim descartará a parte fracionária, resultando em `3`.

> [!WARNING]
> Neste início, mensagens de erro podem parecer intimidadoras. Elas aparecem em vermelho e frequentemente possuem nomes técnicos e expressões em inglês. Mas crie o hábito de tentar compreendê-las. A partir da versão 3.10 do Python elas se tornaram significativamente mais amigáveis. Elas também indicam a linha com erro. Além disso, se você pesquisar em sites de busca por uma mensagem de erro, provavelmente encontrará diversos exemplos e explicações do que pode tê-la provocado e como consertar!

## 9. Expressões aritméticas

Como podemos observar no exemplo anterior, o Python faz operações aritméticas de maneira bastante intuitiva, similar ao que estamos acostumados. Os operadores aceitos são:

| Operação | Operador |
|----------|----------|
| Soma | `+` |
| Subtração | `-` |
| Multiplicação | `*` |
| Divisão | `/` |
| Divisão inteira | `//` |
| Resto da divisão | `%` |
| Potência | `**` |

```python
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao_real = numero1 / numero2
divisao_inteira = numero1 // numero2
resto = numero1 % numero2
elevado = numero1 ** numero2
print('Soma: ', soma)
print('Subtração: ', subtracao)
print('Multiplicação: ', multiplicacao)
print('Divisão: ', divisao_real)
print('Divisão inteira: ', divisao_inteira)
print('Resto da divisão: ', resto)
print('Potência: ', elevado)
```

**Operadores de divisão:** Note que temos 3 operadores de divisão. O que seria cada um deles? Vamos supor que `numero1` seja `15` e `numero2` seja `6`.

```text
 15 |__ 6
```

Quantas vezes o número 6 cabe dentro do 15? Um bom primeiro "chute" é 2:

```text
 15 |__ 6
     2
```

Podemos multiplicar 6 por 2, que dará 12. E então subtraímos esse valor de 15:

```text
 15 |__ 6
-12     2
---
 03
```

Note que, considerando apenas números inteiros, não conseguimos mais prosseguir com a divisão. Neste caso, a **divisão inteira** (`numero1 // numero2`) dará `2`. Já o **resto da divisão** (`numero1 % numero2`) dará `3`.

Porém, considerando casas decimais é possível prosseguir com a divisão:

```text
 15 |__ 6
-12     2.5
---
 03
  30
- 30
----
   0
```

Portanto, a **divisão real** (`numero1 / numero2`) dará `2.5`.

> [!WARNING]
> **Atenção:** números reais em Python usam **ponto** para separar as casas decimais, não vírgula:
>
> - ❌ Errado: `2,5`
> - ✅ Correto: `2.5`

---

# Operações lógicas

## 10. Operações booleanas

Quando estudamos variáveis, vimos que existem alguns tipos primitivos: `str` (texto), `int` (número inteiro), `float` (número real) e `bool` (lógico). Vimos diversas operações aritméticas também, como a soma, a divisão ou a potência, cujos resultados são `int` ou `float`. Porém, podemos ter também operações cujo resultado é `bool`: são as **operações lógicas**.

### 10.1. Comparações

Algumas das operações lógicas mais conhecidas são as **comparações**:

```python
comparacao1 = 5 > 3
print(comparacao1)
comparacao2 = 5 < 3
print(comparacao2)
```

Se executarmos o código acima, a saída que teremos na tela será:

```console
True
False
```

Isso ocorre porque 5 é maior que 3. Portanto, `comparacao1` recebeu uma expressão cujo valor lógico é verdadeiro, portanto seu resultado foi `True`, e o oposto ocorreu para `comparacao2`. O Python possui 6 operadores de comparação:

| Operação | Operador |
|----------|----------|
| Maior que | `>` |
| Maior ou igual | `>=` |
| Menor que | `<` |
| Menor ou igual | `<=` |
| Igual | `==` |
| Diferente | `!=` |

> [!IMPORTANT]
> Note que o operador para comparar se 2 valores são iguais é `==`, e **não** `=`. Isso ocorre porque o operador `=` é o nosso operador de **atribuição**: ele diz que a variável à sua esquerda deve receber o valor da expressão à direita. O operador `==` irá testar se o valor à sua esquerda é igual ao valor à sua direita e irá responder `True` ou `False`, como todos os outros operadores de comparação.

### 10.2. Negação lógica

Outra operação lógica bastante importante é a **negação**. Ela inverte o resultado de uma expressão lógica. Caso a expressão resulte em `True`, a sua negação irá resultar em `False`, e vice-versa.

A negação em Python é representada pela palavra `not`. Vamos modificar o exemplo anterior:

```python
comparacao1 = not 5 > 3
print(comparacao1)
comparacao2 = not 5 < 3
print(comparacao2)
```

O resultado será:

```console
False
True
```

Podemos resumir o funcionamento do `not` utilizando uma **tabela-verdade**. Nela testamos os diferentes valores possíveis para a entrada e anotamos o resultado para cada conjunto de valores:

| A | not A |
|---|-------|
| `True` | `False` |
| `False` | `True` |

### 10.3. Conjunção lógica

Em alguns casos precisamos testar se **duas ou mais condições são verdadeiras**.

Imagine, por exemplo, que o critério de aprovação em uma escola seja a média superior a 6.0 **e** presença superior a 75%. Neste caso, o aluno precisa atender a ambos os critérios para ser aprovado. Se ele tirou uma ótima nota, mas faltou demais, será reprovado. Se ele compareceu a todas as aulas, mas teve notas baixas, idem.

A **conjunção lógica**, também conhecida como **e lógico**, é representada em Python pela palavra `and`.

O código abaixo testa se é verdade que o aluno foi aprovado:

```python
media = float(input('Digite a média do aluno: '))
presenca = float(input('Digite as presenças do aluno: '))

aprovado = media >= 6.0 and presenca >= 0.75
print('O aluno foi aprovado?', aprovado)
```

Execute o código acima e teste algumas combinações diferentes de valores. Note que basta uma das condições ser falsa para que o resultado total seja `False`.

A tabela-verdade para o **e lógico** entre duas entradas A e B é:

| A | B | A and B |
|---|---|---------|
| `False` | `False` | `False` |
| `False` | `True` | `False` |
| `True` | `False` | `False` |
| `True` | `True` | `True` |

### 10.4. Disjunção lógica

Nem sempre precisamos que ambas as condições sejam verdadeiras. Vários de nós já nos deparamos com promoções de queima de estoque anunciadas da seguinte maneira: "promoção válida até o dia 15 deste mês **ou** enquanto durarem os estoques".

Neste caso, para a promoção acabar, **não é necessário que ambas as coisas ocorram** (atingir o dia 15 e zerar o estoque). Se ainda temos 10 itens no estoque, mas hoje é dia 16, a promoção acabou. Se hoje é dia 5, mas o estoque está zerado, a promoção acabou.

A **disjunção lógica**, também chamada de **ou lógico**, é representada em Python pela palavra `or`.

O programa abaixo testa se a promoção acabou:

```python
dia_final = int(input('Digite o dia do mês para encerrar a promoção: '))
dia_atual = int(input('Digite o dia do mês atual: '))
estoque = int(input('Digite a quantidade de itens no estoque: '))

acabou = dia_atual > dia_final or estoque == 0
print(acabou)
```

Faça alguns testes com o programa acima e note que basta uma condição ser verdadeira para seu resultado ser `True`.

A tabela-verdade para o **ou lógico** é:

| A | B | A or B |
|---|---|--------|
| `False` | `False` | `False` |
| `False` | `True` | `True` |
| `True` | `False` | `True` |
| `True` | `True` | `True` |

**Resumo:**

- `not`: inverte a expressão original
- `and`: verdadeiro apenas se ambas as condições forem verdadeiras
- `or`: falso apenas se ambas as condições forem falsas

## 11. Valores truthy e falsy

Valores não-booleanos em Python, como inteiros ou *strings*, podem ser convertidos para booleanos utilizando a função `bool`, da mesma maneira que utilizamos `int` e `float` em exemplos anteriores para converter entradas de *string* para número.

Certos valores serão convertidos para `True`, enquanto outros serão convertidos para `False`. Em certos contextos, como expressões condicionais — que serão estudadas muito em breve — essa conversão ocorre de maneira implícita. Quando um valor pode ser interpretado como `True`, dizemos que ele é um valor **truthy**, e quando ele pode ser interpretado como `False`, ele é conhecido como um valor **falsy**.

**Valores Falsy comuns são:**

- O valor inteiro `0`
- O valor real `0.0`
- Strings vazias (strings com 0 caracteres)
- Coleções vazias (listas, tuplas, dicionários etc. com 0 elementos)

**Valores Truthy comuns são:**

- Inteiros diferentes de `0`
- Reais diferentes de `0.0`
- Strings contendo ao menos 1 caractere
- Coleções (listas, tuplas, dicionários etc.) com pelo menos 1 elemento
- A constante `None`, que representa uma variável "vazia"

> [!NOTE]
> Não se preocupe se não estiver familiarizado com todos os dados exemplificados aqui. Estudaremos cada um deles em outros momentos.

---

# Expressões condicionais

### 12.1. Se

Os programas do capítulo Operações Lógicas não são "amigáveis" para o usuário. Ao invés de mostrar `True` ou `False`, por exemplo, seria mais útil exibir se o aluno foi "Aprovado" ou "Reprovado".

Para que possamos escrever na tela as mensagens "Aprovado" ou "Reprovado", é necessário que haja em algum ponto do código o trecho `print('Aprovado')` e o trecho `print('Reprovado')`. Porém, não gostaríamos que ambos fossem exibidos ao mesmo tempo.

Precisamos **ramificar o fluxo de execução** de nosso programa: em certas circunstâncias, o fluxo deve executar algumas linhas de código e ignorar outras.

Uma **condicional** é uma instrução em Python que decide se outras linhas serão ou não executadas dependendo do resultado de uma condição. A condição nada mais é do que uma expressão lógica. Se a condição for verdadeira, as linhas são executadas. Senão, são ignoradas.

A condicional mais básica em Python é o `if` (se):

```python
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2)/2

if media >= 6.0:
    print('Aprovado')

print('Média: ', media)
```

Execute o programa acima. Note que **se** (`if`) a média é maior ou igual a 6.0, ele exibe a mensagem "Aprovado" e depois a média. Caso contrário, ele apenas exibe a média.

Para dizermos que uma ou mais linhas "pertencem" ao nosso `if`, usamos um símbolo de parágrafo (tecla "Tab" no teclado). O programa sabe que o `if` "acabou" quando as linhas param de ter "tabs". Esses tabs são chamados de **indentação**. Tanto no `if` quanto no restante das estruturas de controle que estudaremos é **obrigatório** ter pelo menos 1 linha indentada abaixo da linha de controle.

### 12.2. Senão

Note que conseguimos fazer nosso programa decidir se ele exibe a mensagem "Aprovado" ou não. O próximo passo seria fazer ele decidir entre 2 mensagens diferentes: "Aprovado" ou "Reprovado". Um primeiro jeito de fazer isso seria um segundo `if` invertendo a condição:

```python
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2)/2

if media >= 6.0:
    print('Aprovado')
if media < 6.0:
    print('Reprovado')

print('Média: ', media)
```

O programa acima funciona. Porém, conforme nossos programas começam a ficar mais complexos e nossos `if` começam a ter linhas demais, podemos nos perder e esquecer que esses 2 `if` são 2 casos mutuamente exclusivos. Pior ainda, podemos vir a acrescentar condições novas em um e esquecer de atualizar no outro.

Nos casos em que temos condições **mutuamente exclusivas**, podemos utilizar um par `if`/`else` (se/senão). Se a condição for verdadeira, faça tal coisa. Senão, faça outra coisa.

```python
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2)/2

if media >= 6.0:
    print('Aprovado')
else:
    print('Reprovado')

print('Média: ', media)
```

Note que o `else` **não possui condição**. A condição dele é implícita: é a negação da condição do `if`. Se o `if` executar, o `else` não executa e vice-versa. Consequentemente, o `else` não pode existir sem um `if`.

### 12.3. Aninhando condições

É possível **aninhar** condições: ou seja, colocar um novo `if` dentro de outro `if` ou `else`. Imagine que nossa escola não reprova direto o aluno com nota inferior a 6, e sim permite que ele faça uma recuperação. Porém, o aluno precisa ter tirado no mínimo média 3 para que permitam que faça a recuperação. Assim temos:

- Se nota maior ou igual a 6: aprovado.
- Senão:
  - Se nota entre 6 e 3: recuperação.
  - Senão: reprovado.

Em Python:

```python
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2)/2

if media >= 6.0:
    print('Aprovado')
else:
    if media >= 3.0:
        print('Recuperação')
    else:
        print('Reprovado')

print('Média: ', media)
```

### 12.4. Senão-se

Note que se começarmos a aninhar muitas condições (`if` dentro de `else` dentro de `else` dentro de `else`...), nosso código pode começar a ficar confuso, com a aparência de uma "escadinha":

```text
Se
Senão:
    Se
    Senão:
        Se
        Senão:
            Se:
            Senão:
                Se:
                 ...
```

Isso pode tornar o código bastante complexo e difícil de atualizar ou corrigir erros posteriormente. Para quebrar a "escadinha", existe a possibilidade de juntarmos o "se" do próximo nível com o "senão" do nível anterior: o `elif`: **else + if** (senão + se).

O `elif` só é executado se um `if` der errado (ou seja, ele é um `else`), mas ele também tem uma condição que deve ser respeitada (ou seja, ele também é um `if`). Podemos reescrever nosso código anterior utilizando um `elif`:

```python
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2)/2

if media >= 6.0:
   print('Aprovado')
elif media >= 3.0:
   print('Recuperação')
else:
   print('Reprovado')

print('Média: ', media)
```

Podemos usar quantos `elif` nós quisermos. Sempre que um deles der errado, o próximo será testado. Quando algum deles der certo, todo o restante será ignorado.

Opcionalmente, podemos ter um `else` ao final do bloco, que só será executado se o `if` e todos os `elif` derem errado.

O bloco, obrigatoriamente, deve ser iniciado com um `if`.

> [!CAUTION]
> **Atenção**
>
> Você lembra dos valores *truthy* e *falsy*? Nós conversamos sobre eles no capítulo Operações Lógicas. Uma variável, qualquer que seja seu tipo, pode ser interpretada pelo `if` como se fosse uma expressão lógica.
>
> Se `x` for um inteiro, o bloco `if x:` será executado caso `x` seja diferente de zero, por exemplo.
>
> Uma fonte comum de erros em iniciantes envolve o uso de `and` ou `or` em condicionais e a forma como Python lida com valores *truthy* e *falsy*. Execute o trecho de código abaixo:
>
> ```python
> seguro = input('Deseja adquirir um seguro opcional (sim/não): ')
>
> if seguro != 'sim' and 'não':
>     print('Você não digitou uma opção válida')
> ```
>
> Você verá que ele nem sempre se comporta como você imaginaria. O Python não irá interpretar a condição do `if` como "seguro diferente de 'sim' **e** seguro diferente de 'não'", e sim como "(seguro diferente de 'sim') **e** ('não')".
>
> Isso ocorre porque no `if` temos uma expressão lógica do tipo `expressão1 and expressão2`. Nossa `expressão1` é `seguro != 'sim'`, e nossa `expressão2` é apenas a *string* `'não'`.
>
> A `expressão2` é, portanto, uma *string* não-vazia, portanto ela é *truthy*. O Python irá implicitamente convertê-la para o valor lógico `True`. Portanto, temos a expressão `(seguro !='sim') and (True)`. Logo, a condição será verdadeira se `seguro !='sim'` e falsa caso contrário. Logo, se você digitar "não", a expressão é falsa e o programa dirá que você digitou algo inválido.
>
> Para evitar esse problema, você precisa ser **explícito** em suas condições:
>
> ```python
> seguro = input('Deseja adquirir um seguro opcional (sim/não): ')
>
> if seguro != 'sim' and seguro != 'não':
>     print('Você não digitou uma opção válida')
> ```

---

# Malhas de repetição condicionais

Imagine que você queira fazer um programa que exibe os números de 1 até 5, em ordem crescente. Uma possibilidade seria:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

Porém, imagine que os requisitos do programa acabam sendo alterados, e agora o seu programa deverá ir até 1000. Ou, pior, imagine que o usuário irá digitar um valor e seu programa deverá contar apenas até o valor digitado. Note como fica difícil resolver esses problemas apenas copiando e colando linhas de código.

Vamos pensar em outro tipo de problema. Na aula passada, fizemos um exercício onde precisávamos validar algumas entradas do usuário. Uma dessas entradas era a idade, e gostaríamos de aceitar apenas valores entre 0 e 150. Sua solução provavelmente foi parecida com o código abaixo:

```python
idade = int(input('Digite a idade: '))

if idade < 0 or idade > 150:
  print('Erro')
```

Mas imagine que, ao invés de apenas mostrar uma mensagem de erro, nós devêssemos obrigar o usuário a continuar digitando valores novos para idade até que ele digite um valor válido (entre 0 e 150). Isso não seria possível utilizando apenas `if`, `elif` e `else`.

### 13.1. Enquanto

Os problemas enunciados acima podem ser resolvidos utilizando estruturas do tipo "enquanto". Em Python, a instrução `while` é bastante parecida com o `if`: ela possui uma expressão lógica, e seu conteúdo só será executado se a expressão for verdadeira. Porém, após chegar ao final, ela **retorna ao início e testa novamente a condição**.

Se ela for verdadeira, seu conteúdo será executado de novo. Ao final da nova execução, a condição é testada novamente, e assim sucessivamente. A execução só será interrompida quando o teste se tornar falso. Vejamos como resolver o problema da idade utilizando o `while`:

```python
idade = int(input('Digite a idade: '))

while idade < 0 or idade > 150:
  print('Erro! Idade deve estar entre 0 e 150!')
  idade = int(input('Digite a idade: '))

print('Obrigado!')
```

Faça alguns testes com o programa acima. Note que se você digitar uma idade válida desde o início, ele nunca chega a mostrar erro: o `while` é como um `if` e será ignorado se sua condição for falsa. Porém, caso você digite valores inválidos, a condição será verdadeira e ele irá executar enquanto você estiver digitando valores falsos.

Estruturas do tipo "enquanto" são conhecidas como **malhas de repetição** ou **loops**.

### 13.2. Condição de parada

No exemplo anterior, o que determina se o loop prossegue ou não é o valor de `idade`. Esse valor, por sua vez, pode mudar em cada execução do loop, já que temos um `input` lá dentro. Experimente rodar o programa sem aquele `input` e verifique o que ocorre.

```python
idade = int(input('Digite a idade: '))

while idade < 0 or idade > 150:
  print('Erro! Idade deve estar entre 0 e 150!')
print('Obrigado!')
```

O que ocorreu é o que chamamos de **loop infinito**: se a condição for verdadeira uma vez, ela será para sempre, já que nunca mais alteramos o valor da variável envolvida no teste lógico. É importante criar caminhos para que a condição possa se tornar falsa em algum momento. Isso é o que chamamos de **condição de parada** do nosso loop.

### 13.3. Sequências numéricas

Iniciamos essa aula enunciando um problema onde gostaríamos de exibir números sequencialmente na tela. Isso é possível de resolver utilizando loops. Primeiro, observe o exemplo abaixo e responda: qual valor aparecerá na tela?

```python
x = 5
x = x + 1
print(x)
```

Essa construção parece pouco intuitiva porque na matemática o operador `=` é bidirecional: a expressão "a = b" significa que a é igual a b e b é igual a a. Ao vermos `x` aparecendo em ambos os lados, parece que podemos simplesmente cortar dos dois lados, resultando em `0 = 1`, o que é uma inverdade.

Em Python o operador `=` na verdade não é o operador de igualdade da matemática, e sim o **operador de atribuição de valores**. Ou seja, o que ele diz é "pegue o resultado da expressão à direita e guarde na variável à esquerda". Portanto, o exemplo acima pega primeiro o valor antigo de `x`, que era `5`, adiciona `1`, resultando em `6`, e guarda este novo resultado na variável `x`, substituindo o valor antigo. Logo, a resposta na tela é `6`.

Se colocarmos uma expressão desse tipo dentro de um loop, podemos gerar sequências numéricas:

```python
final = int(input('Digite o valor final da sequência: '))
numero = 1

while numero <= final:
  print(numero)
  numero = numero + 1
```

O programa acima pede para o usuário digitar um número, que será o valor final da sequência. Então ele irá imprimir a variável `numero`, que vale `1`, e somar `+1` nela. Em seguida imprimirá de novo a variável, agora valendo `2`, e somará `+1` nela. E assim sucessivamente até que ela ultrapasse o valor final, quando o loop deixará de ser executado.

Você consegue modificar o programa acima para fazer uma sequência decrescente? E para gerar a tabuada de um número dado pelo usuário? Você precisará mexer na expressão lógica do loop e no incremento de `numero`.

> [!TIP]
> Em expressões onde uma variável aparece de ambos os lados, podemos utilizar uma abreviação. Por exemplo, a expressão `x = x + 5` pode ser reescrita como: `x += 5`. Isso vale para todas as outras expressões aritméticas (subtração, multiplicação, divisão etc.).

## 14. Comandos de manipulação de fluxo

É possível manipular de algumas maneiras a forma como uma malha de repetição se comporta: nós podemos **interromper** sua execução sem que sua condição de parada tenha sido atingida e podemos **saltar** para o próximo passo sem finalizar o atual.

### 14.1. Break

Vamos montar um exemplo simples: imagine que você irá fazer um joguinho onde o usuário terá 10 tentativas para adivinhar um número secreto. Um bom primeiro passo seria criar um loop que conta as 10 tentativas:

```python
numero_secreto = 42

contador = 0

while contador < 10:
  tentativa = int(input('Adivinhe o número secreto: '))
  if tentativa == numero_secreto:
    print('Acertou')
  else:
    print('Errou')
  contador += 1
```

No momento, mesmo que o usuário acerte, ele irá contar até a décima tentativa. Com o que já aprendemos até o momento, poderíamos consertar isso colocando uma segunda condição de parada:

```python
numero_secreto = 42

contador = 0

tentativa = 0

while contador < 10 and tentativa != numero_secreto:
  tentativa = int(input('Adivinhe o número secreto: '))
  if tentativa == numero_secreto:
    print('Acertou')
  else:
    print('Errou')
  contador += 1
```

Se você executar o programa, verá que ele funciona: caso o usuário acerte ou 10 tentativas sejam feitas, o programa encerra sua execução. Mas note que o código ficou um pouquinho mais bagunçado: estamos testando duas vezes o valor de `tentativa`: na condição do `while` e na condição do `if`. Não seria mais prático dentro do próprio `if`, logo após informar para o usuário que ele acertou, se a gente já pudesse falar para o loop parar de ser executado?

É aí que entra o `break`: quando estamos em uma malha de repetição e encontramos o comando `break`, a malha é **interrompida imediatamente**. Podemos reescrever o programa acima utilizando esse comando:

```python
numero_secreto = 42

contador = 0

while contador < 10:
  tentativa = int(input('Adivinhe o número secreto: '))
  if tentativa == numero_secreto:
    print('Acertou')
    break
  print('Errou')
  contador += 1
```

> [!WARNING]
> Alguns programadores utilizam `while True:` (ou seja, um loop a princípio infinito) e no corpo do loop espalham combinações de `if` + `break`. Exceto em situações muito específicas e raras, isso é uma **má prática** e deve ser evitada, pois compromete bastante a legibilidade do código, e consequentemente sua manutenção no futuro.

### 14.2. Else

Você pode observar que no programa acima, respondemos "Errou" para cada chute errado do usuário. Mas o programa ainda não informou para ele que as tentativas dele se esgotaram. Temos algumas possibilidades aqui!

Uma delas seria testar o valor do contador no final do loop:

```python
numero_secreto = 42

contador = 0

while contador < 10:
  tentativa = int(input('Adivinhe o número secreto: '))
  if tentativa == numero_secreto:
    print('Acertou')
    break
  print('Errou')
  contador += 1
  if contador == 10:
    print('Acabaram as tentativas. Você perdeu.')
```

Outra seria utilizar uma **flag**: uma variável booleana que indica se entramos no `if` ou não:

```python
numero_secreto = 42

contador = 0

acertou = False

while contador < 10:
  tentativa = int(input('Adivinhe o número secreto: '))
  if tentativa == numero_secreto:
    acertou = True
    break
  print('Errou')
  contador += 1

if acertou:
  print('Acertou!')
else:
  print('Acabaram as tentativas. Você perdeu.')
```

Na maioria das linguagens de programação, teríamos que optar por uma dessas alternativas. Comandos que estudamos aqui em Python são comuns a várias linguagens diferentes, incluindo o par `if`/`else`, o `while` e o `break`.

Mas o Python possui uma ferramenta adicional bastante incomum, mas que pode simplificar problemas desse tipo. Ele permite a utilização de um `else` para um loop. A estrutura deve ser a seguinte:

```python
while (condicao_principal):
  ...
  ...
  if (condicao_secundaria):
    break
  ...
  ...
else:
  ...
```

Esse código funcionará da seguinte maneira: se o loop parar pela condição principal (ou seja, executou a quantidade "correta" de repetições), o `else` será executado. Se o loop parar pela condição secundária (ou seja, por conta de um `break`), o `else` será ignorado.

Sendo assim, podemos reescrever nosso programa principal de maneira mais **pythonica** utilizando esse recurso:

```python
numero_secreto = 42

contador = 0

while contador < 10:
  tentativa = int(input('Adivinhe o número secreto: '))
  if tentativa == numero_secreto:
    print('Acertou!')
    break
  print('Errou')
  contador += 1
else:
  print('Acabaram as tentativas. Você perdeu.')
```

Execute o programa e veja que ele só irá mostrar a mensagem de derrota quando as 10 tentativas forem concluídas.

### 14.3. Continue

Existe outro comando de desvio de fluxo de malhas de repetição: o `continue`. A diferença entre ele e o `break` é que o `continue` **encerra apenas o passo atual** de repetição, mas ele **não encerra o loop como um todo**. Quando executamos esse comando, o loop irá voltar para o topo, testar novamente sua condição de parada, e caso ela não tenha sido atingida, ele iniciará uma nova **iteração** (ou seja, um novo passo em um loop).

Vamos reescrever nosso programa anterior invertendo a verificação para vermos o `continue` em ação.

```python
numero_secreto = 42

contador = 0

while contador < 10:
  tentativa = int(input('Adivinhe o número secreto: '))
  contador += 1
  if tentativa != numero_secreto:
    print('Errou!')
    continue
  print('Acertou!')
  break
else:
  print('Acabaram as tentativas. Você perdeu.')
```

Sempre que o usuário errar o chute, o `continue` irá desviar o fluxo de execução de volta para o início do loop, impedindo que as duas últimas linhas do loop sejam executadas. Ou seja, ele não irá dizer "acertou", tampouco executar o `break`.

> [!CAUTION]
> **Atenção:** todos os desvios estudados aqui podem ser utilizados, caso contrário, não existiriam. Porém, em certas situações eles podem tornar o código mais confuso. Por exemplo, quando temos diversos loops aninhados, pode não ficar claro para alguém lendo o código qual dos loops está sendo encerrado. Sempre que for utilizar esses recursos, verifiquem se eles estão melhorando ou piorando a legibilidade do código.

---

# Malhas de repetição com contador

No capítulo de malhas de repetição vimos casos em que precisamos contar quantas vezes o loop se repete, e parar quando a contagem atinge um certo valor. Em outras ocasiões, apenas precisamos de algum tipo de sequência numérica. Nestes casos, era normal utilizar uma variável de contador, incrementá-la em cada passo e utilizar seu valor como condição de parada. O exemplo abaixo imprime todos os números pares entre 0 e 100:

```python
contador = 0
while contador < 100:
    print(contador)
    contador = contador + 2
```

Existe um meio de automatizar todas as operações envolvidas: atribuir um valor inicial, atribuir um valor final e realizar o incremento.

### 15.1 Loops do tipo "para"

Dizemos que o exemplo acima é um loop do tipo "para": **para** contador **de** 0 **até** 100 **com passo** 2 **faça**: imprima contador. Em Python, podemos criar esse tipo de loop utilizando os comandos `for` e `range`. O exemplo abaixo imprime os números de 0 até 9 na tela:

```python
for contador in range(10):
    print(contador)
```

O código acima é equivalente ao seguinte código utilizando `while`:

```python
contador = 0
while contador < 10:
    print(contador)
    contador += 1
```

A palavra "contador" é apenas uma variável. Ela não precisa ser criada previamente: qualquer nome utilizado nesta construção será automaticamente inicializado pelo `for`.

O programa acima atribui o valor inicial 0 à variável. Em seguida, ele executa tudo que vier dentro do loop, e ao chegar ao final, ele retorna ao início, soma 1 na variável e testa se o seu valor atingiu o número entre parênteses. Caso não tenha atingido, ele repete a execução. Dizemos que aquele número é o **valor final exclusivo** (pois o loop exclui esse valor).

De forma geral, tudo que vier dentro de um `for contador in range(x)` irá executar "x" vezes. É o jeito fácil de dizer "repita essas linhas x vezes" em Python.

### 15.2 Parâmetros do range

Foi dito que loops do tipo "para" seguem a forma "para contador de X até Y passo Z faça:". No exemplo acima, os valores iniciais (0) e passo (1) foram atribuídos de forma automática. Caso eles sejam omitidos, 0 e 1 são os valores padrão, respectivamente. Porém, podemos determiná-los, se necessário. O exemplo abaixo inicia a impressão dos números em 1 ao invés de 0:

```python
for contador in range(1, 10):
    print(contador)
```

Dizemos que esse loop possui valor inicial `1`, valor final (exclusivo) `10` e passo `1`.

O código acima é equivalente ao seguinte código utilizando `while`:

```python
contador = 1
while contador < 10:
    print(contador)
    contador += 1
```

Assim como manipulamos o valor inicial e o final, podemos manipular também o passo. Veja o exemplo abaixo:

```python
for contador in range(0, 100, 2):
    print(contador)
```

O código acima é equivalente ao seguinte código utilizando `while`:

```python
contador = 0
while contador < 100:
    print(contador)
    contador += 2
```

Note que o resultado dele na tela é exatamente o mesmo do exemplo com `while` do início deste capítulo! Valor inicial `0`, valor final (exclusivo) `100` e passo `2`. Porém, não precisamos nos preocupar em criar o contador, atribuir valor inicial, incrementar e criar uma condição de parada. Apenas colocamos os números dentro do `range` e ele fez a mágica por nós.

Antes de finalizar, vamos reforçar: o comportamento de cada parâmetro passado para o `range` depende de quantos parâmetros foram passados e da ordem que eles foram passados:

- **1 parâmetro** = valor final exclusivo
- **2 parâmetros** = valor inicial, valor final exclusivo
- **3 parâmetros** = valor inicial, valor final exclusivo, passo

Quantos exercícios de `while` você fez que podem ser resolvidos de maneira mais fácil com o `for`?

> [!TIP]
> É possível utilizar o `for` para gerar sequências numéricas **decrescentes** também. Basta adotar valor final menor do que o inicial e incremento negativo.
>
> ```python
> for contador in range(20, 0, -1):
>   print(contador)
> ```
>
> Qual valor será excluído da sequência: o `20` ou o `0`? Tente deduzir e execute o programa para ver se acertou!

### 15.3. Comandos de desvio de fluxo

Os comandos de desvio de fluxo que estudamos junto do `while` (`break`, `continue` e `else`) também funcionam da mesma maneira com o `for`. Algumas observações sobre eles:

- **`break`**: irá encerrar o loop antes de atingir o fim da sequência
- **`else`**: será executado caso um `break` **não** seja executado e ignorado caso o loop chegue ao final da sequência
- **`continue`**: encerra o passo atual e passa para o próximo avançando na sequência automaticamente

---

# Listas

Já fizemos alguns programas para ler 2 ou 3 notas e calcular a média. Inclusive já fomos além e aprendemos a verificar se o aluno passou ou não. Vamos rever um exemplo desses:

```python
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

print(media)
```

Simples, certo? Mas e se a regra da escola mudasse, e agora cada professor precisasse aplicar 4 provas? Modificaríamos nosso programa:

```python
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4)/4

print(media)
```

Até aqui tudo bem. Mas e se o objetivo fosse testar o quanto o professor consegue ensinar? Para isso, poderíamos calcular a média das médias de todos os alunos do professor. Mas e se o professor trabalha em uma faculdade muito grande e suas turmas têm 80 alunos?

```python
aluno1 = float(input('Digite a nota do aluno 1: '))
aluno2 = float(input('Digite a nota do aluno 2: '))
aluno3 = float(input('Digite a nota do aluno 3: '))
aluno4 = float(input('Digite a nota do aluno 4: '))
aluno5 = float(input('Digite a nota do aluno 5: '))
aluno6 = float(input('Digite a nota do aluno 6: '))
aluno7 = float(input('Digite a nota do aluno 7: '))
aluno8 = float(input('Digite a nota do aluno 8: '))
aluno9 = float(input('Digite a nota do aluno 9: '))
aluno10 = float(input('Digite a nota do aluno 10: '))

# ...
```

> [!CAUTION]
> **Nota do programador:** eu me demito.
> Não ganho bem o suficiente para ISSO!

Para trabalhar com poucos valores, é fácil e conveniente criar uma variável para cada valor e realizar operações individualmente sobre cada uma. Porém, dizemos que esse tipo de solução **não é escalável**: o programa não está preparado para lidar com variações no tamanho da base de dados, e modificá-lo para comportá-las pode ser difícil, trabalhoso ou mesmo inviável.

Imagine se para cada novo perfil em uma rede social o estagiário precisasse criar uma variável nova para o nome, uma para o e-mail, uma para a data de nascimento, e assim sucessivamente... E depois ainda precisasse de linhas novas de código para ler cada um desses valores do novo usuário!

## 16. Listas

É aí que entram as **listas**. Listas são **coleções de objetos** em Python. Falando de maneira simplificada, são variáveis que comportam diversos valores ao mesmo tempo. Vejamos alguns jeitos de criar listas em Python:

```python
primeira_lista = []                              # cria uma lista vazia
segunda_lista = list()                           # cria uma lista vazia
terceira_lista = [1, 3.14, 5, 7, 9, 'onze']     # lista com valores
```

Note que podemos misturar tipos de dados. A `terceira_lista` possui 4 `int`, um `float` e uma `str`.

Bom, e agora, como fazemos para acessar cada valor? Podemos imaginar a lista da seguinte maneira: imagine que ao invés de ter uma caixa para guardar cada item, temos uma cômoda com várias gavetas. Cada item está em uma gaveta. Não estamos acostumados a dizer que algo está na terceira gaveta do armário? A ideia é a mesma: a lista é uma **coleção indexada**, ou seja, podemos acessar cada elemento através de **índices**, que são números indicando a posição. A indexação é automática e **começa a partir do zero**:

| elemento | 1 | 3.14 | 5 | 7 | 9 | 11 |
|----------|---|------|---|---|---|-----|
| índice | 0 | 1 | 2 | 3 | 4 | 5 |

Portanto, para acessar o elemento `"7"` da nossa lista, utilizaríamos o índice `3`. Informamos o índice entre colchetes:

```python
terceira_lista = [1, 3.14, 5, 7, 9, 'onze']  # lista com valores
print(terceira_lista[3])
```

A lista é **mutável**. Isso significa que podemos modificar os valores já existentes:

```python
terceira_lista = [1, 3.14, 5, 7, 9, 'onze']  # lista com valores
terceira_lista[3] = 'sete'                    # troca 7 por 'sete' na lista
print(terceira_lista)
```

É possível utilizar **índices negativos**. `lista[-1]` pega o último elemento, `lista[-2]` o penúltimo, e assim sucessivamente. Mas **não é possível** acessar índices iguais ou superiores ao tamanho da lista. A tentativa de acessar um índice inexistente resultará em erro.

## 17. Quebrando listas

É possível pegar subconjuntos de nossas listas utilizando o conceito de **slices**. Ao invés de passar apenas 1 valor entre colchetes (o índice desejado), podemos passar faixas de valores. Veja o exemplo abaixo:

```python
impares = [1, 3, 5, 7, 9, 11, 13, 15, 17]
meio = impares[3:6]
print(meio)  # resultado na tela: [7, 9, 11]
```

O primeiro valor é o índice inicial da sublista a ser gerada, e o segundo é o índice final (**exclusivo**). Podemos omitir um desses valores para indicar que será desde o início ou até o final:

```python
impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
primeira_metade = impares[:5]
segunda_metade = impares[5:]
print(primeira_metade)  # resultado: [1, 3, 5, 7, 9]
print(segunda_metade)   # resultado: [11, 13, 15, 17, 19]
```

Além de índices inicial e final, podemos também passar um **passo** para os índices. Veja o exemplo abaixo:

```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# múltiplos de 3 abaixo de 10:
mult3_sub10 = numeros[3:10:3]
print(mult3_sub10)  # resultado: [3, 6, 9]
```

> [!WARNING]
> **Atenção:** quando nós atribuímos uma lista a outra variável, a lista **não é copiada**. Observe o exemplo abaixo:
>
> ```python
> lista1 = [1, 3, 5]
> lista2 = lista1
> lista2.append(7)
> print(lista1)  # resultado: [1, 3, 5, 7]
> ```
>
> Modificações aplicadas em `lista2` também afetarão a `lista1`. Isso ocorre porque não foi criada uma lista. O Python apenas fez com que ambas as variáveis (`lista1` e `lista2`) referenciassem a **mesma estrutura na memória**. Quando utilizamos slices, isso não ocorre. O Python cria uma lista contendo os valores restritos pelos índices. Sendo assim, uma estratégia fácil para copiar uma lista para outra é utilizar um slice indo da primeira à última posição:
>
> ```python
> lista1 = [1, 3, 5]
> lista2 = lista1[:]
> lista2.append(7)
> print(lista1)  # resultado: [1, 3, 5]
> print(lista2)  # resultado: [1, 3, 5, 7]
> ```

## 18. Percorrendo listas

Suponha que você queira acessar cada elemento de sua lista individualmente. Digitar todos os índices manualmente cancelaria a escalabilidade do programa, certo? Portanto, podemos usar um loop para gerar os índices:

```python
pares = [0, 2, 4, 6, 8]
tamanho = len(pares)  # calcula o tamanho da lista

# tamanho vale 5, logo índice recebe os valores 0, 1, 2, 3 e 4
for indice in range(tamanho):
  print(pares[indice])
```

Porém, tem um jeito ainda mais fácil de percorrer a lista. O `for` não serve apenas para gerar sequências numéricas junto do `range`: ele serve para **percorrer coleções**. Portanto, podemos trocar o `range` pela própria lista:

```python
pares = [0, 2, 4, 6, 8]

for elemento in pares:
  print(elemento)
```

Assim como no caso das contagens, `"elemento"` é apenas uma variável que será criada de forma automática e poderia ter qualquer nome. Em cada repetição do loop, um valor diferente da lista será copiado para `elemento`.

> [!IMPORTANT]
> Como os elementos são **copiados**, caso você modifique o valor de `elemento` você não irá modificar o valor na lista, e sim uma cópia dele. Além disso, como este loop serve especificamente para percorrer listas, se dentro dele você fizer operações que alterem o tamanho da lista (`append` ou `remove`, por exemplo), o loop poderá executar incorretamente, pulando ou repetindo elementos.

O `for` serve, primariamente, para percorrer coleções. Ou seja, para **iterar** coleções. O `range` age, na prática, como se fosse uma lista contendo os valores determinados por seu parâmetro. Dizemos que a função `range` gera um **iterável**, ou seja, um tipo especial de dado que pode ser percorrido através de um loop.

## 19. Testando a existência de valores

Existe um comando que temos visto bastante recentemente: o `in`. Ele costuma aparecer no `for` para indicar a lista ou a sequência a ser percorrida. Mas ele também possui outra utilidade.

O `in` pode ser utilizado para informar se um elemento está presente em uma lista ou não. Observe a saída do código abaixo.

```python
linguagens = ['Python', 'JavaScript', 'C#', 'Java']

existe_html = 'HTML' in linguagens
existe_java = 'Java' in linguagens

print('HTML:', existe_html)  # HTML: False
print('Java:', existe_java)  # Java: True
```

Normalmente utilizamos esse comando junto de um `if` quando precisamos checar se um elemento existe:

```python
linguagem_desejada = input('Digite a linguagem que você gostaria de aprender: ')

linguagens = ['Python', 'JavaScript', 'C#', 'Java']

if linguagem_desejada in linguagens:
  print('Faça o curso conosco! :)')
else:
  print('Não temos esse curso disponível no momento :(')
```

---

# Funções de listas

As listas possuem diversas funções prontas bastante úteis. Veremos algumas das mais usadas. Não se preocupe em decorar todas elas: sempre podemos consultar nosso material quando precisarmos de um lembrete! Com tempo e prática você irá aos poucos memorizar algumas delas.

## 20. Adicionando elementos

Podemos adicionar novos elementos na lista de duas maneiras. A primeira delas, mais simples, é o `append`. Ele adiciona um elemento **ao final da lista**. Veja o exemplo abaixo:

```python
pares = [0, 2, 4, 6, 8]
pares.append(10)
print(pares)  # resultado: [0, 2, 4, 6, 8, 10]
```

Outra maneira é com o `insert`: além do elemento, ele recebe a **posição** do novo elemento. O primeiro parâmetro é a posição, e a segunda é o valor.

```python
pares = [0, 2, 4, 8, 10]
pares.insert(3, 6)
print(pares)  # resultado: [0, 2, 4, 6, 8, 10]
```

Note que o valor que ocupava a posição anteriormente não é substituído, mas "empurrado" para a próxima posição.

## 21. Removendo elementos

Podemos remover o elemento de 2 jeitos: **por valor** e **por posição**. O `remove` irá remover o **primeiro elemento encontrado** na lista com um dado valor. Ex:

```python
impares = [1, 3, 3, 5, 7, 9]
impares.remove(3)
print(impares)  # resultado: [1, 3, 5, 7, 9]
```

O `pop` remove o elemento que estiver em uma **dada posição**, independentemente de seu valor:

```python
impares = [1, 3, 5, 7, 8, 9]
impares.pop(4)
print(impares)  # resultado: [1, 3, 5, 7, 9]
```

Se nenhum valor for passado no `pop`, ele irá remover necessariamente o **último elemento** da lista.

## 22. Ordenando a lista

Podemos ordenar a lista usando o `sort`.

```python
fibonacci = [8, 1, 0, 5, 13, 1, 3, 2]
fibonacci.sort()
print(fibonacci)  # resultado: [0, 1, 1, 2, 3, 5, 8, 13]
```

Caso desejássemos ordenar em ordem **decrescente**, podemos passar a opção `reverse = True` para o `sort`:

```python
fibonacci = [8, 1, 0, 5, 13, 1, 3, 2]
fibonacci.sort(reverse = True)
print(fibonacci)
```

---

___


# Compreensão de listas e expressões geradoras

Muito do que estudamos até o momento em Python pode ser reproduzido de maneira parecida em outras linguagens. Comandos como `if`, `else`, `while` e `for`, bem como conceitos como criar funções, passar parâmetros e retornar valores são comuns a uma infinidade de linguagens de programação.

Porém, um dos objetivos da linguagem Python é realizar o máximo possível de trabalho com a menor quantidade possível de código, resultando em um código mais limpo e com menos efeitos colaterais.

Com isso, o Python traz maneiras diferentes e mais enxutas de resolver problemas que já lidávamos bem utilizando outras técnicas. Parte dessas técnicas foi inspirada em conceitos de programação funcional, que será explicada um pouco melhor em um capítulo futuro.

As compreensões de listas e expressões geradoras são algumas dessas ferramentas.

## 1. Compreensão de listas

### 1.1. Compreensão de listas contendo apenas um loop

Vamos considerar um problema simples: montar uma lista com os quadrados dos números de 1 até 10. Você provavelmente resolveria esse problema da seguinte maneira:

```python
quadrados = []

for x in range(1, 11):
    quadrados.append(x**2)

print(quadrados)
print(x)
```

Note que utilizamos 3 linhas de código para criar uma lista: uma para declarar a lista, uma para percorrer alguns valores e uma para executar o cálculo e adicionar o resultado à lista.

Além disso, criamos uma variável extra, `x`, que segue existindo em nosso programa mesmo após o loop, como você pode observar pelo segundo `print` do exemplo.

A compreensão de listas resolve todos esses problemas: iremos resumir em uma única linha a criação da nova lista já com todos os valores desejados, e sem variáveis sobrando após a execução:

```python
quadrados_compreensao = [num**2 for num in range(1, 11)]

print(quadrados_compreensao)
```

Note que a variável `x`, criada na versão extensa, ainda existe. A variável `num`, utilizada na compreensão, não:

```python
print('x:', x) # imprime 10
print('num:', num) # erro de variável não existente
```

Vale destacar que você não precisa necessariamente utilizar `range` em suas compreensões. Você pode utilizar qualquer tipo de iterável, como listas, tuplas, strings etc.

O exemplo abaixo monta uma lista contendo a metade do valor de cada elemento de uma outra lista:

```python
numeros = [1, 9, 4, 7, 6, 2]

metades = [n/2 for n in numeros]

print(metades)
```

### 1.2. Condicionais em compreensões

Podemos utilizar compreensões em nossas condicionais. Imagine que não fossem aceitos valores "quebrados" no exemplo anterior. Logo, não podemos dividir os números ímpares, apenas os pares. Fazemos isso usando um `if` na expressão:

```python
metades_pares = [n/2 for n in numeros if n % 2 == 0]
print(metades_pares)
```

Podemos também utilizar `else` na expressão. Vejamos mais um exemplo:

Considere que são aceitos números quebrados no exemplo das metades. Porém, não queremos utilizar o tipo `float` desnecessariamente. Portanto, faremos uma divisão inteira quando o número for par (para que o resultado seja `int`) e uma divisão real quando o número for ímpar (para que o resultado seja `float`). A expressão ficaria assim:

```python
metades_tipo = [n//2 if n % 2 == 0 else n/2 for n in numeros]

print(metades_tipo)
```

Note que quando usamos o `else`, a ordem da compreensão sofre uma alteração. Quando usamos apenas o `if`, ele vem após o `for`. Com o `else`, ambos vêm antes.

Outro ponto importante é que no caso do `else` passamos a ter uma segunda expressão. Quando a condição do `if` é verdadeira, a compreensão irá executar a expressão original. Caso contrário, ela irá executar a expressão do `else`.

Generalizando a sintaxe das compreensões de lista, temos as seguintes combinações:

```python
lista = [expressao for item in colecao]

# equivale a:

for item in colecao:
    lista.append(expressao)
```

```python
[expressao for item in colecao if condicao]

# equivale a:

for item in colecao:
    if condicao:
        lista.append(expressao)
```

```python
[expressao if condicao else expressao_alternativa for item in colecao]

# equivale a:

for item in colecao:
    if condicao:
        lista.append(expressao)
    else:
        lista.append(expressao_alternativa)
```

### 1.3. Aninhando compreensões

É possível aninhar compreensões de lista. Ao colocarmos mais de um `for` consecutivo, o primeiro `for` será considerado o mais externo, e o seguinte, mais interno. O exemplo abaixo mostra todas as combinações possíveis entre alguns nomes e sobrenomes:

```python
nomes = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Emília']
sobrenomes = ['Silva', 'Oliveira']

combinacoes = [nome + ' ' + sobrenome for nome in nomes for sobrenome in sobrenomes]
print(combinacoes)
```

A linha `combinacoes = [nome + ' ' + sobrenome for nome in nomes for sobrenome in sobrenomes]` equivale a:

```python
combinacoes = []

for nome in nomes:
    for sobrenome in sobrenomes:
        combinacoes.append(nome + ' ' + sobrenome)
```

Inclusive podemos utilizar essa forma para trabalhar com matrizes. O exemplo abaixo lê pelo teclado a quantidade de vitórias, empates e derrotas para cada time em um grupo:

```python
times = ['Atlético Python', 'JavaScript United', 'C Seniors', 'Javeiros do Norte']
entradas = ['V', 'E', 'D']

tabela = [[int(input(f'Digite a quantidade de {tipo} do time {time}: ')) for tipo in entradas] for time in times]

print(tabela)
```

## 2. Expressões geradoras

### 2.1. Criando uma expressão geradora

Se você executar o código abaixo, não notará erros de execução. Ambas as linhas executam com sucesso:

```python
colchetes = [x for x in range(10)]

parenteses = (x for x in range(10))
```

Listas são representadas por colchetes, e fazemos compreensão de listas utilizando colchetes. Dicionários utilizam chaves (`{` e `}`), e utilizamos chaves para fazer compreensão de dicionários. A expressão entre parênteses só pode ser uma tupla, certo?

Errado. Não existe compreensão de tuplas em Python. Quando colocamos uma expressão semelhante a uma compreensão de lista entre parênteses, estamos criando uma **expressão geradora**. Note que podemos iterar uma expressão geradora:

```python
gerador_quadrados = (x**2 for x in range(10))

for quadrado in gerador_quadrados:
    print(quadrado)
```

Também podemos convertê-la para outras estruturas, como uma lista ou uma tupla:

```python
gerador_impares = (x for x in range(20) if x % 2 == 1)

lista_impares = list(gerador_impares)

print(lista_impares)
```

Porém, não podemos utilizar nosso gerador uma segunda vez. Execute o código abaixo:

```python
gerador_quadrados = (x**2 for x in range(10))

for quadrado in gerador_quadrados:
    print(quadrado)

lista_quadrados = list(gerador_quadrados)
print(lista_quadrados) # imprime uma lista vazia
```

Para entender porque o resultado foi uma lista vazia, precisamos entender a diferença entre um iterável e um iterador em Python.

### 2.2 Iteráveis e iteradores

Um **iterável** é um objeto em Python que podemos percorrer utilizando um loop. Geralmente pensamos em iteráveis como algum tipo de coleção. Listas, tuplas, dicionários e strings são todos iteráveis.

Porém, o que o loop realmente utiliza não é o iterável, mas o **iterador**. Quando tentamos percorrer um iterável, é criado um iterador a partir dele utilizando a função `iter`. Em cada passo da iteração (do loop), a função `next` é chamada, e ela irá retornar o próximo elemento. Quando os elementos são esgotados, ela irá lançar a exceção (uma espécie de erro sinalizado, que estudaremos em um capítulo futuro) `StopIteration`.

Veja o exemplo abaixo:

```python
lista = [1, 3, 5]

iterador = iter(lista)

print(iterador)

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador)) # Erro: StopIteration
```

Uma diferença fundamental entre um iterável e um iterador é que o iterador já possui todos os exemplos salvos em algum lugar. O iterável não. Ele irá gerar/buscar cada elemento no momento que a função `next` é chamada, e ele não irá salvar os elementos anteriores.

Uma expressão geradora não é um iterável, ela é um iterador. Uma lista é um iterável.

Ou seja, quando nós fazemos uma compreensão de lista, a expressão é avaliada na mesma hora e todos os elementos são gerados e salvos na memória.

Quando utilizamos uma expressão geradora, cada elemento é gerado apenas quando solicitado, e os elementos não ficam salvos.

```python
gerador = (x for x in range(5))

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador)) # Erro: StopIteration
```

Podemos utilizar expressões geradoras quando:

- Iremos trabalhar com uma base de dados tão grande que a geração da lista pode ser excessivamente lenta ou consumir memória demais.
- Quando desejamos obter dados infinitos (uma sequência numérica sem fim, ou então um stream de dados que pode estar chegando por um sensor ou pela internet, por exemplo).
- Quando sabemos com certeza absoluta que só precisaremos iterar uma única vez por cada elemento e não precisaremos deles posteriormente.

Caso você precise dos dados mais de uma vez, a expressão geradora deixa de ser atrativa e compensa mais utilizar compreensão de listas.

## 3. Funções geradoras

Expressões geradoras são uma forma compacta para criar iteradores. Uma das formas mais completas envolve utilizar programação orientada a objeto para definir uma classe com alguns métodos específicos para que os objetos se comportem como geradores. A outra envolve utilizar uma função geradora.

Funções geradoras lembram bastante funções convencionais, mas em vez de `return` elas utilizarão a palavra `yield`.

A função irá retornar um iterador, e iremos sempre chamar `next` passando esse gerador.

Cada vez que o `next` for chamado, o iterador irá executar a função até encontrar o `yield`. O estado da função é salvo e o valor do `yield` é retornado. Quando chamarmos `next` novamente, a função irá executar do ponto que parou até encontrar novamente o `yield`. Quando não houver mais `yield`, a exceção `StopIteration` será lançada.

Vejamos um exemplo:

```python
def funcao_geradora():
    yield 1
    yield 3
    yield 5

meu_gerador = funcao_geradora()

print(next(meu_gerador))
print(next(meu_gerador))
print(next(meu_gerador))
print(next(meu_gerador)) # erro: StopIteration
```

A nossa função geradora pode, inclusive, ter malhas de repetição:

```python
def gerador_de_sequencia(limite:int):
    contador = 0
    while contador < limite:
        yield contador
        contador += 1

iterador_sequencia = gerador_de_sequencia(10)

for x in iterador_sequencia:
    print(x)
```

Caso tenha interesse em se aprofundar nos assuntos deste capítulo e ver alguns experimentos envolvendo tamanho e performance de cada um, segue algumas boas referências:

- https://djangostars.com/blog/list-comprehensions-and-generator-expressions/
- https://towardsdatascience.com/comprehensions-and-generator-expression-in-python-2ae01c48fc50
- https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions

---

# Tuplas

Neste capítulo estudaremos uma estrutura de dados, ou seja, uma forma estruturada de armazenar múltiplos dados. Você provavelmente já estudou pelo menos outra estrutura de dados em Python: a lista.

Vamos brevemente revisar os conceitos de lista, pois eles serão úteis para compreender nossa nova estrutura, a tupla.

Focaremos em funcionalidades, não em funções prontas e métodos de lista.

## 4. Revisão de listas

### 4.1. Criando uma lista e acessando elementos

A lista é uma coleção de objetos em Python. Criando uma única variável para representar a lista, podemos armazenar múltiplos valores. Internamente, esses valores são representados por seus índices: um número inteiro, iniciando em zero e incrementando com passo unitário.

Podemos criar uma lista através da função `list` ou utilizando um par de colchetes:

```python
lista1 = list() # uma lista vazia

lista2 = [] # outra lista vazia

linguagens = ['Python', 'JavaScript', 'SQL'] # uma lista com 3 elementos

dados_variados = [3.14, 1000, True, 'abacate'] # uma lista com dados de tipos diversos

lista_de_listas = [ ['Curso', 'Módulo 1', 'Módulo 2'], ['Data Science', 'Lógica de Programação I', 'Lógica de Programação II'], ['Web Full Stack', 'Front End Estático', 'Front End Dinâmico']]

print(linguagens[0]) # imprime "Python"
print(linguagens[1]) # imprime "JavaScript"
print(dados_variados[2]) # imprime True
print(lista_de_listas[2][0]) # imprime "Web Full Stack"
```

### 4.2. Iterando uma lista

Como os elementos em uma lista são representados por números inteiros, podemos facilmente percorrê-la variando seu índice de maneira automatizada:

```python
for indice in range(4):
    print(dados_variados[indice])
```

Apesar de funcionar, essa forma é considerada pouco legível. Existe uma maneira mais direta de percorrer uma lista. Ao trocarmos a função `range` do nosso `for` pela própria lista, ele irá copiar cada elemento da lista para a variável temporária. Assim conseguimos facilmente, e de maneira bem legível, acessar todos os elementos de uma lista:

```python
for elemento in dados_variados:
    print(elemento)
```

Caso tenhamos listas aninhadas, podemos percorrê-las aninhando loops. Utilizamos um loop para cada "nível" de lista. Execute o bloco abaixo e veja seu resultado na tela:

```python
for linha in lista_de_listas:
    for elemento in linha:
        print(elemento)
```

### 4.3. Slicing de listas

Uma operação bastante comum em uma lista é extrair apenas uma parte dela. Para isso você deve informar, pelo menos, o índice inicial e o índice final, sendo que o índice final não irá entrar na conta — dizemos que ele é um valor "exclusivo", como se fosse um intervalo aberto naquele ponto.

```python
frutas = ['abacate', 'banana', 'carambola', 'damasco', 'embaúba', 'framboesa', 'goiaba']

algumas_frutas = frutas[2:5] 

print(algumas_frutas) # resultado: ['carambola', 'damasco', 'embaúba']
```

Você pode deixar um dos dois índices em branco. Na ausência do primeiro índice, a operação se iniciará com o índice 0 da lista original. Na ausência do segundo, a operação seguirá até o final da lista original.

```python
primeiras3 = frutas[:3]
print(primeiras3)

ultimas3 = frutas[4:]
print(ultimas3)
```

Também podemos utilizar índices negativos. O índice -1 acessa o último elemento da lista, o -2 acessa o penúltimo, e assim sucessivamente. Podemos reescrever o exemplo anterior utilizando números negativos para facilitar ainda mais a legibilidade e tornar o exemplo mais genérico e independente do tamanho da lista:

```python
ultimas3 = frutas[-3:]
print(ultimas3)
```

Você deve se recordar que atribuir uma lista para outra não copia a lista. Veja o exemplo abaixo:

```python
copia_frutas = frutas
copia_frutas.append('heisteria')
print(frutas) # resultado na tela: ['abacate', 'banana', 'carambola', 'damasco', 'embaúba', 'framboesa', 'goiaba', 'heisteria']
```

Quando atribuímos uma lista existente para uma variável, a variável irá referenciar a mesma lista na memória. Portanto, operações realizadas na lista "nova" irão afetar a lista "antiga". Não houve a criação de uma nova lista de fato.

Uma forma fácil de copiar de verdade uma lista para outra lista é utilizar um slice indo do início até o final da lista original:

```python
copia_frutas = frutas[:]
print(copia_frutas)
```

`copia_frutas` e `frutas` não referenciam a mesma lista. Elas referenciam duas listas diferentes contendo os mesmos elementos, mas modificações feitas em uma delas não irão afetar a outra.

É possível passar mais um valor representando um passo ou salto. Por exemplo, podemos pegar os elementos das posições ímpares da lista começando na posição 1 e adotando salto igual a 2:

```python
impares = frutas[1::2]
print(impares)
```

Com saltos negativos, é fácil inverter uma lista:

```python
frutas_inv = frutas[-1::-1]
print(frutas_inv)
```

### 4.4. Concatenação de listas

Uma operação útil em listas é a concatenação. Quando "somamos" duas listas, utilizando o operador `+`, teremos uma nova lista com os elementos das duas listas originais em ordem de aparição:

```python
ds = ['Python', 'SQL', 'R']
web = ['HTML', 'CSS', 'JavaScript']

linguagens = ds + web
print(linguagens) 
#resultado: ['Python', 'SQL', 'R', 'HTML', 'CSS', 'JavaScript']
```

## 5. Tuplas

### 5.1. Operações básicas

Assim como as listas, tuplas também são coleções de objetos. Elas podem armazenar diversos objetos de diferentes tipos. Elas também possuem índice, que se comporta da mesma maneira que os índices de uma lista. Podemos criar tuplas utilizando parênteses ou a função `tuple`. Caso a tupla possua pelo menos 2 elementos, não precisamos dos parênteses, basta separar os valores por vírgula, apesar de ser recomendável utilizá-los para evitar ambiguidades:

```python
tupla1 = tuple() # uma tupla vazia

tupla2 = () # outra tupla vazia

linguagens = ('Python', 'JavaScript', 'SQL') # uma tupla com 3 elementos

dados_variados = 3.14, 1000, True, 'abacate' # uma tupla declarada sem parênteses

tupla_de_tuplas = ( ('Curso', 'Módulo 1', 'Módulo 2'), ('Data Science', 'Lógica de Programação I', 'Lógica de Programação II'), ('Web Full Stack', 'Front End Estático', 'Front End Dinâmico'))

print(linguagens[0]) # imprime "Python"
print(linguagens[1]) # imprime "JavaScript"
print(dados_variados[2]) # imprime True
print(tupla_de_tuplas[2][0]) # imprime "Web Full Stack"
```

Todas as outras operações que revisamos hoje em listas podem ser realizadas com tuplas:

- iteração através de um loop do tipo `for`
- slicing passando índice inicial, final e salto
- concatenação

É possível também fazer conversão de lista para tupla e vice-versa:

```python
lista_frutas = ['abacate', 'banana', 'carambola', 'damasco', 'embaúba', 'framboesa', 'goiaba']

tupla_frutas = tuple(lista_frutas)
print(tupla_frutas)

nova_lista_frutas = list(tupla_frutas)
print(nova_lista_frutas)
```

### 5.2. Imutabilidade

Listas possuem uma propriedade que a tupla não possui: mutabilidade. O código abaixo irá funcionar para a operação na lista, mas irá falhar para a operação na tupla:

```python
lista_frutas = ['abacate', 'banana', 'carambola', 'damasco', 'embaúba', 'framboesa', 'goiaba']
tupla_frutas = ('abacate', 'banana', 'carambola', 'damasco', 'embaúba', 'framboesa', 'goiaba')

lista_frutas[0] = 'ananás'
print(lista_frutas)

tupla_frutas[0] = 'ananás' # erro
```

Por que alguém escolheria uma estrutura imutável? Por que usar uma lista com menos recursos? O principal motivo é precisamente quando não convém alterar os dados. Em Python é muito difícil "proibir" algo: nada impede outro programador de transformar a tupla em uma lista, fazer alterações na lista e salvar a nova tupla "por cima" da velha, utilizando o mesmo nome para a nova.

Porém, quando utilizamos uma tupla, estamos sinalizando que aqueles dados não deveriam ser alterados, e ninguém irá conseguir alterá-los por acidente. Para alterá-los será necessário realizar uma série de conversões de maneira intencional.

Isso aumenta um pouco a segurança e confiabilidade de nosso código em certas situações, evitando a alteração indevida de dados que podem ser críticos para o bom funcionamento do nosso programa.

Adicionalmente, em alguns contextos muito específicos — quantidades muito grandes de dados com uma grande quantidade de operações de leitura versus poucas ou nenhuma operação de escrita — a tupla pode oferecer desempenho significativamente superior à lista. São poucas as situações onde você sentirá essa diferença, seja porque para quantidades muito baixas de dados a lista possui uma série de otimizações que podem torná-la até mais veloz do que a tupla, seja porque para quantidades relativamente grandes de dados a lista ainda será razoavelmente rápida.

### 5.3. Desempacotamento de tupla

Uma operação bastante interessante que podemos realizar com tuplas é o **desempacotamento de tuplas**, que aparecerá em muitos locais com seu nome em inglês, *tuple unpacking*.

O desempacotamento de tupla é uma operação que permite facilmente atribuir o conteúdo de uma tupla a variáveis individuais, sem a necessidade de escrever múltiplas linhas de código e manipular índices. Vejamos um exemplo básico:

```python
x, y, z = ('Lista', 'Tupla', 'Dicionário')
print(x) # Lista
print(y) # Tupla
print(z) # Dicionário
```

Uma limitação inicial que temos com essa técnica é que precisamos utilizar exatamente 1 variável para cada elemento da tupla, mesmo que não estejamos interessados em todos os seus elementos. Podemos contornar isso utilizando o operador `*`. Ao utilizá-lo em uma das variáveis no desempacotamento, estamos sinalizando que ele pode receber múltiplos valores, formando uma coleção com parte dos valores:

```python
linguagens = ('Python', 'JavaScript', 'HTML', 'CSS', 'R')

primeira, *resto = linguagens
print(primeira) # Python
print(resto) # ['JavaScript', 'HTML', 'CSS', 'R']

*resto, ultima = linguagens
print(resto) # ['Python', 'JavaScript', 'HTML', 'CSS']
print(ultima) # R

primeira, *meio, ultima = linguagens
print(primeira) # Python
print(meio) # ['JavaScript', 'HTML', 'CSS']
print(ultima) # R
```

O desempacotamento também pode ser utilizado com listas. Um dos principais motivos para ele frequentemente ser lembrado como uma operação de tupla foi que ele inicialmente só existia, de fato, para tuplas, e foi implementado para listas em versões mais recentes do Python. Outro motivo está relacionado à imutabilidade: como a tupla é imutável, temos mais garantias de que sabemos qual dado está em cada posição dela, tornando essa operação mais confiável em tuplas do que em listas.

### 5.4. Operações com tuplas "implícitas"

O Python oferece alguns truques que permitem escrever códigos mais enxutos do que em outras linguagens, e parte desses truques utiliza sintaxe de tupla. Por exemplo, para criar duas variáveis e atribuir valores simultaneamente a elas, podemos utilizar vírgulas:

```python
x, y = 10, 20

print(x) # 10
print(y) # 20
```

Outro truque relacionado bastante comum é inverter o valor de duas variáveis:

```python
y, x = x, y

print(x) # 20
print(y) # 10
```

Esse tipo de operação é considerado **açúcar sintático**, ou seja, não acrescenta funcionalidades novas, apenas cria formas mais simples e legíveis de realizar operações que já éramos capazes de realizar anteriormente.

Internamente, o Python está usando lógica de criar e desempacotar tuplas para realizar esse tipo de operação.

## 6. Facilidades para iteração

Sempre que possível, é preferível iterar uma coleção — seja ela uma lista ou uma tupla — de maneira direta utilizando `for` sem índices. Há alguns problemas onde pode ser difícil escapar do índice, pois nossa lógica irá depender de posição de alguma maneira.

Veremos duas estruturas que irão nos auxiliar a fazer iteração por índice sem precisar utilizar uma estrutura pouco legível como:

```python
for indice in range(len(lista)):
    ...
    lista[indice] = ...
    ...
```

### 6.1. Enumerate

Considere um problema qualquer onde o índice importa. Por exemplo, suponha que você possua uma lista de strings e gostaria de exibi-la intercalando uma em letra maiúscula e outra em letra minúscula (assim como frequentemente representamos tabelas intercalando as cores de suas linhas em editores de planilha para melhorar a legibilidade).

A lógica desse problema poderia ser resolvida usando índice:

```python
lista_frutas = ['abacate', 'banana', 'carambola', 'damasco', 'embaúba', 'framboesa', 'goiaba']

for indice in range(len(lista_frutas)):
    if indice % 2 == 0:
        print(lista_frutas[indice].upper())
    else:
        print(lista_frutas[indice].lower())
```

Existe uma ferramenta em Python que pode nos ajudar a escrever de maneira mais pythonica, sem precisar acessar lista por índice: o `enumerate`. Primeiro, vamos entender o que ele faz e, em seguida, veremos como deixar o código mais limpo:

```python
for x in enumerate(lista_frutas):
    print(x)
```

Saída na tela:

```console
(0, 'abacate')
(1, 'banana')
(2, 'carambola')
(3, 'damasco')
(4, 'embaúba')
(5, 'framboesa')
(6, 'goiaba')
```

O `enumerate` montou uma estrutura onde cada elemento é uma tupla, sendo o primeiro elemento da tupla um índice da lista, e o segundo o valor associado àquele índice. Aplicando desempacotamento de tupla no `for`, podemos ter, simultaneamente, índice e valor em variáveis separadas, na prática percorrendo a lista tanto por índice quanto por valor. Refazendo o exemplo das maiúsculas/minúsculas:

```python
for indice, valor in enumerate(lista_frutas):
    if indice % 2 == 0:
        print(valor.upper())
    else:
        print(valor.lower())
```

### 6.2. Zip

Vamos pensar em um problema onde precisamos percorrer duas listas simultaneamente. Por exemplo, considere que temos uma lista com os nomes de todos os alunos de uma turma, e outra com as notas, na mesma ordem. Como faríamos para acessar, simultaneamente, o nome de um aluno e a sua nota?

Esse é um problema onde, a princípio, utilizaríamos índice. Se usarmos o mesmo índice nas duas listas, estamos na prática percorrendo ambas as listas simultaneamente:

```python
alunos = ['Paul', 'John', 'George', 'Ringo']
notas = [10, 9.5, 7, 6]

for indice in range(len(alunos)):
    print(f'Aluno {alunos[indice]}: {notas[indice]}')
```

Saída na tela:

```console
Aluno Paul: 10
Aluno John: 9.5
Aluno George: 7
Aluno Ringo: 6
```

Vamos ver agora o `zip` em ação para compreender como ele funciona:

```python
for x in zip(alunos, notas):
    print(x)
```

Saída na tela:

```console
('Paul', 10)
('John', 9.5)
('George', 7)
('Ringo', 6)
```

Assim como no `enumerate`, o `zip` montou tuplas. Cada tupla representa 1 posição das listas originais, e cada posição dentro da tupla representa o dado de uma das listas. Ou seja, cada elemento do `zip` contém 1 elemento de cada lista original, na ordem que eles apareceram nas listas originais. Logo, ele permite percorrer 2 listas simultaneamente.

Novamente podemos aplicar desempacotamento de tuplas em nosso loop e acessar os dados de cada lista individualmente de maneira legível:

```python
alunos = ['Paul', 'John', 'George', 'Ringo']
notas = [10, 9.5, 7, 6]

for aluno, nota in zip(alunos, notas):
    print(f'Aluno {aluno}: {nota}')
```

Saída na tela:

```console
Aluno Paul: 10
Aluno John: 9.5
Aluno George: 7
Aluno Ringo: 6
```


___


# Dicionários

Você provavelmente já viu diversas tabelas onde cada coluna representa uma informação diferente sobre uma pessoa, evento ou objeto. Por exemplo, cada linha pode representar um aluno. A primeira coluna pode ser o nome do aluno, as quatro colunas seguintes podem ser suas notas em provas, a sexta coluna pode ser sua média, a sétima pode ser suas presenças, a oitava pode ser seu status (aprovado ou reprovado) e a nona pode conter algumas observações.

Em programação, as linhas de uma tabela poderiam ser representadas por listas. Neste caso, o índice 0 de cada linha seria sempre o nome, os índices 1 a 4 seriam as notas, o índice 5 seria a média, e assim sucessivamente. Porém, isso nem sempre convém, porque:

- expressões como `lista[1] + lista[2] + lista[3] + lista[4]` nos trazem pouca informação sobre o que significam os dados envolvidos na operação;
- caso seja necessário alterar a estrutura de dados para inserir, por exemplo, mais notas, seria necessário adaptar todo o código alterando todos os números mágicos representando cada coluna;

Seria preferível referenciarmos o nome do aluno por `'nome'`, suas notas poderiam ser uma lista chamada `'notas'`, sua média poderia ser chamada `'media'`, e assim sucessivamente. Aqui entram os **dicionários**, também conhecidos em outras linguagens como *tabelas hash*, *hash maps*, entre outros.

## 1. Dicionários em Python

Quando utilizamos um dicionário (o de papel, com definições), não temos o hábito de procurar pela palavra que está em uma determinada posição. Ao invés disso, nós buscamos pela palavra em si, e ao encontrá-la ela contém uma definição.

A estrutura dicionário em Python é uma coleção de dados. Porém, ela **não é indexada**. Ao adicionarmos elementos em um dicionário, sempre o fazemos aos pares: todo elemento terá uma **chave** e um **valor**.

- A **chave** será uma *string* que utilizaremos como se fosse o índice. É como se fosse a palavra que buscamos em um dicionário de papel.
- O **valor** pode ser qualquer dado: um `int`, um `float`, uma `str`, um `bool`, uma lista, uma tupla, outro dicionário. Ele é como se fosse a definição que encontramos vinculada à palavra que buscamos no dicionário de papel.

### 1.1. Criando um dicionário

Separamos chave e valor utilizando dois pontos (`:`), e separamos um par de outro utilizando vírgula. Utilizamos o símbolo chave (`{` e `}`) para representar um dicionário. O exemplo abaixo representa um aluno como descrito no início do capítulo.

```python
aluno = {'nome':'Mario', 'notas':[7, 9, 5, 6], 'presencas':0.8}
```

Podemos acessar uma informação de um dicionário utilizando a sua chave da mesma maneira que utilizamos um índice em uma lista:

```python
print('Aluno:', aluno['nome']) # Aluno: Mario
print('Notas:', aluno['notas']) # Notas: [7, 9, 5, 6]
```

Também é possível criar dicionários através da função `dict`. Ela pode ser utilizada de diferentes maneiras. Uma delas é passando parâmetros com nomes. Os nomes dos parâmetros se tornarão chaves, e os valores associados serão valores:

```python
notas = dict(Ana = 7, Brenda = 10, Carlos = 8)
print(notas) # resultado: {'Ana': 7, 'Brenda': 10, 'Carlos': 8}
```

Outra possibilidade é utilizar uma coleção (como uma lista ou uma tupla) contendo, internamente, outras coleções com exatamente 2 elementos. O primeiro elemento será chave, o segundo será valor. O exemplo abaixo cria o mesmo dicionário do exemplo anterior:

```python
lista = [['Ana', 7], ['Brenda', 10], ['Carlos', 8]]
dicionario = dict(lista)
print(dicionario)
```

Caso você tenha suas chaves e valores em coleções separadas, uma maneira fácil de explorar a possibilidade anterior é utilizar um `zip`:

```python
nomes = ['Ana', 'Brenda', 'Carlos']
notas = [7, 10, 8]
dicionario_notas = dict(zip(nomes, notas))
```

### 1.2. Adicionando elementos em um dicionário

Para adicionar elementos, não precisamos de uma função pronta (como o `append` das listas). Basta "acessar" a nova chave e atribuir um novo valor.

```python
aluno['media'] = sum(aluno['notas'])/len(aluno['notas'])

aluno['aprovado'] = aluno['media'] >= 6.0 and aluno['presencas'] >= 0.7

print(aluno)
```

Saída na tela:

```console
{'nome': 'Mario', 'notas': [7, 9, 5, 6], 'presencas': 0.8, 'media': 6.75, 'aprovado': True}
```

### 1.3. Percorrendo um dicionário

Dicionários podem ser percorridos com um `for`. Ao fazer isso, as **chaves** serão percorridas, não os valores. Porém, a partir da chave obtém-se o valor:

```python
for chave in aluno:
    print(chave, '--->', aluno[chave])
```

Saída na tela:

```console
nome ---> Mario
notas ---> [7, 9, 5, 6]
presencas ---> 0.8
media ---> 6.75
aprovado ---> True
```

### 1.4. Testando a existência de uma chave

Antes de criar uma chave nova em um dicionário, convém testar se ela já existe, para evitar sobrescrever um valor. Podemos fazer isso com o operador `in` (sim, o mesmo que usamos no `for`!). Neste contexto, ele retornará `True` se a chave existir e `False` caso contrário.

Vamos supor que, no exemplo abaixo, o valor de `'cursos'` seja uma lista com todos os cursos que o usuário está fazendo.

```python
dicionario = {'escola':"Ada", 'unidade':'Faria Lima'}

# Neste caso, 'cursos' ainda não existe.
# Cairemos no else e será criada uma lista com a string 'Python'.

if 'cursos' in dicionario:
    dicionario['cursos'].append('Python')
else:
    dicionario['cursos'] = ['Python']

# Agora a chave já existe. 
# Portanto, será adicionado 'Data Science' à lista. 
if 'cursos' in dicionario:
    dicionario['cursos'].append('Data Science')
else:
    dicionario['cursos'] = ['Data Science']
    
print(dicionario)
```

Saída na tela:

```console
{'escola': "Ada", 'unidade': 'Faria Lima', 'cursos': ['Python', 'Data Science']}
```

## 2. Métodos de dicionários

Você deve ter notado que algumas coisas que fazíamos em listas utilizando métodos (funções), em dicionários fazemos de maneira mais direta. Mas dicionários também possuem seus próprios métodos. Iremos estudar alguns bastante utilizados, mas você pode acessar essa página caso queira conhecer mais.

### 2.1. Acessando valores de maneira segura

Quando tentamos acessar uma chave que não existe em um dicionário ocorre um erro. Vimos que uma forma de driblar isso é testar a existência dela utilizando o `in`. Alguns métodos nos ajudam a "economizar" este teste.

#### 2.1.1. get

O método `get` permite acessar uma chave sem a ocorrência de erro. Caso uma chave não exista, ele irá retornar `None`, a constante nula denotando a ausência de valor.

```python
nomes = ['Ana', 'Brenda', 'Carlos']
notas = [7, 10, 8]
dicionario_notas = dict(zip(nomes, notas))

nota_daniel = dicionario_notas.get('Daniel') # valor de nota_daniel: None
nota_eliza = dicionario_notas['Eliza'] # erro de chave inexistente
```

O `get` aceita como parâmetro opcional um valor padrão que será retornado ao invés de `None` caso a chave não exista:

```python
nota_brenda = dicionario_notas.get('Brenda', 0) # valor de nota_brenda: 10
nota_daniel = dicionario_notas.get('Daniel', 0) # valor de nota_daniel: None
```

#### 2.1.2. setdefault

Um caso específico que vimos foi quando desejamos inserir uma chave caso ela não exista ou acessar seu valor caso ela exista. O método `setdefault` faz exatamente isso. Passamos uma chave e um valor. Se a chave for encontrada, seu valor é retornado. Caso contrário, ela é inserida com o valor passado. Vamos refazer o exemplo do `in` utilizando este método:

```python
dicionario = {'escola':"Ada", 'unidade':'Faria Lima'}
cursos = dicionario.setdefault('cursos', ['Python'])
print(cursos) # resultado na tela: ['Python']
cursos.append('Data Science')
print(dicionario['cursos']) # resultado na tela: ['Python', 'Data Science']
```

### 2.2. Copiando dicionários

#### 2.2.1. Criando um novo dicionário

Quando você já possui um dicionário e gostaria de copiar todo o seu conteúdo para outro dicionário, assim como no caso da lista, você não deve fazer uma atribuição direta, pois não houve cópia, e sim duas variáveis referenciando o mesmo dicionário na memória:

```python
nomes = ['Ana', 'Brenda', 'Carlos']
notas = [7, 10, 8]
dicionario_notas = dict(zip(nomes, notas))
dicionario_notas_copia = dicionario_notas

dicionario_notas_copia['Ana'] = 0
print(dicionario_notas['Ana']) # resultado: 0
```

Para copiar de fato o dicionário você pode utilizar o método `copy`:

```python
nomes = ['Ana', 'Brenda', 'Carlos']
notas = [7, 10, 8]
dicionario_notas = dict(zip(nomes, notas))
dicionario_notas_copia = dicionario_notas.copy()

dicionario_notas_copia['Ana'] = 0
print(dicionario_notas['Ana']) # resultado: 7
print(dicionario_notas_copia['Ana']) # resultado: 0
```

#### 2.2.2. Copiar um dicionário para dicionário já existente

Imagine que você já possui dois dicionários distintos e gostaria de uni-los, copiando os pares chave-valor de um deles para o outro. Você pode fazer isso utilizando o método `update`.

```python
escola = {'escola':"Ada", 'unidade':'Faria Lima'}
mais_escola = {'trilhas':['Data Science', 'Web Full Stack'], 'formato':'online'}

escola.update(mais_escola)

print(escola)
```

Saída na tela:

```console
{'escola': "Ada", 'unidade': 'Faria Lima', 'trilhas': ['Data Science', 'Web Full Stack'], 'formato': 'online'}
```

### 2.3. Removendo elementos de um dicionário

Você pode remover um elemento de um dicionário através do método `pop`. Você deve passar a chave a ser removida.

```python
aluno = {'nome':'Mario', 'notas':[7, 9, 5, 6], 'presencas':0.8}
aluno.pop('presencas')
print(aluno) # resultado: {'nome': 'Mario', 'notas': [7, 9, 5, 6]}
```

### 2.4. Separando chaves e valores

O Python possui funções para obter, separadamente, todas as chaves ou todos os valores de um dicionário. Elas são, respectivamente, `keys` e `values`. Podemos transformar o retorno dessa função em uma lista ou tupla.

```python
aluno = {'nome':'Mario', 'notas':[7, 9, 5, 6], 'presencas':0.8}

chaves = list(aluno.keys())
valores = list(aluno.values())

print('Chaves: ', chaves)
print('Valores:', valores)
```

Saída na tela:

```console
Chaves:  ['nome', 'notas', 'presencas']
Valores: ['Mario', [7, 9, 5, 6], 0.8]
```

Combinando essas funções com o `zip` estudado em um capítulo anterior, podemos iterar chaves e valores simultaneamente de maneira bastante pythonica:

```python
for chave, valor in zip(aluno.keys(), aluno.values()):
    # alguma operação aqui
```

Note que a construção acima também pode ser substituída por um método. O método `items` retorna uma coleção de tuplas, onde cada tupla contém um par chave-valor do dicionário:

```python
print(aluno.items())
```

Saída na tela:

```console
dict_items([('nome', 'Mario'), ('notas', [7, 9, 5, 6]), ('presencas', 0.8)])
```

Portanto, podemos fazer:

```python
for chave, valor in aluno.items():
    # alguma operação aqui
```

### 2.5. Compreensão de dicionários

Da mesma forma que utilizamos compreensão para listas, podemos utilizá-la para dicionários. A diferença é que precisamos, obrigatoriamente, passar um par chave-valor. O exemplo abaixo parte de uma lista de notas e uma lista de alunos e chega em um dicionário associando cada aluno a uma nota.

```python
alunos = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Emília']
medias = [9.0, 8.0, 8.0, 6.5, 7.0]

cadastro = {alunos[i]:medias[i] for i in range(len(alunos))}

print(cadastro)
```

Saída na tela:

```console
{'Ana': 9.0, 'Bruno': 8.0, 'Carla': 8.0, 'Daniel': 6.5, 'Emília': 7.0}
```

Talvez você não tenha achado esse código tão pythonico, e você tem razão. Não gostamos de percorrer listas por índices dessa maneira. Uma estratégia melhor é utilizar o `zip`, estudado em capítulos anteriores:

```python
alunos = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Emília']
medias = [9.0, 8.0, 8.0, 6.5, 7.0]

cadastro = {aluno:media for aluno, media in zip(alunos, medias)}

print(cadastro)
```

> [!NOTE]
> **Observação:** se você tentou fazer uma compreensão de dicionário e esqueceu de utilizar um par chave-valor, talvez você tenha se surpreendido ao notar que não gerou um erro. Isso ocorre porque existe outra estrutura de dados em Python que não estudamos no curso que utiliza os símbolos `{` e `}`: o **set** (conjunto). Ele é uma coleção mutável de elementos (como a lista), mas ele não possui índice (porque a ordem não importa) e ele não aceita elementos repetidos. Caso tenha curiosidade, segue material de referência com o básico de como trabalhar com conjuntos: https://www.programiz.com/python-programming/set

Após o capítulo sobre tuplas, onde foram abordadas questões de desempenho, você pode estar se perguntando quão eficiente ou ineficiente é um dicionário. Surpreendentemente, ele é uma estrutura bastante rápida para consulta. Isso se deve à forma como ele é implementado.

O motivo para um de seus nomes ser *tabela hash* é que ele utiliza o conceito de *hash*. De maneira simplificada, *hash* é um valor numérico obtido a partir de um dado quando realizamos uma sequência de operações sobre esse dado. Essas operações devem ser tais que se o dado mudar, o valor numérico também deve mudar. Quando dois dados diferentes podem gerar o mesmo número, chamamos isso de **colisão de hash**, e isso é bastante indesejável.

Quando o dicionário é criado, uma faixa tamanho razoável de memória é alocada para ele. Quando passamos uma chave, o computador calcula o *hash* dessa chave e utiliza o *hash* como índice para acessar o dado na memória! Inclusive, quando citamos acima que uma chave deve ser uma *string*, isso foi uma simplificação. Qualquer tipo de dado imutável (como uma tupla ou uma constante numérica) pode servir como chave. Objetos personalizados também podem, desde que eles sejam *hashable*. Você pode consultar um tutorial mais básico sobre dicionários [aqui](https://www.programiz.com/python-programming/dictionary), focado em diferentes funções úteis. Já [aqui](https://www.programiz.com/python-programming/dictionary) temos um tutorial mais avançado, que ensina você a criar uma estrutura semelhante a um dicionário do zero, explicando os conceitos envolvidos em cada passo.



___



# Parâmetros e retorno de funções

Quando estudamos funções, aprendemos que elas podem receber dados (parâmetros) e podem fornecer uma resposta (retorno). Porém, o número de parâmetros era fixo para cada função: um dado para cada parâmetro que declaramos na definição da função. Da mesma forma, a função poderia retornar exatamente um resultado.

Em alguns casos, mais flexibilidade seria útil. Utilizando tuplas e dicionários conseguimos essa flexibilidade.

## 1. Funções com retorno múltiplo

Vejamos um caso simples: uma função que retorna os valores máximo e mínimo de uma coleção, separados por vírgula. Vamos imprimir o resultado e verificar o que acontece.

```python
def max_min(colecao):
    maior = max(colecao)
    menor = min(colecao)
    return maior, menor

numeros = [3, 1, 4, 1, 5, 9, 2]

resposta = max_min(numeros)
print(resposta)
print(type(resposta)) # mostra o tipo da variável resposta

maior = resposta[0]
menor = resposta[1]
```

Se você executar o resultado acima, verá que o retorno da função é uma tupla. Lembre-se que expressões contendo valores separados por vírgula em Python, mesmo na ausência de parênteses, são tratadas como tuplas.

No capítulo de tuplas, estudamos a operação de desempacotamento de tuplas. Sua aplicação neste caso pode ajudar a de fato lidar com essa função como sendo uma função que retorna múltiplos valores em vez de simplesmente uma função que retorna uma tupla:

```python
def max_min(colecao):
    maior = max(colecao)
    menor = min(colecao)
    return maior, menor

numeros = [3, 1, 4, 1, 5, 9, 2]

maior_num, menor_num = max_min(numeros)
print(maior_num)
print(menor_num)
```

Saída na tela:

```console
9
1
```

Todas as variações de desempacotamento de tupla que já estudamos, incluindo o uso do operador `*` para agrupar e/ou descartar parte dos valores retornados podem ser empregadas aqui.

## 2. Parâmetros com valores padrão

Uma primeira forma de trabalhar com a ideia de parâmetros opcionais é atribuir valores padrão para nossos parâmetros. Quando fazemos isso, quando a função for chamada, o parâmetro pode ou não ser passado. Caso ele não seja passado, é adotado o valor padrão.

Devemos primeiro colocar os parâmetros "comuns" (conhecidos como argumentos posicionais) para depois colocar os argumentos com valor padrão. Imagine, por exemplo, uma função que padroniza strings jogando todo seu conteúdo para minúsculas ou maiúsculas. Podemos implementá-la da seguinte maneira:

```python
def padroniza_string(texto, lower=True):
    if lower:
        return texto.lower()
    else:
        return texto.upper()

print(padroniza_string('Sem passar o SEGUNDO argumento'))
print(padroniza_string('Passando SEGUNDO argumento True', lower=True))
print(padroniza_string('Passando SEGUNDO argumento False', lower=False))
```

Saída na tela:

```console
sem passar o segundo argumento
passando segundo argumento true
PASSANDO SEGUNDO ARGUMENTO FALSE
```

## 3. Funções com quantidade variável de parâmetros

Talvez você já tenha notado que o `print` é uma função. Se não notou, esse é um bom momento para pensar a respeito. Nós sempre usamos com parênteses, nós passamos informações dentro dos parênteses (os dados a serem impressos) e ele faz um monte de coisa automaticamente: converte todos os dados passados para string, concatena todas as strings com um espaço entre elas e as escreve na tela.

Algo que o `print` tem que as nossas funções não tinham é a capacidade de receber uma quantidade variável de parâmetros/argumentos. Nós podemos passar 0 dados (e, neste caso, ele apenas pulará uma linha), 1 argumento, 2 argumentos, 3 argumentos... Quantos dados quisermos e ele funcionará para todos esses casos. Se temos que declarar todos os parâmetros, como fazer para que múltiplos dados possam ser passados?

### 3.1. Agrupando parâmetros

A solução é utilizar o operador `*`. Ao colocarmos o `*` ao lado do nome de um parâmetro na definição da função, estamos dizendo que aquele argumento será uma coleção. Mais especificamente, uma tupla. Porém, o usuário não irá passar uma tupla. Ele irá passar quantos argumentos ele quiser, separados por vírgula, e o Python automaticamente criará uma tupla.

O exemplo abaixo cria uma função de somatório que pode receber uma quantidade arbitrária de números.

```python
def somatorio(*numeros):
    # remova o símbolo de comentário das linhas abaixo para entender melhor o parâmetro
    # print (numeros)
    # print(type(numeros))
    soma = 0
    for n in numeros:
        soma = soma + n
    return soma

s1 = somatorio(5, 3, 1)
s2 = somatorio(2, 4, 6, 8, 10)
s3 = somatorio(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(s1, s2, s3)
```

Saída na tela:

```console
9 30 55
```

### 3.2. Expandindo uma coleção

O exemplo acima funciona muito bem quando o usuário da função possui vários dados avulsos, pois ele os agrupa em uma coleção. Mas o que acontece quando os dados já estão agrupados?

```python
def somatorio(*numeros):
    print (numeros)
    print(type(numeros))
    soma = 0
    for n in numeros:
        soma = soma + n
    return soma

lista = [1, 2, 3, 4, 5]
s = somatorio(lista)
print(s)
```

Note que o programa dará erro, pois como os `print` dentro da função ilustram, foi criada uma tupla, e na primeira posição da tupla foi armazenada a lista. Isso não funciona com a lógica que projetamos.

Para casos assim, utilizaremos o operador `*` na chamada da função também. Na definição, o operador `*` indica que devemos agrupar itens avulsos em uma coleção. Na chamada, ele indica que uma coleção deve ser expandida em itens avulsos.

```python
def somatorio(*numeros):
    print (numeros)
    print(type(numeros))
    soma = 0
    for n in numeros:
        soma = soma + n
    return soma

lista = [1, 2, 3, 4, 5]
s = somatorio(*lista)
print(s)
```

Saída na tela:

```console
(1, 2, 3, 4, 5)
<class 'tuple'>
15
```

No programa acima, a lista é expandida em 5 valores avulsos, e em seguida a função agrupa os 5 itens em uma tupla chamada "numeros".

## 4. Parâmetros opcionais

Outra possibilidade são funções com parâmetros opcionais. Note que isso é diferente de termos quantidade variável de parâmetros.

No caso da quantidade variável, normalmente são diversos parâmetros com a mesma utilidade (números a serem somados, valores a serem exibidos, etc).

Já os parâmetros opcionais são informações distintas que podem ou não ser passadas para a função. Você pode ou não passá-los, e sempre deve indicar o seu nome ao passá-los.

Já estudamos uma forma de parâmetros opcionais utilizando valores padrão. Mas para funções com uma grande quantidade de parâmetros opcionais, existe outra forma utilizando dicionários, apelidada como `**kwargs`.

### 4.1. Criando `**kwargs`

Para criar parâmetros opcionais, usaremos `**`, e os parâmetros passados serão agrupados em um dicionário: o nome do parâmetro será uma chave, e o valor será o respectivo valor.

O exemplo abaixo simula o cadastro de usuários em uma base de dados. Um usuário pode fornecer seu nome, seu CPF ou ambos.

```python
def cadastro(**usuario):
    
    if not ('nome') in usuario and not ('cpf') in usuario:
        print('Nenhum dado encontrado!')
    else:
        if 'nome' in usuario:
            print(usuario['nome'])
        if 'cpf' in usuario:
            print(usuario['cpf'])
        print('-----')

cadastro(nome = 'João', cpf = 123456789) # tem ambos
cadastro(nome = 'José') # tem apenas nome
cadastro(cpf = 987654321) # tem apenas cpf
cadastro(rg = 192837465) # não tem nome nem cpf
```

Saída na tela:

```console
João
123456789
-----
José
-----
987654321
-----
Nenhum dado encontrado!
```

### 4.2. Expandindo um dicionário

Analogamente ao caso dos parâmetros múltiplos, é possível que o usuário da função já tenha os dados organizados em um dicionário. Neste caso, basta usar `**` na chamada da função para expandir o dicionário em vários parâmetros opcionais:

```python
maria = {'nome':'Maria', 'cpf':2468135790}
cadastro(**maria)
```

## Ordem dos parâmetros

Caso sua função vá combinar múltiplos tipos de parâmetro, sempre siga a seguinte ordem: argumentos posicionais (os comuns), argumentos com asterisco (tupla), argumentos com valor padrão e argumentos com dois asteriscos (dicionário). Por exemplo, na função abaixo:

```python
def funcao(a, b, *c, d=0, e=1, **f)
```

Quando ela for chamada, o Python fará o seguinte:

- os primeiros 2 valores serão atribuídos, respectivamente, para `a` e `b`.
- os próximos valores, independentes de quantos sejam, serão incluídos na tupla `c`.
- se os valores `d` e/ou `e` forem passados explicitamente pelo nome, os valores passados serão adotados, senão, serão adotados os valores padrão.
- quaisquer outros valores passados por nome serão incluídos no dicionário `f`.



___



# Tratamento de Exceção

Você já deve ter notado que algumas operações podem dar errado em certas circunstâncias, e esses erros provocam o tratamento do nosso programa.

Por exemplo, quando solicitamos que o usuário digite um número inteiro e ele digita qualquer outra coisa. O erro ocorre especificamente na conversão da entrada para `int`. Veja o exemplo abaixo:

```python
entrada = 'olá'
inteiro = int(entrada)
```

Erro mostrado na tela:

```console
ValueError: invalid literal for int() with base 10: 'olá'
```

Note que o erro possui um nome, `ValueError`, e uma mensagem explicando o que ocorreu.

Vejamos outro exemplo bastante famoso: a divisão por zero.

```python
x = 1/0
```

Erro mostrado na tela:

```console
ZeroDivisionError: division by zero
```

Observe a mesma estrutura do erro anterior: temos um nome (`ZeroDivisionError`) e uma mensagem explicando o que ocorreu.

Esses erros, que não são erros de lógica nem de sintaxe, são o que chamamos de **exceções**. São pequenos problemas que o programa pode encontrar durante sua execução, como não encontrar um arquivo ou uma função receber um valor de tipo inesperado.

Vamos começar aprendendo como lidar com códigos que podem provocar erros, evitando o travamento do programa, e em seguida iremos aprender a criar as nossas próprias exceções para alertar outros programadores sobre problemas que possam ter ocorrido em nossas classes e funções.

> [!NOTE]
> A documentação oficial do Python traz uma lista completa de exceções que já vem prontas e a relação de hierarquia entre elas.

## 1. Tratando uma exceção

### 1.1. try/except

Tratar uma exceção significa que quando surgir um dos erros mencionados, nós iremos assumir responsabilidade sobre ele e iremos providenciar algum código alternativo. Dessa maneira, o Python não irá mais travar o nosso programa, e sim desviar seu fluxo para o código fornecido.

O bloco mais básico para lidarmos com exceção é o `try/except`.

Dentro do `try` vamos colocar o pedaço de código com potencial para dar erro. Estamos pedindo que o Python tente executar aquele código, cientes de que pode não dar certo.

Dentro do `except`, colocamos o código que deverá ser executado somente se algo de errado ocorrer no `try`. Caso ocorra exceção em alguma linha do `try`, a execução irá imediatamente para o `except`, ignorando o restante do código dentro do `try`. Vejamos um exemplo:

```python
numerador = 1

for denominador in range(3, -1, -1):
    try:
        divisao = numerador/denominador
        print('Deu certo!') # roda APENAS se a linha acima não gerar exceção

    except:
        divisao = 'infinito'
    
    print(f'{numerador}/{denominador} = {divisao}')
```

Saída na tela:

```console
Deu certo!
1/3 = 0.3333333333333333
Deu certo!
1/2 = 0.5
Deu certo!
1/1 = 1.0
1/0 = infinito
```

O bloco acima já resolve a grande maioria dos problemas. Mas vamos estudar mais algumas possibilidades para deixar nosso tratamento ainda mais sofisticado e especializado.

Você deve ter notado que enfatizamos o fato de exceções poderem ter um nome. Esse nome pode nos ajudar a identificar com sucesso qual dos erros possíveis ocorreu e tratá-lo com sucesso.

Vamos considerar a função abaixo:

```python
def divisao(a, b):
    return a/b
```

Um erro óbvio que pode ocorrer nessa função seria o `ZeroDivisionError`, que é obtido quando o zero é passado como segundo parâmetro da função. Porém, ele não é o único erro possível.

O que acontece se passarmos um parâmetro que não seja numérico? `TypeError`, pois utilizamos tipos inválidos para o operador de divisão `/`.

Podemos colocar diversos `except` após o `try`, cada um testando um tipo diferente de erro. Um último `except` genérico englobará todos os casos que não se encaixarem nos específicos. Veja o exemplo:

```python
def divisao(a, b):
    return a/b

denominadores = [0, 2, 3, 'a', 5]

for d in denominadores:
    try:
        div = divisao(1, d)
        
    except ZeroDivisionError:
        div = 'infinito'
        
    except TypeError:        
        div = f'1/{d}'
        
    except:
        div = 'erro desconhecido'
    
    print(f'1/{d} = {div}')
```

Saída na tela:

```console
1/0 = infinito
1/2 = 0.5
1/3 = 0.3333333333333333
1/a = 1/a
1/5 = 0.2
```

### 1.2. else

Nosso bom e velho `else`, tipicamente usado em expressões condicionais acompanhando um `if`, também pode aparecer em blocos `try/except`. Seu efeito é o oposto do `except`: enquanto o `except` é executado quando algo dá errado, o `else` só é executado se absolutamente nada der errado. Por exemplo, poderíamos atualizar nosso exemplo anterior utilizando um `else`:

```python
def divisao(a, b):
    return a/b

denominadores = [0, 2, 3, 'a', 5]

for d in denominadores:
    try:
        div = divisao(1, d)
        
    except ZeroDivisionError:
        print('infinito')
        
    except TypeError:        
        print(f'1/{d}')
        
    except:
        print('erro desconhecido')
        
    else:
        print(f'1/{d} = {div}')
```

Saída na tela:

```console
infinito
1/2 = 0.5
1/3 = 0.3333333333333333
1/a
1/5 = 0.2
```

Note que, no exemplo acima, não tem problema estarmos atribuindo valor pra `div` apenas no bloco `try`. Ela só será usada no `else`, ou seja, só será usada se tudo deu certo.

### 1.4. finally

Muitas vezes um erro pode ocorrer quando já realizamos diversas operações. Dentre essas operações, podemos ter solicitado recursos, como por exemplo abrir um arquivo, estabelecer uma conexão com a internet ou alocar uma grande faixa de memória.

O que aconteceria, por exemplo, se um comando como `return` aparecesse durante o tratamento deste erro após termos solicitado tantos recursos diferentes? O arquivo ficaria aberto, a conexão ficaria aberta, memória seria desperdiçada, etc.

O `finally` garante um local seguro para colocarmos código de limpeza — ou seja, devolver recursos que não serão mais utilizados: fechar arquivos, fechar conexões com servidor etc.

Ele sempre será executado após um bloco `try/except`, mesmo que haja um `return` no caminho.

Veja o exemplo abaixo para entender o que queremos dizer:

```python
def teste(den):
    try:
        x = 1/den
        return x
    except:
        return 'infinito'
    finally:
        print('Opa')

print(teste(1))
print(teste(0))
```

Saída na tela:

```console
Opa
1.0
Opa
infinito
```

Note que o conteúdo do bloco `finally` foi executado em ambas as chamadas, mesmo havendo um `return` dentro do `try` e outro dentro do `except`. Antes de sair da função e retornar o valor, o Python é obrigado a desviar a execução para o bloco `finally` e executar seu conteúdo.

Vejamos um exemplo mais completo: um bloco `try/except` tentará criar um arquivo (não se preocupe com detalhes de como arquivos funcionam — estudaremos isso muito em breve!). Dentro do `try`, teremos um bloco `try/except/finally`. O `try` tentará escrever algumas operações matemáticas no arquivo, o `except` exibirá uma mensagem caso uma operação seja inválida, e o `finally` garantirá que o arquivo será fechado independentemente de um erro ter ou não ocorrido.

```python
def escreve_arquivo(nome_do_arquivo, denominador):
    try:
        arq = open(nome_do_arquivo, 'w') #abre o arquivo
        
        try:
            div = 1/denominador
            arq.write(str(div)) #escreve no arquivo
            return f'O número {div} foi escrito no arquivo.'
        
        except ZeroDivisionError:
            return 'Divisão por zero, não escrevemos no arquivo.'

        except TypeError:        
            return 'Tipo inválido, não escreveremos no arquivo.'

        except:
            return 'Erro desconhecido, não escreveremos no arquivo.'
        
        finally:
            print(f'Fechando o arquivo {nome_do_arquivo}')
            arq.close() # o arquivo SEMPRE será fechado, mesmo que ocorra erro!
            
    
    except:
        return 'Não foi possível abrir o arquivo'
    
    
print(escreve_arquivo('teste1.txt', 1))
print(escreve_arquivo('teste2.txt', 0))
```

Saída na tela:

```console
Fechando o arquivo teste1.txt
O número 1.0 foi escrito no arquivo.
Fechando o arquivo teste2.txt
Divisão por zero, não escrevemos no arquivo.
```

## 2. Levantando exceções

Quando estamos criando nossos próprios módulos, classes ou funções, muitas vezes vamos nos deparar com situações inválidas. Imprimir uma mensagem de erro não é uma boa ideia, pois o programa pode estar rodando em um servidor, pode ter uma interface gráfica, etc.

Logo, o ideal seria lançarmos exceções para sinalizar essas situações. Desta forma, se elas forem ignoradas, o programa irá parar, sinalizando para o programador que existe alguma situação que deveria ser tratada. Adicionalmente, podemos criar nossa própria mensagem de erro, sinalizando para o programador que ele deveria fazer algo a respeito.

Podemos utilizar a palavra `raise` seguida de `Exception()`, passando entre parênteses a mensagem personalizada de erro. Veja o exemplo:

```python
salarios = []

def cadastrar_salario(salario):
    if salario <= 0:
        raise Exception('Salário inválido! Salários devem ser positivos!')
    
    salarios.append(salario)
    
cadastrar_salario(10)
cadastrar_salario(0)
```

Note que na primeira chamada, onde não ocorreu exceção, o salário foi cadastrado na lista. Já na segunda chamada, nossa função lançou a exceção e parou sua execução.

Idealmente, quem pretende utilizar a função deveria fazê-lo agora utilizando `try`, para manter o programa funcionando e tratar adequadamente o problema.

```python
salarios = []

def cadastrar_salario(salario):
    if salario <= 0:
        raise Exception('Salário inválido! Salários devem ser positivos!')
    
    salarios.append(salario)
    
for i in range(3):
    salario = float(input('Digite o salário do funcionário: '))
    
    try:
        cadastrar_salario(salario)
    except:
        print('Opa, salário inválido!')
        
print(salarios)
```

Exemplo de execução:

```console
Digite o salário do funcionário: 1000
Digite o salário do funcionário: -500
Opa, salário inválido!
Digite o salário do funcionário: 1500
[1000.0, 1500.0]
```

O `raise` também pode ser utilizado para lançar exceções que já existem, não necessariamente exceções "novas". Basta trocar `Exception()` pelo nome da exceção desejada. De fato, quando utilizamos `raise Exception()` estamos apenas lançando a exceção mais genérica, da qual outras são derivadas, apenas especificando sua mensagem de erro.

## 3. Criando exceções novas

> [!NOTE]
> Este tópico utiliza conceitos de programação orientada a objeto. Ele está aqui para tornar esse capítulo mais completo. Caso você curse um módulo de programação orientada a objeto futuramente, é recomendável reler este material. Em todo caso, é possível utilizar os exemplos deste tópico como modelo para criar exceções mesmo sem compreender os detalhes do que está ocorrendo.

### 3.1. Herdando de Exception

Muitos problemas simples podem ser resolvidos através do `raise Exception(mensagem)`. Porém, você deve ter notado nos exemplos anteriores que o nome da nossa mensagem de erro foi `Exception`.

Exceções geralmente são implementadas através de classes. O "nome" do erro é o nome da classe de cada exceção. Existe uma exceção genérica chamada de `Exception`. Quando usamos `raise Exception(mensagem)`, estamos lançando essa exceção genérica junto de uma mensagem de erro personalizada.

O problema da nossa abordagem é que por utilizarmos uma exceção genérica não teremos como adicionar um `except` específico para nossa mensagem. Vamos criar nossa própria classe para escolher o nome do nosso erro. Exceções personalizadas geralmente herdam da classe `Exception`. Fazemos isso adicionando `(Exception)` após o nome de nossa classe.

Vamos colocar um construtor que recebe uma mensagem. Podemos definir uma mensagem padrão, caso ninguém passe a mensagem. Em seguida, chamaremos o construtor da superclasse (`Exception`).

```python
class SalarioInvalido(Exception):
    def __init__(self, message = 'Salários devem ser positivos!'):
        self.message = message
        super().__init__(self.message)

salarios = []

def cadastrar_salario(salario):
    if salario <= 0:
        raise SalarioInvalido()
    
    salarios.append(salario)
    
cadastrar_salario(0)
```

Mensagem de erro mostrada na tela:

```console
SalarioInvalido: Salários devem ser positivos!
```

Agora sim temos um erro com seu próprio nome e uma mensagem padrão. Mas note que quem está usando a nossa exceção pode personalizar a mensagem se quiser, basta passar uma mensagem diferente entre parênteses. O tipo do erro ainda será o mesmo e ambos deverão ser identificados como `SalarioInvalido` no `Except`.

```python
class SalarioInvalido(Exception):
    def __init__(self, message = 'Salários devem ser positivos!'):
        self.message = message
        super().__init__(self.message)

salarios = []

def cadastrar_salario(salario):
    if salario <= 0:
        raise SalarioInvalido('Deixa de ser mão-de-vaca e pague seus funcionários!')
    
    salarios.append(salario)
    
cadastrar_salario(0)
```

Mensagem de erro mostrada na tela:

```console
SalarioInvalido: Deixa de ser mão-de-vaca e pague seus funcionários!
```

Para finalizar, vale sempre lembrar que podemos tratar essa exceção específica:

```python
class SalarioInvalido(Exception):
    def __init__(self, message = 'Salários devem ser positivos!'):
        self.message = message
        super().__init__(self.message)

salarios = []

def cadastrar_salario(salario):
    if salario <= 0:
        raise SalarioInvalido()
    
    salarios.append(salario)
    
for i in range(3):
    salario = float(input('Digite o salário do funcionário: '))
    
    try:
        cadastrar_salario(salario)
    except SalarioInvalido:
        print('Nosso RH é uma vergonha :(')
    except:
        print('Exceção genérica')
        
print(salarios)
```

### 3.2. Adicionando atributos à exceção

É possível uma exceção trazer consigo informações sobre o valor que provocou o erro. Por exemplo, seria útil que a classe `SalarioInvalido` pudesse informar qual foi o salário inválido. Isso é útil, por exemplo, em logs que registram tudo o que ocorreu no programa, além de trazer informações importantes para o debugging do código.

Para isso, basta ajustar o construtor da classe de sua exceção:

```python
class SalarioInvalido(Exception):
    def __init__(self, salario, mensagem='Salários devem ser positivos!'):
        self.salario = salario
        self.message = mensagem
        super().__init__(self.message)
```

Agora, ao lançar a exceção, devemos passar o salário:

```python
salarios = []

def cadastrar_salario(salario):
    if salario <= 0:
        raise SalarioInvalido(salario)
    
    salarios.append(salario)
```

Por fim, ao tratar a exceção, podemos dar um alias (um "apelido") para ela utilizando a palavra `as`. Através desse apelido, podemos acessar seus atributos.

Note que imprimir o objeto faz com que sua mensagem seja impressa.

```python
for i in range(3):
    salario = float(input('Digite o salário do funcionário: '))
    
    try:
        cadastrar_salario(salario)
    except SalarioInvalido as excecao:
        print(excecao) # "Salários devem ser positivos!"
        print(f'O salário problemático foi: {excecao.salario}')        
    except:
        print('Exceção genérica')
        
print(salarios)
```

Exemplo de execução:

```console
Digite o salário do funcionário: 1000
Digite o salário do funcionário: -500
Salários devem ser positivos!
O salário problemático foi: -500.0
Digite o salário do funcionário: 1500
[1000.0, 1500.0]
```



___



# Conceitos de Programação Funcional

Neste capítulo vamos abordar um conjunto de técnicas diferente do que temos utilizado até o momento para planejar nossos programas. Para que isso faça sentido, vamos começar entendendo um pouco melhor de que maneiras podemos planejar um programa.

## 1. Paradigmas de programação

Um conceito bastante importante em programação é a ideia de **paradigmas de programação**. Um paradigma é uma forma diferente de pensar o seu programa.

Todos os nossos programas até agora consistem de uma sequência de instruções para o computador. Essas instruções são executadas sequencialmente. A ideia de um programa como um conjunto sequencial de instruções é conhecido como **paradigma imperativo** ou **programação imperativa**, pois o programa pode ser visualizado como um conjunto de verbos no imperativo.

Na prática, nossos programas não são 100% sequenciais, e conseguimos ramificar o fluxo de execução através de condicionais ou malhas de repetição. O uso dessas técnicas foi uma evolução na forma de programar e é conhecido como **programação estruturada**.

Indo um pouco além, dificilmente escrevemos blocos muito grandes de código de uma vez. Ao longo deste curso, criamos o hábito de modularizar os nossos programas encaixando pequenos pedaços de lógica dentro de funções, que agem como mini-programas, e o nosso programa se desenvolve através da interação entre essas funções. Essa forma de programação é conhecida como **programação procedural**. A programação procedural é uma forma mais específica de programação imperativa.

A **programação orientada a objetos** é outro paradigma de programação, onde o foco do programa está na modelagem dos nossos programas como resultado da interação entre diferentes objetos, que possuem seu comportamento ditado por suas respectivas classes. Porém, dentro das classes nós desenvolvemos métodos, que são bastante semelhantes às funções que já conhecemos, e portanto, essa também é uma forma de programação imperativa.

Um ponto importante sobre a relação entre paradigmas e linguagens de programação é que para programar utilizando um certo paradigma, muitas vezes será necessário que a linguagem forneça ferramentas específicas para tal. Por exemplo, é difícil aplicar o paradigma orientado a objeto utilizando uma linguagem que não suporte conceitos importantes deste paradigma, como os próprios objetos, com seus atributos e métodos.

O Python oferece ferramentas para auxiliar na programação procedural, na programação orientada a objeto e na programação funcional, que já discutiremos.

Existe todo um conjunto de formas diferentes de programar conhecido como **programação declarativa**, onde o programador irá se preocupar mais em descrever os resultados desejados do que em enfileirar instruções. O foco está em **o que** deve ser feito, e não em **como** deve ser feito. Uma forma de programação declarativa é a **programação funcional**.

## 2. O que é programação funcional

Assim como na programação procedural, nossos programas serão modularizados em funções, pequenos pedaços reutilizáveis de código que podem receber dados de entrada (parâmetros) e fornecer resultados de sua computação (retorno).

Uma das motivações para a adoção da programação funcional é aumentar o determinismo de nossos programas, isto é, tornar a execução dos programas mais previsíveis. Programas escritos de maneira imperativa tendem a ter efeitos colaterais causados por seu estado. O **estado** de um programa é definido pelo valor de todas as suas variáveis em um dado momento.

Quando um programa se torna muito grande, com diversas funções alterando o conteúdo de diferentes variáveis e objetos, torna-se cada vez mais perigoso que o programador perca o controle sobre o estado do programa, sendo possível que certos conjuntos de valores alterem o comportamento de outras funções e resultem em erros de computação.

### 2.1. Funções puras

Para evitar o não-determinismo, um conceito importante é o de **funções puras**. Uma função pura não possui efeitos colaterais, ou seja, seu funcionamento não irá alterar conteúdo na memória (ex: variáveis) ou dispositivos de entrada e saída. Isso traz algumas vantagens:

- Se nenhum parâmetro da função causa efeitos colaterais, então a função sempre apresentará o mesmo resultado ao receber os mesmos argumentos.
- Se não houver dependência entre os dados de duas funções puras, elas podem ser executadas em paralelo sem causar problemas de concorrência.
- Se o retorno de uma função sem efeitos colaterais não está sendo usado, ela pode ser removida sem afetar o restante do programa.

Vejamos alguns exemplos:

```python
def funcao_pura(numeros: list):
    soma = 0
    for n in numeros:
        soma += n
    return soma

def funcao_impura(numeros: list):
    soma = 0
    for idx in range(len(numeros)):

        if type(numeros[idx]) != int:
            numeros[idx] = int(numeros[idx])
        
        soma += numeros[idx]
        idx += 1
    return soma

entrada = [1, 2.5, 3, 4.5]

funcao_pura(entrada)
print(entrada)
funcao_impura(entrada)
print(entrada)
```

Note que no exemplo acima não utilizamos o retorno de nenhuma das funções. A `funcao_pura` poderia facilmente ser removida e nada mudaria, pois ela não provocou efeitos colaterais. Já a `funcao_impura` afeta o conteúdo da lista que foi passada, o que significa que sua ausência no programa alteraria o resultado.

### 2.2. Funções de primeira classe e funções de alta ordem

Dizemos que algumas linguagens tratam funções como **cidadãs de primeira classe**. Isso significa que nessa linguagem funções podem:

- ser atribuídas para variáveis ou guardadas em estruturas de dados
- ser passadas como parâmetros para outras funções
- ser retornadas por outras funções

É como se funções fossem variáveis como qualquer outra, de um tipo específico "função".

Essas características permitem a criação de **funções de alta ordem**, que são funções que recebem pelo menos uma função como parâmetro e/ou retornam uma função. Vejamos alguns exemplos:

**Atribuindo função para uma variável em Python**

```python
def funcao():
    print('olá mundo')

x = funcao
print('Tipo da variável x:', type(x))
x()
```

Saída na tela:

```console
Tipo da variável x: <class 'function'>
olá mundo
```

**Passando uma função como parâmetro para outra função**

```python
def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

def cumulativo(inicial, quantidade, operacao):
    contador = 1
    acumulado = inicial
    while contador <= quantidade:
        acumulado = operacao(acumulado, contador)
        contador += 1
    return acumulado

somatorio = cumulativo(0, 5, soma)
fatorial = cumulativo(1, 5, multiplicacao)
print(f'Somatório de 1 a 5: {somatorio} | Fatorial de 5: {fatorial}')
```

Saída na tela:

```console
Somatório de 1 a 5: 15 | Fatorial de 5: 120
```

**Retornando uma função**

```python
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def operador_para_funcao(operador):
    if operador == '+':
        return soma
    elif operador == '-':
        return subtracao
    elif operador == '*':
        return multiplicacao
    else:
        return divisao

x = operador_para_funcao('*')
print(x(5, 2))
```

### 2.3. Imutabilidade

Outro ponto bastante explorado pela programação funcional é tentar evitar o uso de estruturas mutáveis. Isso ocorre para evitar efeitos colaterais, como problemas de concorrência na execução paralela de diferentes trechos de código que poderiam afetar uma mesma estrutura.

Em vez de atualizarmos diferentes variáveis para ir salvando o estado de operações, iremos compor chamadas de funções de alta ordem e funções recursivas, e as informações irão fluir através de seus parâmetros e retornos.

Veremos logo mais algumas funções de alta ordem tradicionais e como elas nos ajudam a evitar a mutabilidade.

### 2.4. Clausura

Uma possibilidade criada por todas essas estratégias é a de uma **closure** (clausura em algumas traduções em português), onde uma função pode ser usada para criar outra função junto de um ambiente. Soa complicado, mas através de um exemplo podemos entender facilmente o que está acontecendo:

```python
def cria_somas(x):
    def soma(y):
        return x + y
    return soma

incremento = cria_somas(1)
decremento = cria_somas(-1)

print(incremento(5))
print(incremento(10))
print(incremento(15))

print(decremento(5))
print(decremento(10))
print(decremento(15))
```

Saída na tela:

```console
6
11
16
4
9
14
```

A função "mais interna" possui um valor que foi recebido como parâmetro pela função mais externa. Quando chamamos a função `cria_somas` passando `1`, a função interna foi definida como sempre retornando seu parâmetro + 1. Sendo assim, ao pegarmos essa função retornada, ela permanentemente retornará parâmetro + 1. No segundo caso passamos `-1`. Neste caso, a função mais interna foi criada com `x` valendo `-1`. Logo, ao pegarmos essa função, ela sempre irá retornar seu parâmetro - 1.

### 2.5. Funções anônimas

Outro conceito bastante comum na programação funcional é o de **funções anônimas**, também conhecidas como **funções lambda**. Elas são funções que não necessariamente precisam ser declaradas — no caso do Python, utilizando a palavra `def` — e atribuídas para um nome. A sintaxe para criar uma função lambda em Python é:

```python
lambda parametro1, parametro2, ... : expressao
```

Assim como em outras funções, a lambda pode ser chamada passando parâmetros entre parênteses e sua expressão será retornada. Não utilizamos a palavra `return`, já é subentendido que o resultado da lambda será retornado.

É comum utilizarmos funções lambda para rapidamente passar um parâmetro para uma função ou obter um retorno de uma função. Vejamos alguns exemplos anteriores refeitos utilizando lambdas:

```python
#Exemplo 1
def cumulativo(inicial, quantidade, operacao):
    contador = 1
    acumulado = inicial
    while contador <= quantidade:
        acumulado = operacao(acumulado, contador)
        contador += 1
    return acumulado

somatorio = cumulativo(0, 5, lambda x, y: x + y)
fatorial = cumulativo(1, 5, lambda x, y: x * y)
print(f'Somatório de 1 a 5: {somatorio} | Fatorial de 5: {fatorial}')

#Exemplo 2
def cria_somas(x):
    return lambda y: x + y

incremento = cria_somas(1)
decremento = cria_somas(-1)

print(incremento(5))
print(incremento(10))
print(incremento(15))

print(decremento(5))
print(decremento(10))
print(decremento(15))
```



___



# Conceitos de Programação Funcional (continuação)

Neste capítulo vamos continuar abordando um conjunto de técnicas diferente do que temos utilizado até o momento para planejar nossos programas.

## 2.6. Recursão

### 2.6.1 Recursão com programação imperativa

Antes de entrar na recursão envolvendo programação funcional, vamos ver como funciona a recursão com envolvendo funções e programação imperativa.

Uma função pode chamar outra função? Sim. Rode o programa abaixo e observe que ele funciona:

```python
def soma(a, b):
	resultado = a + b
	return resultado

def media(x, y):
	s = soma(x, y)
	resultado = s/2
	return resultado

m = media(10, 5)
print(m)
```

Mas e se uma função referenciasse ela mesma? Isso também funciona, e chama-se **função recursiva**, ou **recursão**.

A ideia vem da matemática. Vejamos um exemplo. Considere a função fatorial. O fatorial de um número `n` qualquer é igual ao produto entre `n` e todos os seus antecessores inteiros positivos: `n! = n x (n-1) x (n-2) x ... x 2 x 1`.

Considere o fatorial de 5: `5! = 5x4x3x2x1`

Pense agora no fatorial de 4: `4! = 4x3x2x1`

Note que temos destacado em negrito a expressão completa do fatorial de 4 dentro do fatorial de 5. Então é possível reescrever o fatorial de 5 em função do fatorial de 4:

`5! = 5x(4!)`

Porém, dentro do fatorial de 4, temos o fatorial de 3, e assim sucessivamente. Podemos generalizar da seguinte maneira:

```text
f(n) =
    1, se n = 1
    n * f(n-1), se n > 1
```

Ou seja, imagine que você queira calcular `f(4)`. Como `4 > 1`, teremos: `f(4) = 4 * f(3)`

Precisamos expandir `f(3)`: `f(4) = 4 * (3 * f(2))`

E assim sucessivamente: `f(4) = 4 * (3 * (2 * f(1)))`

Opa, `f(1)` nós conhecemos: está definido lá em cima como `1`. Portanto:

`f(4) = 4 * 3 * 2 * 1`

`f(4) = 24`

Note que nós decompomos um problema em várias instâncias "menores" do problema. Quebramos a formulação de uma multiplicação enorme por vários casos de `n x f(n-1)`. Chamamos essa estratégia de **dividir para conquistar**, e ela envolve identificar 2 etapas bastante claras do problema:

- **Caso base**: é um caso para o qual temos um valor conhecido (no exemplo acima, `f(1) = 1`)
- **Caso geral**: é a chamada recursiva, onde faremos referência à própria função.

Note também que esse comportamento tem o comportamento de **pilha**: se colocamos 3 pratos empilhados sobre a mesa, precisamos tirar primeiro o último que colocamos, certo? Caso contrário, a pilha toda tomba. No caso da recursão, para obter `f(4)` caímos em `f(3)`, depois `f(2)`, depois `f(1)`, e foi para ele que obtivemos a primeira resposta, que em seguida usamos para calcular `f(2)`, depois calcular `f(3)` e só então chegamos em `f(4)`. O primeiro passo do problema foi o último a ser resolvido.

Em Python, nossa função ficaria assim:

```python
def fatorial(n):
	if n == 1:
		return 1
	else:
		return n * fatorial(n-1)
```

Se chamarmos `fatorial(4)`, o que acontecerá? O programa começará a executar a função, cairá no `else` e encontrará a função chamada novamente. Neste caso, ele salva `n` valendo `4` e salva que a execução foi interrompida nessa linha. Então ele cria um novo `n` valendo `3`, cai novamente no `else` e salva que a execução foi interrompida nessa linha, e assim sucessivamente.

Note que para cada passo recursivo, as variáveis da função são copiadas e também é salvo o ponto onde a execução parou. Ou seja, funções recursivas podem consumir bastante memória, além de tempo de processamento para ficar criando cópias. A vantagem delas é o rigor matemático: podemos transcrever funções matemáticas quase exatamente como elas são, sem criar loops e variáveis para ficar guardando estados.

### 2.6.2 Recursão com programação funcional

Laços de repetição tradicionais, como o `for`, apresentam pelo menos dois possíveis problemas.

O primeiro deles é a necessidade de mutabilidade e variáveis de controle. Frequentemente, controlamos nossas repetições incrementando algum tipo de variável e testando seu valor.

O segundo é a própria legibilidade do loop: parte do código gerado é para controlar as repetições, e pode se distanciar um pouco da definição do problema em si.

Você já estudou esse conceito antes, mas vamos relembrar: **recursão** é quando uma função é capaz de chamar a si mesma. Tipicamente funções recursivas possuem 1 ou mais **casos base**, ou seja, casos onde nenhuma computação será feita e o resultado será retornado de maneira imediata, e o **caso geral** ou **caso recursivo**, onde o problema será subdividido em sucessivas chamadas para a função, variando seus parâmetros até que um caso base seja atingido.

Um exemplo clássico das aulas de programação é a sequência de Fibonacci. Uma das formas de definir essa sequência é a seguinte:

```text
F(0) = 1
F(1) = 1
F(n) = F(n-1) + F(n-2), se n > 1
```

Compare agora um código em loop (chamado de código iterativo) com um código recursivo. Note que no recursivo não utilizamos qualquer tipo de dado mutável. Observe também qual dos códigos lembra mais a definição original da sequência.

```python
def fib_iterativo(n):
    n1 = 0
    n2 = 1
    contador = 0
    while contador < n:
        n1, n2 = n2, n1+n2
        contador+=1
    return n2

def fib_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_recursivo(n-1) + fib_recursivo(n-2)
```

Uma desvantagem da recursão é a possibilidade de muitos cálculos repetidos serem realizados. Para calcular `F(5)`, teremos `F(4) + F(3)`. Mas no `F(4)`, o `F(3)` irá aparecer novamente.

Algumas linguagens oferecem um recurso chamado de **tail recursion**, ou recursão de cauda. Nelas, o resultado de chamadas recursivas recentes é temporariamente armazenado e pode ser reutilizado em outras chamadas. O Python **NÃO** possui recursão de cauda nativamente, mas é possível manipularmos os parâmetros de nossas funções para obter esse tipo de recursão na prática. Observe o código abaixo:

```python
def fib_cauda(n, n1 = 1, n2 = 1):
    if n == 0:
        return n1
    if n == 1:
        return n2
    return fib_cauda(n - 1, n2, n1 + n2)
```

Em cada passo recursivo, atualizamos `n2` com a próxima soma, o valor anterior de `n2` passa para `n1`, e o nosso `n` decrementa rumo ao caso base. Ao contrário da chamada recursiva anterior, observe que não estamos mais "ramificando" nossas chamadas recursivas, e as chamadas estão sendo resolvidas de maneira mais linear, com cada passo aproveitando os dois resultados anteriores.

## 2.7. Funções de alta ordem em coleções

Qualquer função que receba ou retorne uma função é considerada uma **função de alta ordem**. Mas três funções de alta ordem são consideradas bastante importantes porque permitem realizar diversas operações úteis sobre coleções (listas, arrays, tuplas, etc). Elas resolvem problemas tradicionais envolvendo as coleções, mas sem a necessidade de utilizar loops. Além disso, elas sempre irão retornar uma nova lista ou um valor, não alterando o conteúdo da função original. Elas são as funções `map`, `filter` e `reduce`.

### 2.7.1. Map

A função `map` recebe uma função e uma coleção. Ela irá aplicar a função recebida sobre cada um dos elementos da coleção, retornando uma nova coleção com os retornos de cada uma dessas chamadas.

Em Python, a função `map` retorna um iterador, então cabe a nós convertê-lo para uma estrutura caso necessário, como lista ou tupla.

```python
# exemplo 1 - convertendo todo o conteúdo de uma tupla para float
tupla_str = ('1.0', '3.7', '5.4')
tupla_float = tuple(map(float, tupla_str)) # função: float; coleção: tupla_str
print(tupla_str, tupla_float)

# exemplo 2 - elevando a 2 todos os elementos de uma lista usando uma função já existente
def quadrado(x):
    return x ** 2
numeros = [1, 2, 3, 4]
numeros_quadrados = list(map(quadrado, numeros)) # função: quadrado; coleção: numeros
print(numeros, numeros_quadrados)

# exemplo 3 - elevando a 3 todos os elementos de uma lista usando um lambda
numeros = [1, 2, 3, 4]
numeros_cubo = list(map(lambda x: x**3, numeros))
print(numeros, numeros_cubo)
```

Saída na tela:

```console
('1.0', '3.7', '5.4') (1.0, 3.7, 5.4)
[1, 2, 3, 4] [1, 4, 9, 16]
[1, 2, 3, 4] [1, 8, 27, 64]
```

A função `map` é bastante conhecida no meio da programação funcional e é oferecida em diversas linguagens. Por exemplo, em JavaScript — uma linguagem multiparadigma como o Python — é comum o uso de `map`, bem como o das outras duas funções que estudaremos.

Apesar do Python trazer a função implementada, é possível reproduzir a funcionalidade do `map` utilizando uma compreensão de lista ou uma expressão geradora. O resultado é equivalente: evitamos mutabilidade e efeitos colaterais, geramos uma coleção nova a partir da antiga, mas o código fica mais idiomático.

```python
# exemplo 1 - convertendo todo o conteúdo de uma tupla para float
tupla_str = ('1.0', '3.7', '5.4')
tupla_float = tuple(float(x) for x in tupla_str)
print(tupla_str, tupla_float)

# exemplo 2 - elevando a 2 todos os elementos de uma lista usando uma função já existente
def quadrado(x):
    return x ** 2
numeros = [1, 2, 3, 4]
numeros_quadrados = [quadrado(x) for x in numeros]
print(numeros, numeros_quadrados)

# exemplo 3 - elevando a 3 todos os elementos de uma lista sem usar função pronta
numeros = [1, 2, 3, 4]
numeros_cubo = [x**3 for x in numeros]
print(numeros, numeros_cubo)
```

### 2.7.2. Filter

A função `filter` também recebe uma função que deve retornar um booleano e uma coleção. Ela irá conter apenas os elementos da coleção que provocaram valor `True` na função passada.

```python
# exemplo 1 - detectando pares em uma lista usando função pronta
def eh_par(x):
    return x % 2 == 0
numeros = [3, 6, 4, 8, 7, 9, 2, 5]
pares = list(filter(eh_par, numeros)) # função: eh_par; coleção: numeros
print(pares)

# exemplo 2 - detectando negativos em uma lista usando lambda
numeros = [5, -3, 1, 4, 7, -8, -2]
negativos = list(filter(lambda x: x < 0, numeros))
print(negativos)
```

Saída na tela:

```console
[6, 4, 8, 2]
[-3, -8, -2]
```

Assim como no caso do `map`, podemos reproduzir a funcionalidade do `filter` de maneira mais pythonica utilizando compreensão de lista ou expressão geradora:

```python
# exemplo 1 - pares usando função pronta
def eh_par(x):
    return x % 2 == 0
numeros = [3, 6, 4, 8, 7, 9, 2, 5]
pares = [x for x in numeros if eh_par(x)]
print(pares)

# exemplo 2 - negativos sem função pronta
numeros = [5, -3, 1, 4, 7, -8, -2]
negativos = [x for x in numeros if x < 0]
print(negativos)
```

### 2.7.3. Reduce

A última função especial de alta ordem envolvendo coleções que estudaremos é o `reduce`. Além da função e da coleção, ele receberá também um valor inicial. Ele irá aplicar a função entre o valor inicial e o primeiro valor da coleção. Em seguida, entre o resultado dessa operação e o segundo valor da coleção. Depois, entre o resultado desta operação e o terceiro valor da coleção, e assim sucessivamente. Ou seja, ele **acumula** uma operação ao longo de uma coleção. O exemplo mais tradicional é o somatório.

Se você possui uma lista contendo os valores `[1, 3, 5, 7, 9]` e utilizar o `reduce` com valor inicial `0`, ele retornará o resultado de:

```text
(((((0 + 1) + 3) + 5) + 7) + 9)
```

No Python, o `reduce` não é uma função nativa como o `map` e o `filter`, e devemos importá-la de `functools`.

```python
from functools import reduce

lista = [1, 3, 5, 7, 9]

somatorio = reduce(lambda x, y: x + y, lista, 0) # função: o lambda criado; coleção: lista; valor inicial: 0

print(somatorio)

# colocando valor inicial 5

somatorio_inicial = reduce(lambda x, y: x + y, lista, 5)
print(somatorio_inicial)
```

Saída na tela:

```console
25
30
```

Um uso muito legal do `reduce` é para agrupar dados em categorias. Considere a estrutura abaixo, que lista os cursos de diferentes professores da Ada:

```python
professores = {
    'André': 'Python',
    'Bruna': 'DevOps',
    'Cabral': 'JavaScript',
    'Rafael': 'Python',
}
```

Vamos criar uma estrutura por categoria. Ela fará nosso papel de acumulador e será algo assim:

```python
{'Python': [], 'JavaScript': [], 'DevOps':[]}
```

Ela será determinada de maneira automática, ou seja, vamos determinando as disciplinas e adicionando ao dicionário.

Por fim, precisamos criar a função que usaremos. Para fugir de usar variáveis globais, podemos fazer uma função que gera funções a partir de um dicionário, que tal?

```python
from functools import reduce

def gera_redutor(dicionario):

    def redutor(acumulador, chave):
        if dicionario[chave] in acumulador:
            acumulador[dicionario[chave]].append(chave)
        else:
            acumulador[dicionario[chave]] = [chave]
        return acumulador
    
    return redutor

professores = {
    'André': 'Python',
    'Bruna': 'DevOps',
    'Cabral': 'JavaScript',
    'Rafael': 'Python',
}

redutor_profs = gera_redutor(professores)

profs_por_curso = reduce(redutor_profs,
    professores,
    {})

print(profs_por_curso)
```

Saída na tela:

```console
{'Python': ['André', 'Rafael'], 'DevOps': ['Bruna'], 'JavaScript': ['Cabral']}
```

A ideia não é que você nunca mais utilize técnicas de programação imperativa. O Python não é uma linguagem funcional pura, e muitos de seus recursos mais úteis estão ligados à programação orientada a objeto, por exemplo.

Porém, você agora é capaz de analisar de maneira mais crítica o impacto de diferentes técnicas para resolver um problema e fazer uma escolha mais consciente refletindo sobre os seus benefícios e suas desvantagens.

As ferramentas funcionais são mais instrumentos para sua caixinha de ferramentas, que podem ser incorporados parcialmente em programas orientados a objeto, como ocorre com frequência, por exemplo, no desenvolvimento web em JavaScript.

Algumas referências (em inglês) caso você queira se aprofundar:

- [Uma explicação mais profunda sobre como recursão funciona na memória do computador e como isso muda quando implementamos recursão de cauda](https://towardsdatascience.com/python-stack-frames-and-tail-call-optimization-4d0ea55b0542)
- [Um pouco mais sobre recursão vs loops](https://arstechnica.com/information-technology/2013/04/recursion-or-while-loops-which-is-better)
- O Real Python possui alguns tutoriais e artigos breves e gratuitos [aqui](https://realpython.com/python-functional-programming/) de programação funcional em Python e um curso (pago) mais completo [aqui](https://realpython.com/courses/functional-programming-python/). O material completo deles inclui mais detalhes também sobre `map`, `filter` e `reduce`. O índice está disponível [aqui](https://realpython.com/tutorials/functional-programming/).



___



