# -*- coding: utf-8 -*-
"""
================================================================================
 ESCOLA DE IDIOMAS — Sistema CRUD via Terminal
================================================================================
 Autor  : (seu nome)
 Curso  : Ada — Lógica de Programação em Python
 Projeto: Banco de dados de alunos de uma escola de idiomas
--------------------------------------------------------------------------------
 OBJETIVO
 --------
 Criar, consultar, atualizar e deletar (CRUD) um banco de alunos de uma
 escola de idiomas, com persistência em arquivo .txt, interface de
 terminal estilo "caixa eletrônico" e backup automático antes de alterar.

 ESTRUTURA DE DADOS (em memória)
 -------------------------------
 escola = {
     "alunos": [
         {
             "matricula": 1,
             "nome": "Ana Silva",
             "nivel": "Básico",
             "idade": 15,
             "boletim": {                    # idioma -> lista de notas
                 "Inglês":   [8.5, 7.0],
                 "Espanhol": [9.0],
             },
         },
         ...
     ],
     "nota_minima": 6.0,
 }

 POR QUE ESSA ESTRUTURA?
 -----------------------
 - Dicionário no topo  -> permite guardar configurações junto com os dados.
 - "alunos" é uma LISTA -> preserva a ordem de cadastro, fácil de percorrer.
 - Cada aluno é um DICIONÁRIO -> acesso por chave é legível (aluno["nome"]).
 - "boletim" é DICIONÁRIO -> cada idioma tem sua própria LISTA de notas,
   permitindo múltiplas notas por idioma (ex: prova, trabalho, recuperação).

 CAMADAS DO CÓDIGO (arquitetura em 3 níveis)
 -------------------------------------------
 1) DADOS        -> funções que manipulam a estrutura em memória
 2) PERSISTÊNCIA -> ler/gravar o arquivo .txt e fazer backups
 3) INTERFACE    -> menus, inputs e prints no terminal

 AUTORIZAÇÃO
 -----------
 - Alunos/visitantes: podem consultar, mas NÃO alteram a nota mínima.
 - DIRETOR (login "admin" / senha "admin"): único que altera a nota mínima.
================================================================================
"""

import os
import shutil
from datetime import datetime

# ============================================================================
# CONSTANTES GLOBAIS
# ============================================================================
# Documentação antecipada: todas as "regras" do domínio ficam aqui em cima,
# para que qualquer ajuste futuro (novo idioma, novo nível, etc.) seja feito
# em um único lugar.
# ============================================================================

ARQUIVO_BD      = "escola.txt"           # banco de dados "de trabalho"
ARQUIVO_MODELO  = "escola_modelo.txt"    # cópia de segurança do modelo exemplo
PASTA_BACKUP    = "backups"              # onde os backups automáticos vão

IDIOMAS_VALIDOS = ["Português", "Inglês", "Francês", "Espanhol", "Mandarim"]

# Níveis -> subníveis CEFR (só documental; a validação usa as chaves)
NIVEIS_VALIDOS = {
    "Básico":        ["A1", "A2"],
    "Intermediário": ["B1", "B2"],
    "Avançado":      ["C1", "C2"],
}

NOTA_MINIMA_PADRAO = 6.0
CREDENCIAIS_DIRETOR = {"login": "admin", "senha": "admin"}


# ============================================================================
# CAMADA 1 — DADOS (memória)
# ============================================================================

def criar_escola_vazia():
    """
    (Requisito 3a)
    Cria e retorna a estrutura vazia da escola.

    Retorno:
        dict: {"alunos": [], "nota_minima": 6.0}

    Por que um dicionário no topo e não só uma lista?
    -> Porque queremos guardar configurações (nota_minima) junto com os dados,
       sem precisar de variáveis globais espalhadas pelo código.
    """
    return {
        "alunos": [],
        "nota_minima": NOTA_MINIMA_PADRAO,
    }


def buscar_aluno(escola, matricula):
    """
    Função auxiliar (não pedida explicitamente, mas evita repetição).
    Retorna o dicionário do aluno com a matrícula dada, ou None.

    Aqui já mostramos o padrão de tratamento: qualquer erro inesperado
    cai no except e retorna None (falha silenciosa para uso interno).
    """
    try:
        for aluno in escola["alunos"]:
            if aluno["matricula"] == matricula:
                return aluno
        return None
    except (KeyError, TypeError):
        return None


