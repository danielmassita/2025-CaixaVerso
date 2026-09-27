CAIXAVERSO - FC5 | Analista Dados - II | #1735
Logica de Programação em Python
___

# CAIXAVERSO - FC5 | Analista Dados - II | #1735

https://lms.ada.tech/student/topics/by-class-id/097ee233-0745-490b-b38c-1dc99dfd1305/by-module-id/4e6fa598-53f4-4856-a75d-b7e879ff1b7d

<img width="1024" height="682" alt="image" src="https://github.com/user-attachments/assets/25020c6a-0432-40a2-a039-655d14492299" />


- Professor: [Thiago Tavares Magalhães](https://www.linkedin.com/in/thiagotm/)
  - Senior Data Scientist at SuperSim | Teacher at Ada | Master's Degree in Computational Modeling from the National Laboratory for Scientific Computing

___

# 📚 Resumo das Aulas - Lógica de Programação com Python

---

## <span style="color:#2e6fba;">1. Introdução</span>

Olá! Seja bem-vindo ao curso de lógica de programação com linguagem Python! Vamos repassar algumas orientações iniciais para otimizar o seu uso deste material.

### 1.1. Onde programar em Python?
O Python é uma linguagem interpretada. Isso significa que é necessário termos um interpretador Python instalado em nosso computador para poder executar nossos programas.

Além disso, é importante termos um programa que permita a edição dos códigos. Tecnicamente, qualquer editor de textos puro serviria, incluindo o Bloco de Notas do Windows. Mas programadores normalmente preferem utilizar uma **IDE (Integrated Development Environment)**, que oferecerá uma série de recursos para facilitar ainda mais o nosso trabalho, como utilizar código de cores e formatação para deixar o código mais legível, ferramentas para autocompletar o código, ferramentas para procurar erros (*debuggers* e *linters*), entre outros.

---

### <span style="color:#20b2aa;">Ferramentas e IDEs</span>

* **IDLE:** Editor simples que acompanha a instalação oficial do Python.
  > <span style="color:#d9534f;">**Dica:**</span> Lembre-se de marcar a opção **"Add Python to PATH"** durante a instalação!
* **Thonny:** Focado no aprendizado, leve e ideal para iniciantes acompanharem variáveis e chamadas de funções.
* **Visual Studio Code (VS Code):** Leve, gratuito e altamente customizável através de extensões.
* **PyCharm:** IDE profissional da JetBrains, ideal para projetos maiores e integração com SQL/Web.
* **Anaconda e Jupyter Notebook:** Pacote voltado para ciência e análise de dados. Funciona no formato de "caderno" (código + Markdown).
* **Google Colab:** Notebook 100% online e integrado ao Google Drive.
* **Ambientes Online:**
  * [Repl.it](https://replit.com/)
  * [OnlineGDB](https://www.onlinegdb.com/)
  * [Jupyter Try](https://jupyter.org/try)

---

## <span style="color:#2e6fba;">2. Como estudar Python?</span>

* <span style="color:#5cb85c;">**Pratique:**</span> Acompanhe os exemplos digitando o código na sua IDE. Evite o "copia e cola".
* <span style="color:#f0ad4e;">**Investigue Erros:**</span> Tente entender as mensagens de erro antes de pedir ajuda.
* <span style="color:#5bc0de;">**Experimente:**</span> Altere valores, mude a lógica e veja o resultado acontecer na prática.

---

## <span style="color:#2e6fba;">3. Variáveis, Entradas e Saídas</span>

### 3.1. Variáveis e Tipos Primitivos

Variáveis são pedacinhos de memória reservados para guardar dados temporários.

> <span style="color:#d9534f;">**Padrão Python (snake_case):**</span> Nomes de variáveis devem usar letras minúsculas separadas por underline `_`. Exemplo: `nome_completo`, `idade_usuario`.

```python
# Exemplos de declaração de variáveis e tipos primitivos:
nome = 'Zé'                   # str (string)
email = "ze@letscode.com.br"  # str (string)
idade = 22                    # int (inteiro)
salario = 5999.85             # float (ponto flutuante - usa PONTO, não vírgula)
receber_newsletter = True      # bool (booleano - True ou False)
