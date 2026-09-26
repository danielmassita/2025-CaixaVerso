"""
Seu objetivo é desenvolver um conjunto de funções que explore os conhecimentos adquiridos em aula para criar, consultar, atualizar e deletar um banco de alunos de uma escola, que deve ser armazenado em uma
estrutura (variável) que combine pelo menos listas e dicionários da forma que você julgar mais adequada. Eu gostaria que o seu trabalho atendesse aos seguintes requisitos:

1.  Os alunos devem estar armazenados em uma variável, através de
uma estrutura que combine pelo menos dicionários e listas, da
maneira que você considerar mais adequada.

2.  Para cada aluno, devem existir as informações: número de matrícula,
nome completo, nível, idade e boletim. O boletim deve ser capaz de
guardar todos os nomes das disciplinas que aquele aluno cursa,
assim como as notas das avaliações feitas em cada disciplina. Aqui,
fique à vontade para usar dicionários dentro de dicionários, listas
dentro de listas, dicionários dentro de listas ou listas dentro de
dicionários. Implemente a estrutura seguindo a organização que você
achar melhor.

3.  Quero que você implemente as seguintes funções python:

3.a  Função criar_escola_vazia, que inicializa a variável que será
responsável por armazenar todo o conteúdo da escola, já
contendo uma estrutura vazia, mas compatível com o que o
restante do código entender como sendo a estrutura de dados
que a escola deve conter. Por exemplo, se definirmos que a
escola deve ser uma lista, essa função deve gerar uma lista
vazia.

3.b  Função adicionar_aluno, que recebe obrigatoriamente um
número de matricula, um nome completo, um nível e uma
idade, e acrescenta este aluno na variável que guarda a
escola. A função deve ser capaz de receber, também, uma lista
de turmas para este aluno, caso o usuário queira já no
momento de cadastro do aluno salvá-lo com um boletim contendo suas turmas, mas ainda sem nenhuma nota por
turma.

3.c  Função para cadastrar nota do aluno. A função deve receber o
número de matrícula, o nome da disciplina e cadastrar uma
nota para o aluno indicado na disciplina indicada. Note que
cada aluno deve poder ter múltiplas notas para a mesma
disciplina.

3.d  Função para alterar a nota de um aluno. É semelhante à
função anterior, mas esta precisa receber também a
informação acerca de qual nota se deseja alterar, se a primeira,
a segunda, a terceira, … E sempre para uma disciplina
específica.

3.e  Função para alterar algum dado cadastral de um aluno. A
função deve receber o número de matrícula do aluno, a
identificação de qual dado se deseja alterar e qual é o novo
valor que se deseja que o dado tenha.

3.f  Função para visualizar os dados completos de um aluno. A
função deve receber um número de matrícula e mostrar na tela
todas as informações a respeito de um aluno.

3.g  Função que retorna a média de um aluno para alguma
disciplina e a situação: se aprovado ou reprovado. A função
deve receber o número de matrícula, a disciplina desejada e a
nota mínima para aprovação, e retornar a média das notas
cadastradas para aquele aluno naquela disciplina, bem como a
situação de aprovação com base na nota mínima passada por
parâmetro.

3.h  Função para apagar um aluno da escola. Dado um número de
matrícula, a função deve apagar da escola o registro
correspondente a este aluno, respeitando a estrutura de dados
que foi estabelecida para a escola.

3.i  Função que retorna uma análise geral do desempenho dos
alunos da escola, agregada por disciplina. Isto é, a função
retorna, de uma só vez: a taxa de reprovação, a média de
notas e a quantidade de avaliações por disciplina.

3.j  Função que retorne quantos alunos existem na escola.

4.  Use tratamentos de exceção.

5.  Foque na ideia de: “vou mostrar o máximo que eu sei”. Por exemplo,
se você está com dificuldades na parte de funções, implemente a
lógica por trás dos itens acima sem necessariamente encapsula-las
dentro de funções. Eu saberei que você tem dificuldade com
funções, mas também saberei que você compreendeu todo o resto.
Faça o máximo que você conseguir, ainda que isto não seja
exatamente o que estou pedindo. O objetivo aqui é eu poder ver o
máximo que você aprendeu.


Por fim...​

Se o módulo ou mesmo este trabalho ficou parecendo para você algo
muito complexo, fique muito tranquilo e tranquila. O nosso curso aqui na
Ada tem um ritmo bastante acelerado mesmo. É um excelente primeiro
contato com o assunto, mas é perfeitamente esperado que tudo pareça
muito difícil quando estamos dando nossos primeiros passos na
programação de computadores. Todo começo envolve um início de
aprendizado mais devagar e, não raras vezes, um pouco frustrante.
Comigo foi assim também. Mas siga estudando no seu ritmo, aprendendo
um pouco a cada dia e com a mão na massa sempre que possível. Com
paciência e constância tenho certeza que em algum tempo você terá






"""