def adicionar_aluno(escola, matricula, nome, nivel, idade, idiomas=None):
    """
    (Requisito 3b)
    Adiciona um aluno à escola.

    Parâmetros:
        matricula (int): única, positiva.
        nome (str): não vazio.
        nivel (str): um de NIVEIS_VALIDOS.
        idade (int): > 0.
        idiomas (list[str] | None): idiomas iniciais (boletim sem notas).

    Retorno:
        True se cadastrou, False se falhou.

    Validações demonstram try/except + raise:
    - ValueError  -> dado semanticamente inválido (nome vazio, idade negativa)
    - TypeError   -> tipo errado (matrícula como string, por ex.)
    """
    try:
        # --- Validações de tipo e valor ---
        if not isinstance(matricula, int) or matricula <= 0:
            raise TypeError("Matrícula deve ser um inteiro positivo.")
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome não pode ser vazio.")
        if nivel not in NIVEIS_VALIDOS:
            raise ValueError(
                f"Nível inválido. Use um de: {list(NIVEIS_VALIDOS.keys())}"
            )
        if not isinstance(idade, int) or idade <= 0:
            raise ValueError("Idade deve ser um inteiro positivo.")

        # --- Regra de unicidade ---
        if buscar_aluno(escola, matricula) is not None:
            raise ValueError(f"Já existe aluno com matrícula {matricula}.")

        # --- Constrói o boletim inicial ---
        boletim = {}
        if idiomas:
            for idioma in idiomas:
                if idioma not in IDIOMAS_VALIDOS:
                    raise ValueError(f"Idioma inválido: {idioma}")
                boletim[idioma] = []      # lista de notas vazia

        # --- Monta o dicionário do aluno ---
        novo_aluno = {
            "matricula": matricula,
            "nome": nome.strip(),
            "nivel": nivel,
            "idade": idade,
            "boletim": boletim,
        }
        escola["alunos"].append(novo_aluno)

        print(f"✅ Aluno '{nome}' cadastrado com sucesso.")
        return True

    except (TypeError, ValueError) as erro:
        # Demonstração explícita do tratamento: qualquer erro de validação cai aqui.
        print(f"❌ Erro ao adicionar aluno: {erro}")
        return False


def cadastrar_nota(escola, matricula, idioma, nota):
    """
    (Requisito 3c)
    Cadastra uma NOVA nota para um aluno em um idioma.
    Se o idioma não existir no boletim, ele é criado automaticamente.
    """
    try:
        aluno = buscar_aluno(escola, matricula)
        if aluno is None:
            raise KeyError(f"Aluno com matrícula {matricula} não encontrado.")

        if idioma not in IDIOMAS_VALIDOS:
            raise ValueError(f"Idioma inválido: {idioma}")

        # Coerção + validação da nota
        nota = float(nota)
        if not (0.0 <= nota <= 10.0):
            raise ValueError("Nota deve estar entre 0.0 e 10.0.")

        # Cria a lista se o idioma for novo
        aluno["boletim"].setdefault(idioma, [])
        aluno["boletim"][idioma].append(round(nota, 1))

        print(f"✅ Nota {nota} cadastrada em '{idioma}' para {aluno['nome']}.")
        return True

    except (KeyError, ValueError, TypeError) as erro:
        print(f"❌ Erro ao cadastrar nota: {erro}")
        return False


def alterar_nota(escola, matricula, idioma, posicao, nova_nota):
    """
    (Requisito 3d)
    Altera uma nota específica.
    posicao: 1 = primeira nota, 2 = segunda, etc. (para o USUÁRIO)
    Internamente convertemos para índice (0-based).
    """
    try:
        aluno = buscar_aluno(escola, matricula)
        if aluno is None:
            raise KeyError(f"Aluno {matricula} não encontrado.")

        if idioma not in aluno["boletim"]:
            raise KeyError(f"Aluno não estuda '{idioma}'.")

        notas = aluno["boletim"][idioma]
        if not notas:
            raise ValueError(f"Sem notas cadastradas em '{idioma}'.")

        indice = posicao - 1
        if not (0 <= indice < len(notas)):
            raise IndexError(
                f"Posição {posicao} inválida. Existem {len(notas)} nota(s)."
            )

        nova_nota = float(nova_nota)
        if not (0.0 <= nova_nota <= 10.0):
            raise ValueError("Nova nota deve estar entre 0.0 e 10.0.")

        antiga = notas[indice]
        notas[indice] = round(nova_nota, 1)

        print(f"✅ Nota {posicao} de '{idioma}' alterada: {antiga} → {nova_nota}")
        return True

    except (KeyError, ValueError, IndexError, TypeError) as erro:
        print(f"❌ Erro ao alterar nota: {erro}")
        return False


