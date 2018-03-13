Feature: Confira Seus Creditos

Scenario: Opcao de Voltar
    Given acesso a opcao de seus creditos logado
    When clico em Voltar
    Then visualizo a pagina inicial
    
Scenario: Acesso deslogado, realizar login e continuar fluxo
    Given acesso o aplicativo deslogado
    When clico em Confira seus creditos e forneco o login
    Then devo visualizar o painel de creditos

Scenario: Acesso deslogado - Exibir Tela de Login
    Given acesso o aplicativo deslogado
    When clico em Confira seus creditos
    Then Visualizo a pagina de login

Scenario: Acesso logado – Exibir Painel
    Given acesso a opcao de seus creditos logado
    Then devo visualizar o painel de creditos

Scenario: Como Funciona
    Given acesso a opcao de seus creditos logado
    When clico em Confira seus creditos
    And clico em Como Funciona
    Then devo ser capaz de ler o informativo
