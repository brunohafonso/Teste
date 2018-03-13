Feature: Acompanhar Pedido

Scenario: Acessar a opcao deslogado
    Given abro a aplicacao sem logar
    When clico em acompanhe seu Pedido
    Then devo visualizar a tela de login

Scenario: Acessar a opcao deslogado realizar login e continuar fluxo
    Given abro a aplicacao sem logar
    When entra na opcao acompanhe seu Pedido e realizo meu login
    Then devo estar na pagina de acompanhamento

Scenario: Acessar a opcao logado
    Given na pagina inicial da aplicacao devo estar logado
    When clico em acompanhe seu Pedido
    Then visualizo o painel

Scenario: Validar Opcao Voltar - Acompanhe Seu Pedido
    Given acesso a opcao acompanhe seu pedido
    When clico para voltar
    Then volto para a pagina inicial

Scenario: Validar Opcao Voltar Para Tela Inicial - Acompanhe Seu Pedido
    Given acesso a opcao acompanhe seu pedido
    When clico em voltar para tela inicial
    Then volto para a pagina inicial

