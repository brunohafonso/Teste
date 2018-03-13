import time
import pyautogui
from tools.elements import elementos
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

padrao = 0.5
lista_de_elementos = elementos()

class Actions(object):

    def __init__(self, driver):
        self.driver = driver
    

    def new_coord(self, elemento):
        item = lista_de_elementos.get(elemento).get('xpath')
        try:
            WebDriverWait(self.driver, 18).until(ec.presence_of_element_located((By.XPATH, item)))
        except Exception:
            item = lista_de_elementos.get(elemento).get('id')
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, item)))

        tamanho = self.driver.get_window_size()
        altura = tamanho.get('height')
        largura = tamanho.get('width')

        e = self.driver.find_element_by_xpath(item)
        location = e.location
        size = e.size

        x = location.get('x')
        y = location.get('y')

        elemento_altura = size.get('height')
        elemento_largura = size.get('width')

        if(x < 0):
            x = 0

        elif(x > largura):
            x = largura - x

        if(y < 0):
            y = 0

        elif(y > altura):
            y = altura - y

        nova_largura = x + (elemento_largura/2)
        nova_altura = y + (elemento_altura/2)

        if(nova_altura > altura):
            nova_altura = nova_altura/2

        if(nova_largura > largura):
            nova_largura = nova_largura/2

        self.driver.tap([(nova_largura, nova_altura)])
        time.sleep(padrao)

    def aguarde(self, elemento, tempo=30):
        item = lista_de_elementos.get(elemento).get('xpath')
        return WebDriverWait(self.driver, tempo).until(ec.presence_of_element_located((By.XPATH, item)))
        
    def apagar(self, elemento, vezes=50):
        rodadas = 0
        try:
            self.clica(elemento)
        except Exception:
            self.coordenadas(elemento)
        while rodadas < vezes:
            pyautogui.press('backspace')
            rodadas += 1

    def captura(self, nome_da_foto):
        time.sleep(padrao)
        self.driver.get_screenshot_as_file('./screenshot/{}.png'.format(nome_da_foto))
        time.sleep(padrao)

    def clica(self, texto, espera=padrao):
        lista = texto.split(', ')
        for elemento in lista:
            self.aguarde(elemento)
            self.coordenadas(elemento)
            time.sleep(espera)

    def clica_id(self, texto):
        lista = texto.split(', ')
        for elemento in lista:
            self.driver.find_element_by_id(elemento).click()
            time.sleep(padrao)

    def coordenadas(self, elemento, x_adicional = 0, y_adicional = 0):
        altura = self.obtem_altura()
        largura = self.obtem_largura()
        coordenadas = lista_de_elementos.get(elemento)
        nova_largura = (coordenadas.get('x') * largura) + x_adicional
        nova_altura = (coordenadas.get('y') * altura) + y_adicional
        self.driver.tap([(nova_largura, nova_altura)])
        time.sleep(padrao)
    
    def clique_cego(self, x = None, y = None):
        self.driver.tap([(x, y)])

    def escrita_direta(self,texto, trava = True):
        pyautogui.typewrite(texto)
        time.sleep(padrao)
        if(trava):
            self.driver.back()

    def escreve_manual(self, elemento, texto):
        self.clica(elemento)
        pyautogui.typewrite(texto)
        time.sleep(padrao)
        self.driver.back()

    def escreve(self, elemento, texto):
        self.driver.find_element_by_xpath(lista_de_elementos.get(elemento).get('xpath')).send_keys(texto)
        self.driver.back()

    def obtem_altura(self):
        tamanho = self.driver.get_window_size()
        altura = tamanho.get('height')
        return altura

    def obtem_largura(self):
        tamanho = self.driver.get_window_size()
        largura = tamanho.get('width')
        return largura

    def scroll_para_baixo(self, voltas=1):
        tamanho_da_tela = self.driver.get_window_size()
        largura = tamanho_da_tela.get('width')
        altura = tamanho_da_tela.get('height')
        lado_fixo = int(largura/2)
        posicao_inicial = int(altura*0.2)
        posicao_final = int(altura*0.8)
        vezes = 0
        while(vezes <= voltas):
            self.driver.swipe(lado_fixo, posicao_inicial, lado_fixo, posicao_final)
            vezes += 1

    def scroll_para_cima(self, voltas=1):
        tamanho_da_tela = self.driver.get_window_size()
        largura = tamanho_da_tela.get('width')
        altura = tamanho_da_tela.get('height')
        lado_fixo = int(largura/2)
        posicao_inicial = int(altura*0.95)
        posicao_final = int(altura*0.2)
        vezes = 0
        while (vezes <= voltas):
            self.driver.swipe(lado_fixo, posicao_inicial, lado_fixo, posicao_final)
            vezes += 1

    def scroll_para_direita(self, voltas=1):
        tamanho_da_tela = self.driver.get_window_size()
        largura = tamanho_da_tela.get('width')
        altura = tamanho_da_tela.get('height')
        lado_fixo = int(altura / 2)
        posicao_inicial = int(largura*0.2)
        posicao_final = int(largura*0.8)
        vezes = 0
        while (vezes <= voltas):
            self.driver.swipe(posicao_inicial, lado_fixo, posicao_final, lado_fixo)
            vezes += 1

    def scroll_para_esquerda(self, voltas=1):
        tamanho_da_tela = self.driver.get_window_size()
        largura = tamanho_da_tela.get('width')
        altura = tamanho_da_tela.get('height')
        lado_fixo = int(altura / 2)
        posicao_inicial = int(largura*0.8)
        posicao_final = int(largura*0.2)
        vezes = 0
        while (vezes <= voltas):
            self.driver.swipe(posicao_inicial, lado_fixo, posicao_final, lado_fixo)
            vezes += 1

    def trocar(self, elemento, texto):
        time.sleep(padrao)
        total = 0
        vezes = len(texto)*2
        self.clica(elemento)
        while total < vezes:
            pyautogui.press('backspace')
            total += 1
        pyautogui.typewrite(texto)
        self.driver.back()