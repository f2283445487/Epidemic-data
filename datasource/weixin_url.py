from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def get_url():
    driver = webdriver.Chrome()
    driver.get('https://wsjkw.sh.gov.cn/xwfb/index.html')
    time.sleep(1)
    texts = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div[2]/div/ul/li[1]')
    news = texts.text
    if "（0-24时）" in news:
        texts.click()
        win = driver.window_handles
        driver.switch_to.window(win[-1])
        url = driver.current_url
        driver.quit()
        return url
    else:
        return False
