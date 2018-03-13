Feature: Avaliacoes

Scenario: Acessar a opcao deslogado
    Given abro a aplicacao sem logar
    When clico em Avaliacoes
    Then devo visualizar a tela de login

Scenario: Acessar a opcao deslogado realizar login e continuar fluxo
    Given abro a aplicacao sem logar
    When entra na opcao Avaliacoes e realizo meu login
    Then devo estar no painel de Avaliacoes

Scenario: Acessar a opcao logado
    Given na pagina inicial da aplicacao devo estar logado
    When clico em Avaliacoes
    Then visualizo o painel de Avaliacoes
    
Scenario: Validar Opcao Voltar - Avaliacoes
    Given acesso a opcao avaliacoes
    When clico para voltar
    Then volto para a pagina inicial

Scenario: Validar Opcao Voltar Para Tela Inicial - Avaliacoes
    Given acesso a opcao avaliacoes
    When clico na frase voltar para tela inicial
    Then volto para a pagina inicial