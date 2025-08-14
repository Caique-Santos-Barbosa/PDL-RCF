# Script PowerShell para configurar e fazer push do projeto PDL-RCF para o GitHub
# Autor: Caique Santos Barbosa

Write-Host "🚀 Configurando repositório PDL-RCF para GitHub..." -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Green

# Verificar se o git está instalado
try {
    git --version | Out-Null
    Write-Host "✅ Git encontrado!" -ForegroundColor Green
} catch {
    Write-Host "❌ Git não está instalado. Por favor, instale o Git primeiro." -ForegroundColor Red
    exit 1
}

# Verificar se estamos no diretório correto
if (-not (Test-Path "app.py")) {
    Write-Host "❌ Arquivo app.py não encontrado. Execute este script no diretório raiz do projeto." -ForegroundColor Red
    exit 1
}

# Inicializar repositório git (se não existir)
if (-not (Test-Path ".git")) {
    Write-Host "📁 Inicializando repositório Git..." -ForegroundColor Yellow
    git init
}

# Adicionar todos os arquivos
Write-Host "📝 Adicionando arquivos ao Git..." -ForegroundColor Yellow
git add .

# Fazer commit inicial
Write-Host "💾 Fazendo commit inicial..." -ForegroundColor Yellow
$commitMessage = @"
🎉 Initial commit: PDL-RCF - Sistema de Reconhecimento Facial para Controle de Porta

- Sistema completo de reconhecimento facial
- Interface web moderna com Flask
- 100% compatível com Replit
- Sistema de usuários e perfis
- Controle de porta com simulação
- Documentação completa
- Configurações para deploy

Desenvolvido por Caique Santos Barbosa
"@

git commit -m $commitMessage

# Configurar branch principal
Write-Host "🌿 Configurando branch principal..." -ForegroundColor Yellow
git branch -M main

# Adicionar remote do GitHub
Write-Host "🔗 Configurando remote do GitHub..." -ForegroundColor Yellow
git remote add origin https://github.com/Caique-Santos-Barbosa/PDL-RCF.git

# Verificar se o remote foi adicionado corretamente
$remotes = git remote -v
if ($remotes -match "origin") {
    Write-Host "✅ Remote configurado com sucesso!" -ForegroundColor Green
} else {
    Write-Host "❌ Erro ao configurar remote. Verifique a URL do repositório." -ForegroundColor Red
    exit 1
}

# Fazer push para o GitHub
Write-Host "🚀 Fazendo push para o GitHub..." -ForegroundColor Yellow
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "🎉 SUCESSO! Projeto enviado para o GitHub!" -ForegroundColor Green
    Write-Host "==========================================" -ForegroundColor Green
    Write-Host "📋 Repositório: https://github.com/Caique-Santos-Barbosa/PDL-RCF" -ForegroundColor Cyan
    Write-Host "🌐 Clone URL: https://github.com/Caique-Santos-Barbosa/PDL-RCF.git" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "📝 Próximos passos:" -ForegroundColor Yellow
    Write-Host "1. Acesse o repositório no GitHub" -ForegroundColor White
    Write-Host "2. Configure o README se necessário" -ForegroundColor White
    Write-Host "3. Adicione colaboradores se desejar" -ForegroundColor White
    Write-Host "4. Configure GitHub Pages se quiser" -ForegroundColor White
    Write-Host ""
    Write-Host "🔗 Links úteis:" -ForegroundColor Yellow
    Write-Host "- Repositório: https://github.com/Caique-Santos-Barbosa/PDL-RCF" -ForegroundColor Cyan
    Write-Host "- Issues: https://github.com/Caique-Santos-Barbosa/PDL-RCF/issues" -ForegroundColor Cyan
    Write-Host "- Wiki: https://github.com/Caique-Santos-Barbosa/PDL-RCF/wiki" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "✅ Configuração concluída!" -ForegroundColor Green
} else {
    Write-Host "❌ Erro ao fazer push. Verifique suas credenciais do GitHub." -ForegroundColor Red
    Write-Host "💡 Dicas:" -ForegroundColor Yellow
    Write-Host "- Configure um token de acesso pessoal no GitHub" -ForegroundColor White
    Write-Host "- Ou use SSH keys para autenticação" -ForegroundColor White
    exit 1
} 