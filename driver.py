from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver

from scroll import scroll

browser = None

proxy_address = "127.0.0.1:8118"
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': proxy_address,
})

gecko = "/home/ubuntu/Desktop/jibba/geckodriver"
firefox = "/usr/bin/firefox"

firefox_binary = FirefoxBinary(firefox)

def callback(driver):
    driver.quit()

def driver(binary=None, proxy=None):
    return webdriver.Firefox(executable_path=gecko, firefox_binary=binary, proxy=proxy)

if __name__ == "__main__":
    driver = driver(binary=firefox_binary, proxy=proxy)
    # driver.get("https://www.reddit.com/search/?q=apt34")
    driver.get("https://www.9gag.com")
    scroll(driver, 1, 10, callback)
