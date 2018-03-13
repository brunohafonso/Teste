Feature: Fale Conosco

Scenario: Acesso deslogado - Exibir Tela de Login
    Given Acesso o aplicativo deslogado 
    When acesso a opcao fale conosco
    Then devo visualizar a tela de login

Scenario: Acesso deslogado, realizar login e continuar fluxo
    Given Acesso o aplicativo deslogado 
    When acesso a opcao de fale conosco informo login
    Then devo visualizar o painel do fale conosco
    
Scenario: Acesso logado – Exibir Painel
    Given Acesso o aplicativo logado
    When acesso a opcao fale conosco
    Then devo visualizar o painel do fale conosco
    
Scenario: Alterar E-mail e enviar Mensagem
    Given Acesso a opcao de fale conosco
    When Preencho os dados e altero o email
    Then consigo enviar mensagem
    
Scenario: Alterar Nome e enviar Mensagem
    Given Acesso a opcao de fale conosco
    When Preencho os dados e altero o nome
    Then consigo enviar mensagem
    
Scenario: Deixar Dados em Branco e Enviar
    Given Acesso a opcao de fale conosco
    When Deixo os dados em branco
    Then nao consigo enviar mensagem
    
Scenario: Troca de tipo de Mensagem
    Given Acesso a opcao de fale conosco
    Then consigo alterar o tipo de mensagem
    
Scenario: Opcao de Voltar
    Given Acesso a opcao de fale conosco
    When clico em voltar
    Then volto para a tela inicial

