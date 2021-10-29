from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
from internet_connection import check_internet

def checking_ads(browser, wait, ads):  # this function checks if there is ads by their XPATH, and if there is, forces the click on them
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, ads)))
        ads = browser.find_element(By.XPATH, ads)
        browser.execute_script("arguments[0].click();", ads)
    except TimeoutException:
        pass

def youtube_video():
    option = Options() # I called the Options() function
    option.add_experimental_option("detach", True) # I added an option that keeps the browser open
    browser = webdriver.Chrome(chrome_options = option)  # Here I opened a specific web browser, in this case, Chrome
    browser.maximize_window() # I maximized the open window
    wait = WebDriverWait(browser, 10) # I created a variable that waits 10 seconds for making a specific action when it's called, before the next step
    internet = check_internet()
    browser.get("https://www.youtube.com/") # I opened a specific page
    time.sleep(2) # I put the open page to wait 2 seconds, for loading the all elements
    string = "trailer 4k" # a string I'll use later

    # this line of code accepts the cookies button
    browser.find_element(By.XPATH, '/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[2]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a/tp-yt-paper-button').click()
    # this line of code goes to the youtube search bar and it selects it
    browser.find_element(By.XPATH, '//div[@id="search-input"]').click()
    # this line of code goes to the specific youtube search bar that accepts input,  and sets it with the string variable that i created, and types in the RETURN Key
    browser.find_element(By.XPATH, '//input[@id="search"]').send_keys(string + Keys.RETURN)
    # this line of code waits 5 seconds until the all elements, by their common path, are found
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//a[@id="video-title"]')))
    # this variable stores, by their common path, the all found elements
    searching_urls = browser.find_elements(By.XPATH, '//a[@id="video-title"]')
    # this is an empty list
    total_urls = []
    # this "for" searches through each found element, its specific "href", and extracts it and puts it in total_urls list
    for searching_url in searching_urls:
        total_urls.append(searching_url.get_attribute("href"))

    # this variable generates a random number between 0 and the length of the list - 1
    random_number = random.randint(0, len(total_urls) - 1)
    # this variable selects the clip from total_urls that corresponds to the position(-1) that was random selected before
    generate_link = total_urls[random_number]
    # this line of code opens that selected clip
    check_internet()
    browser.get(generate_link)
    # this line of code puts the specific page to wait 3 seconds, for loading the all elements of the page
    time.sleep(3)
    # this line of code search the play button, by its specific CLASS_NAME, and clicks it
    browser.find_element(By.CLASS_NAME, "ytp-play-button").click()
    # this lines checks if there is ads, and if there is, clicks on them
    checking_ads(browser, wait, "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button")
    checking_ads(browser, wait, "/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-mealbar-promo-renderer/div/div[2]/ytd-button-renderer[1]/a/tp-yt-paper-button/yt-formatted-string")