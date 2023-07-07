from selenium import webdriver
from os import environ, path
import platform, sys, json
from pytest import mark
import platform
import time
import subprocess
from selenium.webdriver import Remote
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
load_dotenv()

def initDriver():
    if platform.system() == 'Darwin':
        driver = webdriver.Chrome(environ.get("CHROMEDRIVERMAC"))
    elif platform.system() == 'Windows':
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'normal'
        # options.add_argument('--remote-debugging-port=9222') # port number bisa diubah sesuai keinginan
        # tentukan path ke driver Chrome
        path_to_chromedriver = environ.get("CHROMEDRIVERWIN")
        # jalankan Chrome dengan opsi dan path yang ditentukan
        driver = webdriver.Chrome(executable_path=path_to_chromedriver, chrome_options=options)
    # driver.get(environ.get("HOST"))
    driver.maximize_window()
    return driver

def secondaryinit():
    if platform.system() == 'Darwin':
        driver = webdriver.Chrome(environ.get("CHROMEDRIVERMAC"))
    elif platform.system() == 'Windows':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", "localhost:9222")
        # tentukan path ke driver Chrome
        path_to_chromedriver = environ.get("CHROMEDRIVERWIN")
        # jalankan Chrome dengan opsi dan path yang ditentukan
        driver = webdriver.Chrome(executable_path=path_to_chromedriver, chrome_options=options)

    driver.execute_script("window.open('http://srikandi.torche.id')")
    handles = driver.window_handles
    # alihkan fokus ke tab baru
    driver.switch_to.window(handles[1])
    # jalankan script pada tab baru
    # ...
    return driver

def loadDataPath():
    if platform.system() == 'Windows':
        file = open(environ.get("WINJSONDATA"), 'r')
    elif platform.system() == 'Darwin':
        file = open(environ.get("MACJSONDATA"), 'r')

    data = json.load(file)
    return data

def webfirefox(): #webdriver form firefox
    if platform.system() == 'Windows':
        options = FirefoxOptions()
        # options.add_argument("--headless")
        driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
    elif platform.system() == 'Darwin':
        pass
    # driver.get(environ.get("HOSTKUMBANG"))
    #driver.get(environ.get("HOST"))
    driver.maximize_window()
    return driver
