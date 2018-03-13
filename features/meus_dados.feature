Feature: Meus Dados

Scenario: Alterar CPF e salvar
    Given Acesso meus dados
    When altero o CPF e salvo
    Then a alteracao e feita com sucesso

Scenario: Alterar Gênero e salvar
    Given Acesso meus dados
    When altero o genero e salvo
    Then a alteracao e feita com sucesso

Scenario: Alterar Nome e salvar
    Given Acesso meus dados
    When altero o nome e salvo
    Then a alteracao e feita com sucesso

Scenario: Deixar Dados em Branco e salvar
    Given Acesso meus dados
    When deixo os dados em branco e tento salvar
    Then dara erro na tela