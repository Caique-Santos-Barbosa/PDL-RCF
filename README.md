# 🚪 PDL-RCF - Porta Facial V1

Sistema de reconhecimento facial para controle de porta com interface web moderna e compatibilidade total com Replit.

## 🌟 Características

- **Reconhecimento facial avançado** usando OpenCV e face_recognition
- **Interface web responsiva** com Flask e WebSocket
- **Sistema de usuários completo** com perfis personalizados
- **Upload de vídeos de fundo** e músicas personalizadas
- **Sistema de licenciamento** com controle de acesso
- **Histórico de acessos** em tempo real
- **100% compatível com Replit** para demonstração e desenvolvimento
- **Suporte completo à IA do Replit** com configurações otimizadas

## 🚀 Deploy Rápido

### No Render (Produção - Recomendado)
1. Acesse [render.com](https://render.com)
2. Clique em "New +" → "Web Service"
3. Conecte este repositório GitHub
4. Configure as variáveis de ambiente
5. Deploy automático
6. Acesse a URL fornecida

### No Replit (Desenvolvimento)
1. Acesse [replit.com](https://replit.com)
2. Clique em "Create Repl"
3. Escolha "Python"
4. Importe este repositório
5. Clique em "Run"
6. Acesse a URL fornecida

### Local
```bash
git clone https://github.com/Caique-Santos-Barbosa/PDL-RCF.git
cd PDL-RCF
pip install -r requirements.txt
python app.py
```

## 🤖 Suporte Total à IA do Replit

Este projeto foi **especificamente configurado** para máxima compatibilidade com o Replit Agent e Assistant:

### ✅ Funcionalidades da IA Habilitadas
- **Code Completion** - Autocompletar código em tempo real
- **Code Explanation** - Explicar qualquer parte do código
- **Code Generation** - Gerar funcionalidades completas
- **Bug Detection** - Detectar e corrigir bugs automaticamente
- **Refactoring** - Melhorar e otimizar código existente
- **Auto Apply Changes** - Aplicar mudanças automaticamente

### 🔧 Configurações Otimizadas para IA
- **Modelo**: GPT-4 (mais avançado)
- **Memória**: 2GB otimizada
- **CPU**: 2 cores dedicados
- **Debug**: Totalmente habilitado
- **Package Search**: Busca inteligente
- **Code Context**: Contexto completo do projeto

### 📝 Como Usar a IA (Guia Rápido)
1. **Abrir IA**: Use `Ctrl + K` ou clique no ícone da IA
2. **Assistant Mode**: Use Advanced Assistant para mudanças automáticas
3. **Agent Mode**: Use para criar funcionalidades completas
4. **Perguntas Inteligentes**: 
   - "Explique esta função"
   - "Crie um sistema de backup"
   - "Otimize esta performance"
   - "Adicione validação aqui"

### 🎯 Exemplos Práticos de Uso
```
✨ "Adicione um sistema de notificações em tempo real"
🔧 "Melhore a performance do reconhecimento facial"
🐛 "Analise e corrija este erro"
📊 "Crie um dashboard de analytics"
🔒 "Implemente autenticação JWT"
```

### 📚 Documentação Completa
Veja o arquivo `AI_USAGE_GUIDE.md` para guia detalhado de uso da IA.

## 📋 Funcionalidades

### ✅ Interface Web
- Painel principal com reconhecimento facial
- Interface de administração completa
- Sistema de usuários e perfis
- Upload de mídia (fotos, vídeos, músicas)
- Configurações de volume e horários

### ✅ Reconhecimento Facial
- Detecção automática de rostos
- Comparação com banco de dados de usuários
- Tolerância configurável
- Logs detalhados de reconhecimento

### ✅ Sistema de Usuários
- Cadastro de usuários com fotos
- Perfis personalizados
- Músicas e fundos personalizados
- Controle de permissões

### ✅ Controle de Porta
- Integração com sistema de porta física
- Modo simulação para Replit
- Logs de acessos
- Controle remoto via API

## 🔧 Tecnologias

- **Backend**: Python, Flask, Flask-SocketIO
- **Frontend**: HTML5, CSS3, JavaScript
- **IA**: OpenCV, face_recognition, dlib
- **Comunicação**: WebSocket, REST API
- **Deploy**: Replit, Docker

## 📁 Estrutura do Projeto

```
PDL-RCF/
├── app.py                      # Aplicação principal
├── replit_config.py            # Configurações Replit
├── replit_start.py             # Script de inicialização
├── test_replit_compatibility.py # Testes de compatibilidade
├── requirements.txt            # Dependências Python
├── pyproject.toml             # Configuração do projeto
├── .replit                    # Configuração Replit
├── static/                    # Arquivos estáticos
│   ├── css/
│   ├── videos/
│   └── users/
├── templates/                 # Templates HTML
└── docs/                      # Documentação
```

## 🔐 Acesso ao Sistema

### Admin Master
- **URL**: `/admin_master`
- **Senha**: `Gds2024aa@@`

### Painel Principal
- **URL**: `/`
- **Funcionalidades**: Reconhecimento facial, interface de usuário

## 📊 Compatibilidade

| Ambiente | Status | Observações |
|----------|--------|-------------|
| **Render** | ✅ 100% | Produção recomendada |
| **Replit** | ✅ 100% | Desenvolvimento |
| **Replit AI** | ✅ 100% | Suporte completo habilitado |
| **Local** | ✅ 100% | Todas as funcionalidades |
| **Docker** | ✅ 100% | Containerizado |
| **Produção** | ✅ 100% | Pronto para deploy |

## 🛠️ Configuração

### Variáveis de Ambiente
```bash
# Replit (automático)
REPLIT_MODE=true
PORT=5000

# Local
FLASK_ENV=development
DEBUG_MODE=true
```

### Dependências
```bash
pip install -r requirements.txt
```

## 📝 API Endpoints

### Reconhecimento Facial
- `POST /api/user_recognition` - Reconhecer usuário
- `POST /api/upload_rosto` - Upload de foto

### Controle de Porta
- `POST /api/porta/abrir` - Abrir porta
- `POST /api/porta/fechar` - Fechar porta
- `GET /api/porta/status` - Status da porta

### Usuários
- `GET /api/usuarios` - Listar usuários
- `POST /api/usuarios` - Criar usuário
- `PUT /api/usuarios/<email>` - Atualizar usuário
- `DELETE /api/usuarios/<email>` - Remover usuário

## 🧪 Testes

```bash
# Teste de compatibilidade
python test_replit_compatibility.py

# Inicialização
python replit_start.py

# Executar aplicação
python app.py
```

## 📞 Suporte

- **Email**: caiquesantosbarbosa@gmail.com
- **WhatsApp**: +55 (11) 96419-6205
- **GitHub**: [@caique300797](https://github.com/caique300797)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 🎯 Roadmap

- [ ] Integração com banco de dados externo
- [ ] Sistema de backup automático
- [ ] Cache de reconhecimento facial
- [ ] Interface mobile responsiva
- [ ] Integração com sistemas de segurança

---

**Desenvolvido com ❤️ por Caique Santos Barbosa**

[![Render](https://img.shields.io/badge/Render-Deploy%20Ready-brightgreen)](https://render.com)
[![Replit](https://img.shields.io/badge/Replit-100%25%20Compatible-blue)](https://replit.com)
[![Replit AI](https://img.shields.io/badge/Replit%20AI-Supported-blue)](https://replit.com)
[![Python](https://img.shields.io/badge/Python-3.9+-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-red)](https://flask.palletsprojects.com)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-green)](https://opencv.org)