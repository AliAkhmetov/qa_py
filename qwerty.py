from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyowm
from pyowm.commons.enums import SubscriptionTypeEnum
from pyowm.utils.measurables import kelvin_to_celsius
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

city = 'Moscow'
config = {
    'subscription_type': SubscriptionTypeEnum.FREE,
    'language': 'ru',
    'connection': {
        'use_ssl': True,
        'verify_ssl_certs': True,
        'use_proxy': False,
        'timeout_secs': 5
    },
    'proxies': {
        'http': 'http://user:pass@host:port',
        'https': 'socks5://user:pass@host:port'
    }
}
owm = pyowm.OWM('a21ee967a86474db7e93abd3c1656aa6', config=config)
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather

login = 'python.qa.ali@gmail.com'
pass0 = 'passali1234'
driver = webdriver.Chrome()
driver.get("https://mail.google.com/")
login1 = driver.find_element_by_xpath('//div[@class="Xb9hP"]/input')
login1.click()
login1.click()
login1.send_keys(login)

next1 = driver.find_element_by_xpath('//span[contains(text(),"Далее")]/..')
next1.click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,'//div[contains(text(),"Введите пароль")]' )))

pass1 = driver.find_element_by_xpath('//div[contains(text(),"Введите пароль")]/preceding-sibling::input')
pass1.click()
pass1.click()
pass1.send_keys(pass0)

next2 = driver.find_element_by_xpath('//span[contains(text(),"Далее")]/..')
next2.click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,'//div[contains(text(),"Написать")]' )))


send_mess = driver.find_element_by_xpath('//div[contains(text(),"Написать")]' )
send_mess.click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//textarea[@name="to"]')))


pol = driver.find_element_by_xpath('//textarea[@name="to"]')
pol.click()
pol.click()
pol.send_keys(login)
pol.send_keys(Keys.ENTER)


theam = driver.find_element_by_xpath('//input[@name="subjectbox"]')
theam.click()
theam.click()
theam.send_keys('погода и дата')

mess_text = driver.find_element_by_xpath('//div[@aria-label="Тело письма"]')
mess_text.click()
mess_text.click()
mess_text.send_keys( "В городе " + city + " сейчас температура: " + str(kelvin_to_celsius(w.temp["temp"])) + " по Цельсию." + '\n' + "Дата и время:" + str(datetime.today()) )
mess_text.send_keys(Keys.CONTROL + Keys.ENTER)

driver.quit()