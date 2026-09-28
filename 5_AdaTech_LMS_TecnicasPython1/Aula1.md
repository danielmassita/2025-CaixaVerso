# Instale o Git antes da Aula 1
### DS-PY-004 — Técnicas de Programação I

Leva 10 minutos. Você só precisa de duas coisas prontas quando a aula começar:

- [ ] O comando `git --version` respondendo no seu terminal
- [ ] Uma conta criada no GitHub

Todo o resto — configuração, comandos, publicação de repositório — a gente faz junto em sala.

---

## 1. Instale

### Windows

No **PowerShell**:

```powershell
winget install --id Git.Git -e --source winget
```

Ou baixe o instalador em **https://git-scm.com/download/win** e avance com **Next** em tudo. Duas telas valem uma pausa:

- **"Choosing the default editor"** → escolha **Visual Studio Code** ou **Notepad**. O padrão é o Vim, que é difícil de fechar se você nunca usou.
- **"Adjusting the name of the initial branch"** → marque **Override... → `main`**.

### macOS

Abra o **Terminal** e digite `git --version`. Se aparecer uma janela oferecendo instalar as *Command Line Developer Tools*, aceite — resolve sozinho.

Se você usa Homebrew: `brew install git`.

### Linux

```bash
sudo apt install git        # Ubuntu, Debian, Mint
sudo dnf install git        # Fedora
sudo pacman -S git          # Arch
```

---

## 2. Confirme

**Feche e reabra o terminal** (importante, principalmente no Windows) e rode:

```bash
git --version
```

Se aparecer `git version 2.x.x`, terminou. O número exato não importa.

---

## 3. Crie a conta no GitHub

Acesse **https://github.com/signup**.

- Escolha um nome de usuário que você não terá vergonha de pôr no currículo — este perfil vai virar seu portfólio.
- Confirme o e-mail (olhe o spam).
- Ative a autenticação de dois fatores quando for oferecida. É obrigatória na plataforma e é mais fácil resolver agora do que no meio de uma entrega.

**Anote o e-mail que você usou** — vamos precisar dele na configuração do Git em aula.

---

## Se travar

| Problema | Solução |
|---|---|
| `git: command not found` / `não é reconhecido` | Feche e reabra o terminal. Persistindo, reinstale marcando *"Git from the command line and also from 3rd-party software"* |
| O instalador abriu uma tela que não entendi | Pode seguir com **Next**; só as duas telas citadas acima importam |
| Não consegui instalar | Venha assim mesmo — resolvemos nos primeiros minutos da aula |

Chegou até aqui? Está pronto. Traga o notebook `aula1_git.ipynb` aberto.
