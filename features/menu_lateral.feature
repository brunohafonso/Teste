Feature: Menu Lateral e Notificacoes

Scenario: Validar a opcao de Inicio do menu Lateral
    Given estou na pagina inicial do app
    When clico no menu lateral e em seguida Inicio
    Then volto continuo na tela inicial

Scenario: Recolher ao mudar de Página
    Given estou na pagina inicial do app
    When acesso as Notificacoes e mudo de tela
    Then as Notificacoes sao recolhidas

Scenario: Exibir Informações de Versão
    Given estou na pagina inicial do app
    When acesso as Notificacoes
    Then Consigo ver a versao do app

Scenario: Botão Atualizar
    Given estou na pagina inicial do app
    When acesso as Notificacoes
    Then consigo ver o botao de atualizacao
