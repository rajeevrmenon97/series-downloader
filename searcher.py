from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os

class searcher:

    def __init__(self, socks_host = "", socks_port = 0):
        chrome_binary = os.environ.get('GOOGLE_CHROME_SHIM')
        options = Options()
        if chrome_binary is not None:
            options.binary_location = chrome_binary
        if socks_host is not "" and socks_port is not 0:
            options.add_argument("--proxy-server=socks5://" + socks_host + ":" + str(socks_port))
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(chrome_options=options)

    def open_address(self,address):
        self.driver.get(address)

    def search(self,text):
        search_field = self.driver.find_element_by_id("lst-ib")
        search_field.send_keys(text)
        search_button = self.driver.find_element_by_name("btnK")
        search_button.click()

    def get_search_results(self):
        results = self.driver.find_elements_by_class_name("rc")
        print(results)

    def __del__(self):
        self.driver.close()

if __name__ == '__main__':
    obj = searcher("localhost",1080)
    obj.open_address("http://google.co.in/")
    obj.search("flash")
    obj.get_search_results()
