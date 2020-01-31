from selenium import webdriver
from time import sleep
from secrets.secrets import pw

class InstaBot:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome(executable_path='/home/nasserboan/projetos/inst-scrapper/chromedriver')
        self.driver.get('https://www.instagram.com/')
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[2]/p/a').click()
        sleep(2)

        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(username)
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(pw)
        sleep(1)

        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()

        sleep(5)

InstaBot('nsboan',pw)