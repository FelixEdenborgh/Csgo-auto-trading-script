
# Steg 1: Öppna cmd och skriv in cd C:\Program Files (x86)\Google\Chrome\Application
# Steg 2: skriv in detta: chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\Selenium\Chrome_Test_Profile
# Steg 3: gå till https://steamcommunity.com/groups/CSGOTrader och logga in

# Setup
from selenium.webdriver.chrome import webdriver
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver.exe",chrome_options=opt)

tradeLink = "Check my items out, come trade with me!   https://steamcommunity.com/tradeoffer/new/?partner=8287706&token=PwLx86nP"


while(True):
    # Lägger in trade linken i textarean
    search = driver.find_element_by_xpath(
        '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[2]/textarea').send_keys(
        tradeLink)

    time.sleep(3)

    # Klickar skicka kommentar knappen
    search = driver.find_element_by_xpath(
        '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[3]/span[2]').click()

    time.sleep(300)
