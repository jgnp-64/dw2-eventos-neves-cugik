# 1. Como rodar o projeto?

## Ativar ambiente virtual:

```
python -m venv venv
venv\Scripts\activate
```

## E então instalar o ***Flask***:

```
pip install flask
```
### Após isso, só é necessário executar ___app.py___


# Comandos importantes para o git

## Configurar nome e email
```
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```
## Clonar repositório
```
git clone URL_REPOSITORIO
```
## Verificar mudanças ainda não salvas
```
git status
```
## Adicionar todas as mudanças ainda não salvas
```
git add .
```
## Subir as modificações
```
git commit -m "Mensagem do commit"
git push
```
### E caso não quiser colocar nenhuma mensagem:
```
git commit --allow-empty-message -m ""
```
## Atualizar o repositório já clonado 
```
git pull
```