def alterar_dado_cadastral(escola, matricula, campo, novo_valor):
    """
    (Requisito 3e)
    Altera um dado cadastral: nome, nivel ou idade.
    (Matrícula e boletim são imutáveis por aqui.)
    """
    try:
        aluno = buscar_aluno(escola, matricula)
        if aluno is None:
            raise KeyError(f"Aluno {matricula} não encontrado.")

        campos_permitidos = {"nome", "nivel", "idade"}
        if campo not in campos_permitidos:
            raise ValueError(
                f"Campo inválido. Permitidos: {sorted(campos_permitidos)}"
            )

        if campo == "idade":
            novo_valor = int(novo_valor)
            if novo_valor <= 0:
                raise ValueError("Idade deve ser positiva.")
        if campo == "nivel" and novo_valor not in NIVEIS_VALIDOS:
            raise ValueError(f"Nível inválido: {novo_valor}")

        antigo = aluno[campo]
        aluno[campo] = novo_valor
        print(f"✅ {campo} de {aluno['nome']} alterado: '{antigo}' → '{novo_valor}'")
        return True

    except (KeyError, ValueError, TypeError) as erro:
        print(f"❌ Erro ao alterar dado cadastral: {erro}")
        return False


def visualizar_aluno(escola, matricula):
    """
    (Requisito 3f)
    Imprime na tela TODAS as informações de um aluno,
    formatadas como um boletim escolar.
    """
    try:
        aluno = buscar_aluno(escola, matricula)
        if aluno is None:
            raise KeyError(f"Aluno {matricula} não encontrado.")

        print("\n" + "═" * 55)
        print(f" 📋 FICHA DO ALUNO — MATRÍCULA {aluno['matricula']}")
        print("═" * 55)
        print(f" Nome  : {aluno['nome']}")
        print(f" Nível : {aluno['nivel']}")
        print(f" Idade : {aluno['idade']} anos")
        print("─" * 55)
        print(" 📚 BOLETIM")
        print("─" * 55)

        if not aluno["boletim"]:
            print(" (nenhum idioma cadastrado)")
        else:
            for idioma, notas in aluno["boletim"].items():
                if notas:
                    medias = sum(notas) / len(notas)
                    print(f" {idioma:<12}: {notas}  |  média: {medias:.1f}")
                else:
                    print(f" {idioma:<12}: (sem notas cadastradas)")
        print("═" * 55 + "\n")

    except (KeyError, TypeError) as erro:
        print(f"❌ Erro ao visualizar aluno: {erro}")


def calcular_media(escola, matricula, idioma):
    """
    (Requisito 3g)
    Retorna (media, situacao) para o aluno/idioma.
    A nota mínima vem de escola["nota_minima"] (config global).
    Retorno é uma TUPLA — desempacotável: media, sit = calcular_media(...)
    """
    try:
        aluno = buscar_aluno(escola, matricula)
        if aluno is None:
            raise KeyError(f"Aluno {matricula} não encontrado.")

        if idioma not in aluno["boletim"]:
            raise KeyError(f"Aluno não estuda '{idioma}'.")

        notas = aluno["boletim"][idioma]
        if not notas:
            raise ValueError(f"Sem notas em '{idioma}'.")

        media = round(sum(notas) / len(notas), 1)
        minimo = escola["nota_minima"]
        situacao = "APROVADO" if media >= minimo else "REPROVADO"

        print(f"📊 {aluno['nome']} — {idioma}: média {media} → {situacao}")
        return media, situacao

    except (KeyError, ValueError, ZeroDivisionError) as erro:
        print(f"❌ Erro ao calcular média: {erro}")
        return None, None


