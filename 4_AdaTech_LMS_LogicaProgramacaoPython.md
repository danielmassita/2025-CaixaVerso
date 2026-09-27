CAIXAVERSO - FC5 | Analista Dados - II | #1735
Logica de Programação em Python
___

# CAIXAVERSO - FC5 | Analista Dados - II | #1735

https://lms.ada.tech/student/topics/by-class-id/097ee233-0745-490b-b38c-1dc99dfd1305/by-module-id/4e6fa598-53f4-4856-a75d-b7e879ff1b7d

<img width="1024" height="682" alt="image" src="https://github.com/user-attachments/assets/25020c6a-0432-40a2-a039-655d14492299" />


- Professor: [Thiago Tavares Magalhães](https://www.linkedin.com/in/thiagotm/)
  - Senior Data Scientist at SuperSim | Teacher at Ada | Master's Degree in Computational Modeling from the National Laboratory for Scientific Computing

___

Introdução
Olá! Seja bem-vindo ao curso de lógica de programação com linguagem Python! Vamos repassar algumas orientações iniciais para otimizar o seu uso deste material.

1. Onde programar em Python?
O Python é uma linguagem interpretada. Isso significa que é necessário termos um interpretador Python instalado em nosso computador para poder executar nossos programas.

Além disso, é importante termos um programa que permita a edição dos códigos. Tecnicamente, qualquer editor de textos puro serviria, incluindo o Bloco de Notas do Windows. Mas programadores normalmente preferem utilizar uma IDE (Integrated Development Environment), que oferecerá uma série de recursos para facilitar ainda mais o nosso trabalho, como utilizar código de cores e formatação para deixar o código mais legível, ferramentas para autocompletar o código, ferramentas para procurar erros (debuggers e linters), entre outros.

Vamos passar brevemente por algumas diferentes opções que poderiam ser adotadas. Mas antes de iniciar a instalação de qualquer uma delas, verifique se o seu professor planejou o curso considerando alguma ferramenta específica.

Caso queira entender melhor como funciona o processo de interpretação do Python, aqui está uma ótima referência!

1.1. IDLE
Ao baixar o interpretador Python no site oficial, ele irá trazer junto consigo um editor bastante simples, o IDLE.

Ele possui poucos recursos comparado com as próximas IDEs que mencionaremos, mas já é um bom quebra-galho caso você precise editar rapidamente um código.

Caso seu professor tenha optado por trabalhar com a distribuição padrão do Python disponível no site oficial, procure baixar a versão mais recente disponível no site e lembre-se de marcar a opção "Add Python to PATH" durante a instalação. Isso evitará uma série de problemas na hora de instalar outros recursos e bibliotecas.

1.2. Thonny
O Thonny não é exatamente uma IDE profissional, utilizada no mercado. Seu foco é no aprendizado de Python. Ela oferece recursos especialmente úteis para quem ainda está aprendendo, como acompanhar o valor de variáveis e chamadas de função. Ela também é bastante leve. Ela pode ser obtida gratuitamente no site do projeto.

1.3. Visual Studio Code
O Visual Studio Code é uma IDE gratuita da Microsoft. Seu grande charme é a possibilidade de ter seus recursos expandidos através de extensões. Sendo assim, ele é, na prática, compatível com praticamente qualquer linguagem em uso atualmente, e é bastante fácil acrescentar novas ferramentas a ele. Ele também é bastante leve e fácil de ser configurado.

Você pode fazer o download no site oficial e configurá-lo para suportar Python.

1.4. PyCharm
O PyCharm é uma IDE profissional fornecida pela JetBrains, responsável por diversas IDEs, como o IntelliJ, bastante popular entre desenvolvedores Java e Kotlin. Suas ferramentas são populares de maneira geral entre desenvolvedores web e mobile. O PyCharm possui alguns recursos para facilitar a integração com outros sistemas (em particular com linguagem JavaScript e SQL), e para gerenciar a instalação de bibliotecas, evitando que uma atualização de biblioteca em um projeto possa acidentalmente "quebrar" outro projeto. Em contrapartida, ela é mais pesada, o que pode atrapalhar a experiência de quem estiver utilizando computadores mais lentos.

Sua versão Community pode ser baixada gratuitamente no site da JetBrains.

1.5. Anaconda e Jupyter Notebook
O Anaconda é um pacote completo para análise de dados que já vem com uma versão especial do Python (o IPython, ou Interactive Python) pré-instalada, bem como diversas bibliotecas prontas extremamente populares na comunidade científica. Essas bibliotecas incluem uma infinidade de funções prontas para conexão com internet, computação matemática, computação científica, aprendizado de máquina, visualização de dados, conexão com banco de dados, entre outras.

Uma das ferramentas inclusas no Anaconda é o Jupyter Notebook. O grande diferencial dele em relação a uma IDE convencional é o seu formato de "caderno", onde é possível intercalar trechos de códigos com anotações formatadas utilizando a linguagem Markdown.

Ele é extremamente popular na análise de dados, pois é possível ir escrevendo pequenos trechos de código e já visualizando o resultado na forma de gráficos, tabelas e anotações.

O Anaconda pode ser obtido gratuitamente em seu site oficial e já virá com o Jupyter instalado. Alternativamente, você pode seguir o tutorial no blog da Let's Code para instalar apenas o Jupyter e dar os seus primeiros passos.

Tanto o Visual Studio Code quanto o PyCharm podem ser utilizados para abrir os notebooks. Inicie a instalação pelo Anaconda, e através do aplicativo Anaconda Navigator, busque a opção de abrir a IDE desejada e ele fará a mágica por você.

1.6. Google Colab
O Google possui o seu próprio notebook, compatível com Jupyter. Ele é 100% online e integrado com Google Drive. Você precisa estar logado com a sua conta Google e o seu trabalho será salvo em seu Drive.

Ele pode ser acessado aqui.

1.7. Programando online
Caso algum dia você se encontre sem o Python instalado em sua máquina - por exemplo, o seu computador quebrou e você conseguiu outro emprestado em cima da hora da aula - não se preocupe. Não faltam opções para programar direto no navegador. Vejamos algumas opções:

Repl.it: uma IDE online bastante simples, com visualização da saída do código logo ao lado do editor.

OnlineGDB: uma IDE online com suporte a múltiplas linguagens de programação diferentes. Não se esqueça de selecionar "Python3" no menu antes de começar os seus trabalhos.

Jupyter: O Jupyter oferece uma área em seu site para você experimentá-lo sem precisar instalar. Ele será executado direto no seu navegador e possui acesso às bibliotecas padrão de ciência de dados.

Google Colab: Já mencionado anteriormente, vale reforçar que ele é online e não exige qualquer instalação na sua máquina.

2. Como estudar Python?
Gostamos de dizer que o nome da nossa escola não é Let's Talk, e sim Let's Code. Participar das aulas é bastante importante, mas mais importante do que escutar o professor falar é programar.

Sempre que você ver um código de exemplo nesse material, execute o código na sua IDE. Experimente com o código também: modifique, altere detalhes e veja o que acontece. E, claro, não deixe de fazer os exercícios propostos pelo professor. Eles foram planejados para sedimentar os novos conceitos recém-introduzidos e ajudar a consolidar e integrar os conceitos anteriores.

DICA: Quando for executar os exemplos, evite utilizar o famoso “copia e cola”. Ao invés disso, digite o código e aproveite para se familiarizar com a sintaxe da linguagem.

Quando o seu código não funcionar, não desista, nem simplesmente copie de alguém que funcionou. Busque entender a mensagem de erro (caso haja alguma) e tente ler e entender o que o código está fazendo em cada passo. Caso não consiga resolver, busque o professor, um monitor ou mesmo um colega de turma com quem você se sinta à vontade e mostre seu código para que eles possam ajudar você a entender o seu erro.

E quando você tiver uma ideia, não tenha medo de tentar implementá-la e ver o que acontece!

3. Material extra e referências
Caso você queira complementar seus estudos, há diversas opções baratas ou mesmo gratuitas. Citaremos alguns aqui que são bastante populares e serviram de base para o nosso material aqui.

Livros
Pense em Python (2ª edição) - Allen B. Downey: esse livro é bastante introdutório, e possui uma linguagem extremamente acessível. É ideal para quem está começando e usa vários exemplos em código. Ele é disponibilizado gratuitamente e pode ser lido online. A versão impressa pode ser comprada no site da Editora Novatec.

Think Python (2nd edition) - Allen B. Downey: é a versão original do livro acima. Quem tem facilidade com a língua inglesa pode preferir ler o original. Assim como na tradução, é possível ler gratuitamente online ou adquirir a versão impressa no mesmo link.

Python Basics (4th edition) - RealPython.com: disponível apenas em inglês, é um livro escrito pela equipe que mantém o site RealPython.com. Esse livro é bastante introdutório, mirando estudantes iniciantes. Mas ele percorre uma variedade muito maior de tópicos que o Think Python, e acaba oferecendo mais aplicações.

Python Tricks - Dan Bader: disponível apenas em inglês, escrito por um dos editores do RealPython.com. Esse livro é um pouco mais avançado, e seria mais interessante para quem já chegou aqui sabendo Python ou então após a conclusão do módulo. Ele é um livro de aprofundamento, que irá ajudar quem já sabe o básico de Python a explorar mais a fundo os diferentes recursos que a linguagem oferece.

Python Fluente - Luciano Ramalho: assim como o livro anterior, ele é recomendável para quem já está confortável com a linguagem e gostaria de se aprofundar. Foi escrito por um brasileiro e possui traduções para diversas línguas. É uma leitura obrigatória para programadores Python experientes.

Toda a coleção do Al Sweigart: esse autor escreve diversos livros totalmente baseados em projetos e atividades. Eles são bem legais para complementar os estudos justamente pela oportunidade de ver tudo funcionando na prática. Seus livros são em inglês, mas estão todos disponíveis gratuitamente no próprio site do autor, e assim como em outros casos, também podem ser comprados em versões impressas.

Sites
Documentação Oficial do Python: disponível em português, é ponto de parada obrigatório para todos os programadores. Ela explica detalhadamente todos os recursos da linguagem e possui uma referência bastante completa de todas as bibliotecas incluídas na linguagem.

RealPython.com: um site riquíssimo em cursos, artigos e tutoriais. Alguns são gratuitos, outros são pagos. Eles possuem um newsletter que envia dicas de Python regularmente por e-mail.

StackOverflow: talvez você não tenha utilidade imediata para ele. Mas conforme você for programando e pesquisando erros, frequentemente cairá neste site. Ele é um site de perguntas e respostas sobre programação com filtros bastante eficientes para garantir a prevalência de perguntas relevantes e respostas corretas.

Ademais, há uma infinidade de blogs, tutoriais e vídeos, muitas vezes em sites com temáticas específicas (ex: análise de dados ou machine learning). Não deixe de pesquisar quando você tiver dúvidas específicas, você ficará surpreso com quanto material bom de Python existe gratuitamente por aí! :)

