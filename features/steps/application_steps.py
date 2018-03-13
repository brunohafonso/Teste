from behave import *
from tools.application import America
from driver.driver import DriverBuilder
import time
import random

driver = DriverBuilder()
america = America(driver.get_driver())
america.inicio()

@given(u'abro a aplicacao sem logar')
def step_impl(context):
    america.aguarde('menu lateral')
    america.coordenadas('banner')
    america.troca_login()
    america.coordenadas('voltar')

@when(u'clico em acompanhe seu Pedido')
def step_impl(context):
    america.clica('acompanhe seu pedido')

@then(u'devo visualizar a tela de login')
def step_impl(context):
    america.aguarde('email')
    america.coordenadas('voltar')

@when(u'entra na opcao acompanhe seu Pedido e realizo meu login')
def step_impl(context):
    america.clica('acompanhe seu pedido')
    america.aguarde('email')
    america.login_manual()
    america.coordenadas('banner')
    america.coordenadas('banner')

@then(u'devo estar na pagina de acompanhamento')
def step_impl(context):
    america.aguarde('tela inicial')
    america.pagina_inicial()

@given(u'na pagina inicial da aplicacao devo estar logado')
def step_impl(context):
    america.troca_login()
    america.login()
    america.coordenadas('banner')
    america.coordenadas('banner')

@then(u'visualizo o painel')
def step_impl(context):
    america.aguarde('tela inicial')
    america.pagina_inicial()

@given(u'acesso a opcao acompanhe seu pedido')
def step_impl(context):
    america.clica('acompanhe seu pedido')

@when(u'clico para voltar')
def step_impl(context):
    america.clica('voltar pesquisa')

@then(u'volto para a pagina inicial')
def step_impl(context):
    america.aguarde('novidades')

@when(u'clico em voltar para tela inicial')
def step_impl(context):
    america.new_coord('tela inicial')
    america.aguarde('novidades')

@when(u'clico em agendar pedido')
def step_impl(context):
    america.clica('agendar pedido')

@then(u'acesso o fluxo de agendamento de pedidos')
def step_impl(context):
    america.new_coord('primeiro endereco')
    time.sleep(15)
    america.coordenadas('horario')
    time.sleep(2)
    america.coordenadas('confirmarhorarioagendamento')
    time.sleep(0.8)
    america.new_coord('prosseguir')
    america.aguarde('para compartilhar')
    america.pagina_inicial()

@given(u'estar logado e acessar agendamento de pedido')
def step_impl(context):
    america.troca_login()
    america.login()
    america.aguarde('agendar pedido')
    america.clica('agendar pedido')

@when(u'nao informo horario')
def step_impl(context):
    america.new_coord('primeiro endereco')
    america.new_coord('prosseguir')

@then(u'deve apresentar erro')
def step_impl(context):
    america.new_coord('ok')
    america.pagina_inicial()

@when(u'clico em Avaliacoes')
def step_impl(context):
    america.clica('menu lateral')
    america.new_coord('lateral avaliacoes')

@when(u'entra na opcao Avaliacoes e realizo meu login')
def step_impl(context):
    america.acessa_opcao('avaliacoes')
    america.login_manual()

@then(u'devo estar no painel de Avaliacoes')
def step_impl(context):
    america.aguarde('painel avaliacoes')
    america.pagina_inicial()
    
@then(u'visualizo o painel de Avaliacoes')
def step_impl(context):
    america.aguarde('painel avaliacoes')
    america.pagina_inicial()

@given(u'acesso a opcao avaliacoes')
def step_impl(context):
    america.acessa_opcao('avaliacoes')

@when(u'clico na frase voltar para tela inicial')
def step_impl(context):
    position = 600
    while(america.aguarde('painel avaliacoes',1)):
        america.clique_cego(x = 360, y = position)
        position += 10
        try:
            america.aguarde('novidades',1)
            break
        except Exception:
            continue

