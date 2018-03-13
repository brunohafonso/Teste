Feature: Restaurantes

Scenario: Exibir Dados dos Restaurantes
    Given estou na pagina inicial e clico em Restaurantes
    When escolho um Restaurante
    Then Consigo ver seus Dados

Scenario: Listar todos os Restaurantes
    Given estou na pagina inicial e clico em Restaurantes
    Then Consigo ver a lista completa

Scenario: Opcao de Voltar
    Given estou na pagina inicial e clico em Restaurantes
    When navego pela pagina de Restaurantes e clico em Voltar
    Then devo voltar para a lista e para a pagina inicial

Scenario: Pesquisar por Nome
    Given estou na pagina inicial e clico em Restaurantes
    When busco um Restaurante por Nome
    Then o resultado sera o que pesquisei

Scenario: Pesquisar por Nome Invalido
    Given estou na pagina inicial e clico em Restaurantes
    When busco um Restaurante por Nome que nao existe
    Then exibira imagem de erro

Scenario: Acesso deslogado - Exibir Painel
    Given estou na pagina inicial deslogado
    When clico em Restaurantes
    Then exibira a lista de Restaurantes

Scenario: Acesso logado – Exibir Painel
    Given estou na pagina inicial logado
    When clico em Restaurantes
    Then exibira a lista de Restaurantes

Scenario: Pesquisar Proximos A Mim
    Given estou na pagina inicial e clico em Restaurantes
    When clico em Proximos a mim
    Then exibira um mapa com os resultados