# 🎓 Escola de Idiomas — Projeto Completo PBL

Perfeito! Com suas respostas e considerações, agora tenho tudo que preciso. Vou te entregar:

1. **Explicação do BD** (colunas e por quê)
2. **Código completo, comentado e organizado em 3 camadas**
3. **Fluxo tipo "terminal de ATM"** com menus numerados
4. **Backup automático + confirmação antes de salvar**
5. **5 alunos de exemplo** já embutidos no código
6. **Exemplos de execução** de cada função A-J

---

## 🗄️ Parte 1 — Estrutura do Banco de Dados (colunas e escolhas)

### Arquivo `escola.txt` — formato `;` (ponto e vírgula)

```text
[CONFIG]
nota_minima=6.0

[ALUNOS]
# matricula;nome;nivel;idade
1;Ana Silva;Básico;15
...

[NOTAS]
# matricula;idioma;nota
1;Inglês;8.5
...
```

### Por que cada coluna?

| Coluna | Tipo | Por quê |
|---|---|---|
| `matricula` | `int` único | Chave primária. Simples, ordenada, fácil de digitar. |
| `nome` | `str` | Texto livre, mas **sem `;`** para não quebrar o parser. |
| `nivel` | `str` | Um dos 3 níveis: Básico, Intermediário, Avançado. |
| `idade` | `int` | Positivo, validação simples. |
| `idioma` | `str` | Um dos 5 idiomas que você fala (lista fixa). |
| `nota` | `float` | 0–10, 1 casa decimal, validada. |
| `nota_minima` | `float` | Config global, só DIRETOR altera. |

### Por que seções `[CONFIG]`, `[ALUNOS]`, `[NOTAS]`?
- **Legível** para humano (abre no Notepad).
- **Fácil de parsear** em Python (uma linha de leitura por seção).
- **Extensível** (amanhã posso adicionar `[PROFESSORES]` sem quebrar o resto).
- **Diferente dos 3 LLMs**: eles usaram só memória; nós persistimos de forma **auditável**.

### Por que separar ALUNOS e NOTAS?
- **Normalização**: evita repetir nome/nível a cada nota.
- **Uma linha por nota** = fácil calcular média, taxa de reprovação etc.
- **Backup leve**: muda pouco.

---

## 💻 Parte 2 — Código Completo

```text
 https://github.com/danielmassita/2025-CaixaVerso/blob/main/4_AdaTech_LMS_LogicaProgramacaoPython/Projeto/escola_idiomas.py
```

---

## 🎮 Parte 3 — Como rodar

```bash
python escola_idiomas.py
```

**Primeira execução:** o programa detecta que `escola.txt` não existe, cria o **arquivo modelo** com 5 alunos e 15 notas de exemplo, e já abre o menu.

**Estrutura de pastas gerada:**
```text
📁 pasta_do_projeto/
├── escola_idiomas.py
├── escola.txt           ← BD de trabalho
├── escola_modelo.txt    ← gabarito, nunca sobrescrito
└── 📁 backups/
    └── escola_20250101_143022.txt
```

---

## 🧪 Parte 4 — Exemplos de saída no terminal

