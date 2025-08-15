# 🚀 Deploy no Render - PDL-RCF

Este guia irá ajudá-lo a fazer deploy do projeto PDL-RCF no Render.

## 📋 Pré-requisitos

- Conta no [Render](https://render.com)
- Repositório GitHub configurado
- Projeto funcionando localmente

## 🚀 Deploy Automático

### Método 1: Deploy via GitHub (Recomendado)

1. **Acesse o Render**
   - Vá para [render.com](https://render.com)
   - Faça login ou crie uma conta

2. **Criar Novo Web Service**
   - Clique em "New +"
   - Selecione "Web Service"
   - Conecte seu repositório GitHub

3. **Configurar o Serviço**
   - **Name**: `pdl-rcf`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Plan**: Free

4. **Variáveis de Ambiente**
   ```
   PYTHON_VERSION=3.9.16
   FLASK_ENV=production
   REPLIT_MODE=false
   DEBUG_MODE=false
   PORT=10000
   SECRET_KEY=(gerado automaticamente)
   ```

5. **Clicar em "Create Web Service"**

### Método 2: Deploy via render.yaml

1. **Usar o arquivo render.yaml**
   - O arquivo já está configurado
   - Render detectará automaticamente
   - Configure as variáveis de ambiente

## 🔧 Configurações Específicas

### Variáveis de Ambiente

```bash
# Configurações básicas
PYTHON_VERSION=3.9.16
FLASK_ENV=production
REPLIT_MODE=false
DEBUG_MODE=false
PORT=10000

# Segurança
SECRET_KEY=(gerado automaticamente pelo Render)

# Configurações opcionais
DATABASE_URL=(para futuras implementações)
```

### Configurações de Build

```bash
# Build Command
pip install -r requirements.txt

# Start Command
python app.py
```

### Health Check

- **Path**: `/`
- **Timeout**: 30 segundos
- **Interval**: 10 segundos

## 📁 Estrutura de Arquivos

```
PDL-RCF/
├── render.yaml              # Configuração Render
├── render_config.py         # Configurações específicas
├── gunicorn_config.py       # Configuração Gunicorn
├── wsgi.py                  # Arquivo WSGI
├── app.py                   # Aplicação principal
├── requirements.txt         # Dependências
└── ... (outros arquivos)
```

## 🎯 Funcionalidades no Render

### ✅ Funcionando
- Interface web completa
- Sistema de usuários
- Upload de fotos e vídeos
- Sistema de licenciamento
- Histórico de acessos
- WebSocket para comunicação em tempo real

### ⚠️ Limitações
- Controle físico da porta (ambiente virtual)
- Câmera em tempo real (sem hardware)
- Upload limitado a 50MB (plano free)
- Armazenamento temporário

### 🔧 Adaptações
- Modo simulação para controle de porta
- Upload de imagens para reconhecimento
- Configurações otimizadas para produção

## 🚀 Deploy Manual

### Passo 1: Preparar o Projeto
```bash
# Clone o repositório
git clone https://github.com/Caique-Santos-Barbosa/PDL-RCF.git
cd PDL-RCF

# Verificar dependências
pip install -r requirements.txt
```

### Passo 2: Testar Localmente
```bash
# Testar com configurações de produção
export FLASK_ENV=production
export DEBUG_MODE=false
python app.py
```

### Passo 3: Deploy no Render
1. Conecte o repositório
2. Configure as variáveis de ambiente
3. Deploy automático

## 📊 Monitoramento

### Logs
- Acesse os logs no dashboard do Render
- Configure alertas para erros
- Monitore performance

### Métricas
- Tempo de resposta
- Uso de CPU e memória
- Número de requisições

### Health Checks
- Verificação automática de saúde
- Reinicialização automática em caso de falha

## 🔧 Solução de Problemas

### Erro de Build
```bash
# Verificar dependências
pip install -r requirements.txt

# Verificar Python version
python --version
```

### Erro de Runtime
```bash
# Verificar logs
# Configurar variáveis de ambiente
# Verificar portas
```

### Erro de Dependências
```bash
# Instalar dlib-binary
pip install dlib-binary

# Verificar OpenCV
pip install opencv-python
```

## 🎯 Otimizações

### Performance
- Gunicorn com gevent
- Workers otimizados
- Timeout configurado
- Keep-alive habilitado

### Segurança
- Chave secreta gerada automaticamente
- Headers de segurança
- Rate limiting
- Validação de entrada

### Escalabilidade
- Workers baseados em CPU
- Conexões otimizadas
- Preload de aplicação

## 📝 Exemplos de Uso

### Acessar a Aplicação
```
URL: https://pdl-rcf.onrender.com
Admin: https://pdl-rcf.onrender.com/admin_master
Senha: Gds2024aa@@
```

### API Endpoints
```
GET  /                    # Interface principal
GET  /admin_master        # Painel admin
POST /api/user_recognition # Reconhecimento facial
POST /api/porta/abrir     # Abrir porta
```

## 🔄 Atualizações

### Deploy Automático
- Push para main branch
- Deploy automático no Render
- Health check automático

### Deploy Manual
- Trigger manual no dashboard
- Rollback se necessário
- Configurações específicas

## 📞 Suporte

Se encontrar problemas:

1. **Verifique os logs** no Render
2. **Teste localmente** primeiro
3. **Verifique variáveis** de ambiente
4. **Entre em contato**: caiquesantosbarbosa@gmail.com

## 🎉 Resultado

Após o deploy, você terá:

- ✅ **Aplicação online** 24/7
- ✅ **Deploy automático** via GitHub
- ✅ **Monitoramento** completo
- ✅ **Escalabilidade** automática
- ✅ **SSL gratuito** incluído

---

**🚀 Sua aplicação estará online e funcionando!** 