@given(u'Acesso a opcao Cardapio')
def step_impl(context):
    america.coordenadas('banner')
    america.coordenadas('banner')
    america.clica('cardapio')

@when(u'escolho um grupo e um produto')
def step_impl(context):
    america.clica('para compartilhar')
    america.new_coord('batata rustica')

@then(u'O preco nao e exibido')
def step_impl(context):
    america.aguarde('fazer pedido cardapio')
    america.pagina_inicial()

@then(u'consigo visualizar os grupos')
def step_impl(context):
    america.scroll_para_cima(5)
    america.pagina_inicial()

@when(u'clico em fazer pedido')
def step_impl(context):
    position = 800
    while(america.aguarde('fazer pedido cardapio',1)):
        america.clique_cego(x = 360, y = position)
        position += 15
        try:
            america.aguarde('primeiro endereco',1)
            break
        except Exception:
            continue

@then(u'devo entrar no fluxo de pedido')
def step_impl(context):
    try:
        america.aguarde('primeiro endereco')
    except Exception:
        pass
    america.pagina_inicial()

@when(u'escolho uma opcao')
def step_impl(context):
    america.clica('para compartilhar')
    america.new_coord('batata rustica')
    america.new_coord('fazer pedido cardapio')

@when(u'clico no botao Voltar')
def step_impl(context):
    america.aguarde('fazer pedido cardapio')
    america.coordenadas('voltar pesquisa')

@then(u'As paginas anteriores serao exibidas')
def step_impl(context):
    america.aguarde('batata rustica')
    america.coordenadas('voltar pesquisa')
    america.aguarde('para compartilhar')
    america.coordenadas('voltar pesquisa')
    america.pagina_inicial()

@when(u'escolho um grupo')
def step_impl(context):
    america.clica('para compartilhar')

@then(u'consigo trocar de grupos pela barra Superior')
def step_impl(context):
    america.coordenadas('mudar grupo direita')
    america.coordenadas('mudar grupo direita')
    america.coordenadas('mudar grupo direita')
    america.pagina_inicial()

@given(u'Estando logado acesso a opcao Cardapio')
def step_impl(context):
    america.troca_login()
    america.login()
    america.clica('cardapio')

@when(u'clico em um produto para adicionar ao Carrinho')
def step_impl(context):    
    america.clica('para compartilhar')
    america.new_coord('batata rustica')
    america.new_coord('fazer pedido cardapio')
    america.new_coord('primeiro endereco')

@then(u'o produto deve ser adicionado')
def step_impl(context):
    america.coordenadas('abrir carrinho')
    america.aguarde('batata rustica')
    america.pagina_inicial()

@when(u'clico no Carrinho')
def step_impl(context):
    america.clica('cardapio')
    america.clica('para compartilhar')
    america.new_coord('batata rustica')
    america.new_coord('fazer pedido cardapio')
    america.new_coord('primeiro endereco')
    america.pagina_inicial()
    america.new_coord('carrinho')

@then(u'devo conseguir alterar o pedido')
def step_impl(context):
    america.new_coord('aumenta quantidade')
    america.aguarde('quantidade') == False
    america.pagina_inicial()

@then(u'devo conseguir remover o pedido')
def step_impl(context):
    america.new_coord('diminuir quantidade')
    america.pagina_inicial()

@when(u'escolho a opcao de continuar escolhendo')
def step_impl(context):
    america.new_coord('continuar escolhendo')

@then(u'devo ver a tela de grupos de Cardapio')
def step_impl(context):
    america.aguarde('para compartilhar')
    america.pagina_inicial()

@given(u'acesso a opcao de seus creditos logado')
def step_impl(context):
    america.coordenadas('banner')
    america.coordenadas('banner')
    america.troca_login()
    america.login()
    america.clica('confira seus creditos')

@when(u'clico em Voltar')
def step_impl(context):
    america.coordenadas('voltar')

@then(u'visualizo a pagina inicial')
def step_impl(context):
    america.aguarde('novidades')

