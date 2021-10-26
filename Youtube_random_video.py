from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

def youtube_video():
    option = Options()
    option.add_experimental_option("detach", True)
    browser = webdriver.Chrome(chrome_options = option)
    browser.maximize_window()
    browser.get("https://www.youtube.com/")
    string = "music"

    browser.find_element(By.XPATH, '/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[2]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a/tp-yt-paper-button').click()
    browser.find_element(By.XPATH, '//div[@id="search-input"]').click()
    browser.implicitly_wait(25)
    browser.find_element(By.XPATH, '//input[@id="search"]').send_keys(string + Keys.RETURN)
    searching_urls = browser.find_elements(By.XPATH, '//a[@id="video-title"]')
    total_urls = []

    for searching_url in searching_urls:
        total_urls.append(searching_url.get_attribute("href"))

    random_number = random.randint(1, len(total_urls) - 1)
    generate_link = total_urls[random_number]
    browser.get(generate_link)
    browser.find_element(By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[5]/button').send_keys(Keys.SPACE)