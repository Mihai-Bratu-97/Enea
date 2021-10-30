import socket
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_internet():
    try:
        socket.create_connection(("youtube.com", 80))
        return True
    except OSError:
        return False

def check_wait(chrome, seconds):
    wait = WebDriverWait(chrome, seconds)
    return wait

def option():
    option = Options() # I called the Options() function
    option.add_experimental_option("detach", True)  # I added an option that keeps the browser open
    return option

def check_browser():
    browser = webdriver.Chrome(options = option())  # Here I opened a specific web browser, in this case, Chrome
    return browser

def open_url(chrome, ytb_link):
    chrome.maximize_window()
    while not test_internet():
        chrome.get(ytb_link)
    chrome.get(ytb_link)
    time.sleep(2)

def accept_cookies(chrome):
    try:
        chrome.find_element(By.XPATH, '/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[2]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a/tp-yt-paper-button').click()
    except:
        print("The cookies button wasn't found!")

def youtube_search_bar(waitting, chrome):
    while not test_internet():
        pass
    # this line of code goes to the youtube search bar and it selects it
    try:
        waitting.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="search-input"]'))).click()
    # this line of code goes to the specific youtube search bar that accepts input,  and sets it with the string variable that i created, and types in the RETURN Key
        chrome.find_element(By.XPATH, '//input[@id="search"]').send_keys("trailer 4k" + Keys.RETURN)
    except:
        print("The searchbar wasn't found!")

def random_video(waitting, chrome):
    # this line of code waits 10 seconds until the all elements, by their common path, are found
    try:
        waitting.until(EC.visibility_of_all_elements_located((By.XPATH, '//a[@id="video-title"]')))
    # this variable stores, by their common path, the all found elements
        searching_urls = chrome.find_elements(By.XPATH, '//a[@id="video-title"]')
    # this is an empty list
        total_urls = []
    # this "for" searches through each found element, its specific "href", and extracts it and puts it in total_urls list
        for searching_url in searching_urls:
            total_urls.append(searching_url.get_attribute("href"))

    # this variable generates a random number between 0 and the length of the list - 1
        random_number = random.randint(0, len(total_urls) - 1)
    # this variable selects the clip from total_urls that corresponds to the position(-1) that was random selected before
        generate_link = total_urls[random_number]
        return generate_link
    except:
        print("Couldn't find any videos!")

def open_clip(link, chrome):
    try:
        while not test_internet():
            chrome.get(link)
        chrome.get(link)
    except:
        print("The video couldn't be open")

def play_clip(waitting):
    # this line of code search the play button, by its specific CLASS_NAME, and clicks it
    waitting.until(EC.element_to_be_clickable((By.CLASS_NAME, "ytp-play-button"))).click()

def ads(waitting):
    while not test_internet():
        continue
    try:
        count = 0
        while count < 2:
            waitting.until(EC.element_to_be_clickable((By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button/div'))).click()
            count += 1
    except:
        print("There wasn't any ads button, or just one was displayed, or there were ads that can't be skipped!")

def youtube_premium_ads(waitting):
    while not test_internet():
        continue
    try:
        waitting.until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-mealbar-promo-renderer/div/div[2]/ytd-button-renderer[1]/a/tp-yt-paper-button/yt-formatted-string"))).click()
    except:
        print("Youtube premium button wasn't displayed!")

def youtube_script():
    browser = check_browser()
    wait = check_wait(browser, 10)
    open_url(browser, "https://www.youtube.com/")
    accept_cookies(browser)
    youtube_search_bar(wait, browser)
    random_link = random_video(wait, browser)
    open_clip(random_link, browser)
    play_clip(wait)
    ads(wait)
    wait = check_wait(browser, 4)
    youtube_premium_ads(wait)