@given(u'acesso o aplicativo deslogado')
def step_impl(context):
    america.troca_login()
    america.coordenadas('voltar')

@when(u'clico em Confira seus creditos e forneco o login')
def step_impl(context):
    america.clica('confira seus creditos')
    america.login_manual()

@then(u'devo visualizar o painel de creditos')
def step_impl(context):
    america.aguarde('como funciona')
    america.pagina_inicial()

@when(u'clico em Confira seus creditos')
def step_impl(context):
    america.clica('confira seus creditos')

@then(u'Visualizo a pagina de login')
def step_impl(context):
    america.aguarde('email')
    america.coordenadas('voltar')

@when(u'clico em Como Funciona')
def step_impl(context):
    america.scroll_para_cima(2)

@then(u'devo ser capaz de ler o informativo')
def step_impl(context):
    america.scroll_para_cima(5)
    america.pagina_inicial()

@given(u'abro o aplicativo deslogado')
def step_impl(context):
    america.aguarde('menu lateral')

@when(u'Clico em Trocar Login')
def step_impl(context):
    america.troca_login()

@when(u'informo uma senha em branco')
def step_impl(context):
    america.login(senha='')

@then(u'deve reportar erro de senha')
def step_impl(context):
    try:
        america.aguarde('senha invalida')
    except Exception:
        america.coordenadas('voltar')
    america.coordenadas('voltar')

@when(u'informo uma senha errada')
def step_impl(context):
    america.login(senha='dskjlfahdskjnhvdskjhsakj')

@when(u'informo email e senha em branco')
def step_impl(context):
    america.login(usuario = '', senha = '')

@then(u'deve reportar erro de campos em branco')
def step_impl(context):
    america.aguarde('senha invalida')
    america.aguarde('email invalido')
    america.coordenadas('voltar')

@when(u'informo email em branco')
def step_impl(context):
    america.login(usuario = '')

@when(u'informo email invalido')
def step_impl(context):
    america.login(usuario = 'nem@existe.esse.email')
    america.coordenadas('acessar')

@then(u'deve reportar erro de email em branco')
def step_impl(context):
    america.aguarde('email invalido')
    america.coordenadas('voltar')

@then(u'deve reportar erro de email invalido')
def step_impl(context):
    america.aguarde('email-nao-cadastrado')
    america.new_coord('email-nao-cadastrado')
    america.coordenadas('voltar')

@when(u'informo email e senha invalidos')
def step_impl(context):
    america.login(usuario = 'nao@existe.com.br', senha = 'nemtemsenha')
    america.coordenadas('acessar')

@then(u'deve reportar erro de login e senha invalido')
def step_impl(context):
    america.aguarde('email-nao-cadastrado')
    america.new_coord('email-nao-cadastrado')
    america.coordenadas('voltar')

@then(u'devo visualizar a pagina Inicial')
def step_impl(context):
    america.aguarde('novidades')

@when(u'Clico em Novidades')
def step_impl(context):
    america.clica('novidades')

@then(u'exibe as Novidades')
def step_impl(context):
    time.sleep(10)
    america.pagina_inicial()

@given(u'abro o aplicativo logado')
def step_impl(context):
    america.troca_login()
    america.login()

@given(u'abro o aplicativo')
def step_impl(context):
    america.aguarde('menu lateral')

@when(u'Clico em Novidades e clico em voltar')
def step_impl(context):
    america.clica('novidades, voltar pesquisa')

@when(u'Clico em Novidades e deslizo todos os banners')
def step_impl(context):
    america.clica('novidades')
    america.scroll_para_direita(4)

@then(u'Volta para o primeiro')
def step_impl(context):
    time.sleep(5)
    america.pagina_inicial()

@given(u'acesso a acompanhe seu pedido')
def step_impl(context):
    america.aguarde('menu lateral')
    america.coordenadas('banner')
    america.coordenadas('banner')
    america.clica('acompanhe seu pedido')

