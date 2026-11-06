Sistema de Folha de Pagamento
Aplicação de linha de comando desenvolvida em Java para cadastrar colaboradores e calcular salários conforme o tipo de vínculo: padrão, comissionado ou por produção.
Projeto de portfólio e aprendizado. Os dados são armazenados em memória durante a execução. Não calcula impostos ou descontos trabalhistas e não substitui um sistema profissional de folha de pagamento.

Funcionalidades
- Cadastrar colaboradores de três tipos.
- Listar colaboradores e seus salários.
- Consultar um colaborador pela matrícula.
- Calcular comissões sobre vendas.
- Calcular adicionais por peças produzidas.
- Consultar a folha completa e o total a pagar.
- Validar entradas e impedir matrículas duplicadas.
Tecnologias
- Java 8+
- ArrayList para armazenamento em memória.
- Scanner para entrada de dados.
- BigDecimal para somar os salários arredondados em centavos.
Regras de cálculo
Todos os colaboradores possuem salário base de R$ 2.000,00.
- Padrão: recebe apenas o salário base.
- Comissionado: recebe salário base + valor das vendas × percentual de comissão ÷ 100.
- Produção: recebe salário base + quantidade de peças × valor por peça.
Próximas melhorias planejadas
- Editar e excluir colaboradores.
- Persistir os cadastros em banco de dados.
- Exportar a folha de pagamento para CSV.
- Consultar o histórico de pagamentos por mês.
- Criar uma interface gráfica ou aplicação web.
- Ampliar os testes automatizados dos fluxos do menu.
Aprendizados demonstrados
Este projeto permite praticar lógica de programação, criação de classes e objetos, herança, encapsulamento, polimorfismo, sobrescrita de métodos, coleções com ArrayList, estruturas de repetição e seleção, tratamento de exceções, validação de entradas e testes automatizados.
Autor
Leonardo Albuquerque — estudante de Engenharia de Software.
