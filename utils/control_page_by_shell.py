from selenium import webdriver
from time import sleep


def start_by_shell(login_url):
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get(url=login_url)
    sleep(300)



if __name__ == '__main__':
    start_by_shell('http://127.0.0.1:5000')