Cursos digitais Ada
Além dos materiais acima, temos também diversos cursos digitais da Ada, que podem ser muito úteis em sua jornada de aprendizagem de lógica de programação e Python! Seguem as principais recomendações:

Funcionamento do computador: https://cursos.letscode.com.br/curso-digital/65757051-1636-4c95-8cb3-fd14198d741b

Lógica Pura: https://cursos.letscode.com.br/curso-digital/2120c9f0-02ba-45c1-a81d-3ed26232cc0c

Introdução a Python: https://cursos.letscode.com.br/curso-digital/ad77ffa3-6dde-4efb-9e0d-3b14e60b097b

Como melhorar o seu aprendizado: https://cursos.letscode.com.br/curso-digital/956710f8-d7cf-4bff-93d7-b9d544a82e77

História da Ciência da Computação: https://cursos.letscode.com.br/curso-digital/4114870c-c8e7-4701-aa55-3b6277a8ae67

 

Variáveis, entradas e saídas
4. Variáveis
Em nossos programas, frequentemente precisaremos armazenar dados temporariamente. Esses dados podem ser adquiridos de alguma maneira (digitados pelo teclado, lidos de um arquivo etc.) ou calculados pelo nosso programa com base em outros dados. Imagine, por exemplo, que você gostaria de calcular a média de um aluno a partir de suas notas. Precisaremos que o aluno digite suas notas, e o programa irá calcular um novo valor, a média. Armazenaremos nossos dados temporariamente em variáveis.

Variáveis são "pedacinhos de memória" onde guardamos dados. Sempre que referenciamos o nome, o pedacinho de memória é acessado e seu dado é recuperado.

Criamos variáveis dando um nome a elas e usando o operador de atribuição (o sinal de igualdade: =) para atribuir um valor inicial.

x = 10
No exemplo acima, foi criada uma variável chamada x que guarda o valor 10. Ou seja, reservamos um pedacinho de memória e guardamos o número 10 lá.

Tente sempre utilizar nomes intuitivos para suas variáveis. O nome deveria ser uma boa descrição do dado que a variável guarda. Nomes como 'x', 'y', 'z', 'a', 'b', 'c', 'a1', 'a2', 'a3' etc. podem se tornar bastante confusos quando nossos códigos são muito grandes. Quanto mais descritivos os nomes forem, melhor.

Os nomes de variáveis podem conter letras, números e o símbolo _, mas eles não podem começar com número.

Dica: existe uma grande variedade de padrões diferentes que podemos adotar para nomear nossas variáveis. Em Python é recomendável utilizar o padrão conhecido como snake case, em que nomes de variáveis com múltiplas palavras adotam o símbolo _ para separar as palavras. Exemplos: nome_completo, nota_da_prova etc.

5. Tipos de variáveis
Variáveis podem ter diferentes tipos. Alguns tipos são considerados tipos primitivos, ou seja, eles são tipos de dados mais básicos que podem ser utilizados para compor outros tipos mais complexos. Em Python esses tipos levam os seguintes nomes:

int: números inteiros, ou seja, números sem parte decimal: 0, 5, -1, 1000
float: números reais, ou seja, números com parte decimal: 1.0, -2.7, 3.14
str: cadeias de caracteres (strings), ou seja, dados textuais: 'Olá Mundo!', "eu tenho 18 anos"
bool: valores lógicos (booleanos), ou seja, apenas um entre dois valores possíveis: True ou False
nome = 'Zé' # uma variável do tipo string - note as aspas
email = "ze@letscode.com.br" # outra string
idade = 22 # uma variável inteira
salario = 5999.85 # uma variável float - usamos ponto, não vírgula
receber_newsletter = True # uma variável bool
O Python é uma linguagem dinamicamente tipada. Isso significa que não precisamos especificar o tipo de uma variável: a própria linguagem tenta determinar o tipo de acordo com o dado atribuído à variável.