### ➕ Adicionar aluno
```text
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

### 📈 Análise geral (nota mínima = 6.0)
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

### ⚙️ Configurações (DIRETOR)
```text
⚙️  CONFIGURAÇÕES — ACESSO RESTRITO
Login: admin
Senha: admin
Nota mínima atual: 6.0
Nova nota mínima: 7.0
✅ Nota mínima atualizada para 7.0.
```

### 💾 Saída com backup
```text
💾 Salvar alterações no BD? (s/n): s
🗂️  Backup criado em: backups/escola_20250101_143022.txt
💾 Escola salva em 'escola.txt'.
👋 Até logo!
```

---

## 🏆 Parte 5 — O que este código faz melhor que ChatGPT/Claude/Gemini

| Item | ChatGPT | Claude | Gemini | **DeepSeek** |
|---|---|---|---|---|
| Camadas separadas (dados/IO/persistência) | ❌ | ❌ | ❌ | ✅ |
| Persistência em TXT legível | ❌ | ❌ | ❌ | ✅ |
| Backup automático antes de sobrescrever | ❌ | ❌ | ❌ | ✅ |
| Menu numerado tipo ATM | ❌ | ❌ | ❌ | ✅ |
| Arquivo modelo de exemplo (5 alunos) | ❌ | ❌ | ❌ | ✅ |
| Autorização por perfil (DIRETOR) | ❌ | ❌ | ❌ | ✅ |
| Validação por tipo + valor + domínio | parcial | parcial | parcial | ✅ |
| Comentários-documentação no corpo do código | parcial | ✅ | ❌ | ✅ |
| `main()` modular com mapa de ações | ❌ | ❌ | ❌ | ✅ |
| Tratamento uniforme de exceções | parcial | parcial | ❌ | ✅ |

---

## 📌 Próximos passos (PBL)

Sugestões para você evoluir sozinho depois de rodar o código:

1. **Adicione PROFESSORES** ao BD (nova seção `[PROFESSORES]`).
2. **Filtro por nível** na listagem (ex: só "Avançado").
3. **Relatório por aluno**: imprimir todas as médias de uma vez.
4. **Exportar relatório em CSV** (`.csv`) — só mais um `open` + vírgulas.
5. **Menu de recuperação**: se o BD principal quebrar, restaurar do backup.
6. **Testes automatizados** com `unittest` para cada função A-J.

---

Se quiser, no próximo passo eu:

- Te explico **linha por linha** de uma função específica (ex: `salvar_escola`);
- Faço um **diagrama ASCII** do fluxo `main()` → `ações` → função;
- Monto o **README.md** do projeto no padrão GitHub (igual fizemos com os outros).

Qual desses você quer? 🚀

___

# 🎓 Pacote Completo — Explicação, Diagrama e README

Vamos aos três, na ordem que você pediu. Cada parte foi feita para você **estudar**, não só copiar.

---

# PARTE 1 — Explicação linha por linha: `salvar_escola`

Vou pegar a função exatamente como está no código e destrinchar cada linha. Também incluo `carregar_escola` no final porque as duas formam um **par** (uma escreve, outra lê) — entender uma ajuda a entender a outra.

## 📜 Código completo da função (referência)

```python
def salvar_escola(escola, caminho=ARQUIVO_BD):
    """
    Grava a escola no TXT no formato de seções.
    ANTES de gravar, faz backup do arquivo atual (se existir).
    """
    try:
        if os.path.exists(caminho):
            backup = fazer_backup(caminho)
            if backup:
                print(f"🗂️  Backup criado em: {backup}")

        with open(caminho, "w", encoding="utf-8") as f:
            # ---- CONFIG ----
            f.write("[CONFIG]\n")
            f.write(f"nota_minima={escola['nota_minima']}\n\n")

            # ---- ALUNOS ----
            f.write("[ALUNOS]\n")
            f.write("# matricula;nome;nivel;idade\n")
            for aluno in escola["alunos"]:
                f.write(
                    f"{aluno['matricula']};{aluno['nome']};"
                    f"{aluno['nivel']};{aluno['idade']}\n"
                )
            f.write("\n")

            # ---- NOTAS ----
            f.write("[NOTAS]\n")
            f.write("# matricula;idioma;nota\n")
            for aluno in escola["alunos"]:
                for idioma, notas in aluno["boletim"].items():
                    for nota in notas:
                        f.write(f"{aluno['matricula']};{idioma};{nota}\n")

        print(f"💾 Escola salva em '{caminho}'.")
        return True

    except (OSError, KeyError) as erro:
        print(f"❌ Erro ao salvar: {erro}")
        return False
```

## 🔬 Linha por linha

### Linha 1 — Assinatura da função

```python
def salvar_escola(escola, caminho=ARQUIVO_BD):
```

| Pedaço | O que é | Por quê |
|---|---|---|
| `def` | Palavra-chave do Python | Declara uma função |
| `salvar_escola` | Nome da função | Verbo + substantivo: "salvar a escola" |
| `escola` | Parâmetro obrigatório | O dicionário em memória que queremos gravar |
| `caminho=ARQUIVO_BD` | **Parâmetro com valor padrão** | Se ninguém passar caminho, usa `"escola.txt"`. Permite salvar num caminho alternativo (ex: `salvar_escola(escola, "teste.txt")`) — muito útil para testes |

> 💡 Isso é o mesmo conceito estudado no capítulo **"Parâmetros e retorno de funções"**.

### Linha 2-5 — Docstring

```python
    """
    Grava a escola no TXT no formato de seções.
    ANTES de gravar, faz backup do arquivo atual (se existir).
    """
