from selenium import webdriver
import time
from selenium.webdriver.common import by

browser = webdriver.Chrome()
browser.get('https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363')
time.sleep(10)
xpath = '/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[1]/div/div[3]/div/div/div/div[1]'
button = browser.find_element(by.By.XPATH, xpath)
button.click()
time.sleep(10)