6. Comentários
Note que nos exemplos acima, escrevemos textos no meio do código utilizando o símbolo #. Esses textos são comentários: quando utilizamos o símbolo #, o Python irá ignorar tudo o que vier em seguida (na mesma linha). Utilizamos comentários para explicar pedaços do nosso código para que nós mesmos ou outros colegas no futuro entendam o que fizemos e possam modificar ou corrigir o código com mais facilidade. Também podemos escrever comentários de múltiplas linhas utilizando aspas triplas - neste caso, as utilizamos para abrir e depois para fechar o bloco de comentários.

'''
Este é um comentário de várias linhas.
Tudo que veio após o primeiro trio de aspas e antes do segundo
será ignorado pelo Python.
'''
Na verdade, esse tipo de comentário não é exatamente um comentário, mas uma string com múltiplas linhas. O Python enxerga que apenas "declaramos" uma string no meio do código, sem utilizá-la ou atribuí-la para qualquer variável, e por conta disso ela é ignorada, funcionando na prática como um comentário.

Na maioria das IDEs você possui teclas de atalho para facilmente transformar um bloco inteiro de código em comentário para temporariamente desabilitá-lo. Isso pode ser útil quando estamos testando soluções alternativas para um problema ou corrigindo erros. No Visual Studio Code, por exemplo, você pode utilizar ctrl+/ para transformar uma seleção em comentário.

7. Saídas
Chamamos de saídas do nosso programa todos os dados que são gerados pelo programa e serão fornecidos para o usuário. A função de saída em tela no Python é o print. Colocamos entre parênteses o dado que queremos que apareça.

print('olá mundo!') # exibe a frase 'olá mundo' na tela
Os dados a serem exibidos não precisam ser valores constantes, como a frase fixa acima. Eles podem ser variáveis:

idade = 20
print(idade)
Note que quando usamos aspas, o Python trata o valor como uma string, um texto literal. Quando não usamos aspas, o Python irá considerar que aquele é o nome de uma variável e irá acessá-la para buscar seu valor.

Podemos exibir múltiplos dados em um print. Para isso, basta separá-los por vírgula e eles irão aparecer na tela na mesma ordem que apareceram no código:

nome = 'Mario'
linguagem = 'Python'
print('Oi, eu sou o', nome, 'e eu programo em', linguagem)
 
```
Resultado na tela:
Oi, eu sou o Mario e eu programo em Python
```
Note que os dados aparecem em tela separados por um espaço automaticamente. Dois prints sucessivos também possuem uma quebra de linha entre eles. Você pode passar as opções sep e end dentro de seu print para especificar diferentes comportamentos. Exemplo:

nome = 'Mario'
linguagem = 'Python'
print('Oi, eu sou o', nome, sep='@', end='***')
print('Eu programo em', linguagem, sep='@')
 
```
Resultado na tela:
Oi, eu sou o@Mario***Eu programo em@Python
```
Dica: caso você ache confuso separar os dados por vírgulas, você pode alternativamente utilizar uma f-string. Não entraremos em detalhes agora, mas o funcionamento básico é simples: coloque um f antes de abrir aspas, e dentro do texto você pode colocar o nome das variáveis entre chaves. o print abaixo terá o mesmo resultado que o exemplo anterior:

print(f'Oi, eu sou o {nome} e eu programo em {linguagem}`)
8. Entradas
Assim como temos dados de saída - dados gerados pelo código e fornecidos para o usuário - também temos dados de entrada: informações que o usuário possui e deve fornecer ao código. Para receber entradas pelo teclado, utilizaremos a função input. Devemos levar uma variável a receber o valor capturado pelo input.

nome = input()
print('Olá', nome)
O programa acima captura o nome do usuário e em seguida mostra a mensagem "olá" seguida do nome do usuário. Note que o programa fica parado em uma tela em branco com um cursor piscando aguardando a digitação pelo usuário. Isso pode ser confuso para o usuário, que não sabe o que o programa está esperando. Por isso, dentro dos parênteses do input podemos colocar uma mensagem simples informando o que o programa gostaria que ele fizesse:

nome = input('Qual é o seu nome?')
print('Olá', nome)
8.1. Determinando o tipo da entrada
Vamos imaginar um programa que informa quantos anos falta para que uma criança atinja a maioridade. Podemos ler a idade da criança pelo teclado (entrada), subtrair a idade do número 18 (processamento) e exibir o resultado da conta na tela (saída). Considere a solução abaixo:

idade = input('Digite a sua idade: ')
resto = 18 - idade
print('Faltam', resto, 'anos.')
Se você copiar e executar o programa, ele dará erro na segunda linha. Isso ocorre porque o teclado é uma "máquina de escrever" um pouco mais moderna. Portanto, tudo que entra pelo teclado é considerado pelo Python como texto (ou seja, str). Porém, não podemos "fazer contas" com textos. Fazemos contas com números. Portanto, neste caso, precisamos falar para o Python interpretar a nossa entrada como um número. Um bom tipo de dado para "idade" seria um número inteiro. Fazemos isso colocando o nome do tipo desejado, e entre parênteses colocamos nosso input:

idade = int(input('Digite a sua idade: '))
resto = 18 - idade
print('Faltam', resto, 'anos.')
Chamamos essa operação de coerção de tipo. Em materiais em inglês você verá essa operação com o nome casting. Tome cuidado: operações de coerção podem resultar em perdas de dados. Se você converter o número float 3.9 para int, ele não arredondará para 4, e sim descartará a parte fracionária, resultando em 3.

Neste início, mensagens de erro podem parecer intimidadoras. Elas aparecem em vermelho e frequentemente possuem nomes técnicos e expressões em inglês. Mas crie o hábito de tentar compreendê-las. A partir da versão 3.10 do Python elas se tornaram significativamente mais amigáveis. Elas também indicam a linha com erro. Além disso, se você pesquisar em sites de busca por uma mensagem de erro, provavelmente encontrará diversos exemplos e explicações do que pode tê-la provocado e como consertar!

9. Expressões aritméticas
Como podemos observar no exemplo anterior, o Python faz operações aritméticas de maneira bastante intuitiva, similar ao que estamos acostumados. Os operadores aceitos são:

Soma: +
Subtração: -
Multiplicação: *
Divisão: /
Divisão inteira: //
Resto da divisão: %
Potência: **
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: ''))
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
Operadores de divisão: Note que temos 3 operadores de divisão. O que seria cada um deles? Vamos supor que numero1 seja 15 e numero2 seja 6.

 15 |__ 6
Quantas vezes o número 6 cabe dentro do 15? Um bom primeiro "chute" é 2:

 15 |__ 6
     2
Podemos multiplicar 6 por 2, que dará 12. E então subtraímos esse valor de 15:

 15 |__ 6
-12     2
---
 03
