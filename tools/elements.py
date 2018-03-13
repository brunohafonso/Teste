largura = 720
altura = 1280


def elementos():
    return {
    # Tela Inicial
        "pular": {
            "xpath": "//android.view.View[@content-desc='Pular']",
            "x": 0.496,
            "y": 0.916
        },
        "entrar": {
            "xpath": "//android.view.View[@content-desc='ENTRAR']",
            "x": 0.524,
            "y": 0.56
        },
    # Menu Lateral
        "menu lateral": {
            "xpath": "//android.widget.Button[@content-desc='menu']",
            "x": 0.113,
            "y": 0.03
        },
        "inicio": {
            "xpath": '//android.widget.Button[@content-desc="INÍCIO"]',
            "x": 173/largura,
            "y": 258/altura
        },
        "lateral fazer pedido": {
            "xpath": "//android.view.View[@content-desc='FAZER PEDIDO']",
            "x": 0.303,
            "y": 0.281
        },
        "lateral cardapio": {
            "xpath": '//android.widget.Button[@content-desc="CARDÁPIO"]',
            "x": 0.283,
            "y": 0.351
        },
        "lateral agendar pedido": {
            "xpath": '//android.widget.Button[@content-desc="AGENDAR PEDIDO"]',
            "x": 0.319,
            "y": 0.425
        },
        "lateral favoritos": {
            "xpath": '//android.widget.Button[@content-desc="FAVORITOS"]',
            "x": 0.319,
            "y": 0.427
        },
        "lateral acompanhe seu pedido": {
            "xpath": '//android.widget.Button[@content-desc="ACOMPANHE SEU PEDIDO"]',
            "x": 0.333,
            "y": 0.571
        },
        "lateral confira seus creditos": {
            "xpath": '//android.widget.Button[@content-desc="CONFIRA SEUS CRÉDITOS"]',
            "x": 0.322,
            "y": 0.645
        },
        "lateral novidades": {
            "xpath": '//android.widget.Button[@content-desc="NOVIDADES DO AMERICA"]',
            "x": 0.319,
            "y": 0.72
        },
        "lateral avaliacoes": {
            "xpath": '//android.widget.Button[@content-desc="AVALIAÇÕES"]',
            "x": 0.279,
            "y": 0.789
        },
        "restaurantes": {
            "xpath": "//android.widget.Button[@content-desc='RESTAURANTES']",
            "x": 237/largura,
            "y": 1035/altura
        },
        'ver todos os restaurantes':{
            'xpath': '//android.widget.Button[@content-desc="VER TODOS RESTAURANTES"]',
            'x':537/largura,
            'y':1134/altura
        },
        "lateral fale conosco": {
            "xpath": "//android.widget.Button[@content-desc='FALE CONOSCO']",
            "x": 199/720,
            "y": 1115/1280
        },
        "entrar lateral": {
            "xpath": "//android.widget.Button[@content-desc='ENTRAR']",
            "x": 0.264,
            "y": 0.12
        },
    # Menu Principal
        'banner': {
            'xpath':'//android.widget.Image[@content-desc="close circle-outline"]',
            'x': 615/720,
            'y': 87/1280
        },
        "fazer pedido": {
            "xpath": "//android.view.View[@content-desc='FAZER PEDIDO']",
            "x": 0.492,
            "y": 0.288
        },
        "cardapio": {
            "xpath": "//android.view.View[@content-desc='CARDÁPIO']",
            "x": 0.251,
            "y": 0.473
        },
        "agendar pedido": {
            "xpath": "//android.view.View[@content-desc='AGENDAR PEDIDOS']",
            "x": 0.744,
            "y": 0.473
        },
        "favoritos": {
            "xpath": "//android.view.View[@content-desc='FAVORITOS']",
            "x": 0.256,
            "y": 0.667
        },
        "acompanhe seu pedido": {
            "xpath": "//android.view.View[@content-desc='ACOMPANHE SEU PEDIDO']",
            "x": 0.725,
            "y": 0.667
        },
        "confira seus creditos": {
            "xpath": "//android.view.View[@content-desc='CONFIRA SEUS CRÉDITOS']",
            "x": 0.268,
            "y": 0.857
        },
        "novidades": {
            "xpath": "//android.view.View[@content-desc='NOVIDADES DO AMERICA']",
            "x": 0.736,
            "y": 0.857
        },
    # Cardapio
        'grupo salada':{
            'xpath':'//android.view.View[@content-desc="SALADAS"]',
            'x':largura/(largura + largura),
            'y':754/altura
        },
        'opcao de salada':{
            'xpath':'//android.view.View[@content-desc="KALE CARPACCIO"]',
            'x':largura/(largura + largura),
            'y':776/altura
        },
        'home made':{
            'xpath':'//android.view.View[@content-desc="HOME MADE POTATO"]',
            'x':largura/(largura + largura),
            'y':1014/altura
        },        
        "para compartilhar": {
            "xpath": '//android.view.View[@content-desc="PARA COMPARTILHAR"]',
            "x": 347/720,
            "y": 280/1280
        },
        "batata frita": {
            "xpath":'//android.view.View[@content-desc="BATATA FRITA"]' ,
            "x": 357/720,
            "y": 469/1280
        },
        'batata rustica':{
            'xpath':'//android.view.View[@content-desc="BATATA RÚSTICA AMERICA"]'
        },
        'da grelha':{
            'xpath':'//android.view.View[@content-desc="DA GRELHA"]',
            'x':largura/(largura + largura),
            'y':968/altura
        },
        'california':{
            'xpath':'//android.view.View[@content-desc="CALIFORNIA"]',
            'x':largura/(largura + largura),
            'y':454/altura
        },
    #login
        "email": {
            "xpath":'//android.view.View[@content-desc="email"]',
            "x": 0.132,
            "y": 0.325
        },
        "senha": {
            "x": 0.422,
            "y": 0.443,
            "xpath":'//android.view.View[@content-desc="senha"]'
        },
        "acessar": {
            "xpath": "//android.widget.Button[@content-desc='Acessar']",
            "x": 0.509,
            "y": 0.557
        },
        "esqueceu senha": {
            "xpath": "//android.view.View[@content-desc='Esqueceu sua senha?']",
            "x": 0.632,
            "y": 0.672
        },
        "campo email redefinicao": {
            "xpath": "//android.webkit.WebView[@content-desc='Restaurante America']/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View",
            "x": 0.426,
            "y": 0.452
        },
        "submeter": {
            "xpath": "//android.widget.Button[@content-desc='Submeter']",
            "x": 0.481,
            "y": 0.534
        },
        "facebook": {
            "xpath": "//android.webkit.WebView[@content-desc='Restaurante America']/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View[6]",
            "x": 0.338,
            "y": 0.866
        },
        "cadastrar por email": {
            "xpath": "//android.webkit.WebView[@content-desc='Restaurante America']/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[6]",
            "x": 0.647,
            "y": 0.866
        },
        "cadastrarnome": {
            "xpath": "//android.webkit.WebView[@content-desc='Restaurante America']/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View",
            "x": 0.136,
            "y": 0.412
        },
        "cadastrartelefone": {
            "xpath": "//android.webkit.WebView[@content-desc='Restaurante America']/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View",
            "x": 0.117,
            "y": 0.519
        },
        "cadastraremail": {
            "xpath": "//android.webkit.WebView[@content-desc='Restaurante America']/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View[2]/android.view.View",
            "x": 0.117,
            "y": 0.62
        },
        "cadastrarsenha": {
            "xpath": "//android.webkit.WebView[@content-desc='Restaurante America']/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View[4]/android.view.View/android.view.View/android.view.View[2]/android.view.View",
            "x": 0.117,
            "y": 0.73
        },
        "primeiro endereco": {
            "xpath": "//android.view.View[@content-desc='Guido Caloi, Nº 1000']",
            "x": 0.325,
            "y": 0.281
        },
        "procurarlocalizacaoatual": {
            "xpath": "//android.widget.Button[@content-desc='Localização atual']",
            "x": 0.481,
            "y": 0.497
        },
        "procurarporcep": {
            "xpath": "//android.widget.Button[@content-desc='Por CEP']",
            "x": 0.481,
            "y": 0.565
        },
        "insiraocep": {
            "xpath": "//android.widget.EditText[@content-desc='Insira o CEP']",
            "x": 0.132,
            "y": 0.327
        },
        "prosseguir": {
            "xpath": '//android.widget.Button[@content-desc="Prosseguir"]',
            'id':'Prosseguir',
            "x": 0.481,
            "y": 0.395
        },
        "inserironumero": {
            "xpath": "//android.webkit.WebView[@content-desc='Restaurante America']/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[6]/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View",
            "x": 0.206,
            "y": 0.395
        },
        "inserircomplemento": {
            "xpath": "//android.webkit.WebView[@content-desc='Restaurante America']/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[6]/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View",
            "x": 0.206,
            "y": 0.554
        },
        "voltar pesquisa": {
            "xpath": "//android.widget.Button[@content-desc='none ']",
            "x": 0.063,
            "y": 0.11
        },
        "procurarporrua": {
            "xpath": "//android.widget.Button[@content-desc='Por rua']",
            "x": 0.481,
            "y": 0.637
        },
        "digitearua": {
            "xpath": "//android.webkit.WebView[@content-desc='Restaurante America']/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[9]/android.view.View/android.view.View/android.view.View[2]/android.view.View",
            "x": 0.194,
            "y": 0.75
        },
        "buscarrua": {
            "xpath": "//android.widget.Button[@content-desc='Buscar']",
            "x": 0.5,
            "y": 0.813
        },
        "adicionar favoritos": {
            "xpath": "//android.view.View[@content-desc=' Adicionar este produto aos favoritos']",
            "x": 0.5,
            "y": 0.767
        },
        "adicionaraocarrinho": {
            "xpath": "//android.widget.Button[@content-desc='ADICIONAR AO CARRINHO']",
            "x": 0.5,
            "y": 0.883
        },
        "abrir carrinho": {
            "xpath": "//android.webkit.WebView[@content-desc='Restaurante America']/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View",
            "x": 0.883,
            "y": 0.039
        },
        "adicionartalher": {
            "xpath": "//android.view.View[@content-desc='Enviar Talher']",
            "x": 0.271,
            "y": 0.459
        },
        "cpfnanota": {
            "xpath": "//android.view.View[@content-desc='CPF na nota']",
            "x": 0.744,
            "y": 0.48
        },
        "escolherformadepagto": {
            "xpath": "//android.widget.Button[@content-desc='Adicionar Pagamento']",
            "x": 0.485,
            "y": 0.628
        },
        "pagarnocartao": {
            "xpath": "//android.view.View[@content-desc='Cartões de crédito']",
            "x": 0.422,
            "y": 0.298
        },
        "pagaremdinheiro": {
            "xpath": "//android.view.View[@content-desc='Dinheiro']",
            "x": 0.422,
            "y": 0.471
        },
        "editartroco": {
            "xpath": "//android.webkit.WebView[@content-desc='Restaurante America']/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View",
            "x": 0.26,
            "y": 0.295
        },
        "naoprecisatroco": {
            "xpath": "//android.view.View[@content-desc='Não preciso de troco']",
            "x": 0.5,
            "y": 0.414
        },
        "okparatroco": {
            "xpath": "//android.view.View[@content-desc='Ok']",
            "x": 0.5,
            "y": 0.375
        },
        "escolhahorario": {
            "xpath": "//android.widget.Spinner[@content-desc='Escolha o Horário']",
            "x": 0.472,
            "y": 0.292
        },
        "confirmarhorario": {
            "xpath": "//android.widget.Button[@content-desc='Confirmar']",
            "x": 0.472,
            "y": 0.62
        },
        "swipe2slide": {
            "xpath": "//android.widget.Button[@content-desc='Go to slide 2']",
            "x": 0.496,
            "y": 0.968
        },
        "swipe3slide": {
            "xpath": "//android.widget.Button[@content-desc='Go to slide 3']",
            "x": 0.546,
            "y": 0.968
        },
        "proximo a mim": {
            "xpath": '//android.widget.Button[@content-desc="PRÓXIMO A MIM"]',
            "x": 0.831,
            "y": 0.955
        },
        "procurar restaurante por nome": {
            "xpath": "//android.widget.Button[@content-desc='search outline PROCURAR POR NOME']",
            "x": 0.431,
            "y": 0.955
        },
        "busca restaurante por nome": {
            "xpath": '//android.widget.EditText[@content-desc="Busca"]',
            "x": 357/largura,
            "y": 172/altura
        },
        "resultado busca": {
            "xpath": '//android.view.View[@content-desc="Paulista"]',
            "x": 357/largura,
            "y": 172/altura
        },
        "tipodemsg": {
            "xpath": "//android.widget.Spinner[@content-desc='Tipo de mensagem']",
            "x": 0.45,
            "y": 0.502
        },
        "mensagem": {
            "xpath": "//android.webkit.WebView[@content-desc='Restaurante America']/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[5]/android.view.View/android.view.View/android.view.View/android.view.View[2]",
            "x": 0.5,
            "y": 0.765
        },
        "enviarmensagem": {
            "xpath": '//android.view.View[@content-desc="Enviar"]',
            "x": 0.492,
            "y": 0.963
        },
        "voltar": {
            "xpath": "//android.webkit.WebView[@content-desc='Restaurante America']/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]",
            "x": 0.115,
            "y": 0.087
        },
        "trocar login": {
            "xpath": "//android.widget.Button[@content-desc='trocar login']",
            "x": 0.713,
            "y": 0.97
        },
        "fazer pedido cardapio": {
            'xpath': '//android.widget.Button[@content-desc="FAZER PEDIDO"]',
            'x': 300/720,
            'y': 1037/1280
        },
        "senha invalida": {
            'xpath': '//android.view.View[@content-desc="Insira uma senha válida"]'
        },
        "email invalido": {
            'xpath': '//android.view.View[@content-desc="Insira seu e-mail"]'
        },
        'confirmar facebook': {
            'x': 300/720,
            'y': 768/1280
        },
        'campo facebook': {
            'x': 255/720,
            'y': 526/1280
        },
        'campo facebook2': {
            'x': 279/720,
            'y': 526/1280
        },
        'Log In ': {
            'x': 307/720,
            'y': 692/1280
        },
        "como funciona":{
            'xpath': '//android.view.View[@content-desc="Como funciona"]',
            'x': 353/720,
            'y': 1240/1280
        },

        'Critica': {
            'x': 356/720,
            'y': 1055/1280
        },

        'Elogio': {
            'x': 356/720,
            'y': 846/1280
        },

        'Sugestao': {
            'x': 356/720,
            'y': 969/1280
        },

        'NomeFaleConosco': {
            'xpath':'//android.widget.EditText[@content-desc="TESTE INDRAZ"]',
            'x': 106/720,
            'y': 409/1280
        },

        'EmailFaleConosco': {
            'xpath':'//android.widget.EditText[@content-desc="gzerbine@indracompany.com"]',
            'x': 106/720,
            'y': 636/1280
        },

        'CelularFaleConosco': {
            'xpath':'//android.widget.EditText[@content-desc="(62) 98318-2796"]',
            'x': 106/720,
            'y': 779/1280
        },
        'item favorito':{
            'x':0.3,
            'y':0.3
        },
        'nome':{
            'xpath':'//android.view.View[@content-desc="nome completo"]',
            'x':103/720,
            'y':331/1280
        },
        'email dados':{
            'xpath':'//android.view.View[@content-desc="e-mail"]',
            'x':122/720,
            'y':495/1280
        },
        'celular dados':{
            'xpath':'//android.view.View[@content-desc="nº celular"]',  
            'x':112/720,
            'y':759/1280
        },
        'cpf dados':{
            'xpath':'//android.view.View[@content-desc="CPF"]',
            'x':122/720,
            'y':917/1280
        },
        'genero dados':{
            'xpath':'//android.view.View[@content-desc="gênero"]',
            'x':101/720,
            'y':860/1280
        },
        'masculino dados':{
            'x':359/720,
            'y':968/1280
        },
        'feminino dados': {
            'x': 359/720,
            'y': 1028/1280
        },
        'salvar dados':{
            'x':355/720,
            'y':1200/1280
        },
        'oksenha':{
            "x": 0.509,
            "y": 0.557
        },
        'senha dados':{
            'xpath':'//android.view.View[@content-desc="senha alterar senha"]',
            'x': 112/720,
            'y': 594/1280
        },
        'senhaatual':{
            'xpath':'//android.view.View[@content-desc="senha atual"]',
            'x': 142/720,
            'y': 515/1280
        },
        'novasenha':{
            'xpath': '//android.view.View[@content-desc="nova senha"]',
            'x': 142/720,
            'y': 627/1280
        },
        'confirmasenha':{
            'xpath': '//android.view.View[@content-desc="confirme a nova senha"]',
            'x': 142/720,
            'y': 767/1280
        },
        'atualizarsenha':{
            'xpath': '//android.widget.Button[@content-desc="ATUALIZAR"]',
            'x': 360/720,
            'y': 927/1280
        },
        'dados restaurante':{
            'xpath':'(//android.view.View[@content-desc="Alphaville"])[1]'
        },
        'restaurante alphaville':{
            'xpath':'//android.view.View[@content-desc="Alphaville"]',
            'x':158/largura,
            'y':355/altura
        },
        'primeiro restaurante':{
            'xpath':'//android.view.View[@content-desc="Alameda Santos"]'
        },
        'ultimo restaurante':{
            'xpath':'//android.view.View[@content-desc="Shopping Anália Franco"]'
        },
        'qtd_mais':{
            'xpath':'//android.webkit.WebView[@content-desc="Restaurante America"]/android.view.View[4]/android.view.View[4]',
            'x':686/largura,
            'y':627/altura
        },
        'qtd_menos':{
            'xpath':'//android.webkit.WebView[@content-desc="Restaurante America"]/android.view.View[4]/android.view.View[2]',
            'x':686/largura,
            'y':627/altura
        },
        'master':{
            'x':278/largura,
            'y':949/altura
        },
        'finalizar pedido':{
            'xpath':'//android.widget.Button[@content-desc="Finalizar Pedido"]'
        },
        "endereco salvo": {
            "xpath": "//android.view.View[@content-desc='Guido Caloi, Nº 1002']",
            "x": 0.325,
            "y": 0.281
        },
        'email-nao-cadastrado':{
            'xpath':'//android.widget.Button[@content-desc="cancelar"]'
        },
        'ok':{
            'xpath':'//android.widget.Button[@content-desc="OK"]'
        },
        'tela inicial':{
            'xpath':'//android.view.View[@content-desc="TELA INICIAL"]'
        },
        'confirmarhorarioagendamento':{
            'xpath':'//android.widget.Button[@content-desc="Confirmar"]',
            'x':619/largura,
            'y':706/altura
        },
        'horario':{
            'xpath':'//android.widget.Spinner[@content-desc="Escolha o Horário"]',
            'id':'Escolha o Horário',
            'x':360/largura,
            'y':371/altura
        },
        'painel avaliacoes':{
            'xpath':'//android.view.View[@content-desc="AVALIAÇÕES"]'
        },
        'frase voltar - avaliacoes':{
            'xpath':'//android.widget.Button[@content-desc="VOLTAR PARA TELA INICIAL"]',
            'x':364/largura,
            'y':882/altura
        },
        'aumenta quantidade':{
            'xpath':'//android.view.View[@content-desc="+"]'
        },
        'diminui quantidade':{
            'xpath':'//android.view.View[@content-desc="-"]'
        },
        'quantidade':{
            'xpath':'(//android.view.View[@content-desc="1"])[2]'
        },
        'mudar grupo direita':{
            'x':552/largura,
            'y':137/altura
        },
        'mudar grupo esquerda':{
            'x':552/largura,
            'y':137/altura
        },
        'atualizar':{
            'xpath':'//android.view.View[@content-desc="ATUALIZAR"]'
        },
        'versao':{
            'xpath':'//android.view.View[@content-desc="Versão instalada: 2.2.12 Versão atual: 2.3.4"]'
        },
        'valida notificacao':{
            'xpath':'//android.webkit.WebView[@content-desc="Restaurante America"]/android.view.View[14]'
        },
        'Restaurante invalido':{
           'xpath':'//android.widget.Image[@content-desc="icoBadYellow"]'
        },
        'mapa':{
            'xpath':'//android.widget.Image[@content-desc="icoPin"]'
        },
        'termos':{
            'xpath':'//android.view.View[@content-desc="Termos e condições"]',
            'x': 360, 
            'y':1134
        },
        'fale em branco':{
            'xpath':'//android.view.View[@content-desc="Informe um nome"]'
        }

    }