@given(u'estou na pagina inicial do app')
def step_impl(context):
    america.troca_login()
    america.login()

@when(u'clico no menu lateral e em seguida Inicio')
def step_impl(context):
    america.pagina_inicial()

@then(u'volto continuo na tela inicial')
def step_impl(context):
    america.aguarde('novidades')

@when(u'acesso as Notificacoes e mudo de tela')
def step_impl(context):
    america.scroll_para_cima()
    america.acessa_opcao('cardapio')
    america.pagina_inicial()

@then(u'as Notificacoes sao recolhidas')
def step_impl(context):
    america.aguarde('novidades')

@when(u'acesso as Notificacoes')
def step_impl(context):
    america.scroll_para_cima()

@then(u'Consigo ver a versao do app')
def step_impl(context):
    america.aguarde('versao')
    america.pagina_inicial()

@then(u'consigo ver o botao de atualizacao')
def step_impl(context):
    america.aguarde('atualizar')
    america.pagina_inicial()

@given(u'estou na pagina inicial e clico em Restaurantes')
def step_impl(context):
    america.aguarde('menu lateral')
    america.new_coord('menu lateral')
    america.new_coord('restaurantes')
    america.new_coord('proximo a mim')
    america.new_coord('ver todos os restaurantes')

@when(u'escolho um Restaurante')
def step_impl(context):
    try:
        america.aguarde('primeiro restaurante')
        america.new_coord('primeiro restaurante')
    except Exception:
        america.new_coord('menu lateral')
        america.new_coord('restaurantes')
        america.new_coord('proximo a mim')
        america.new_coord('ver todos os restaurantes')
        america.aguarde('primeiro restaurante')
        america.new_coord('primeiro restaurante')

@then(u'Consigo ver seus Dados')
def step_impl(context):
    america.aguarde('dados restaurante')
    america.pagina_inicial()

@then(u'Consigo ver a lista completa')
def step_impl(context):
    america.scroll_para_cima(3)

@when(u'navego pela pagina de Restaurantes e clico em Voltar')
def step_impl(context):
    america.new_coord('primeiro restaurante')
    america.clica('voltar pesquisa')

@then(u'devo voltar para a lista e para a pagina inicial')
def step_impl(context):
    america.aguarde('primeiro restaurante')
    america.clica('voltar pesquisa')
    america.aguarde('novidades')

@when(u'busco um Restaurante por Nome')
def step_impl(context):
    america.new_coord('procurar restaurante por nome')
    america.new_coord('busca restaurante por nome')
    america.escrita_direta('Paulista')

@then(u'o resultado sera o que pesquisei')
def step_impl(context):
    america.aguarde('resultado busca')
    america.pagina_inicial()

@when(u'busco um Restaurante por Nome que nao existe')
def step_impl(context):
    america.new_coord('procurar restaurante por nome')
    america.new_coord('busca restaurante por nome')
    america.escrita_direta('nao existe', trava=False)

@then(u'exibira imagem de erro')
def step_impl(context):
    america.aguarde('Restaurante invalido')
    america.pagina_inicial()

@given(u'estou na pagina inicial deslogado')
def step_impl(context):
    america.troca_login()
    america.coordenadas('voltar')

@when(u'clico em Restaurantes')
def step_impl(context):
    america.clica('menu lateral')
    america.new_coord('restaurantes')
    america.new_coord('proximo a mim')
    america.new_coord('ver todos os restaurantes')

@then(u'exibira a lista de Restaurantes')
def step_impl(context):
    america.scroll_para_cima(3)
    america.aguarde('ultimo restaurante')
    america.pagina_inicial()

@given(u'estou na pagina inicial logado')
def step_impl(context):
    america.troca_login()
    america.login()

@when(u'clico em Proximos a mim')
def step_impl(context):
    america.new_coord('proximo a mim')

@then(u'exibira um mapa com os resultados')
def step_impl(context):
    america.aguarde('mapa')
    america.pagina_inicial()

