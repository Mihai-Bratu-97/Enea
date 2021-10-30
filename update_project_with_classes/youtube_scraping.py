from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import socket


class YoutubeScript:
    def __init__(self):
        self.chrome = self.create_chrome()
        self.open_site()
        self.wait = WebDriverWait(self.chrome, 10)
        self.cookies()
        self.youtube_searching_bar()
        self.random_clip()
        self.open_random_clip()
        self.start_random_clip()
        self.ads()
        self.checking_youtube_premium()

    def checking_internet(self):
        try:
            socket.create_connection(("youtube.com", 80))
            return True
        except OSError:
            return False

    def create_option(self):
        options = Options()
        options.add_experimental_option("detach", True)
        return options

    def create_chrome(self):
        return webdriver.Chrome(chrome_options=self.create_option())

    def open_site(self):
        self.chrome.maximize_window()
        while not self.checking_internet():
            try:
                self.chrome.get("https://www.youtube.com/")
            except:
                pass
        self.chrome.get("https://www.youtube.com/")
        time.sleep(1.5)

    def cookies(self):
        try:
            self.chrome.find_element(By.XPATH,
                                     '/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[2]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a/tp-yt-paper-button').click()
        except:
            print("There is no cookie button")
            return None

    def youtube_searching_bar(self):
        while not self.checking_internet():
            continue
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="search-input"]'))).click()
            self.chrome.find_element(By.XPATH, '//input[@id="search"]').send_keys("trailer 4k" + Keys.RETURN)
        except:
            print("The search-bar couldn't be accesed")
            return None

    def random_clip(self):
        while not self.checking_internet():
            continue
        try:
            self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//a[@id="video-title"]')))
            searching_urls = self.chrome.find_elements(By.XPATH, '//a[@id="video-title"]')
            total_urls = []
            for searching_url in searching_urls:
                total_urls.append(searching_url.get_attribute("href"))
            random_number = random.randint(0, len(total_urls))
            get_link = total_urls[random_number]
            return get_link
        except:
            print("Couldn't find any videos!")
            return None

    def open_random_clip(self):
        try:
            while not self.checking_internet():
                self.chrome.get(self.random_clip())
            self.chrome.get(self.random_clip())
        except:
            print("The video couldn't be open")
            return None

    def start_random_clip(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ytp-play-button"))).click()
        except:
            print("The play button couldn't be found!")
            return None

    def ads(self):
        while not self.checking_internet():
            continue
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button/div')))
            for i in range(2):
                self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button/div'))).click()
        except:
            print("There wasn't any ads button, or just one was displayed, or there were ads that can't be skipped!")
            return None


    def checking_youtube_premium(self):
        while not self.checking_internet():
            continue
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-mealbar-promo-renderer/div/div[2]/ytd-button-renderer[1]/a/tp-yt-paper-button/yt-formatted-string")))
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-mealbar-promo-renderer/div/div[2]/ytd-button-renderer[1]/a/tp-yt-paper-button/yt-formatted-string"))).click()
        except:
            print("Youtube premium button wasn't displayed!")
            return None