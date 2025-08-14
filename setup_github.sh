#!/bin/bash

# Script para configurar e fazer push do projeto PDL-RCF para o GitHub
# Autor: Caique Santos Barbosa

echo "🚀 Configurando repositório PDL-RCF para GitHub..."
echo "=================================================="

# Verificar se o git está instalado
if ! command -v git &> /dev/null; then
    echo "❌ Git não está instalado. Por favor, instale o Git primeiro."
    exit 1
fi

# Verificar se estamos no diretório correto
if [ ! -f "app.py" ]; then
    echo "❌ Arquivo app.py não encontrado. Execute este script no diretório raiz do projeto."
    exit 1
fi

# Inicializar repositório git (se não existir)
if [ ! -d ".git" ]; then
    echo "📁 Inicializando repositório Git..."
    git init
fi

# Adicionar todos os arquivos
echo "📝 Adicionando arquivos ao Git..."
git add .

# Fazer commit inicial
echo "💾 Fazendo commit inicial..."
git commit -m "🎉 Initial commit: PDL-RCF - Sistema de Reconhecimento Facial para Controle de Porta

- Sistema completo de reconhecimento facial
- Interface web moderna com Flask
- 100% compatível com Replit
- Sistema de usuários e perfis
- Controle de porta com simulação
- Documentação completa
- Configurações para deploy

Desenvolvido por Caique Santos Barbosa"

# Configurar branch principal
echo "🌿 Configurando branch principal..."
git branch -M main

# Adicionar remote do GitHub
echo "🔗 Configurando remote do GitHub..."
git remote add origin https://github.com/Caique-Santos-Barbosa/PDL-RCF.git

# Verificar se o remote foi adicionado corretamente
if git remote -v | grep -q "origin"; then
    echo "✅ Remote configurado com sucesso!"
else
    echo "❌ Erro ao configurar remote. Verifique a URL do repositório."
    exit 1
fi

# Fazer push para o GitHub
echo "🚀 Fazendo push para o GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUCESSO! Projeto enviado para o GitHub!"
    echo "=========================================="
    echo "📋 Repositório: https://github.com/Caique-Santos-Barbosa/PDL-RCF"
    echo "🌐 Clone URL: https://github.com/Caique-Santos-Barbosa/PDL-RCF.git"
    echo ""
    echo "📝 Próximos passos:"
    echo "1. Acesse o repositório no GitHub"
    echo "2. Configure o README se necessário"
    echo "3. Adicione colaboradores se desejar"
    echo "4. Configure GitHub Pages se quiser"
    echo ""
    echo "🔗 Links úteis:"
    echo "- Repositório: https://github.com/Caique-Santos-Barbosa/PDL-RCF"
    echo "- Issues: https://github.com/Caique-Santos-Barbosa/PDL-RCF/issues"
    echo "- Wiki: https://github.com/Caique-Santos-Barbosa/PDL-RCF/wiki"
    echo ""
    echo "✅ Configuração concluída!"
else
    echo "❌ Erro ao fazer push. Verifique suas credenciais do GitHub."
    echo "💡 Dicas:"
    echo "- Configure um token de acesso pessoal no GitHub"
    echo "- Ou use SSH keys para autenticação"
    exit 1
fi 