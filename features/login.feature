Feature: Login - Troca Login

Scenario: Acesso deslogado
    Given abro o aplicativo deslogado
    When Clico em Trocar Login
    Then devo visualizar a tela de login

Scenario: E-mail certo – Senha em branco
    Given abro o aplicativo deslogado
    When Clico em Trocar Login
    And informo uma senha em branco
    Then deve reportar erro de senha

Scenario: E-mail certo – Senha errada
    Given abro o aplicativo deslogado
    When Clico em Trocar Login
    And informo uma senha errada
    Then deve reportar erro de senha

Scenario: E-mail e Senha em branco
    Given abro o aplicativo deslogado
    When Clico em Trocar Login
    And informo email e senha em branco
    Then deve reportar erro de campos em branco

Scenario: E-mail em branco – Senha correta
    Given abro o aplicativo deslogado
    When Clico em Trocar Login
    And informo email em branco
    Then deve reportar erro de email em branco
    
Scenario: E-mail errado – Senha certa
    Given abro o aplicativo deslogado
    When Clico em Trocar Login
    And informo email invalido
    Then deve reportar erro de email invalido

Scenario: E-mail errado – Senha errada
    Given abro o aplicativo deslogado
    When Clico em Trocar Login
    And informo email e senha invalidos
    Then deve reportar erro de login e senha invalido

Scenario: Opcao de Voltar
    Given abro o aplicativo deslogado
    When Clico em Trocar Login
    And clico em Voltar
    Then devo visualizar a pagina Inicial
