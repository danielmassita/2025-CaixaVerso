# 🎓 Escola de Idiomas Ada — Sistema CRUD em Python

> Projeto final do módulo **Lógica de Programação em Python** — curso Ada (CAIXAVERSO FC5 | Analista de Dados II | #1735).
> Sistema de gestão de uma escola de idiomas via terminal, com persistência em arquivo TXT, backup automático e interface estilo caixa eletrônico.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-blue)
![Sem dependências](https://img.shields.io/badge/depend%C3%AAncias-nenhuma-success)

---

## 📚 Sumário

- [Sobre o projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Estrutura do banco de dados](#-estrutura-do-banco-de-dados)
- [Arquitetura em 3 camadas](#-arquitetura-em-3-camadas)
- [Como rodar](#-como-rodar)
- [Como usar (menu)](#-como-usar-menu)
- [Exemplos de saída](#-exemplos-de-saída)
- [Conceitos aplicados](#-conceitos-aplicados)
- [Melhorias futuras](#-melhorias-futuras)
- [Autor](#-autor)

---

## 🎯 Sobre o projeto

Um sistema de linha de comando para gerenciar alunos de uma **escola de idiomas**, permitindo:

- Cadastrar, consultar, atualizar e deletar (CRUD) alunos;
- Registrar e alterar **múltiplas notas** por idioma;
- Calcular **médias**, **situação** e **taxa de reprovação** por idioma;
- Persistir tudo em arquivo `.txt` **legível por humanos**;
- Fazer **backup automático** antes de qualquer gravação;
- Restringir a alteração da nota mínima ao perfil **DIRETOR**.

O projeto foi desenvolvido em ritmo de **Problem Based Learning (PBL)**, com foco em compreensão — não apenas em "fazer funcionar".

---

## ⚙️ Funcionalidades

| # | Função | Descrição |
|---|--------|-----------|
| 1 | `criar_escola_vazia` | Inicializa a estrutura vazia da escola |
| 2 | `adicionar_aluno` | Cadastra aluno com matrícula, nome, nível, idade e idiomas |
| 3 | `cadastrar_nota` | Adiciona nota a um idioma (cria o idioma se não existir) |
| 4 | `alterar_nota` | Altera a N-ésima nota de um idioma específico |
| 5 | `alterar_dado_cadastral` | Altera nome, nível ou idade do aluno |
| 6 | `visualizar_aluno` | Exibe ficha completa com boletim |
| 7 | `calcular_media` | Retorna média + situação (aprovado/reprovado) |
| 8 | `apagar_aluno` | Remove um aluno pelo número de matrícula |
| 9 | `analise_geral` | Estatísticas agregadas por idioma |
| 10 | `quantidade_alunos` | Total de alunos cadastrados |
| ➕ | `salvar_escola` / `carregar_escola` | Persistência em TXT |
| ➕ | `fazer_backup` | Cópia timestamped antes de sobrescrever |

---

## 🗄️ Estrutura do banco de dados

Arquivo `escola.txt`, no formato `.ini`-like com seções:

```text
[CONFIG]
nota_minima=6.0

[ALUNOS]
# matricula;nome;nivel;idade
1;Ana Silva;Básico;15
2;Carlos Souza;Intermediário;17
...

[NOTAS]
# matricula;idioma;nota
1;Inglês;8.5
1;Inglês;7.0
1;Espanhol;9.0
...
```

### Por que esse formato?

- **Legível no Bloco de Notas** — qualquer pessoa entende.
- **Sem dependências** — sem JSON, sem pickle, sem SQLite.
- **Fácil de parsear** — uma leitura linha a linha resolve.
- **Extensível** — basta adicionar uma nova seção `[PROFESSORES]`.
- **Semi-normalizado** — alunos e notas em seções separadas evitam repetição.

---

## 🏗️ Arquitetura em 3 camadas

```text
┌──────────────────────────────────────────────────┐
│  CAMADA 3 — INTERFACE (terminal)                 │
│  main(), exibir_menu(), fluxo_*                  │
├──────────────────────────────────────────────────┤
│  CAMADA 1 — DADOS / REGRAS                       │
│  adicionar_aluno, calcular_media, apagar_aluno…  │
├──────────────────────────────────────────────────┤
│  CAMADA 2 — PERSISTÊNCIA (TXT)                   │
│  salvar_escola, carregar_escola, fazer_backup    │
└──────────────────────────────────────────────────┘
```

Cada camada só conversa com a de baixo:
- A interface **não sabe** abrir arquivo.
- A persistência **não sabe** imprimir menu.
- Os dados **não sabem** que existe um `.txt`.

---

## 🚀 Como rodar

### Requisitos
- Python **3.10+** (usa f-strings e `match/case` opcional em versões futuras)
- Nenhuma biblioteca externa

### Instalação

```bash
git clone https://github.com/<seu-usuario>/escola-idiomas.git
cd escola-idiomas
python escola_idiomas.py
```

Na primeira execução, o programa cria automaticamente:
- `escola.txt` — banco de dados (com **5 alunos de exemplo**)
- `escola_modelo.txt` — cópia do gabarito, nunca sobrescrita
- `backups/` — pasta onde os backups serão guardados

---

## 🖥️ Como usar (menu)

```text
╔══════════════════════════════════════════════════════════╗
║    🎓 ESCOLA DE IDIOMAS ADA — TERMINAL DE ATENDIMENTO    ║
╠══════════════════════════════════════════════════════════╣
║ Nota mínima: 6.0             | Alunos: 5                 ║
╚══════════════════════════════════════════════════════════╝

 ┌──────────────────────────────────────────────────────┐
 │  1. 📋  Listar todos os alunos                       │
 │  2. 🔍  Visualizar aluno (boletim completo)          │
 │  3. ➕  Adicionar aluno                              │
 │  4. 📝  Cadastrar nota                               │
 │  5. ✏️   Alterar nota                                │
 │  6. 🔧  Alterar dado cadastral                       │
 │  7. 📊  Calcular média e situação                    │
 │  8. 🗑️   Apagar aluno                                │
 │  9. 📈  Análise geral por idioma                     │
 │ 10. 🔢  Quantidade de alunos                         │
 │ 11. ⚙️   Configurações (DIRETOR)                     │
 │ 12. 💾  Salvar e sair                                │
 │  0. 🚪  Sair SEM salvar                              │
 └──────────────────────────────────────────────────────┘
```

### 🔐 Acesso ao menu 11 (Configurações)

```text
Login: admin
Senha: admin
```

Apenas o DIRETOR pode alterar a **nota mínima de aprovação**.

---

## 🖨️ Exemplos de saída

### ➕ Adicionar aluno

```text
➕ NOVO ALUNO
Matrícula (número inteiro): 6
Nome completo: Fabiana Costa
Níveis disponíveis: ['Básico', 'Intermediário', 'Avançado']
Nível: Avançado
Idade: 22
Idiomas (separe por vírgula, ex: Inglês,Espanhol): Inglês,Mandarim
✅ Aluno 'Fabiana Costa' cadastrado com sucesso.
```

### 🔍 Visualizar aluno

```text
═══════════════════════════════════════════════════════
 📋 FICHA DO ALUNO — MATRÍCULA 3
═══════════════════════════════════════════════════════
 Nome  : Beatriz Lima
 Nível : Avançado
 Idade : 20 anos
───────────────────────────────────────────────────────
 📚 BOLETIM
───────────────────────────────────────────────────────
 Inglês      : [9.5, 9.0]  |  média: 9.2
 Português   : [10.0]      |  média: 10.0
═══════════════════════════════════════════════════════
```

### 📈 Análise geral por idioma

```text
📈 ANÁLISE GERAL POR IDIOMA
────────────────────────────────────────────────────────────
Idioma             Média    Reprovação    Avaliações
────────────────────────────────────────────────────────────
Inglês               7.5          16.7%             6
Espanhol             6.0          33.3%             3
Francês              7.7           0.0%             3
Português           10.0           0.0%             1
Mandarim             3.5         100.0%             1
────────────────────────────────────────────────────────────
```

### 💾 Salvamento com backup automático

```text
💾 Salvar alterações no BD? (s/n): s
🗂️  Backup criado em: backups/escola_20250101_143022.txt
💾 Escola salva em 'escola.txt'.
👋 Até logo!
```

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece |
|----------|--------------|
| **Variáveis e tipos primitivos** | Toda a estrutura de dados |
| **Condicionais (`if/elif/else`)** | Menu, validações |
| **Malhas de repetição (`while/for`)** | Menu principal, escrita do TXT |
| **Listas** | `escola["alunos"]`, notas de cada idioma |
| **Tuplas** | Retorno `(media, situacao)` de `calcular_media` |
| **Dicionários** | Cada aluno, o boletim, a escola |
| **Funções (parâmetros/retorno)** | Todas as 12 funções |
| **Parâmetros com valor padrão** | `salvar_escola(escola, caminho=ARQUIVO_BD)` |
| **`*args` e `**kwargs`** | Base conceitual para flexibilidade |
| **Tratamento de exceção (`try/except/finally`)** | Toda operação de I/O e validação |
| **`raise` de exceções** | Validações em `adicionar_aluno` |
| **Compreensão de listas** | `sum(1 for n in notas if n < minimo)` |
| **Funções de alta ordem (`map/filter/reduce`)** | Uso de `lambda` no menu |
| **Persistência em arquivo** | `open`, `with`, `write`, `read` |
| **Módulos (`os`, `shutil`, `datetime`)** | Caminhos, backup, timestamp |

---

## 🔮 Melhorias futuras

- [ ] Adicionar seção `[PROFESSORES]` no BD
- [ ] Exportar relatório em `.csv`
- [ ] Filtro por nível na listagem
- [ ] Menu de restauração de backup
- [ ] Testes automatizados com `unittest`
- [ ] Refatorar para **orientação a objetos** (`class Escola`, `class Aluno`)
- [ ] Migrar persistência para **JSON** ou **SQLite**
- [ ] Adicionar níveis CEFR completos (A1–C2) como subnível

---

## 🤝 Contribuindo

Sugestões e PRs são bem-vindos! Abra uma *issue* descrevendo o problema ou a melhoria antes de mandar o *pull request*.

---

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---

## 👤 Autor

**<Seu Nome>**
- 🎓 Aluno(a) **DANIEL MASSITA TONOLLI** do curso **CAIXAVERSO FC5 — Analista de Dados II (#1735)**
- 📚 Módulo: **Lógica de Programação em Python**
- 👨‍🏫 Professor: **Thiago Tavares Magalhães** - https://www.linkedin.com/in/thiagotm/
- 🏫 Instituição: **Ada (Let's Code)**

---

## 🙏 Agradecimentos

- Ao professor **Thiago Tavares Magalhães** pelo material didático e pelo incentivo.
- À **Ada** pela estrutura do curso e pelos cursos digitais complementares.
- A você, que está lendo este README — bons estudos! 🚀

---

## Identificação e Controle do Enunciado (DEBUG MENTAL):

# 📍 Mapa do Projeto — Onde Cada Requisito Foi Atendido

---

## 🔹 Requisitos Gerais (itens 1, 2, 4 e 5)

| Item do PDF | O que pede | Onde está no código |
|---|---|---|
| **1** | Alunos guardados em variável que misture **listas + dicionários** | No topo do arquivo (docstring) + função `criar_escola_vazia()` → retorna `{"alunos": [], "nota_minima": 6.0}`. A "escola" é um **dicionário** que tem uma **lista** de alunos dentro |
| **2** | Cada aluno tem **matrícula, nome, nível, idade e boletim**; boletim guarda **disciplinas + notas** | Dentro de `adicionar_aluno()` — monta o dicionário `novo_aluno` com essas 5 chaves. O `boletim` é um **dicionário** onde cada idioma (disciplina) tem uma **lista** de notas |
| **4** | Usar **tratamento de exceção** | Todas as funções têm `try/except`. Exemplos: `adicionar_aluno` (linha do `try`), `carregar_escola` (captura erro de arquivo), `main()` (rede de segurança) |
| **5** | Mostrar o máximo de conhecimento | Comentários explicativos, 3 camadas (dados/persistência/interface), backup automático, menu interativo, autenticação de diretor — tudo além do que foi pedido |

---

## 🔹 Requisito 3 — Funções Obrigatórias (a até j)

### 🅰️ `criar_escola_vazia` — Item **3a**

| O que pede | O que foi feito |
|---|---|
| Função que inicializa a escola vazia | Função `criar_escola_vazia()` retorna `{"alunos": [], "nota_minima": 6.0}` |

---

### 🅱️ `adicionar_aluno` — Item **3b**

| O que pede | O que foi feito |
|---|---|
| Cadastra aluno com **matrícula, nome, nível, idade** (obrigatórios) | Parâmetros `matricula, nome, nivel, idade` |
| Aceita **lista de turmas** opcional (boletim sem notas) | Parâmetro `idiomas=None` — se passado, cria o boletim com `{"Inglês": [], "Espanhol": []}` |

---

### 🅲 `cadastrar_nota` — Item **3c**

| O que pede | O que foi feito |
|---|---|
| Cadastra nota para aluno em disciplina | Parâmetros `matricula, idioma, nota` |
| Permite **múltiplas notas** na mesma disciplina | Usa `.setdefault(idioma, []).append(nota)` → várias notas vão se acumulando na lista |

---

### 🅳 `alterar_nota` — Item **3d**

| O que pede | O que foi feito |
|---|---|
| Altera nota específica (1ª, 2ª, 3ª...) em disciplina específica | Parâmetros `matricula, idioma, posicao, nova_nota` |
| Conversão de "posição humana" (1, 2, 3) para índice Python (0, 1, 2) | Linha `indice = posicao - 1` |

---

### 🅴 `alterar_dado_cadastral` — Item **3e**

| O que pede | O que foi feito |
|---|---|
| Altera dado cadastral (nome, nível ou idade) | Parâmetros `matricula, campo, novo_valor` |
| Valida o campo alterado (só permite nome/nivel/idade) | `campos_permitidos = {"nome", "nivel", "idade"}` |
| Atribuição dinâmica da chave | `aluno[campo] = novo_valor` — funciona para qualquer campo |

---

### 🅵 `visualizar_aluno` — Item **3f**

| O que pede | O que foi feito |
|---|---|
| Mostra **todos** os dados de um aluno | Imprime ficha formatada com bordas ASCII: nome, nível, idade e boletim completo (com médias por idioma) |

---

### 🅶 `calcular_media` — Item **3g**

| O que pede | O que foi feito |
|---|---|
| Retorna **média** e **situação** (aprovado/reprovado) | `return media, situacao` — retorno múltiplo em **tupla** |
| Recebe matrícula, disciplina e **nota mínima** | Parâmetros `matricula, idioma` — a nota mínima é lida de `escola["nota_minima"]` |

---

### 🅷 `apagar_aluno` — Item **3h**

| O que pede | O que foi feito |
|---|---|
| Apaga aluno pela matrícula | Parâmetro `matricula` |
| Respeita a estrutura | Usa `enumerate` + `.pop(indice)` para remover o dicionário da lista |

---

### 🅸 `analise_geral` — Item **3i**

| O que pede | O que foi feito |
|---|---|
| Retorna **taxa de reprovação**, **média** e **quantidade de avaliações** por disciplina | Retorna dicionário `{idioma: {"media": X, "taxa_reprovacao": Y, "quantidade_avaliacoes": Z}}` |
| Agrega de todos os alunos | Percorre `escola["alunos"]` → `aluno["boletim"]` → notas, agrupando por idioma |

---

### 🅹 `quantidade_alunos` — Item **3j**

| O que pede | O que foi feito |
|---|---|
| Retorna quantos alunos existem na escola | `return len(escola["alunos"])` — uma linha |

---

## 🔹 Recursos Extras (além do pedido)

| Recurso | Onde está | Por que foi incluído |
|---|---|---|
| **Persistência em TXT** | `salvar_escola`, `carregar_escola` | Simula um banco de dados real |
| **Backup automático** | `fazer_backup` | Segurança antes de sobrescrever |
| **Arquivo modelo** | `criar_arquivo_modelo` | Gabarito com 5 alunos de exemplo |
| **Menu interativo** | `main()` + `exibir_menu` | Simula terminal de caixa eletrônico |
| **12 fluxos de UI** | `fluxo_listar`, `fluxo_adicionar`, ... | Separam input/print da lógica |
| **Autenticação de diretor** | `fluxo_configuracoes` | Só "admin/admin" altera a nota mínima |
| **Camadas bem separadas** | Dados / Persistência / Interface | Boa arquitetura |

---

## 🎯 Resumo em 1 frase por item

| Item | Frase |
|---|---|
| **1** | Escola = dicionário com lista de alunos dentro ✅ |
| **2** | Aluno = dicionário com `matricula, nome, nivel, idade, boletim` ✅ |
| **3a** | `criar_escola_vazia()` ✅ |
| **3b** | `adicionar_aluno()` com `idiomas` opcional ✅ |
| **3c** | `cadastrar_nota()` com múltiplas notas por disciplina ✅ |
| **3d** | `alterar_nota()` por posição (1ª, 2ª, 3ª...) ✅ |
| **3e** | `alterar_dado_cadastral()` genérica ✅ |
| **3f** | `visualizar_aluno()` com ficha ASCII ✅ |
| **3g** | `calcular_media()` retorna tupla `(média, situação)` ✅ |
| **3h** | `apagar_aluno()` com `pop` ✅ |
| **3i** | `analise_geral()` com taxa/média/quantidade ✅ |
| **3j** | `quantidade_alunos()` com `len` ✅ |
| **4** | Tratamento de exceção em todas as funções ✅ |
| **5** | Extras: TXT, backup, menu, autenticação ✅ |

---

## 📋 Fim Checklist para Entrega

