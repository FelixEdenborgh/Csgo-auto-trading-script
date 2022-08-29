
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
    time.sleep(25)
    # CsgoTrader groups
    driver.get("https://steamcommunity.com/groups/CSGOTrader")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[2]/textarea').send_keys(tradeLink)
    except:
        print("Cant add trade link for CsgoTrader")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for CsgoTrader")


    # -----------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # SkinsAndMore
    driver.get("https://steamcommunity.com/groups/SkinsAndMore")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for SkinsAndMore")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for SkinsAndMore")

    # -----------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # Csgotradesss
    driver.get("https://steamcommunity.com/groups/csgotradesss")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for Csgotradesss")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for Csgotradesss")

    # -----------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # csgotradebot
    driver.get("https://steamcommunity.com/groups/csgotradebot")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for csgotradebot")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for csgotradebot")

    # -----------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # csgolounge
    driver.get("https://steamcommunity.com/groups/csgolounge")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for csgolounge")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for csgolounge")

    # -----------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # iTraders
    driver.get("https://steamcommunity.com/groups/iTraders")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[10]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for iTraders")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[10]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for iTraders")

    # -----------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # tradecenter2016
    driver.get("https://steamcommunity.com/groups/tradecenter2016")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for tradecenter2016")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for tradecenter2016")

    # -----------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # community_market
    driver.get("https://steamcommunity.com/groups/community_market")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for community_market")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for community_market")

    # -----------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # Original_Traders_Group
    driver.get("https://steamcommunity.com/groups/Original_Traders_Group")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[10]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for Original_Traders_Group")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[10]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for Original_Traders_Group")

    # -----------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # freeetrade
    driver.get("https://steamcommunity.com/groups/freeetrade")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for freeetrade")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for freeetrade")

    # -----------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # Trading-Lounge
    driver.get("https://steamcommunity.com/groups/Trading-Lounge")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for Trading-Lounge")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for Trading-Lounge")

    # ------------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # Pc Gamer
    driver.get("https://steamcommunity.com/groups/pcgamer")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[10]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for Pc Gamer")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[10]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for Pc Gamer")

    # ------------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # HLTV.org
    driver.get("https://steamcommunity.com/groups/HLTV")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for HLTV.org")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for HLTV.org")

    # ------------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # Razer Zone
    driver.get("https://steamcommunity.com/groups/razerzone")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for Razer Zone")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for Razer Zone")

    # ------------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # Left4DeadPC
    driver.get("https://steamcommunity.com/groups/Left4Dead2PC")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for Left4DeadPC")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for Left4DeadPC")

    # ------------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # Bitcoin
    driver.get("https://steamcommunity.com/groups/bitcoin")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for Bitcoin")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for Bitcoin")

    # ------------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # ccsgo
    driver.get("https://steamcommunity.com/groups/CCSGO")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for ccsgo")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for ccsgo")

    # ------------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # Trading revolution
    driver.get("https://steamcommunity.com/groups/TradingRevolution")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for Trading revolution")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for Trading revolution")

    # ------------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # Dota_2 Trade
    driver.get("https://steamcommunity.com/groups/D2TradeCenter")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for Dota_2 Trade")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for Dota_2 Trade")

    # ------------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # Bitcoin Traders
    driver.get("https://steamcommunity.com/groups/BitcoinForSteam")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for Bitcoin Traders")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for Bitcoin Traders")

    # ------------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # Steam Trading Cards Group
    driver.get("https://steamcommunity.com/groups/tradingcards")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for Steam Trading Cards Group")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for Steam Trading Cards Group")

    # ------------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # Cs:go Trade Hub
    driver.get("https://steamcommunity.com/groups/CSGOTradeHub")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for Cs:go Trade Hub")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[6]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for Cs:go Trade Hub")

    # ------------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # Cs:go Trade
    driver.get("https://steamcommunity.com/groups/CSGOFGT")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for Cs:go Trade")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for Cs:go Trade")



    # ------------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # CsgoAnalyst
    driver.get("https://steamcommunity.com/groups/steamanalyst")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for CsgoAnalyst")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for CsgoAnalyst")

    # ------------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # CsgoPricecheck
    driver.get("https://steamcommunity.com/groups/CSGOPricecheck")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for CsgoPricecheck")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for CsgoPricecheck")

    # ------------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # Scream OnetapArmy
    driver.get("https://steamcommunity.com/groups/1TapElite")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for CsgoPricecheck")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for CsgoPricecheck")

    # ------------------------------------------------------------------------------------------------------------------
    time.sleep(25)
    # Csmoney
    driver.get("https://steamcommunity.com/groups/csmoneytrade")
    time.sleep(25)
    try:
        # Lägger in trade linken i textarean
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[2]/textarea').send_keys(
            tradeLink)
    except:
        print("Cant add trade link for Csmoney")

    time.sleep(3)
    try:
        # Klickar skicka kommentar knappen
        search = driver.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[8]/div/form/div/div[3]/span[2]').click()
    except:
        print("Cant click send commentary button for Csmoney")