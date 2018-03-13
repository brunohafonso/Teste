import time
import random
from helper.actions import Actions

usuario_padrao = 'gzerbine@indracompany.com'
senha_padrao = 'gazn1987'

class America(Actions):

    def inicio(self):
        time.sleep(15)
        try:
            self.clica('pular')
            self.clica('entrar')
        except Exception:
            self.aguarde('menu lateral', tempo=10)
            self.coordenadas('banner')
            self.coordenadas('banner')

    def aumentar_quantidade_pedido(self, vezes=1):
        rodadas = 0
        while(rodadas < vezes):
            self.coordenadas('qtd_mais')
            rodadas += 1
    
    def acessa_opcao(self, opcao):
        try:
            self.aguarde('menu lateral')
            self.aguarde(opcao, 3)
            self.clica(opcao)
        except Exception:
            self.clica('menu lateral')
            self.scroll_para_baixo()
            self.new_coord('lateral {}'.format(opcao))
        
    def troca_login(self):
        self.clica('menu lateral')
        self.scroll_para_cima()
        self.clica('trocar login')

    def login(self, usuario = usuario_padrao, senha = senha_padrao):
        self.escreve('email', usuario)
        self.escreve('senha', senha)
        self.clica('acessar')
        time.sleep(15)
        try:
            self.aguarde('banner', 10)
        except Exception:
            pass
        self.coordenadas('banner')
        self.coordenadas('banner')
        self.coordenadas('banner')        

    def login_manual(self, usuario = usuario_padrao, senha = senha_padrao):
        self.escreve_manual('email', usuario)
        self.escreve_manual('senha', senha)
        self.clica('acessar')
        time.sleep(25)
        self.coordenadas('banner')
        self.coordenadas('banner')
        self.coordenadas('banner')    

    def pagina_inicial(self):
        self.coordenadas('banner')
        self.coordenadas('banner')
        self.clica('menu lateral')
        self.scroll_para_baixo()
        self.clica('inicio')

    def sair(self):
        self.troca_login()
        self.coordenadas('voltar')

    def verifica_login(self):
        try:
            self.aguarde('email', 5)
            self.login()
        except Exception:
            pass
