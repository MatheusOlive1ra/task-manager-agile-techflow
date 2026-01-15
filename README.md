
# Sistema Ágil de Gerenciamento de Tarefas

## Objetivo
Desenvolver um sistema web simples para gerenciamento de tarefas, aplicando conceitos
de Engenharia de Software, metodologias ágeis e controle de qualidade.

## Escopo Inicial
- CRUD de tarefas
- Testes automatizados
- Integração contínua com GitHub Actions

## Metodologia
Foi utilizada a metodologia Kanban, com organização das tarefas através do GitHub Projects,
nas colunas To Do, In Progress e Done.

## Controle de Qualidade
O projeto utiliza testes automatizados com PyTest, executados automaticamente através
de um pipeline de integração contínua configurado no GitHub Actions.

## Mudança de Escopo
Durante o desenvolvimento, foi adicionada a funcionalidade de priorização de tarefas,
permitindo identificar atividades críticas, atendendo uma nova necessidade do cliente.

## Execução do Projeto
```bash
pip install flask pytest
python src/app.py
