# prosperar-core

Projeto de Machine Learning para o "Prosperar"

## Como rodar:

### Usando docker

Precisar haver uma pasta *files* como irma do projeto *prosperar-core*

```
docker build --tag=prosperar-core .
docker run -v <caminho/para/pasta/de/arquivos>:/app/files -it prosperar-core
```