def apagar_aluno(escola, matricula):
    """
    (Requisito 3h)
    Remove o aluno da escola. Retorna True/False.
    Demonstra o uso de enumerate + pop.
    """
    try:
        for indice, aluno in enumerate(escola["alunos"]):
            if aluno["matricula"] == matricula:
                escola["alunos"].pop(indice)
                print(f"🗑️  Aluno '{aluno['nome']}' (matrícula {matricula}) removido.")
                return True
        raise KeyError(f"Aluno {matricula} não encontrado.")
    except (KeyError, TypeError) as erro:
        print(f"❌ Erro ao apagar aluno: {erro}")
        return False


def analise_geral(escola):
    """
    (Requisito 3i)
    Retorna uma análise agregada por idioma:
        {
          "Inglês": {
              "media": 7.3,
              "taxa_reprovacao": 25.0,     # em %
              "quantidade_avaliacoes": 12,
          }, ...
        }

    Aqui usamos CONCEITOS FUNCIONAIS:
    - dicionário como acumulador
    - reduce não é necessário aqui, mas usamos compreensão de listas
    """
    try:
        if not escola["alunos"]:
            raise ValueError("Escola vazia.")

        # 1) Agrupa todas as notas por idioma
        por_idioma = {}
        for aluno in escola["alunos"]:
            for idioma, notas in aluno["boletim"].items():
                if notas:
                    por_idioma.setdefault(idioma, []).extend(notas)

        # 2) Calcula métricas
        minimo = escola["nota_minima"]
        resultado = {}
        for idioma, notas in por_idioma.items():
            media = round(sum(notas) / len(notas), 1)
            reprovadas = sum(1 for n in notas if n < minimo)
            taxa = round(reprovadas / len(notas) * 100, 1)
            resultado[idioma] = {
                "media": media,
                "taxa_reprovacao": taxa,
                "quantidade_avaliacoes": len(notas),
            }
        return resultado

    except (ValueError, ZeroDivisionError, KeyError) as erro:
        print(f"❌ Erro na análise geral: {erro}")
        return {}


def quantidade_alunos(escola):
    """(Requisito 3j) Retorna quantos alunos estão cadastrados."""
    try:
        return len(escola["alunos"])
    except (TypeError, KeyError):
        return 0


# ============================================================================
# CAMADA 2 — PERSISTÊNCIA (TXT)
# ============================================================================

