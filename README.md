# Controle Financeiro Pessoal

Aplicação de linha de comando desenvolvida em Python para registrar receitas e despesas, armazenar movimentações em SQLite e consultar um resumo financeiro.

> Projeto de portfólio e aprendizado. Não se conecta a bancos, não movimenta dinheiro e não substitui um sistema financeiro profissional.

## Funcionalidades

- Cadastrar receitas e despesas.
- Listar movimentações.
- Filtrar movimentações por tipo.
- Excluir uma movimentação.
- Consultar saldo, total de receitas e total de despesas.
- Persistir os dados em banco SQLite local.

## Tecnologias

- Python 3.10+
- SQLite (`sqlite3`, biblioteca padrão do Python)
- SQL

## Como executar

1. Instale o Python 3.10 ou superior.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto.
4. Execute:

```bash
python src/main.py
```

O banco `data/financeiro.db` será criado automaticamente na primeira execução.

No Windows, se `python` não funcionar, tente `py src/main.py`.

## Estrutura

```text
controle-financeiro-python/
├── data/                 # Banco local criado automaticamente
├── src/
│   ├── database.py       # Conexão e operações SQL
│   └── main.py           # Menu e interação com o usuário
├── tests/
│   └── test_database.py  # Testes automatizados básicos
├── .gitignore
└── README.md
```

## Próximas melhorias planejadas

- [ ] Editar movimentações.
- [ ] Filtrar por intervalo de datas e categoria.
- [ ] Exportar dados para CSV.
- [ ] Criar gráficos com Matplotlib.
- [ ] Criar uma interface gráfica ou aplicação web.
- [ ] Adicionar validações e testes para todos os fluxos.

## Aprendizados demonstrados

Este projeto permite praticar lógica de programação, funções, tratamento de exceções, validação de entradas, persistência de dados, modelagem simples de banco relacional, comandos SQL e versionamento com Git.

## Autor

Leonardo Albuquerque — estudante de Engenharia de Software.
