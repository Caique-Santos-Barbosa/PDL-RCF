# Porta Facial V1 - Versão Replit

Este é o sistema de reconhecimento facial para controle de porta adaptado para funcionar no ambiente Replit.

## 🚀 Como usar no Replit

### 1. Importar o projeto
- Crie um novo Repl no Replit
- Escolha "Python" como linguagem
- Importe este projeto ou clone do repositório

### 2. Instalar dependências
O Replit irá automaticamente instalar as dependências listadas no `requirements.txt` e `pyproject.toml`.

### 3. Executar o projeto
- Clique no botão "Run" no Replit
- O servidor será iniciado automaticamente
- Acesse a URL fornecida pelo Replit

## 🔧 Configurações específicas do Replit

### Funcionalidades adaptadas:
- **Controle de porta física**: Desabilitado (modo simulação)
- **Câmera física**: Desabilitada (use upload de imagens)
- **Armazenamento**: Usa diretórios temporários
- **Porta**: Usa a porta padrão do Replit (geralmente 5000)

### Limitações no Replit:
1. **Controle de porta física**: Não disponível (ambiente virtual)
2. **Câmera em tempo real**: Não disponível
3. **Armazenamento persistente**: Limitado (dados são perdidos ao reiniciar)
4. **Upload de arquivos**: Limitado a 100MB

## 📁 Estrutura de arquivos

```
Porta Facial V1/
├── app.py                 # Aplicação principal
├── replit_config.py       # Configurações específicas do Replit
├── requirements.txt       # Dependências Python
├── pyproject.toml        # Configuração do projeto
├── .replit               # Configuração do Replit
├── static/               # Arquivos estáticos
│   ├── css/
│   ├── videos/
│   └── users/
└── templates/            # Templates HTML
```

## 🎯 Funcionalidades disponíveis

### ✅ Funcionando no Replit:
- Interface web completa
- Sistema de usuários
- Upload de fotos para reconhecimento
- Upload de vídeos de fundo
- Sistema de licenciamento
- Histórico de acessos
- Configurações de volume
- Simulação de abertura de porta

### ❌ Não disponível no Replit:
- Controle físico da porta
- Câmera em tempo real
- Armazenamento persistente de arquivos

## 🔐 Acesso ao sistema

### Admin Master:
- URL: `/admin_master`
- Senha padrão: `Gds2024aa@@`

### Painel principal:
- URL: `/`
- Funciona normalmente para demonstração

## 📝 Como testar

1. **Criar usuários**: Use a interface admin para adicionar usuários
2. **Upload de fotos**: Faça upload de fotos dos usuários
3. **Testar reconhecimento**: Use a API `/api/user_recognition` com imagens
4. **Simular acesso**: Use `/api/simular_autenticacao/<email>`

## 🛠️ Solução de problemas

### Erro de dependências:
```bash
# No console do Replit
pip install -r requirements.txt
```

### Erro de porta:
- O Replit define automaticamente a porta
- Verifique a URL fornecida pelo Replit

### Erro de armazenamento:
- Os arquivos são temporários no Replit
- Faça backup dos dados importantes

## 🔄 Deploy

Para fazer deploy em produção:
1. Use um servidor real (não Replit)
2. Configure o controle físico da porta
3. Use armazenamento persistente
4. Configure câmeras físicas

## 📞 Suporte

Para suporte técnico:
- Email: caiquesantosbarbosa@gmail.com
- WhatsApp: +55 (11) 96419-6205

---

**Nota**: Esta versão é otimizada para demonstração e desenvolvimento no Replit. Para uso em produção, use a versão completa do projeto. 