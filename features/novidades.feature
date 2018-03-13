Feature: Novidades

Scenario: Acesso deslogado - Exibir Painel
    Given abro o aplicativo deslogado
    When Clico em Novidades
    Then exibe as Novidades

Scenario: Acesso logado – Exibir Painel
    Given abro o aplicativo logado
    When Clico em Novidades
    Then exibe as Novidades

Scenario: Opcao de Voltar
    Given abro o aplicativo
    When Clico em Novidades e clico em voltar
    Then volto para a pagina inicial

Scenario: Rotatividade dos Banners
    Given abro o aplicativo
    When Clico em Novidades e deslizo todos os banners
    Then Volta para o primeiro