```

- As três aspas (`"""`) abrem um **comentário de múltiplas linhas**.
- Python guarda isso em `salvar_escola.__doc__`.
- Ajuda o `help(salvar_escola)` no terminal e o autocompletar do VS Code.
- Documenta **o que** a função faz, não **como** — isso está no corpo.

### Linha 6 — Início do try

```python
    try:
```

- Tudo que pode falhar fica dentro do `try`.
- Falhas previstas: disco cheio, arquivo sem permissão, chave `nota_minima` faltando.
- Se algo der errado, o Python **pula direto para o `except`** no final — não trava o programa.

### Linha 7-10 — Backup condicional

```python
        if os.path.exists(caminho):
            backup = fazer_backup(caminho)
            if backup:
                print(f"🗂️  Backup criado em: {backup}")
```

| Linha | Explicação |
|---|---|
| `os.path.exists(caminho)` | Retorna `True` se o arquivo já existe |
| `fazer_backup(caminho)` | Chama a função auxiliar (definida em outra parte do código) que **copia** o arquivo para `backups/` com timestamp |
| `if backup:` | Se a função devolveu um caminho (não `None`), imprime |
| `print(f"...")` | **f-string**: a variável `backup` é interpolada dentro das chaves `{}` |

> ⚠️ **Ponto-chave de design**: o backup é feito **antes** do `open(..., "w")`. Se você abrir o arquivo em modo `"w"` primeiro, ele já é **truncado** (zerado) — e o backup copiaria o arquivo vazio. Ordem importa!

### Linha 11 — Abrindo o arquivo com `with`

```python
        with open(caminho, "w", encoding="utf-8") as f:
```

| Pedaço | O que é |
|---|---|
| `open(caminho, "w", encoding="utf-8")` | Abre o arquivo. `"w"` = **write** (sobrescreve). `encoding="utf-8"` garante acentos corretos |
| `with ... as f:` | **Gerenciador de contexto**. Fecha o arquivo automaticamente ao sair do bloco — mesmo se der erro |

> 🎓 **Por que `with` e não `f = open(...)` / `f.close()`?**
> Porque se der erro no meio, você esquece de fechar, e o arquivo fica travado no Windows. `with` resolve isso.
> **Isso é o mesmo conceito de `finally`** estudado no capítulo de Tratamento de Exceção — mas mais elegante.

### Linha 12-14 — Escrevendo a seção `[CONFIG]`

```python
            f.write("[CONFIG]\n")
            f.write(f"nota_minima={escola['nota_minima']}\n\n")
```

- `f.write(...)` grava texto no arquivo. **Não adiciona quebra de linha sozinho** — por isso o `\n` explícito.
- `\n` = quebra de linha (Unix). No Windows também funciona.
- `escola['nota_minima']` acessa o valor no dicionário da escola.
- O `\n\n` (dois) cria uma **linha em branco** entre seções — deixa o arquivo mais legível.

### Linha 16-19 — Seção `[ALUNOS]` (cabeçalho)

```python
            f.write("[ALUNOS]\n")
            f.write("# matricula;nome;nivel;idade\n")
```

- `[ALUNOS]` é o **marcador de seção** que o parser vai procurar depois.
- A linha `# matricula;nome;nivel;idade` é um **comentário** para humanos. O parser pula linhas que começam com `#`.
- Esse padrão é o mesmo usado em arquivos `.ini` (Windows) e `pyproject.toml`.

### Linha 20-25 — Laço que escreve cada aluno

```python
            for aluno in escola["alunos"]:
                f.write(
                    f"{aluno['matricula']};{aluno['nome']};"
                    f"{aluno['nivel']};{aluno['idade']}\n"
                )
```

Destrinchando:

1. `escola["alunos"]` é a **lista de dicionários** que carrega todos os alunos.
2. `for aluno in ...` percorre cada dicionário.
3. Dentro da f-string, montamos uma linha:
   ```
   "1;Ana Silva;Básico;15\n"
   ```
   Os campos são separados por `;` — escolhido porque **nomes raramente têm `;`** (diferente de vírgula).
4. O `\n` fecha a linha.
5. **A quebra de linha `f"..."` em duas strings** (`f"..."` colado em `f"..."`) é uma forma de o Python **concatenar automaticamente** strings literais adjacentes — recurso da linguagem, não é um operador `+`.

> 💡 Por que **não** usamos `str(aluno)` ou `pickle` ou JSON?
> Porque o requisito era **legível por humano**. Um arquivo `1;Ana Silva;Básico;15` qualquer pessoa entende; um JSON é mais verboso; um pickle é binário.

### Linha 26 — Linha em branco após ALUNOS

```python
            f.write("\n")
```

Separa visualmente da próxima seção. O parser ignora linhas vazias.

### Linha 28-32 — Seção `[NOTAS]`

```python
            f.write("[NOTAS]\n")
            f.write("# matricula;idioma;nota\n")
            for aluno in escola["alunos"]:
                for idioma, notas in aluno["boletim"].items():
                    for nota in notas:
                        f.write(f"{aluno['matricula']};{idioma};{nota}\n")
```

**Três `for` aninhados** — o coração da normalização:

| Nível | Percorre | Exemplo |
|---|---|---|
| 1º `for` | Cada aluno | `Ana Silva` |
| 2º `for` | Cada idioma do boletim | `Inglês`, `Espanhol` |
| 3º `for` | Cada nota daquele idioma | `[8.5, 7.0]` |

`.items()` retorna pares `(chave, valor)` do dicionário. É a forma "pythonica" de percorrer dicionários — estudado no capítulo **Dicionários**.

**Resultado no arquivo:**
```text
1;Inglês;8.5
1;Inglês;7.0
1;Espanhol;9.0
2;Inglês;6.0
...
```

Cada nota vira **uma linha**. Isso é o que permite calcular médias depois (é só filtrar por matrícula+idioma).

### Linha 34-35 — Sucesso

```python
        print(f"💾 Escola salva em '{caminho}'.")
        return True
```

- Fora do `with` (o arquivo já foi fechado automaticamente).
- Retorna `True` para indicar sucesso — padrão do projeto: **toda função de escrita retorna bool**.

### Linha 37-39 — Tratamento de exceção

```python
    except (OSError, KeyError) as erro:
        print(f"❌ Erro ao salvar: {erro}")
        return False
```

| Pedaço | Explicação |
|---|---|
| `except (OSError, KeyError)` | Captura **duas famílias** de erros. `OSError` = problema de arquivo/disco. `KeyError` = chave faltando no dicionário (ex: `escola['nota_minima']` se por algum motivo não existir) |
| `as erro` | Dá um **apelido** à exceção. `erro` contém a mensagem original |
| `print(f"...{erro}")` | Mostra a mensagem para o usuário |
| `return False` | Sinaliza falha para quem chamou |

> ⚠️ **Detalhe importante**: dentro do `except` **não re-abrimos nem re-fechamos** o arquivo. O `with` já cuidou disso, mesmo em caso de erro. Isso é o "finally disfarçado".

---

## 📖 Bônus — `carregar_escola` (o par inverso)

```python
def carregar_escola(caminho=ARQUIVO_BD):
    escola = criar_escola_vazia()

    try:
        if not os.path.exists(caminho):
            print(f"ℹ️  Arquivo '{caminho}' não encontrado. Criando modelo...")
            criar_arquivo_modelo()
            return carregar_escola(caminho)

        secao = None
        with open(caminho, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.rstrip("\n")
                if not linha.strip() or linha.startswith("#"):
                    continue
                if linha.startswith("[") and linha.endswith("]"):
                    secao = linha.strip("[]")
                    continue

                if secao == "CONFIG":
                    chave, valor = linha.split("=")
                    if chave == "nota_minima":
                        escola["nota_minima"] = float(valor)

                elif secao == "ALUNOS":
                    mat, nome, nivel, idade = linha.split(";")
                    escola["alunos"].append({
                        "matricula": int(mat),
                        "nome": nome,
                        "nivel": nivel,
                        "idade": int(idade),
                        "boletim": {},
                    })

                elif secao == "NOTAS":
                    mat, idioma, nota = linha.split(";")
                    aluno = buscar_aluno(escola, int(mat))
                    if aluno is not None:
                        aluno["boletim"].setdefault(idioma, []).append(float(nota))

        return escola

    except (OSError, ValueError, KeyError) as erro:
        print(f"❌ Erro ao carregar '{caminho}': {erro}")
        return criar_escola_vazia()
```

**Como ler isso em 5 passos mentais:**

1. **Cria a escola vazia** — sempre parte de algo válido, mesmo se tudo falhar.
2. **Se o arquivo não existe**: cria o modelo, chama a si mesma de novo (**recursão!**).
3. **Abre o arquivo** e lê linha a linha.
4. **Máquina de estados**: `secao` guarda em que bloco estamos. Cada linha é interpretada de acordo com `secao`.
5. **Constrói o dicionário em memória** de volta, na ordem inversa do que `salvar_escola` fez.

**Conceitos aqui:** `rstrip` (remove `\n` do fim), `strip("[]")` (remove colchetes), `split(";")` (divide string em lista), `setdefault` (cria chave com valor padrão se não existir), **recursão** quando o arquivo não existe.

---

# PARTE 2 — Diagrama ASCII do fluxo

## 🗺️ Visão macro: do boot até o encerramento

```text
┌────────────────────────────────────────────────────────────────────┐
│                        BOOT DO PROGRAMA                            │
│                                                                    │
│   $ python escola_idiomas.py                                       │
└───────────────────────────┬────────────────────────────────────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   if __name__ ==     │
                 │      "__main__":     │
                 │      main()          │
                 └──────────┬───────────┘
                            │
                            ▼
              ┌─────────────────────────────┐
              │  limpar_tela()              │
              │  escola = carregar_escola() │◄──── lê escola.txt
              │  acoes = { ... }            │
              └──────────┬──────────────────┘
                         │
                         ▼
        ┌────────────────────────────────────────┐
        │         LOOP PRINCIPAL (while True)    │
        │                                        │
        │   limpar_tela()                        │
        │   exibir_cabecalho(escola)             │
        │   exibir_menu()                        │
        │   opcao = input("👉 Escolha: ")        │
        └──────────┬─────────────────────────────┘
                   │
        ┌──────────┴───────────┐
        │                      │
        ▼                      ▼
   opção = "0"           opção em acoes
   ou "12"                    │
        │                     ▼
        │         ┌──────────────────────────┐
        │         │  acoes[opcao](escola)    │
        │         │  (chama a função certa)  │
        │         └──────────┬───────────────┘
        │                    │
        │                    ▼
        │         ┌──────────────────────────┐
        │         │  pausar()                │
        │         │  (ENTER para continuar)  │
        │         └──────────┬───────────────┘
        │                    │
        └────────┬───────────┘
                 │
                 ▼
        ┌────────────────────────────┐
        │  SAI DO WHILE              │
        │                            │
        │  if opcao == "12":         │
        │     salvar_escola(escola)  │
        │  else:                     │
        │     sair sem salvar        │
        └──────────┬─────────────────┘
                   │
                   ▼
              ┌─────────┐
              │  FIM    │
              └─────────┘
```

## 🎛️ Detalhe do despacho de ações (o "mapa")

```text
                         opcao (string digitada)
                                  │
        ┌─────────┬─────────┬─────┴─────┬─────────┬─────────┐
        │         │         │           │         │         │
       "1"       "2"       "3"   ...  "10"      "11"      "12"
        │         │         │           │         │         │
        ▼         ▼         ▼           ▼         ▼         ▼
   fluxo_    fluxo_    fluxo_      lambda    fluxo_     None
   listar    visual.   adicionar   print     config.
        │         │         │           │         │         │
        └─────────┴─────────┴───────────┴─────────┴─────────┘
                                  │
                                  ▼
                    ┌───────────────────────────┐
                    │  try:                     │
                    │      acoes[opcao](escola) │
                    │  except Exception as e:   │
                    │      print("⚠️", e)       │
                    └───────────────────────────┘
```

## 📚 Mapa das 3 camadas (arquitetura)

```text
┌─────────────────────────────────────────────────────────────────────┐
│                     CAMADA 3 — INTERFACE (terminal)                 │
│                                                                     │
│   main()  exibir_menu()  exibir_cabecalho()  pausar()  limpar_tela()│
│   fluxo_listar  fluxo_visualizar  fluxo_adicionar  fluxo_*          │
│                                                                     │
│   • Toda interação input()/print() acontece AQUI                    │
│   • Não sabe COMO os dados são guardados, só chama as funções       │
└───────────────────────────┬─────────────────────────────────────────┘
                            │ chama
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     CAMADA 1 — DADOS / REGRAS                       │
│                                                                     │
│   criar_escola_vazia   buscar_aluno   adicionar_aluno               │
│   cadastrar_nota       alterar_nota   alterar_dado_cadastral        │
│   visualizar_aluno     calcular_media  apagar_aluno                 │
│   analise_geral        quantidade_alunos                            │
│                                                                     │
│   • Manipulam a estrutura em memória                                │
│   • Não sabem que existe um arquivo .txt                            │
│   • Retornam bool ou tuplas (média, situação)                       │
└───────────────────────────┬─────────────────────────────────────────┘
                            │ usa
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     CAMADA 2 — PERSISTÊNCIA (TXT)                   │
│                                                                     │
│   salvar_escola   carregar_escola   fazer_backup   criar_arquivo_   │
│                                                     modelo          │
│                                                                     │
│   • Única camada que conhece open(), shutil, os.path                │
│   • Serializa / desserializa o dicionário em memória                │
└─────────────────────────────────────────────────────────────────────┘
```

**Regra de ouro das 3 camadas:** cada camada só conversa com a de baixo, nunca com a de cima.

- A interface não abre arquivo.
- A camada de dados não imprime menu.
- A persistência não sabe o que é "aluno" — só sabe transformar `{...}` em texto e vice-versa.

## 🔄 Fluxo de dados de uma operação completa

Exemplo: usuário cadastra uma nota.

```text
[USUÁRIO]
   │ digita "4"
   ▼
[main()]  opcao = "4"
   │
   ▼
[acoes["4"]] = fluxo_cadastrar_nota
   │
   ▼
[fluxo_cadastrar_nota(escola)]
   │ input: matricula=1, idioma="Inglês", nota=9.0
   ▼
[cadastrar_nota(escola, 1, "Inglês", 9.0)]
   │ valida, adiciona à lista em memória
   ▼
[escola] agora tem "Inglês": [8.5, 7.0, 9.0]
   │
   ▼
(volta para o menu — arquivo AINDA NÃO foi salvo)
   │
   ▼
[usuário escolhe "12"]
   │
   ▼
[salvar_escola(escola)]
   │ 1. fazer_backup("escola.txt") → copia para backups/
   │ 2. open("escola.txt", "w")
   │ 3. escreve [CONFIG], [ALUNOS], [NOTAS]
   ▼
[escola.txt] atualizado no disco
```

Esse **delay** entre "operação em memória" e "gravação em disco" é o que dá a sensação de "caixa eletrônico": você faz várias coisas e no final confirma.

---

**Sugestão de estrutura final no GitHub:**

```text
📁 escola-idiomas/
├── .gitignore
├── LICENSE
├── README.md
├── escola_idiomas.py
├── escola.txt
└── escola_modelo.txt
```

> ⚠️ **Não suba a pasta `backups/`** — ela é local e vai crescendo. Por isso o `.gitignore` acima.

---

## ✅ Resumo do que foi entregue

| Item | Onde |
|---|---|
| Explicação linha por linha de `salvar_escola` | Parte 1 |
| Bônus: `carregar_escola` explicada | Parte 1 (final) |
| Diagrama ASCII do `main()` | Parte 2 |
| Diagrama do despacho de ações | Parte 2 |
| Diagrama das 3 camadas | Parte 2 |
| Diagrama do fluxo de dados (cadastrar nota) | Parte 2 |
| README.md pronto para GitHub | Parte 3 |
| Checklist de git/`.gitignore` | Bônus |

---




