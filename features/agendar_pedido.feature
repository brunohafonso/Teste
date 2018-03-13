Feature: Agendar Pedido

Scenario: Tentar agendar sem informar horario
    Given estar logado e acessar agendamento de pedido
    When nao informo horario
    Then deve apresentar erro

Scenario: Validar Opcao Voltar - Agendar Pedido
    Given acesso a acompanhe seu pedido
    When clico para voltar
    Then volto para a pagina inicial