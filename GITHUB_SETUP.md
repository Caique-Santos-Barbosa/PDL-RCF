# 🚀 Configuração do Repositório GitHub - PDL-RCF

Este guia irá ajudá-lo a configurar e fazer push do projeto PDL-RCF para o GitHub.

## 📋 Pré-requisitos

- [Git](https://git-scm.com/) instalado
- Conta no [GitHub](https://github.com)
- Token de acesso pessoal do GitHub (recomendado)

## 🔧 Método 1: Script Automático (Recomendado)

### Para Linux/Mac:
```bash
chmod +x setup_github.sh
./setup_github.sh
```

### Para Windows (PowerShell):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\setup_github.ps1
```

## 🔧 Método 2: Configuração Manual

### 1. Inicializar Git
```bash
git init
```

### 2. Adicionar arquivos
```bash
git add .
```

### 3. Fazer commit inicial
```bash
git commit -m "🎉 Initial commit: PDL-RCF - Sistema de Reconhecimento Facial para Controle de Porta

- Sistema completo de reconhecimento facial
- Interface web moderna com Flask
- 100% compatível com Replit
- Sistema de usuários e perfis
- Controle de porta com simulação
- Documentação completa
- Configurações para deploy

Desenvolvido por Caique Santos Barbosa"
```

### 4. Configurar branch principal
```bash
git branch -M main
```

### 5. Adicionar remote do GitHub
```bash
git remote add origin https://github.com/Caique-Santos-Barbosa/PDL-RCF.git
```

### 6. Fazer push
```bash
git push -u origin main
```

## 🔐 Configuração de Autenticação

### Opção 1: Token de Acesso Pessoal (Recomendado)

1. Acesse [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. Clique em "Generate new token (classic)"
3. Selecione os escopos:
   - `repo` (acesso completo aos repositórios)
   - `workflow` (opcional, para GitHub Actions)
4. Copie o token gerado
5. Use o token como senha quando solicitado

### Opção 2: SSH Keys

1. Gerar chave SSH:
```bash
ssh-keygen -t ed25519 -C "seu-email@exemplo.com"
```

2. Adicionar chave ao SSH agent:
```bash
ssh-add ~/.ssh/id_ed25519
```

3. Copiar chave pública:
```bash
cat ~/.ssh/id_ed25519.pub
```

4. Adicionar no GitHub: Settings > SSH and GPG keys > New SSH key

5. Usar URL SSH:
```bash
git remote set-url origin git@github.com:Caique-Santos-Barbosa/PDL-RCF.git
```

## 📁 Estrutura do Repositório

Após o push, seu repositório terá a seguinte estrutura:

```
PDL-RCF/
├── README.md                    # Documentação principal
├── LICENSE                      # Licença MIT
├── .gitignore                   # Arquivos ignorados pelo Git
├── app.py                       # Aplicação principal
├── replit_config.py             # Configurações Replit
├── replit_start.py              # Script de inicialização
├── test_replit_compatibility.py # Testes de compatibilidade
├── requirements.txt             # Dependências Python
├── pyproject.toml              # Configuração do projeto
├── .replit                     # Configuração Replit
├── replit.nix                  # Dependências do sistema
├── Dockerfile                  # Containerização
├── docker-compose.yml          # Orquestração
├── setup_github.sh             # Script de setup (Linux/Mac)
├── setup_github.ps1            # Script de setup (Windows)
├── static/                     # Arquivos estáticos
│   ├── css/
│   ├── videos/
│   └── users/
├── templates/                  # Templates HTML
└── docs/                       # Documentação adicional
    ├── README_REPLIT.md
    ├── QUICK_START_REPLIT.md
    ├── CHANGELOG_REPLIT.md
    └── COMPATIBILITY_CHECK.md
```

## 🎯 Configurações Adicionais no GitHub

### 1. Configurar Descrição
- Acesse o repositório no GitHub
- Clique em "About" (lado direito)
- Adicione descrição: "Sistema de reconhecimento facial para controle de porta com interface web moderna"

### 2. Configurar Tópicos
Adicione os tópicos:
- `python`
- `flask`
- `opencv`
- `face-recognition`
- `replit`
- `facial-recognition`
- `door-control`
- `web-interface`

### 3. Configurar Website
- URL: `https://replit.com/@seu-usuario/PDL-RCF`

### 4. Configurar Issues
- Habilite Issues no repositório
- Configure templates se desejar

### 5. Configurar Wiki
- Habilite Wiki no repositório
- Adicione documentação adicional

## 🔗 Links Úteis

- **Repositório**: https://github.com/Caique-Santos-Barbosa/PDL-RCF
- **Issues**: https://github.com/Caique-Santos-Barbosa/PDL-RCF/issues
- **Wiki**: https://github.com/Caique-Santos-Barbosa/PDL-RCF/wiki
- **Actions**: https://github.com/Caique-Santos-Barbosa/PDL-RCF/actions

## 📝 Próximos Passos

1. **Verificar o push**: Acesse o repositório no GitHub
2. **Configurar proteções**: Settings > Branches > Add rule
3. **Configurar Actions**: Se desejar CI/CD
4. **Adicionar colaboradores**: Settings > Collaborators
5. **Configurar Pages**: Settings > Pages (opcional)

## 🆘 Solução de Problemas

### Erro: "Authentication failed"
- Verifique suas credenciais
- Use token de acesso pessoal
- Configure SSH keys

### Erro: "Repository not found"
- Verifique se o repositório existe
- Verifique as permissões
- Verifique a URL do remote

### Erro: "Permission denied"
- Verifique se você tem permissão para o repositório
- Use token de acesso pessoal com permissões adequadas

## 📞 Suporte

Se encontrar problemas:
- **Email**: caiquesantosbarbosa@gmail.com
- **WhatsApp**: +55 (11) 96419-6205
- **GitHub**: [@caique300797](https://github.com/caique300797)

---

**✅ Repositório configurado com sucesso!** 