Note que, considerando apenas números inteiros, não conseguimos mais prosseguir com a divisão. Neste caso, a divisão inteira (numero1 // numero2) dará 2. Já o resto da divisão (numero1 % numero2) dará 3.

Porém, considerando casas decimais é possível prosseguir com a divisão:

 15 |__ 6 
-12     2.5
---
 03
  30
- 30
----
   0
Portanto, a divisão real (numero1 / numero2) dará 2.5.

Atenção: números reais em Python usam ponto para separar as casas decimais, não vírgula:

Errado: 2,5
Correto: 2.5
 

Operações lógicas
10. Operações booleanas
Quando estudamos variáveis, vimos que existem alguns tipos primitivos: str (texto), int (número inteiro), float (número real) e bool (lógico). Vimos diversas operações aritméticas também, como a soma, a divisão ou a potência, cujos resultados são int ou float. Porém, podemos ter também operações cujo resultado é bool: são operações lógicas.

10.1. Comparações
Algumas das operações lógicas mais conhecidas são as comparações:

comparacao1 = 5 > 3
print(comparacao1)
comparacao2 = 5 < 3
print(comparacao2)
Se executarmos o código acima, a saída que teremos na tela será:

True
False
Isso ocorre porque 5 é maior que 3. Portanto, comparacao1 recebeu uma expressão cujo valor lógico é verdadeiro, portanto seu resultado foi True, e o oposto ocorreu para comparacao2. O Python possui 6 operadores de comparação:

Maior que: >
Maior ou igual: >=
Menor que: <
Menor ou igual: <=
Igual: ==
Diferente: !=
Note que o operador para comparar se 2 valores são iguais é ==, e não =. Isso ocorre porque o operador = é o nosso operador de atribuição: ele diz que a variável à sua esquerda deve receber o valor da expressão à direita. O operador de == irá testar se o valor à sua esquerda é igual ao valor à sua direita e irá responder True ou False, como todos os outros operadores de comparação.

10.2. Negação lógica
Outra operação lógica bastante importante é a negação. Ela inverte o resultado de uma expressão lógica. Caso a expressão resulte em True, a sua negação irá resultar em False, e vice-versa.

A negação em Python é representada pela palavra not. Vamos modificar o exemplo anterior:

comparacao1 = not 5 > 3
print(comparacao1)
comparacao2 = not 5 < 3
print(comparacao2)
O resultado será:

False
True
Podemos resumir o funcionamento do not utilizando uma tabela-verdade. Nela testamos os diferentes valores possíveis para a entrada e anotamos o resultado para cada conjunto de valores:

A	not A
True	False
False	True
10.3. Conjunção lógica
Em alguns casos precisamos testar se duas ou mais condições são verdadeiras.

Imagine, por exemplo, que o critério de aprovação em uma escola seja a média superior a 6.0 e presença superior a 75%. Neste caso, o aluno precisa atender a ambos os critérios para ser aprovado. Se ele tirou uma ótima nota, mas faltou demais, será reprovado. Se ele compareceu a todas as aulas, mas teve notas baixas, idem.

A conjunção lógica, também conhecida como e lógico, é representada em Python pela palavra and.

O código abaixo testa se é verdade que o aluno foi aprovado:

media = float(input('Digite a média do aluno: '))
presenca = float(input('Digite as presenças do aluno: '))
 
aprovado = media >= 6.0 and presenca >= 0.75
print('O aluno foi aprovado?', aprovado)
Execute o código acima e teste algumas combinações diferentes de valores. Note que basta uma das condições ser falsa para que o resultado total seja False.

A tabela-verdade para o e lógico entre duas entradas A e B é:

A	B	A and B
False	False	False
False	True	False
True	False	False
True	True	True
10.4. Disjunção lógica
Nem sempre precisamos que ambas as condições sejam verdadeiras. Vários de nós já nos deparamos com promoções de queima de estoque anunciadas da seguinte maneira: "promoção válida até o dia 15 deste mês ou enquanto durarem os estoques".

Neste caso, para a promoção acabar, não é necessário que ambas as coisas ocorram (atingir o dia 15 e zerar o estoque). Se ainda temos 10 itens no estoque, mas hoje é dia 16, a promoção acabou. Se hoje é dia 5, mas o estoque está zerado, a promoção acabou.

A disjunção lógica, também chamada de ou lógico, é representada em Python pela palavra or.

O programa abaixo testa se a promoção acabou:

dia_final = int(input('Digite o dia do mês para encerrar a promoção: '))
dia_atual = int(input('Digite o dia do mês atual: '))
estoque = int(input('Digite a quantidade de itens no estoque: '))
 
acabou = dia_atual > dia_final or estoque == 0
print(acabou)
Faça alguns testes com o programa acima e note que basta uma condição ser verdadeira para seu resultado ser True.

A tabela-verdade para o ou lógico é:

A	B	A and B
False	False	False
False	True	True
True	False	True
True	True	True
Resumo:

not: inverte a expressão original
and: verdadeiro apenas se ambas as condições forem verdadeiras
or: falso apenas se ambas as condições forem falsas
11. Valores truthy e falsy
Valores não-booleanos em Python, como inteiros ou strings, podem ser convertidos para booleanos utilizando a função bool, da mesma maneira que utilizamos int e float em exemplos anteriores para converter entradas de string para número.

Certos valores serão convertidos para True, enquanto outros serão convertidos para False. Em certos contextos, como expressões condicionais - que serão estudadas muito em breve - essa conversão ocorre de maneira implícita. Quando um valor pode ser interpretado como True, dizemos que ele é um valor truthy, e quando ele pode ser interpretado como False, ele é conhecido como um valor falsy.

Valores Falsy comuns são:

O valor inteiro 0
O valor real 0.0
Strings vazias (strings com 0 caracteres)
Coleções vazias (listas, tuplas, dicionários etc. com 0 elementos)
Valores Truthy comuns são:

Inteiros diferentes de 0
Reais diferentes de 0.0
Strings contendo ao menos 1 caractere
Coleções (listas, tuplas, dicionários etc.) com pelo menos 1 elemento
A constante None, que representa uma variável "vazia"
Não se preocupe se não estiver familiarizado com todos os dados exemplificados aqui. Estudaremos cada um deles em outros momentos.

 

Expressões condicionais
12.1. Se
Os programas do capítulo Operações Lógicas não são "amigáveis" para o usuário. Ao invés de mostrar True ou False, por exemplo, seria mais útil exibir se o aluno foi "Aprovado" ou "Reprovado".

Para que possamos escrever na tela as mensagens "Aprovado" ou "Reprovado", é necessário que haja em algum ponto do código o trecho print('Aprovado') e o trecho print('Reprovado'). Porém, não gostaríamos que ambos fossem exibidos ao mesmo tempo.

Precisamos ramificar o fluxo de execução de nosso programa: em certas circunstâncias, o fluxo deve executar algumas linhas de código e ignorar outras.

Uma condicional é uma instrução em Python que decide se outras linhas serão ou não executadas dependendo do resultado de uma condição. A condição nada mais é do que uma expressão lógica. Se a condição for verdadeira, as linhas são executadas. Senão, são ignoradas.

A condicional mais básica em Python é o if (se):

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
 
media = (nota1 + nota2)/2
 
if media >= 6.0:
    print('Aprovado')

print('Média: ', media)
Execute o programa acima. Note que se (if) a média é maior ou igual a 6.0, ele exibe a mensagem "Aprovado" e depois a média. Caso contrário, ele apenas exibe a média.

Para dizermos que uma ou mais linhas "pertencem" ao nosso if, usamos um símbolo de parágrafo (tecla "Tab" no teclado). O programa sabe que o if "acabou" quando as linhas param de ter "tabs". Esses tabs são chamados de indentação. Tanto no if quanto no restante das estruturas de controle que estudaremos é obrigatório ter pelo menos 1 linha indentada abaixo da linha de controle.

12.2. Senão
Note que conseguimos fazer nosso programa decidir se ele exibe a mensagem "Aprovado" ou não. O próximo passo seria fazer ele decidir entre 2 mensagens diferentes: "Aprovado" ou "Reprovado". Um primeiro jeito de fazer isso seria um segundo if invertendo a condição:

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
 
media = (nota1 + nota2)/2
 
if media >= 6.0:
    print('Aprovado')
if media < 6.0:
    print('Reprovado')
    
print('Média: ', media)
O programa acima funciona. Porém, conforme nossos programas começam a ficar mais complexos e nossos if começam a ter linhas demais, podemos nos perder e esquecer que esses 2 if são 2 casos mutuamente exclusivos. Pior ainda, podemos vir a acrescentar condições novas em um e esquecer de atualizar no outro.

Nos casos em que temos condições mutuamente exclusivas, podemos utilizar um par if/else (se/senão). Se a condição for verdadeira, faça tal coisa. Senão, faça outra coisa.

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
 
media = (nota1 + nota2)/2
 
if media >= 6.0:
    print('Aprovado')
else:
    print('Reprovado')
    
print('Média: ', media)
Note que o else não possui condição. A condição dele é implícita: é a negação da condição do if. Se o if executar, o else não executa e vice-versa. Consequentemente, o else não pode existir sem um if.

12.3. Aninhando condições
É possível aninhar condições: ou seja, colocar um novo if dentro de outro if ou else. Imagine que nossa escola não reprova direto o aluno com nota inferior a 6, e sim permite que ele faça uma recuperação. Porém, o aluno precisa ter tirado no mínimo média 3 para que permitam que faça a recuperação. Assim temos:

Se nota maior ou igual a 6: aprovado.
Senão:
Se nota entre 6 e 3: recuperação.
Senão: reprovado. Em Python:
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
12.4. Senão-se
Note que se começarmos a aninhar muitas condições (if dentro de else dentro de else dentro de else...), nosso código pode começar a ficar confuso, com a aparência de uma "escadinha":

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
Isso pode tornar o código bastante complexo e difícil de atualizar ou corrigir erros posteriormente. Para quebrar a "escadinha", existe a possibilidade de juntarmos o "se" do próximo nível com o "senão" do nível anterior: o elif: else + if (senão + se).

O elif só é executado se um if der errado (ou seja, ele é um else), mas ele também tem uma condição que deve ser respeitada (ou seja, ele também é um if). Podemos reescrever nosso código anterior utilizando um elif:

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
Podemos usar quantos elif nós quisermos. Sempre que um deles der errado, o próximo será testado. Quando algum deles der certo, todo o restante será ignorado.

Opcionalmente, podemos ter um else ao final do bloco, que só será executado se o if e todos os elif derem errado.

O bloco, obrigatoriamente, deve ser iniciado com um if.

Atenção
Você lembra dos valores truthy e falsy? Nós conversamos sobre eles no capítulo Operações Lógicas. Uma variável, qualquer que seja seu tipo, pode ser interpretada pelo if como se fosse uma expressão lógica.

Se x for um inteiro, o bloco if x: será executado caso x seja diferente de zero, por exemplo.

Uma fonte comum de erros em iniciantes envolve o uso de and ou or em condicionais e a forma como Python lida com valores truthy e falsy. Execute o trecho de código abaixo:

seguro = input('Deseja adquirir um seguro opcional (sim/não): ')
 
if seguro != 'sim' and 'não':
    print('Você não digitou uma opção válida')
Você verá que ele nem sempre se comporta como você imaginaria. O Python não irá interpretar a condição do if como "seguro diferente de 'sim' e seguro diferente de 'não'", e sim como "(seguro diferente de 'sim') e ('não').

Isso ocorre porque no if temos uma expressão lógica do tipo expressão1 and expressão2. Nossa expressão1 é seguro != 'sim', e nossa expressão2 é apenas a string 'não'.

A expressão2 é, portanto, uma string não-vazia, portanto ela é truthy. O Python irá implicitamente convertê-la para o valor lógico True. Portanto, temos a expressão (seguro !='sim') and (True). Logo, a condição será verdadeira se seguro !='sim' e falsa caso contrário. Logo, se você digitar "não", a expressão é falsa e o programa dirá que você digitou algo inválido.

Para evitar esse problema, você precisa ser explícito em suas condições:

seguro = input('Deseja adquirir um seguro opcional (sim/não): ')
 
if seguro != 'sim' and seguro !='não':
    print('Você não digitou uma opção válida')
 

Malhas de repetição condicionais
Imagine que você queira fazer um programa que exibe os números de 1 até 5, em ordem crescente. Uma possibilidade seria:

print(1)
print(2)
print(3)
print(4)
print(5)
Porém, imagine que os requisitos do programa acabam sendo alterados, e agora o seu programa deverá ir até 1000. Ou, pior, imagine que o usuário irá digitar um valor e seu programa deverá contar apenas até o valor digitado. Note como fica difícil resolver esses problemas apenas copiando e colando linhas de código.

Vamos pensar em outro tipo de problema. Na aula passada, fizemos um exercício onde precisávamos validar algumas entradas do usuário. Uma dessas entradas era a idade, e gostaríamos de aceitar apenas valores entre 0 e 150. Sua solução provavelmente foi parecida com o código abaixo:

idade = int(input('Digite a idade: '))
 
if idade < 0 or idade > 150:
  print('Erro')
Mas imagine que, ao invés de apenas mostrar uma mensagem de erro, nós devêssemos obrigar o usuário a continuar digitando valores novos para idade até que ele digite um valor válido (entre 0 e 150). Isso não seria possível utilizando apenas if, elif e else.

13.1. Enquanto
Os problemas enunciados acima podem ser resolvidos utilizando estruturas do tipo "enquanto". Em Python, a instrução while é bastante parecida com o if: ela possui uma expressão lógica, e seu conteúdo só será executado se a expressão for verdadeira. Porém, após chegar ao final, ela retorna ao início e testa novamente a condição.

Se ela for verdadeira, seu conteúdo será executado de novo. Ao final da nova execução, a condição é testada novamente, e assim sucessivamente. A execução só será interrompida quando o teste se tornar falso. Vejamos como resolver o problema da idade utilizando o while:

idade = int(input('Digite a idade: '))
 
while idade < 0 or idade > 150:
  print('Erro! Idade deve estar entre 0 e 150!')
  idade = int(input('Digite a idade: '))
 
print('Obrigado!')
Faça alguns testes com o programa acima. Note que se você digitar uma idade válida desde o início, ele nunca chega a mostrar erro: o while é como um if e será ignorado se sua condição for falsa. Porém, caso você digite valores inválidos, a condição será verdadeira e ele irá executar enquanto você estiver digitando valores falsos.

Estruturas do tipo "enquanto" são conhecidas como malhas de repetição ou loops.

13.2. Condição de parada
No exemplo anterior, o que determina se o loop prossegue ou não é o valor de idade. Esse valor, por sua vez, pode mudar em cada execução do loop, já que temos um input lá dentro. Experimente rodar o programa sem aquele input e verifique o que ocorre.

idade = int(input('Digite a idade: '))
 
while idade < 0 or idade > 150:
  print('Erro! Idade deve estar entre 0 e 150!')  
print('Obrigado!')
O que ocorreu é o que chamamos de loop infinito: se a condição for verdadeira uma vez, ela será para sempre, já que nunca mais alteramos o valor da variável envolvida no teste lógico. É importante criar caminhos para que a condição possa se tornar falsa em algum momento. Isso é o que chamamos de condição de parada do nosso loop.

13.3. Sequências numéricas
Iniciamos essa aula enunciando um problema onde gostaríamos de exibir números sequencialmente na tela. Isso é possível de resolver utilizando loops. Primeiro, observe o exemplo abaixo e responda: qual valor aparecerá na tela?

x = 5
x = x + 1
print(x)
Essa construção parece pouco intuitiva porque na matemática o operador = é bidirecional: a expressão "a = b" significa que a é igual a b e b é igual a a. Ao vermos x aparecendo em ambos os lados, parece que podemos simplesmente cortar dos dois lados, resultando em 0 = 1, o que é uma inverdade.

Em Python o operador = na verdade não é o operador de igualdade da matemática, e sim o operador de atribuição de valores. Ou seja, o que ele diz é "pegue o resultado da expressão à direita e guarde na variável à esquerda". Portanto, o exemplo acima pega primeiro o valor antigo de x, que era 5, adiciona 1, resultando em 6, e guarda este novo resultado na variável x, substituindo o valor antigo. Logo, a resposta na tela é 6.

Se colocarmos uma expressão desse tipo dentro de um loop, podemos gerar sequências numéricas:

final = int(input('Digite o valor final da sequência: '))
numero = 1
 
while numero <= final:
  print(numero)
  numero = numero + 1
O programa acima pede para o usuário digitar um número, que será o valor final da sequência. Então ele irá imprimir a variável numero, que vale 1, e somar +1 nela. Em seguida imprimirá de novo a variável, agora valendo 2, e somará +1 nela. E assim sucessivamente até que ela ultrapasse o valor final, quando o loop deixará de ser executado.

Você consegue modificar o programa acima para fazer uma sequência decrescente? E para gerar a tabuada de um número dado pelo usuário? Você precisará mexer na expressão lógica do loop e no incremento de numero.

Em expressões onde uma variável aparece de ambos os lados, podemos utilizar uma abreviação. Por exemplo, a expressão x = x + 5 Pode ser reescrita como: x += 5 Isso vale para todas as outras expressões aritméticas (subtração, multiplicação, divisão etc.).

14. Comandos de manipulação de fluxo
É possível manipular de algumas maneiras a forma como uma malha de repetição se comporta: nós podemos interromper sua execução sem que sua condição de parada tenha sido atingida e podemos saltar para o próximo passo sem finalizar o atual.

14.1. Break
Vamos montar um exemplo simples: imagine que você irá fazer um joguinho onde o usuário terá 10 tentativas para adivinhar um número secreto. Um bom primeiro passo seria criar um loop que conta as 10 tentativas:

numero_secreto = 42
 
contador = 0
 
while contador < 10:
  tentativa = int(input('Adivinhe o número secreto: '))
  if tentativa == numero_secreto:
    print('Acertou')
  else:
    print('Errou')
  contador += 1
No momento, mesmo que o usuário acerte, ele irá contar até a décima tentativa. Com o que já aprendemos até o momento, poderíamos consertar isso colocando uma segunda condição de parada:

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
Se você executar o programa, verá que ele funciona: caso o usuário acerte ou 10 tentativas sejam feitas, o programa encerra sua execução. Mas note que o código ficou um pouquinho mais bagunçado: estamos testando duas vezes o valor de tentativa: na condição do while e na condição do if. Não seria mais prático dentro do próprio if, logo após informar para o usuário que ele acertou, se a gente já pudesse falar para o loop parar de ser executado?

É aí que entra o break: quando estamos em uma malha de repetição e encontramos o comando break, a malha é interrompida imediatamente. Podemos reescrever o programa acima utilizando esse comando:

numero_secreto = 42
 
contador = 0
 
while contador < 10:
  tentativa = int(input('Adivinhe o número secreto: '))
  if tentativa == numero_secreto:
    print('Acertou')
    break
  print('Errou')
  contador += 1
Alguns programadores utilizam while True: (ou seja, um loop a princípio infinito) e no corpo do loop espalham combinações de if + break. Exceto em situações muito específicas e raras, isso é uma má prática e deve ser evitada, pois compromete bastante a legibilidade do código, e consequentemente sua manutenção no futuro.

14.2. Else
Você pode observar que no programa acima, respondemos "Errou" para cada chute errado do usuário. Mas o programa ainda não informou para ele que as tentativas dele se esgotaram. Temos algumas possibilidades aqui!

Uma delas seria testar o valor do contador no final do loop:

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
Outra seria utilizar uma flag: uma variável booleana que indica se entramos no if ou não:

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
Na maioria das linguagens de programação, teríamos que optar por uma dessas alternativas. Comandos que estudamos aqui em Python são comuns a várias linguagens diferentes, incluindo o par if/else, o while e o break.

Mas o Python possui uma ferramenta adicional bastante incomum, mas que pode simplificar problemas desse tipo. Ele permite a utilização de um else para um loop. A estrutura deve ser a seguinte:

 
while (condicao_principal):
  ...
  ...
  if (condicao_secundaria):
    break
  ...
  ...
else:
  ...
Esse código funcionará da seguinte maneira: se o loop parar pela condição principal (ou seja, executou a quantidade "correta" de repetições), o else será executado. Se o loop parar pela condição secundária (ou seja, por conta de um break), o else será ignorado.

Sendo assim, podemos reescrever nosso programa principal de maneira mais pythonica utilizando esse recurso:

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
Execute o programa e veja que ele só irá mostrar a mensagem de derrota quando as 10 tentativas forem concluídas.

14.3. Continue
Existe outro comando de desvio de fluxo de malhas de repetição: o continue. A diferença entre ele e o break é que o continue encerra apenas o passo atual de repetição, mas ele não encerra o loop como um todo. Quando executamos esse comando, o loop irá voltar para o topo, testar novamente sua condição de parada, e caso ela não tenha sido atingida, ele iniciará uma nova iteração (ou seja, um novo passo em um loop).

Vamos reescrever nosso programa anterior invertendo a verificação para vermos o continue em ação.

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
Sempre que o usuário errar o chute, o continue irá desviar o fluxo de execução de volta para o início do loop, impedindo que as duas últimas linhas do loop sejam executadas. Ou seja, ele não irá dizer "acertou", tampouco executar o break.

Atenção: todos os desvios estudados aqui podem ser utilizados, caso contrário, não existiriam. Porém, em certas situações eles podem tornar o código mais confuso. Por exemplo, quando temos diversos loops aninhados, pode não ficar claro para alguém lendo o código qual dos loops está sendo encerrado. Sempre que for utilizar esses recursos, verifiquem se eles estão melhorando ou piorando a legibilidade do código.

 

Malhas de repetição com contador
No capítulo de malhas de repetição vimos casos em que precisamos contar quantas vezes o loop se repete, e parar quando a contagem atinge um certo valor. Em outras ocasiões, apenas precisamos de algum tipo de sequência numérica. Nestes casos, era normal utilizar uma variável de contador, incrementá-la em cada passo e utilizar seu valor como condição de parada. O exemplo abaixo imprime todos os números pares entre 0 e 100:

contador = 0
while contador < 100:
    print(contador)
    contador = contador + 2
Existe um meio de automatizar todas as operações envolvidas: atribuir um valor inicial, atribuir um valor final e realizar o incremento.

15.1 Loops do tipo "para"
Dizemos que o exemplo acima é um loop do tipo "para": para contador de 0 até 100 com passo 2 faça: imprima contador. Em Python, podemos criar esse tipo de loop utilizando os comandos for e range. O exemplo abaixo imprime os números de 0 até 9 na tela:

for contador in range(10):
    print(contador)
O código acima é equivalente ao seguinte código utilizando while:

contador = 0
while contador < 10:
    print(contador)
    contador += 1
A palavra "contador" é apenas uma variável. Ela não precisa ser criada previamente: qualquer nome utilizado nesta construção será automaticamente inicializado pelo for.

O programa acima atribui o valor inicial 0 à variável. Em seguida, ele executa tudo que vier dentro do loop, e ao chegar ao final, ele retorna ao início, soma 1 na variável e testa se o seu valor atingiu o número entre parênteses. Caso não tenha atingido, ele repete a execução. Dizemos que aquele número é o valor final exclusivo (pois o loop exclui esse valor).

De forma geral, tudo que vier dentro de um for contador in range(x) irá executar "x" vezes. É o jeito fácil de dizer "repita essas linhas x vezes" em Python.

15.2 Parâmetros do range
Foi dito que loops do tipo "para" seguem a forma "para contador de X até Y passo Z faça:". No exemplo acima, os valores iniciais (0) e passo (1) foram atribuídos de forma automática. Caso eles sejam omitidos, 0 e 1 são os valores padrão, respectivamente. Porém, podemos determiná-los, se necessário. O exemplo abaixo inicia a impressão dos números em 1 ao invés de 0:

for contador in range(1, 10):
    print(contador)
Dizemos que esse loop possui valor inicial 1, valor final (exclusivo) 10 e passo 1.

O código acima é equivalente ao seguinte código utilizando while:

contador = 1
while contador < 10:
    print(contador)
    contador += 1
Assim como manipulamos o valor inicial e o final, podemos manipular também o passo. Veja o exemplo abaixo:

for contador in range(0, 100, 2):
    print(contador)
O código acima é equivalente ao seguinte código utilizando while:

contador = 0
while contador < 100:
    print(contador)
    contador += 2
Note que o resultado dele na tela é exatamente o mesmo do exemplo com while do início deste capítulo! Valor inicial 0, valor final (exclusivo) 100 e passo 2. Porém, não precisamos nos preocupar em criar o contador, atribuir valor inicial, incrementar e criar uma condição de parada. Apenas colocamos os números dentro do range e ele fez a mágica por nós.

Antes de finalizar, vamos reforçar: o comportamento de cada parâmetro passado para o range depende de quantos parâmetros foram passados e da ordem que eles foram passados:

1 parâmetro = valor final exclusivo
2 parâmetros = valor inicial, valor final exclusivo
3 parâmetros = valor inicial, valor final exclusivo, passo
Quantos exercícios de while você fez que podem ser resolvidos de maneira mais fácil com o for?

Dica: é possível utilizar o for para gerar sequências numéricas decrescentes também. Basta adotar valor final menor do que o inicial e incremento negativo.

for contador in range(20, 0, -1):
  print(contador)
Qual valor será excluído da sequência: o 20 ou o 0? Tente deduzir e execute o programa para ver se acertou!

15.3. Comandos de desvio de fluxo
Os comandos de desvio de fluxo que estudamos junto do while (break, continue e else) também funcionam da mesma maneira com o for. Algumas observações sobre eles:

break: irá encerrar o loop antes de atingir o fim da sequência
else: será executado caso um break seja executado e ignorado caso o loop chegue ao final da sequência
continue: encerra o passo atual e passa para o próximo avançando na sequência automaticamente
 

Listas
Já fizemos alguns programas para ler 2 ou 3 notas e calcular a média. Inclusive já fomos além e aprendemos a verificar se o aluno passou ou não. Vamos rever um exemplo desses:

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
 
media = (nota1 + nota2)/2
 
print(media)
Simples, certo? Mas e se a regra da escola mudasse, e agora cada professor precisasse aplicar 4 provas? Modificaríamos nosso programa:

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
 
media = (nota1 + nota2 + nota3 + nota4)/4
 
print(media)
Até aqui tudo bem. Mas e se o objetivo fosse testar o quanto o professor consegue ensinar? Para isso, poderíamos calcular a média das médias de todos os alunos do professor. Mas e se o professor trabalha em uma faculdade muito grande e suas turmas têm 80 alunos?

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
Nota do programador: eu me demito.
Não ganho bem o suficiente para ISSO!
```
Para trabalhar com poucos valores, é fácil e conveniente criar uma variável para cada valor e realizar operações individualmente sobre cada uma. Porém, dizemos que esse tipo de solução não é escalável: o programa não está preparado para lidar com variações no tamanho da base de dados, e modificá-lo para comportá-las pode ser difícil, trabalhoso ou mesmo inviável.

Imagine se para cada novo perfil em uma rede social o estagiário precisasse criar uma variável nova para o nome, uma para o e-mail, uma para a data de nascimento, e assim sucessivamente... E depois ainda precisasse de linhas novas de código para ler cada um desses valores do novo usuário!

16. Listas
É aí que entram as listas. Listas são coleções de objetos em Python. Falando de maneira simplificada, são variáveis que comportam diversos valores ao mesmo tempo. Vejamos alguns jeitos de criar listas em Python:

primeira_lista = [] # cria uma lista vazia
segunda_lista = list() # cria uma lista vazia
terceira_lista = [1, 3.14, 5, 7, 9, 'onze'] # lista com valores
Note que podemos misturar tipos de dados. A terceira_lista possui 4 int, um float e uma str.

Bom, e agora, como fazemos para acessar cada valor? Podemos imaginar a lista da seguinte maneira: imagine que ao invés de ter uma caixa para guardar cada item, temos uma cômoda com várias gavetas. Cada item está em uma gaveta. Não estamos acostumados a dizer que algo está na terceira gaveta do armário? A ideia é a mesma: a lista é uma coleção indexada, ou seja, podemos acessar cada elemento através de índices, que são números indicando a posição. A indexação é automática e começa a partir do zero:

elemento	1	3.14	5	7	9	11
índice	0	1	2	3	4	5
Portanto, para acessar o elemento "7" da nossa lista, utilizaríamos o índice 3. Informamos o índice entre colchetes:

terceira_lista = [1, 3.14, 5, 7, 9, 'onze'] # lista com valores
print(terceira_lista[3])
A lista é mutável. Isso significa que podemos modificar os valores já existentes:

terceira_lista = [1, 3.14, 5, 7, 9, 'onze'] # lista com valores
terceira_lista[3] = 'sete' # troca 7 por 'sete' na lista
print(terceira_lista)
É possível utilizar índices negativos. lista[-1] pega o último elemento, lista[-2] o penúltimo, e assim sucessivamente. Mas não é possível acessar índices iguais ou superiores ao tamanho da lista. A tentativa de acessar um índice inexistente resultará em erro.

17. Quebrando listas
É possível pegar subconjuntos de nossas listas utilizando o conceito de slices. Ao invés de passar apenas 1 valor entre colchetes (o índice desejado), podemos passar faixas de valores. Veja o exemplo abaixo:

impares = [1, 3, 5, 7, 9, 11, 13, 15, 17]
meio = impares[3:6]
print(meio) # resultado na tela: [7, 9, 11]
O primeiro valor é o índice inicial da sublista a ser gerada, e o segundo é o índice final (exclusivo). Podemos omitir um desses valores para indicar que será desde o início ou até o final:

impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
primeira_metade = impares[:5]
segunda_metade = impares[5:]
print(primeira_metade) # resultado: [1, 3, 5, 7, 9]
print(segunda_metade) # resultado: [11, 13, 15, 17, 19]
Além de índices inicial e final, podemos também passar um passo para os índices. Veja o exemplo abaixo:

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# múltiplos de 3 abaixo de 10:
mult3_sub10 = numeros[3:10:3]
print(mult3_sub10) # resultado: [3, 6, 9]
Atenção: quando nós atribuímos uma lista a outra variável, a lista não é copiada. Observe o exemplo abaixo:

lista1 = [1, 3, 5]
lista2 = lista1
lista2.append(7)
print(lista1) # resultado: [1, 3, 5, 7]
Modificações aplicadas em lista2 também afetarão a lista1. Isso ocorre porque não foi criada uma lista. O Python apenas fez com que ambas as variáveis (lista1 e lista2) referenciassem a mesma estrutura na memória. Quando utilizamos slices, isso não ocorre. O Python cria uma lista contendo os valores restritos pelos índices. Sendo assim, uma estratégia fácil para copiar uma lista para outra é utilizar um slice indo da primeira à última posição:

lista1 = [1, 3, 5]
lista2 = lista1[:]
lista2.append(7)
print(lista1) # resultado: [1, 3, 5]
print(lista2) # resultado: [1, 3, 5, 7]
18. Percorrendo listas
Suponha que você queira acessar cada elemento de sua lista individualmente. Digitar todos os índices manualmente cancelaria a escalabilidade do programa, certo? Portanto, podemos usar um loop para gerar os índices:

pares = [0, 2, 4, 6, 8]
tamanho = len(pares) # calcula o tamanho da lista
 
# tamanho vale 5, logo índice recebe os valores 0, 1, 2, 3 e 4
for indice in range(tamanho):
  print(pares[indice])
Porém, tem um jeito ainda mais fácil de percorrer a lista. O for não serve apenas para gerar sequências numéricas junto do range: ele serve para percorrer coleções. Portanto, podemos trocar o range pela própria lista:

pares = [0, 2, 4, 6, 8]
 
for elemento in pares:
  print(elemento)
Assim como no caso das contagens, "elemento" é apenas uma variável que será criada de forma automática e poderia ter qualquer nome. Em cada repetição do loop, um valor diferente da lista será copiado para elemento.

Importante: Como os elementos são copiados, caso você modifique o valor de elemento você não irá modificar o valor na lista, e sim uma cópia dele. Além disso, como este loop serve especificamente para percorrer listas, se dentro dele você fizer operações que alterem o tamanho da lista (append ou remove, por exemplo), o loop poderá executar incorretamente, pulando ou repetindo elementos.

O for serve, primariamente, para percorrer coleções. Ou seja, para iterar coleções. O range age, na prática, como se fosse uma lista contendo os valores determinados por seu parâmetro. Dizemos que a função range gera um iterável, ou seja, um tipo especial de dado que pode ser percorrido através de um loop.

19. Testando a existência de valores
Existe um comando que temos visto bastante recentemente: o in. Ele costuma aparecer no for para indicar a lista ou a sequência a ser percorrida. Mas ele também possui outra utilidade.

O in pode ser utilizado para informar se um elemento está presente em uma lista ou não. Observe a saída do código abaixo.

linguagens = ['Python', 'JavaScript', 'C#', 'Java']
 
existe_html = 'HTML' in linguagens
existe_java = 'Java' in linguagens
 
print('HTML:', existe_html) # HTML: False
print('Java:', existe_java) # Java: True
Normalmente utilizamos esse comando junto de um if quando precisamos checar se um elemento existe:

linguagem_desejada = input('Digite a linguagem que você gostaria de aprender: ')
 
linguagens = ['Python', 'JavaScript', 'C#', 'Java']
 
if linguagem_desejada in linguagens:
  print('Faça o curso conosco! :)')
else:
  print('Não temos esse curso disponível no momento :(')
 

Funções de listas
As listas possuem diversas funções prontas bastante úteis. Veremos algumas das mais usadas. Não se preocupe em decorar todas elas: sempre podemos consultar nosso material quando precisarmos de um lembrete! Com tempo e prática você irá aos poucos memorizar algumas delas.

20. Adicionando elementos
Podemos adicionar novos elementos na lista de duas maneiras. A primeira delas, mais simples, é o append. Ele adiciona um elemento ao final da lista. Veja o exemplo abaixo:

pares = [0, 2, 4, 6, 8]
pares.append(10)
print(pares) # resultado: [0, 2, 4, 6, 8, 10]
Outra maneira é com o insert: além do elemento, ele recebe a posição do novo elemento. O primeiro parâmetro é a posição, e a segunda é o valor.

pares = [0, 2, 4, 8, 10]
pares.insert(3, 6)
print(pares) #resultado: [0, 2, 4, 6, 8, 10]
Note que o valor que ocupava a posição anteriormente não é substituído, mas "empurrado" para a próxima posição.

21. Removendo elementos
Podemos remover o elemento de 2 jeitos: por valor e por posição. O remove irá remover o primeiro elemento encontrado na lista com um dado valor. Ex:

impares = [1, 3, 3, 5, 7, 9]
impares.remove(3)
print(impares) # resultado: [1, 3, 5, 7, 9]
O pop remove o elemento que estiver em uma dada posição, independentemente de seu valor:

impares = [1, 3, 5, 7, 8, 9]
impares.pop(4)
print(impares) # resultado: [1, 3, 5, 7, 9]
Se nenhum valor for passado no pop, ele irá remover necessariamente o último elemento da lista.

22. Ordenando a lista
Podemos ordenar a lista usando o sort.

fibonacci = [8, 1, 0, 5, 13, 1, 3, 2]
fibonacci.sort()
print(fibonacci) # resultado: [0, 1, 1, 2, 3, 5, 8, 13]
Caso desejássemos ordenar em ordem decrescente, podemos passar a opção reverse = True para o sort:

fibonacci = [8, 1, 0, 5, 13, 1, 3, 2]
fibonacci.sort(reverse = True)
print(fibonacci) # r








___

### Bibliografia Extra

- http://bit.ly/MasEraSoPedir
  `https://www.geledes.org.br/quadrinho-explica-por-que-as-mulheres-se-sentem-tao-cansadas/`
- https://drauziovarella.uol.com.br/mulher/carga-mental-feminina-por-que-as-mulheres-estao-exaustas/ 
- https://thinkolga.com/report/economia-trabalho/
- https://www.instagram.com/despatologiza/
  - <img width="878" height="776" alt="image" src="https://github.com/user-attachments/assets/e89771a5-fd3d-462e-a275-fe07dd0a480b" />

"""
