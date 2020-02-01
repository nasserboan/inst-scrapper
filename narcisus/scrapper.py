from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
import random

from secrets.secrets import pw

class VanityBot:
    def __init__(self,my_username,pw):
        self.my_username = my_username

        ## acessando o driver e setando algumas opções
        self.chrome_options = Options()
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options = self.chrome_options)

        ## acessando o instagram
        self.driver.get('https://www.instagram.com/')
        sleep(1)

        ## acessando a tela de login
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[2]/p/a').click()
        sleep(1)

        ## achando login e enviando username
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(self.my_username)
        sleep(1)

        ## achando senha e enviando pw
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(pw)
        sleep(1)

        ## clicando em login
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
        sleep(3)

        ## clicando em 'agora não'
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        sleep(1)

        ## acessando o perfil
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a').click()
        sleep(1)


    def _scroll_following(self,username):
        self.username = username

        ## selecionando a div de following
        following = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
        self.driver.execute_script('arguments[0].scrollIntoView()',following)
        sleep(1)

        ## inspecionando o tamanho da div e quando ambos os tamanhos antes e depois do scroll forem iguais ela para
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(random.randint(1,4))
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0,arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, following)

        links = following.find_elements_by_tag_name('a')
        following = [name.text for name in links if name.text != '']

        return following

    def get_my_following(self):

        ## acessando os meus seguidores
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
        sleep(1)

        my_following = self._scroll_following(self.my_username)

        return my_following


    def get_any_following(self,any_username):

        self.any_username = any_username
        self.driver.get(f'https://www.instagram.com/{any_username}')
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
        sleep(1)
        any_following = self._scroll_following(self.any_username)

        return any_following