def fazer_backup(caminho_origem):
    """
    Cria uma cópia timestamped do arquivo antes de sobrescrever.
    Backup fica em ./backups/escola_AAAAMMDD_HHMMSS.txt
    """
    try:
        if not os.path.exists(caminho_origem):
            return None
        os.makedirs(PASTA_BACKUP, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        destino = os.path.join(PASTA_BACKUP, f"escola_{timestamp}.txt")
        shutil.copy2(caminho_origem, destino)
        return destino
    except OSError as erro:
        print(f"⚠️  Não foi possível criar backup: {erro}")
        return None


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


def carregar_escola(caminho=ARQUIVO_BD):
    """
    Lê o TXT e reconstrói a estrutura em memória.
    Se o arquivo não existir, cria a escola vazia E o arquivo modelo.
    """
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


def criar_arquivo_modelo():
    """
    Cria o arquivo modelo com 5 alunos de exemplo.
    Esse arquivo NUNCA é sobrescrito pelo uso normal — ele é o 'gabarito'
    para o usuário entender a estrutura do banco.
    """
    escola = criar_escola_vazia()

    # 5 alunos de exemplo — propositalmente com desempenhos variados
    adicionar_aluno(escola, 1, "Ana Silva",     "Básico",        15, ["Inglês", "Espanhol"])
    adicionar_aluno(escola, 2, "Carlos Souza",  "Intermediário", 17, ["Inglês", "Francês"])
    adicionar_aluno(escola, 3, "Beatriz Lima",  "Avançado",      20, ["Inglês", "Português"])
    adicionar_aluno(escola, 4, "Diego Mendes",  "Básico",        14, ["Espanhol", "Mandarim"])
    adicionar_aluno(escola, 5, "Elena Rocha",   "Intermediário", 18, ["Francês", "Inglês"])

    # Notas de exemplo
    notas = [
        (1, "Inglês", 8.5), (1, "Inglês", 7.0), (1, "Espanhol", 9.0),
        (2, "Inglês", 6.0), (2, "Inglês", 5.5), (2, "Francês", 7.5),
        (3, "Inglês", 9.5), (3, "Inglês", 9.0), (3, "Português", 10.0),
        (4, "Espanhol", 4.0), (4, "Espanhol", 5.0), (4, "Mandarim", 3.5),
        (5, "Francês", 8.0), (5, "Francês", 7.5), (5, "Inglês", 6.5),
    ]
    for mat, idioma, nota in notas:
        cadastrar_nota(escola, mat, idioma, nota)

    # Grava em disco (o modelo também gera backup do antigo, se houver)
    salvar_escola(escola, ARQUIVO_BD)
    salvar_escola(escola, ARQUIVO_MODELO)
    print("📦 Arquivo modelo criado com 5 alunos de exemplo.")


# ============================================================================
# CAMADA 3 — INTERFACE (terminal estilo ATM)
# ============================================================================

def limpar_tela():
    """Limpa o terminal (Windows ou Unix)."""
    os.system("cls" if os.name == "nt" else "clear")


def exibir_cabecalho(escola):
    """Cabeçalho fixo com nome da escola e nota mínima atual."""
    print("╔" + "═" * 58 + "╗")
    print("║" + " 🎓 ESCOLA DE IDIOMAS ADA — TERMINAL DE ATENDIMENTO ".center(58) + "║")
    print("╠" + "═" * 58 + "╣")
    print(f"║ Nota mínima de aprovação: {escola['nota_minima']:<4} "
          f"| Alunos: {quantidade_alunos(escola):<26} ║")
    print("╚" + "═" * 58 + "╝")


def exibir_menu():
    """Menu numerado — o usuário digita o número da opção."""
    print("""
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
 └──────────────────────────────────────────────────────┘""")


def pausar():
    """Pausa para o usuário ler a saída antes de voltar ao menu."""
    input("\n↩️  Pressione ENTER para continuar...")


# --- Fluxos por opção (aqui fica a "cola" de input/print) -------------------

def fluxo_listar(escola):
    print("\n📋 LISTA DE ALUNOS")
    print("-" * 55)
    for a in escola["alunos"]:
        print(f" [{a['matricula']:>3}] {a['nome']:<20} "
              f"{a['nivel']:<14} {a['idade']} anos")
    print("-" * 55)


def fluxo_visualizar(escola):
    mat = int(input("Matrícula do aluno: "))
    visualizar_aluno(escola, mat)


def fluxo_adicionar(escola):
    print("\n➕ NOVO ALUNO")
    mat = int(input("Matrícula (número inteiro): "))
    nome = input("Nome completo: ")
    print(f"Níveis disponíveis: {list(NIVEIS_VALIDOS.keys())}")
    nivel = input("Nível: ").strip()
    idade = int(input("Idade: "))
    idiomas_txt = input(f"Idiomas (separe por vírgula, ex: Inglês,Espanhol): ")
    idiomas = [i.strip() for i in idiomas_txt.split(",") if i.strip()]
    adicionar_aluno(escola, mat, nome, nivel, idade, idiomas)


def fluxo_cadastrar_nota(escola):
    print("\n📝 CADASTRAR NOTA")
    mat = int(input("Matrícula: "))
    print(f"Idiomas válidos: {IDIOMAS_VALIDOS}")
    idioma = input("Idioma: ").strip()
    nota = float(input("Nota (0-10): "))
    cadastrar_nota(escola, mat, idioma, nota)


def fluxo_alterar_nota(escola):
    print("\n✏️  ALTERAR NOTA")
    mat = int(input("Matrícula: "))
    idioma = input("Idioma: ").strip()
    pos = int(input("Qual nota? (1=primeira, 2=segunda, ...): "))
    nova = float(input("Nova nota: "))
    alterar_nota(escola, mat, idioma, pos, nova)


def fluxo_alterar_dado(escola):
    print("\n🔧 ALTERAR DADO CADASTRAL")
    mat = int(input("Matrícula: "))
    print("Campos permitidos: nome | nivel | idade")
    campo = input("Campo: ").strip().lower()
    valor = input("Novo valor: ").strip()
    alterar_dado_cadastral(escola, mat, campo, valor)


def fluxo_calcular_media(escola):
    print("\n📊 CALCULAR MÉDIA")
    mat = int(input("Matrícula: "))
    idioma = input("Idioma: ").strip()
    calcular_media(escola, mat, idioma)


def fluxo_apagar(escola):
    print("\n🗑️  APAGAR ALUNO")
    mat = int(input("Matrícula: "))
    confirma = input(f"Confirma apagar matrícula {mat}? (s/n): ").lower()
    if confirma == "s":
        apagar_aluno(escola, mat)
    else:
        print("Operação cancelada.")


def fluxo_analise(escola):
    print("\n📈 ANÁLISE GERAL POR IDIOMA")
    resultado = analise_geral(escola)
    if not resultado:
        print("Nada para analisar.")
        return
    print("-" * 60)
    print(f"{'Idioma':<14}{'Média':>8}{'Reprovação':>14}{'Avaliações':>14}")
    print("-" * 60)
    for idioma, d in resultado.items():
        print(f"{idioma:<14}{d['media']:>8.1f}"
              f"{d['taxa_reprovacao']:>13.1f}%{d['quantidade_avaliacoes']:>14}")
    print("-" * 60)


def fluxo_configuracoes(escola):
    """
    Só o DIRETOR pode alterar a nota mínima.
    Demonstra autenticação simples com dicionário de credenciais.
    """
    print("\n⚙️  CONFIGURAÇÕES — ACESSO RESTRITO")
    login = input("Login: ").strip()
    senha = input("Senha: ").strip()

    if login != CREDENCIAIS_DIRETOR["login"] or senha != CREDENCIAIS_DIRETOR["senha"]:
        print("🚫 Credenciais inválidas. Acesso negado.")
        return

    print(f"Nota mínima atual: {escola['nota_minima']}")
    try:
        nova = float(input("Nova nota mínima: "))
        if not (0.0 <= nova <= 10.0):
            raise ValueError("Nota mínima deve estar entre 0 e 10.")
        escola["nota_minima"] = round(nova, 1)
        print(f"✅ Nota mínima atualizada para {escola['nota_minima']}.")
    except ValueError as erro:
        print(f"❌ {erro}")


# ============================================================================
# MAIN — laço principal
# ============================================================================

def main():
    """
    Ponto de entrada. Carrega o BD, mostra o menu e direciona cada opção.
    Ao sair, pergunta se deseja salvar as alterações.
    """
    limpar_tela()
    escola = carregar_escola()

    # Mapa: número -> função que executa o fluxo
    acoes = {
        "1":  fluxo_listar,
        "2":  fluxo_visualizar,
        "3":  fluxo_adicionar,
        "4":  fluxo_cadastrar_nota,
        "5":  fluxo_alterar_nota,
        "6":  fluxo_alterar_dado,
        "7":  fluxo_calcular_media,
        "8":  fluxo_apagar,
        "9":  fluxo_analise,
        "10": lambda e: print(f"\n🔢 Total de alunos: {quantidade_alunos(e)}"),
        "11": fluxo_configuracoes,
        "12": None,   # sair salvando
        "0":  None,   # sair sem salvar
    }

    while True:
        limpar_tela()
        exibir_cabecalho(escola)
        exibir_menu()

        opcao = input(" 👉 Escolha uma opção: ").strip()

        if opcao in ("0", "12"):
            break
        elif opcao in acoes:
            try:
                acoes[opcao](escola)
            except Exception as erro:
                # Captura qualquer coisa inesperada para o terminal não travar
                print(f"⚠️  Erro inesperado: {erro}")
        else:
            print("❌ Opção inválida.")

        pausar()

    # ---------------- Saída ----------------
    if opcao == "12":
        confirma = input("\n💾 Salvar alterações no BD? (s/n): ").lower()
        if confirma == "s":
            salvar_escola(escola)
            print("👋 Até logo!")
        else:
            print("🚪 Saindo sem salvar.")
    else:
        print("🚪 Saindo sem salvar (opção 0).")


# ============================================================================
# EXECUÇÃO
# ============================================================================

if __name__ == "__main__":
    main()
