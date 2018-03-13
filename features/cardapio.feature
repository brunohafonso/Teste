Feature: Cardapio

Scenario: Exibicao do Prato Sem exibir Preco
    Given Acesso a opcao Cardapio
    When escolho um grupo e um produto
    Then O preco nao e exibido

Scenario: Exibicao dos Grupos
    Given Acesso a opcao Cardapio
    Then consigo visualizar os grupos
    
Scenario: Fazer Pedido e entrar no fluxo de Fazer Pedido
    Given Estando Logado acesso a opcao Cardapio
    When escolho um grupo e um produto
    And clico em fazer pedido
    Then devo entrar no fluxo de pedido

Scenario: Opcao de Voltar
    Given Acesso a opcao Cardapio
    When escolho uma opcao
    And clico no botao Voltar
    Then As paginas anteriores serao exibidas

Scenario: Troca de Grupos pela Barra Superior
    Given Acesso a opcao Cardapio
    When escolho um grupo
    Then consigo trocar de grupos pela barra Superior