@when(u'acesso a opcao fale conosco')
def step_impl(context):
    america.new_coord('menu lateral')
    america.new_coord('lateral fale conosco')

@when(u'acesso a opcao de fale conosco informo login')
def step_impl(context):
    america.new_coord('menu lateral')
    america.new_coord('lateral fale conosco')
    america.login_manual()
    america.coordenadas('banner')

@then(u'devo visualizar o painel do fale conosco')
def step_impl(context):
    america.aguarde('EmailFaleConosco')
    america.pagina_inicial()

@given(u'Acesso o aplicativo logado')
def step_impl(context):
    america.troca_login()
    america.login()

@given(u'Acesso a opcao de fale conosco')
def step_impl(context):
    america.troca_login()
    america.login()
    america.coordenadas('banner')
    america.new_coord('menu lateral')
    america.new_coord('lateral fale conosco')

@when(u'Preencho os dados e altero o email')
def step_impl(context):
    america.trocar('EmailFaleConosco','email@alterado.teste.br')
    america.scroll_para_cima(2)
    america.coordenadas('tipodemsg')
    time.sleep(2)
    america.coordenadas('Sugestao')
    time.sleep(2)

@then(u'consigo enviar mensagem')
def step_impl(context):
    america.coordenadas('mensagem')
    america.escrita_direta('Teste Fale Conosco')
    america.scroll_para_cima(2)
    america.coordenadas('enviarmensagem')
    america.aguarde('novidades')

@when(u'Preencho os dados e altero o nome')
def step_impl(context):
    america.trocar('NomeFaleConosco', 'nomealterado')

@when(u'Deixo os dados em branco')
def step_impl(context):
    america.apagar('NomeFaleConosco')
    america.driver.back()
    america.apagar('EmailFaleConosco', vezes = 100)
    america.driver.back()
    america.apagar('CelularFaleConosco')

@then(u'nao consigo enviar mensagem')
def step_impl(context):
    america.scroll_para_cima(2)
    america.coordenadas('enviarmensagem')
    america.aguarde('fale em branco')
    america.pagina_inicial()

@then(u'consigo alterar o tipo de mensagem')
def step_impl(context):
    america.coordenadas('tipodemsg')
    america.coordenadas('Critica')
    america.coordenadas('tipodemsg')
    america.coordenadas('Elogio')
    america.coordenadas('tipodemsg')
    america.coordenadas('Sugestao')
    america.pagina_inicial()

@then(u'volto para a tela inicial')
def step_impl(context):
    america.aguarde('novidades')

@given(u'Acesso meus dados')
def step_impl(context):
    america.aguarde('menu lateral')
    america.troca_login()
    america.login()
    america.coordenadas('banner')
    america.clica('menu lateral')
    america.scroll_para_baixo()
    america.coordenadas('entrar lateral')

@when(u'altero o CPF e salvo')
def step_impl(context):
    num = random.randrange(0,9)
    america.trocar('cpf dados','{}{}{}{}{}{}{}{}{}{}{}'.format(num, num, num, num, num, num, num, num, num, num, num))

@then(u'a alteracao e feita com sucesso')
def step_impl(context):
    america.scroll_para_baixo()
    america.coordenadas('salvar dados')

@when(u'altero o genero e salvo')
def step_impl(context):
    america.coordenadas('genero dados')
    america.coordenadas('masculino dados')
    america.coordenadas('genero dados')
    america.coordenadas('feminino dados')
    america.coordenadas('genero dados')
    america.coordenadas('masculino dados')    

@when(u'altero o nome e salvo')
def step_impl(context):
    america.trocar('nome', 'novo nome')

@when(u'deixo os dados em branco e tento salvar')
def step_impl(context):
    america.apagar('nome')
    america.apagar('celular dados')

@then(u'dara erro na tela')
def step_impl(context):
    america.aguarde('menu lateral')
    america.pagina_inicial()